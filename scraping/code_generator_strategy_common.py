from scraping.code_generator_protocol import CodeGeneratorProtocol
from scraping.code_generator_strategy import CodeGeneratorStrategy
from scraping.constants import LISTNODE_OR_NONE_TYPES, NODE_OR_NONE_TYPES, TREENODE_OR_NONE_TYPES


class CodeGeneratorCommonStrategy(CodeGeneratorStrategy):
    def generate_test_function_code(self, scraper: CodeGeneratorProtocol):
        test_function_parameters = ""
        type_changing_code = ""
        for param in scraper.functions[0].parameters:
            if param.name == "self":
                continue
            if param.type in TREENODE_OR_NONE_TYPES:
                test_function_parameters += f"{param.name}_arr: list[int], "
                type_changing_code += f"    {param.name} = TreeNode.from_array({param.name}_arr)\r\n"
            elif param.type in NODE_OR_NONE_TYPES:
                test_function_parameters += f"{param.name}_arr: list[int], "
                type_changing_code += f"    {param.name} = Node.from_array({param.name}_arr)\r\n"
            elif param.type in LISTNODE_OR_NONE_TYPES:
                test_function_parameters += f"{param.name}_arr: list[int], "
                type_changing_code += f"    {param.name} = ListNode.from_array({param.name}_arr)\r\n"
            else:
                test_function_parameters += f"{param.name}: {param.type}, "
        test_function_parameters = test_function_parameters.strip().strip(",")
        type_changing_code = type_changing_code.strip()
        if type_changing_code:
            type_changing_code += "\r\n    "

        return_type_changing_code = ""
        if scraper.functions[0].returnType in TREENODE_OR_NONE_TYPES:
            return_type_changing_code = "actual = TreeNode.to_array(actual_root)"
        elif scraper.functions[0].returnType in NODE_OR_NONE_TYPES:
            return_type_changing_code = "actual = Node.to_array(actual_root)"
        elif scraper.functions[0].returnType in LISTNODE_OR_NONE_TYPES:
            return_type_changing_code = "actual = ListNode.to_array(actual_root)"

        actual_code = f"actual = so.{scraper.functions[0].name}({scraper.functions[0].get_argument_list_code()})"
        if return_type_changing_code:
            actual_code = "\r\n".join(
                [
                    f"actual_root = so.{scraper.functions[0].name}({scraper.functions[0].get_argument_list_code()})",
                    f"    {return_type_changing_code}",
                ]
            )

        scraper.test_function_code = "\r\n".join(
            [
                "",
                (
                    f"def test(testObj: unittest.TestCase, {test_function_parameters}, "
                    f"expected:{scraper.functions[0].returnType}) -> None:"
                ),
                f"    {type_changing_code}so = Solution()",
                f"    {actual_code}",
                "    testObj.assertEqual(actual, expected)",
                "",
            ]
        )
