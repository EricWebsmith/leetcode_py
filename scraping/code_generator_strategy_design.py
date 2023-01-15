from code_generator_protocol import CodeGeneratorProtocol
from code_generator_strategy import CodeGeneratorStrategy


class CodeGeneratorDesignStrategy(CodeGeneratorStrategy):
    def __init__(self) -> None:

        super().__init__()

    def parse_function_code(self, scraper: CodeGeneratorProtocol):

        def_at = scraper.code_definition.find('def ')
        while def_at > 0:

            open_at = scraper.code_definition.find('(', def_at)
            function_name = scraper.code_definition[def_at+4:open_at]
            if function_name != '__init__':
                scraper.function_names.append(function_name)
            def_at = scraper.code_definition.find('def ', open_at)

    def generate_test_function_code(self, scraper: CodeGeneratorProtocol):
        test_function_parameters = ''
        type_changing_code = ''
        for param in scraper.function_params:
            if param.type == 'Optional[TreeNode]' or param.type == 'TreeNode':
                test_function_parameters += f'{param.name}_arr: list[int], '
                type_changing_code += f'    {param.name} = array_to_treenode({param.name}_arr)'
            else:
                test_function_parameters += f'{param.name}: {param.type}, '
        test_function_parameters = test_function_parameters.strip().strip(',')

        cases = '\n'
        for function_name in scraper.function_names:
            case = '\r\n'.join([
                f'            case "{function_name}":'
                f'                actual = obj.{function_name}(*params[i])'
                '                testObj.assertEqual(actual, expected[i])'
                ''])

            cases += case

        scraper.test_function_code = '\r\n'.join([
            'def test(testObj: unittest.TestCase, actions:list, params:list , expected:list) -> None:',
            '    n = len(actions)',
            f'    obj = {scraper.classname}(*params[0])',
            "    print('------------test case-----------')",
            "    for i in range(1, n):",
            "        print(i, actions[i], params[i], expected[i])",
            "    print('-------done-------------')",
            "    for i in range(1, n):",
            "        print(i, actions[i], params[i], expected[i])",
            "        match actions[i]:",
            f"            {cases}",])
