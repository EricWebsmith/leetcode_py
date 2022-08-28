import sys
import os
from typing import List
import leetcode
import leetcode.auth
import re
from lxml import etree
import json
from dotenv import dotenv_values
from parameter import Parameter
from code_generator_strategy import CodeGeneratorStrategy
from code_generator_common_strategy import CodeGeneratorCommonStrategy
from code_generator_design_strategy import CodeGeneratorDesignStrategy

DESIGN = 'DESIGN'
COMMON = 'COMMON'

env = dotenv_values()
leetcode_session = env['LEETCODE_SESSION']
csrf_token = env['CSRF_TOKEN']

class Scraper:
    def __init__(self):
        self.headers = {}
        self.title = ''
        self.id = ''
        self.title_slug = ''
        self.problem_type = ''
        self.code_definition = ''
        self.content = ''
        self.classname = ''
        self.functoin_code = ''
        # common 
        self.function_name = ''
        # design
        self.function_names: List[str] = []
        self.typed_param_str = ''
        self.untyped_param_str = ''
        self.function_params: List[Parameter] = []
        self.function_return_type = ''
        self.definition_for = ''
        self.test_function_code = ''
        self.code = ''
        self.test_cases = []
        self.test_case_code = ''
        self.html = None
        self.api_instance = self.get_api_instance(leetcode_session, csrf_token)
        self.code_generation_strategy: CodeGeneratorStrategy = None

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
        input_string = re.sub('\\bfalse\\b', 'False', input_string)
        input_string = re.sub('\\btrue\\b', 'True', input_string)
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
        output_string = re.sub('\\bfalse\\b', 'False', output_string)
        output_string = re.sub('\\btrue\\b', 'True', output_string)
        return input_string+', '+output_string

    def generate_test_case_code(self):
        test_cases = self.html.xpath("//pre")
        test_case_string = ''
        test_case_index = 1
        for i, tc in enumerate(test_cases):
            params = self.parse_test_cases(tc)
            if params == None:
                continue
            params = params.strip(',')
            test_case_string += f"\n    def test_{test_case_index}(self):\n        test(self, {params})\n"
            test_case_string
            test_case_index += 1
        self.test_case_code = test_case_string

    def select_code_generation_strategry(self):
        if self.problem_type == DESIGN or DESIGN in self.title.upper():
            self.problem_type = DESIGN
            self.code_generation_strategy = CodeGeneratorDesignStrategy()
            print("It is a design question.")
        elif self.problem_type == '':
            self.problem_type = COMMON
            self.code_generation_strategy = CodeGeneratorCommonStrategy()

    def __call__(self, title_slug:str, problem_type:str):
        self.title_slug = title_slug
        self.problem_type = problem_type.upper()
        question = self.get_detail(title_slug)
        self.id = question.question_frontend_id
        self.title = question.title
        self.select_code_generation_strategry()

        code_definitions = json.loads(question.code_definition)
        self.code_definition = [
            d for d in code_definitions if d['value'] == 'python3'][0]['defaultCode']
        self.remove_comments()
        self.get_classname()
        self.code_generation_strategy.parse_function_code(self)
        self.html = etree.HTML(question.content)
        self.generate_test_case_code()
        self.code_generation_strategy.generate_test_function_code(self)
        self.generate_code()

    def remove_comments(self):
        lines = self.code_definition.split('\n')
        lines = [line.strip('\n').strip('\r') for line in lines]

        code_definition = ''

        is_comment = False
        for line in lines:
            if line.startswith('"""'):
                is_comment = not is_comment

            if not is_comment and not line.startswith('"""') and not line.startswith('#'):
                code_definition += line + '\n'
        print(code_definition)
        self.code_definition = code_definition

    def get_classname(self):
        class_at = self.code_definition.index('class')
        colon_at = self.code_definition.index(':', class_at)
        self.classname = self.code_definition[class_at+6:colon_at]

    def generate_code(self):
        self.code = f"""from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

{self.code_definition}
        pass

{self.test_function_code}

class TestClass(unittest.TestCase):
    {self.test_case_code}    

if __name__ == '__main__':
    unittest.main()

'''

'''
"""

title_slug = sys.argv[1] if len(sys.argv) >= 2 else 'time-based-key-value-store'
title_slug = re.sub('https://leetcode.c[n|om]/problems/', '', title_slug)
title_slug = re.sub('https://leetcode.c[n|om]/contest/(bi)?weekly-contest-\d+/problems/', '', title_slug)
title_slug = title_slug.replace('solution/', '')
title_slug = title_slug.replace('submissions/', '')

problem_type = ''
if len(sys.argv) >= 3:
    problem_type = sys.argv[2]

scraper = Scraper()
scraper(title_slug, problem_type)

if not os.path.exists('test'):
    os.mkdir('test')

title_slug_fixed = title_slug.replace('-', '_')

path = f'test/lc_{scraper.id}_{title_slug_fixed}.py'

with open(path, mode='w') as f:
    f.write(scraper.code)

print(f'{scraper.id}. {scraper.title} done')

import subprocess
subprocess.call(['code', path])