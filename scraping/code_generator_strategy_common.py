from parameter import Parameter
from code_generator_strategy import CodeGeneratorStrategy
from scraping.code_generator_protocol import CodeGeneratorProtocol


class CodeGeneratorCommonStrategy(CodeGeneratorStrategy):
    def parse_function_code(self, scraper: CodeGeneratorProtocol):
        def_at = scraper.code_definition.index('def ')
        open_at = scraper.code_definition.index('(', def_at)
        close_at = scraper.code_definition.index(')', open_at)
        arrow_at = scraper.code_definition.index('->', open_at)
        comma_at = scraper.code_definition.index(':', arrow_at)

        # function name
        scraper.function_name = scraper.code_definition[def_at+4:open_at]
        # parameters
        scraper.typed_param_str = scraper.code_definition[open_at+7: close_at]

        for param in scraper.typed_param_str.split(','):
            param_name_type = param.split(':')
            paramObj = Parameter(
                param_name_type[0].strip(), param_name_type[1].strip().strip("'").strip('"'))
            scraper.function_params.append(paramObj)
            scraper.untyped_param_str += paramObj.name+','
        scraper.untyped_param_str = scraper.untyped_param_str.strip(',')

        # return type
        scraper.function_return_type = scraper.code_definition[arrow_at+2: comma_at].strip(
        )
        scraper.functoin_code = scraper.code_definition

    def generate_test_function_code(self, scraper: CodeGeneratorProtocol):
        test_function_parameters = ''
        type_changing_code = ''
        for param in scraper.function_params:
            if param.type == 'Optional[TreeNode]' or param.type == 'TreeNode':
                test_function_parameters += f'{param.name}_arr: List[int], '
                type_changing_code += f'    {param.name} = array_to_treenode({param.name}_arr)\r\n'
            elif param.type == 'Optional[Node]' or param.type == 'Node':
                test_function_parameters += f'{param.name}_arr: List[int], '
                type_changing_code += f'    {param.name} = array_to_node({param.name}_arr)\r\n'
            elif param.type == 'Optional[ListNode]' or param.type == 'ListNode':
                test_function_parameters += f'{param.name}_arr: List[int], '
                type_changing_code += f'    {param.name} = array_to_listnode({param.name}_arr)\r\n'
            else:
                test_function_parameters += f'{param.name}: {param.type}, '
        test_function_parameters = test_function_parameters.strip().strip(',')
        type_changing_code = type_changing_code.strip()

        return_type_changing_code = ''
        if scraper.function_return_type in ['Optional[TreeNode]', 'TreeNode']:
            return_type_changing_code = 'actual = treenode_to_array(actual_root)'
        elif scraper.function_return_type in ['Optional[Node]', 'Node']:
            return_type_changing_code = 'actual = node_to_array(actual_root)'
        elif scraper.function_return_type in ['Optional[ListNode]', 'ListNode']:
            return_type_changing_code = 'actual = listnode_to_array(actual_root)'

        actual_code = f"""
    actual = so.{scraper.function_name}({scraper.untyped_param_str})
"""
        if return_type_changing_code:
            actual_code = f"""
    actual_root = so.{scraper.function_name}({scraper.untyped_param_str})
    {return_type_changing_code}
"""

        scraper.test_function_code = f"""

def test(testObj: unittest.TestCase, {test_function_parameters}, expected:{scraper.function_return_type}) -> None:
    {type_changing_code}
    so = Solution()
    {actual_code}
    testObj.assertEqual(actual, expected)
"""
