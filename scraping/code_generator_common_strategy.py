from parameter import Parameter
from code_generator_strategy import CodeGeneratorStrategy
from scraper_protocol import ScraperProtocol


class CodeGeneratorCommonStrategy(CodeGeneratorStrategy):
    def parse_function_code(self, scraper: ScraperProtocol):
        def_at = scraper.code_definition.index('def ')
        open_at = scraper.code_definition.index('(')
        close_at = scraper.code_definition.index(')')
        scraper.typed_param_str = scraper.code_definition[open_at+7: close_at]

        for param in scraper.typed_param_str.split(','):
            param_name_type = param.split(':')
            paramObj = Parameter(param_name_type[0].strip(), param_name_type[1].strip())
            scraper.function_params.append(paramObj)
            scraper.untyped_param_str += paramObj.name+','
        scraper.untyped_param_str = scraper.untyped_param_str.strip(',')
        scraper.function_name = scraper.code_definition[def_at+4:open_at]
        scraper.functoin_code = scraper.code_definition

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

        scraper.test_function_code = f"""
def test(testObj: unittest.TestCase, {test_function_parameters}, expected:int) -> None:
    {type_changing_code}
    so = Solution()
    actual = so.{scraper.function_name}({scraper.untyped_param_str})
    testObj.assertEqual(actual, expected)
        """
