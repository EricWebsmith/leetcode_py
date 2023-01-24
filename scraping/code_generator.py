import logging
import re

from scraping.code_generator_strategy import CodeGeneratorStrategy
from scraping.code_generator_strategy_common import CodeGeneratorCommonStrategy
from scraping.code_generator_strategy_design import CodeGeneratorDesignStrategy
from scraping.constants import COMMON, DESIGN
from scraping.parameter import fix_type
from scraping.py_function import PyFunction
from scraping.scraper_result import ScraperResult


class CodeGenerator:
    def __init__(self, result: ScraperResult, problem_type: str) -> None:
        self.headers: dict = dict()
        self.title = result.title
        self.id = result.id
        self.title_slug = result.title_slug
        self.problem_type = problem_type
        self.code_definition = result.code_definition
        self.content = ""
        self.classname = ""
        self.functions: list[PyFunction] = []
        self.definition_for = ""
        self.test_function_code = ""
        self.code = ""
        self.test_cases = result.test_cases
        self.test_case_code = ""
        self.html = None
        self.code_generation_strategy: CodeGeneratorStrategy | None = None

    def parse_function_code(self):
        lines = [line.strip() for line in self.code_definition.split("\n")]
        for line in lines:
            if not line.startswith("def"):
                continue
            py_func = PyFunction.from_code(line)
            self.functions.append(py_func)

    def parse_test_cases(self, tc_string):
        # get input
        input_at = tc_string.find("Input")
        if input_at == -1:
            return None
        output_at = tc_string.find("Output")
        input_string = tc_string[input_at + 5 : output_at]
        input_string = input_string.strip(":")
        input_string = input_string.strip()
        input_string = input_string.replace("\n", ", ")
        input_string = re.sub("\\bnull\\b", "None", input_string)
        input_string = re.sub("\\bfalse\\b", "False", input_string)
        input_string = re.sub("\\btrue\\b", "True", input_string)
        while "=" in input_string:
            equalAt = input_string.find("=")
            commaAt = equalAt - 1
            while commaAt > 0:
                if input_string[commaAt] == ",":
                    break
                commaAt -= 1
            input_string = input_string[:commaAt] + ", " + input_string[equalAt + 1 :]
        # get output
        explanation_t = tc_string.find("Explanation")
        output_string = tc_string[output_at + 6 : explanation_t]
        output_string = output_string.strip(":")
        output_string = output_string.strip()
        output_string = re.sub("\\bnull\\b", "None", output_string)
        output_string = re.sub("\\bfalse\\b", "False", output_string)
        output_string = re.sub("\\btrue\\b", "True", output_string)
        return input_string + ", " + output_string

    def generate_test_case_code(self):
        test_case_string = ""
        test_case_index = 1
        for tc in self.test_cases:
            params = self.parse_test_cases(tc)
            if params is None:
                continue
            params = params.strip(",")
            test_case_string += f"\n    def test_{test_case_index}(self):\n        test(self, {params})\n"
            test_case_string
            test_case_index += 1
        self.test_case_code = test_case_string

    def select_code_generation_strategry(self):
        if self.problem_type.upper() == DESIGN or DESIGN in self.title.upper():
            self.problem_type = DESIGN
            self.code_generation_strategy = CodeGeneratorDesignStrategy()
            logging.info("It is a design question.")
        else:
            self.problem_type = COMMON
            self.code_generation_strategy = CodeGeneratorCommonStrategy()

    def __call__(self):
        self.select_code_generation_strategry()

        self.remove_comments()
        self.get_classname()
        self.parse_function_code()
        self.generate_test_case_code()
        self.code_generation_strategy.generate_test_function_code(self)
        self.generate_code()

    def remove_comments(self):
        lines = self.code_definition.split("\n")
        lines = [line.strip("\n").strip("\r") for line in lines]

        code_definition = ""

        is_comment = False
        for line in lines:
            if line.startswith('"""'):
                is_comment = not is_comment

            if not is_comment and not line.startswith('"""') and not line.startswith("#"):
                code_definition += line + "\n"

        self.code_definition = fix_type(code_definition)

    def get_classname(self):
        class_at = self.code_definition.index("class")
        colon_at = self.code_definition.index(":", class_at)
        self.classname = self.code_definition[class_at + 6 : colon_at]

    def generate_code(self):
        self.code = "\r\n".join(
            [
                "from heapq import heappop, heappush",
                "import unittest",
                "from functools import cache",
                "from collections import deque, defaultdict",
                "from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array",
                "from data_structure.nary_tree import Node, array_to_node, node_to_array",
                "from data_structure.link_list import ListNode, listnode_to_array, array_to_listnode",
                "",
                "",
                f"{self.code_definition}",
                "        pass",
                "",
                f"{self.test_function_code}",
                "",
                "class TestClass(unittest.TestCase):",
                f"    {self.test_case_code}",
                "",
                "if __name__ == '__main__':",
                "    unittest.main()",
                "",
                "",
                "'''",
                "",
                "'''",
                "",
            ]
        )


if __name__ == "__main__":
    result = ScraperResult()
    result.id = "2413"
    result.title = "Smallest Even Multiple"
    result.title_slug = "smallest-even-multiple"
    result.code_definition = "\r\n".join(["class Solution:", "    def smallestEvenMultiple(self, n: int) -> int:"])

    result.test_cases = [
        "\r\n".join(
            [
                "Input: n = 5",
                "Output: 10",
                "Explanation: The smallest multiple of both 5 and 2 is 10.",
            ]
        ),
        "\r\n".join(
            [
                "Input: n = 6",
                "Output: 6",
                "Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.",
            ]
        ),
    ]
    cg = CodeGenerator(result, "COMMON")
    cg()
