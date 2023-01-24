import logging

import requests  # type: ignore
from dotenv import dotenv_values
from lxml import etree  # type: ignore

from scraping.scraper_result import ScraperResult

env = dotenv_values()
Cookie = env["Cookie"]


class ContestScraper:
    def __init__(self) -> None:
        pass

    def __call__(self, url: str) -> ScraperResult:
        result = ScraperResult()
        headers = {"cookie": Cookie}
        res = requests.get(url, headers=headers)
        res.encoding = "utf-8"
        text = res.text
        title_slug_at = text.find("questionTitleSlug:")
        newline_at = text.find("',", title_slug_at)
        title_slug = text[title_slug_at + len("questionTitleSlug:") + 2 : newline_at]
        result.title_slug = title_slug.strip()

        title_at = text.find("questionTitle:")
        newline_at = text.find("',", title_at)
        result.title = text[title_at + len("questionTitle:") + 2 : newline_at]

        codeDefinition_at = text.find("codeDefinition:")
        newline_at = text.find("\n", codeDefinition_at)
        codeDefinition_str = text[codeDefinition_at + len("codeDefinition:") : newline_at - 1]
        code_definitions = eval(codeDefinition_str)
        result.code_definition = [d for d in code_definitions if d["value"] == "python3"][0]["defaultCode"]

        html = etree.HTML(text)

        id_title = html.xpath("//h3/text()")[0]
        result.id = id_title.split(".")[0]

        test_cases = html.xpath("//pre")
        for tc in test_cases:
            tc_string = tc.xpath("string()")
            result.test_cases.append(tc_string)

        return result


if __name__ == "__main__":
    s = ContestScraper()
    result = s("https://leetcode.com/contest/weekly-contest-311/problems/smallest-even-multiple/")
    logging.info(result)
