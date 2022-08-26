from parameter import Parameter
from code_generator_strategy import CodeGeneratorStrategy
from scraper_protocol import ScraperProtocol


class CodeGeneratorDesignStrategy(CodeGeneratorStrategy):
    def parse_function_code(self, scraper: ScraperProtocol):

        def_at = scraper.code_definition.find('def ')
        while def_at>0:
        
            open_at = scraper.code_definition.find('(', def_at)
            function_name = scraper.code_definition[def_at+4:open_at]
            if function_name != '__init__':
                scraper.function_names.append(function_name)
            def_at = scraper.code_definition.find('def ', open_at)

    def generate_test_function_code(self, scraper: ScraperProtocol):
        test_function_parameters = ''
        type_changing_code = ''
        for param in scraper.function_params:
            if param.type == 'Optional[TreeNode]' or  param.type == 'TreeNode':
                test_function_parameters += f'{param.name}_arr: List[int], '
                type_changing_code += f'    {param.name} = array_to_treenode({param.name}_arr)'
            else:
                test_function_parameters += f'{param.name}: {param.type}, '
        test_function_parameters = test_function_parameters.strip().strip(',')

        cases = '\n'
        for function_name in scraper.function_names:
            case = f"""
            case "{function_name}":
                actual = obj.{function_name}(*params[i])
                testObj.assertEqual(actual, expected[i])
            """
            cases+=case



        scraper.test_function_code = f"""
def test(testObj: unittest.TestCase, actions:List, params:List , expected:List) -> None:
    n = len(actions)
    obj = {scraper.classname}(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:
            {cases}
        """
