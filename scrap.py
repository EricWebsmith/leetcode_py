
# install:
#
# pip install python-leetcode
#
# url: https://pypi.org/project/python-leetcode/
#
# use:
# ```
# python scrap.py title_slug
# ```
# you can find title_slug from url.
# like
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
# slug is "sum-of-mutated-array-closest-to-target"
# ```
# python scrap.py "sum-of-mutated-array-closest-to-target"
# ```
# you should create config.py yourself.
# it contains only the following two variables.
# open the following url from chrome to check the following two variable
# chrome://settings/cookies/detail?site=leetcode.com

import sys
from dataclasses import dataclass
import leetcode
import leetcode.auth
import re
from lxml import etree
import json

from config import leetcode_session, csrf_token

@dataclass
class Parameter:
    name: str
    type: str

class Scraper:
    def __init__(self):
        self.headers = {}
        self.title = ''
        self.id = ''
        self.title_slug = ''
        self.type = type
        self.code_definition = ''
        self.content = ''
        self.functoin_code = ''
        self.function_name = ''
        self.typed_param_str = ''
        self.untyped_param_str = ''
        self.function_params = []
        self.function_return_type = ''
        self.definition_for = ''
        self.test_function_code = ''
        self.code = ''
        self.test_cases = []
        self.test_case_code = ''
        self.html = None
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

    def parse_function_code(self):
        def_at = self.code_definition.index('def ')
        open_at = self.code_definition.index('(')
        close_at = self.code_definition.index(')')
        self.typed_param_str = self.code_definition[open_at+7: close_at]

        for param in self.typed_param_str.split(','):
            param_name_type = param.split(':')
            paramObj = Parameter(param_name_type[0].strip(), param_name_type[1].strip())
            self.function_params.append(paramObj)
            self.untyped_param_str += paramObj.name+','
        self.untyped_param_str = self.untyped_param_str.strip(',')
        self.function_name = self.code_definition[def_at+4:open_at]

        self.functoin_code = self.code_definition

    def parse_test_cases(self, tc):
        tc_string = tc.xpath('string()')
        # get input
        input_at = tc_string.find('Input')
        if input_at == -1:
            return None
        output_at = tc_string.find('Output')
        input_string = tc_string[input_at+5:output_at]
        input_string = input_string.strip(':')
        input_string = input_string.strip()
        input_string = input_string.replace('\n', ', ')
        input_string = re.sub('\\bnull\\b', 'None', input_string)
        while '=' in input_string:
            equalAt = input_string.find('=')
            commaAt = equalAt - 1
            while commaAt > 0:
                if input_string[commaAt] == ',':
                    break
                commaAt -= 1
            input_string = input_string[:commaAt] + \
                ', ' + input_string[equalAt+1:]
        # get output
        explanation_t = tc_string.find('Explanation')
        output_string = tc_string[output_at+6:explanation_t]
        output_string = output_string.strip(':')
        output_string = output_string.strip()
        output_string = re.sub('\\bnull\\b', 'None', output_string)
        return input_string+', '+output_string

    def generate_test_case_code(self):
        test_cases = self.html.xpath("//pre")
        test_case_string = ''
        test_case_index = 1
        for i, tc in enumerate(test_cases):
            params = self.parse_test_cases(tc)
            if params == None:
                continue
            test_case_string += f"\n    def test_{test_case_index}(self):\n        test(self{params})\n"
            test_case_index += 1
        self.test_case_code = test_case_string

    def __call__(self, title_slug, type):
        self.title_slug = title_slug
        self.type = type
        question = self.get_detail(title_slug)
        self.id = question.question_frontend_id
        self.title = question.title
        if self.type == '' and 'Design' in self.title:
            self.type = 'Design'
            print("It is a design question.")
        elif self.type == '':
            self.type = 'Common'

        code_definitions = json.loads(question.code_definition)
        self.code_definition = [
            d for d in code_definitions if d['value'] == 'python3'][0]['defaultCode']
        self.remove_comments()
        self.extract_definition_for()
        self.parse_function_code()
        self.html = etree.HTML(question.content)
        self.generate_test_case_code()
        self.parse_test_function_code()
        self.generate_code()
        # return self.code

    def remove_comments(self):
        lines = self.code_definition.split('\n')
        lines = [line.strip('\n').strip('\r') for line in lines]

        code_definition = ''

        is_comment = False
        for line in lines:
            if line.startswith('"""'):
                is_comment = not is_comment

            if not is_comment and not line.startswith('"""'):
                code_definition += line + '\n'
        print(code_definition)
        self.code_definition = code_definition

    def extract_definition_for(self):
        lines = self.code_definition.split('\n')
        lines = [line.strip('\n').strip('\r') for line in lines]

        code_definition = ''
        definition_for = ''
        is_definition_for = False
        for line in lines:
            if line.startswith('#'):
                is_definition_for = True
            if is_definition_for and not line.startswith('#'):
                is_definition_for = False

            if is_definition_for:
                definition_for += line + '\n'
            else:
                code_definition += line + '\n'
        self.definition_for = definition_for
        self.code_definition = code_definition

    def parse_test_function_code(self):

        test_function_parameters = ''
        type_changing_code = ''
        for param in self.function_params:
            if param.type == 'Optional[TreeNode]' or  param.type == 'TreeNode':
                test_function_parameters += f'{param.name}_arr: List[int], '
                type_changing_code += f'    {param.name} = array_to_treenode({param.name}_arr)'
            else:
                test_function_parameters += f'{param.name}: {param.type}, '
        test_function_parameters = test_function_parameters.strip().strip(',')

        self.test_function_code = f"""
def test(testObj: unittest.TestCase, {test_function_parameters}, expected:int) -> None:
    {type_changing_code}
    s = Solution()
    actual = s.{self.function_name}({self.untyped_param_str})
    testObj.assertEqual(actual, expected)
        """

    def generate_code(self):
        self.code = f"""
from heapq import heappop, heappush
import unittest
from typing import List, Optional
from utils.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from utils.nary_tree import Node, array_to_node, node_to_array

{self.code_definition}
        pass

{self.test_function_code}

class TestStringMethods(unittest.TestCase):
    {self.test_case_code}    

if __name__ == '__main__':
    unittest.main()
        """


title_slug = sys.argv[1]
title_slug = title_slug.replace('https://leetcode.com/problems/', '')
title_slug = title_slug.replace('/', '')

question_type = ''
if len(sys.argv) >= 3:
    question_type = sys.argv[2]

scraper = Scraper()
scraper(title_slug, question_type)

with open(f'test/{scraper.id}. {scraper.title}.test.py', mode='w') as f:
    f.write(scraper.code)

print(f'{scraper.id}. {scraper.title} done')
