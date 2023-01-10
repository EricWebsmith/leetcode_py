import json

import leetcode  # type: ignore
import leetcode.auth  # type: ignore
from dotenv import dotenv_values
from lxml import etree  # type: ignore
from scraper_result import ScraperResult

env = dotenv_values()
leetcode_session = env['LEETCODE_SESSION']
csrf_token = env['CSRF_TOKEN']


class ProblemScraper:
    def __init__(self) -> None:
        self.api_instance = self.get_api_instance(leetcode_session, csrf_token)

    def get_api_instance(self, leetcode_session, csrf_token):
        csrf_token = leetcode.auth.get_csrf_cookie(leetcode_session)
        configuration = leetcode.Configuration()
        configuration.api_key["x-csrftoken"] = csrf_token
        configuration.api_key["csrftoken"] = csrf_token
        configuration.api_key["LEETCODE_SESSION"] = leetcode_session
        configuration.api_key["Referer"] = "https://leetcode.com"
        configuration.debug = False
        api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))
        return api_instance

    def get_detail(self, title_slug):
        graphql_request = leetcode.GraphqlQuery(
            query="""
                query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    questionFrontendId
                    title
                    content
                    codeDefinition
                }
                }
            """,
            variables=leetcode.GraphqlQueryGetQuestionDetailVariables(
                title_slug),
            operation_name="getQuestionDetail",
        )

        result = self.api_instance.graphql_post(body=graphql_request)
        return result.data.question

    def __call__(self, title_slug: str) -> ScraperResult:
        result = ScraperResult()
        result.title_slug = title_slug
        question = self.get_detail(title_slug)
        result.id = question.question_frontend_id
        result.title = question.title
        code_definitions = json.loads(question.code_definition)
        result.code_definition = [
            d for d in code_definitions if d['value'] == 'python3'][0]['defaultCode']
        content = etree.HTML(question.content)
        test_cases = content.xpath("//pre")
        for tc in test_cases:
            tc_string = tc.xpath('string()')
            result.test_cases.append(tc_string)

        return result


if __name__ == '__main__':
    s = ProblemScraper()
    result = s('two-sum')
    print(result)
