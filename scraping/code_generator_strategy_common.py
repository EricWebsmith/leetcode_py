from code_generator_protocol import CodeGeneratorProtocol
from code_generator_strategy import CodeGeneratorStrategy
from parameter import Parameter

TREENODE_AND_OPTIONAL_TYPES = ["Optional[TreeNode]", "TreeNode | None", "TreeNode"]
NODE_AND_OPTIONAL_TYPES = ["Optional[Node]", "Node | None", "Node"]
LISTNODE_AND_OPTIONAL_TYPES = ["Optional[ListNode]", "ListNode | None", "ListNode"]


class CodeGeneratorCommonStrategy(CodeGeneratorStrategy):
    def parse_function_code(self, scraper: CodeGeneratorProtocol):
        def_at = scraper.code_definition.index("def ")
        open_at = scraper.code_definition.index("(", def_at)
        close_at = scraper.code_definition.index(")", open_at)
        arrow_at = scraper.code_definition.find("->", open_at)
        comma_at = scraper.code_definition.index(":", close_at)

        # function name
        scraper.function_name = scraper.code_definition[def_at + 4 : open_at]
        # parameters
        scraper.typed_param_str = scraper.code_definition[open_at + 7 : close_at]

        for param in scraper.typed_param_str.split(","):
            param_name_type = param.split(":")
            param_type = "Any"
            if len(param_name_type) == 2:
                param_type = param_name_type[1].strip().strip("'").strip('"')
            paramObj = Parameter(param_name_type[0].strip(), param_type)
            scraper.function_params.append(paramObj)
            scraper.untyped_param_str += paramObj.name + ","
        scraper.untyped_param_str = scraper.untyped_param_str.strip(",")

        # return type
        scraper.function_return_type = "None"
        if arrow_at > 0:
            scraper.function_return_type = scraper.code_definition[
                arrow_at + 2 : comma_at
            ].strip()
        scraper.functoin_code = scraper.code_definition

    def generate_test_function_code(self, scraper: CodeGeneratorProtocol):
        test_function_parameters = ""
        type_changing_code = ""
        for param in scraper.function_params:
            if param.type in TREENODE_AND_OPTIONAL_TYPES:
                test_function_parameters += f"{param.name}_arr: list[int], "
                type_changing_code += (
                    f"    {param.name} = array_to_treenode({param.name}_arr)\r\n"
                )
            elif param.type in NODE_AND_OPTIONAL_TYPES:
                test_function_parameters += f"{param.name}_arr: list[int], "
                type_changing_code += (
                    f"    {param.name} = array_to_node({param.name}_arr)\r\n"
                )
            elif param.type in LISTNODE_AND_OPTIONAL_TYPES:
                test_function_parameters += f"{param.name}_arr: list[int], "
                type_changing_code += (
                    f"    {param.name} = array_to_listnode({param.name}_arr)\r\n"
                )
            else:
                test_function_parameters += f"{param.name}: {param.type}, "
        test_function_parameters = test_function_parameters.strip().strip(",")
        type_changing_code = type_changing_code.strip()
        if type_changing_code:
            type_changing_code += "\r\n    "

        return_type_changing_code = ""
        if scraper.function_return_type in TREENODE_AND_OPTIONAL_TYPES:
            return_type_changing_code = "actual = treenode_to_array(actual_root)"
        elif scraper.function_return_type in NODE_AND_OPTIONAL_TYPES:
            return_type_changing_code = "actual = node_to_array(actual_root)"
        elif scraper.function_return_type in LISTNODE_AND_OPTIONAL_TYPES:
            return_type_changing_code = "actual = listnode_to_array(actual_root)"

        actual_code = (
            f"actual = so.{scraper.function_name}({scraper.untyped_param_str})"
        )
        if return_type_changing_code:
            actual_code = "\r\n".join(
                [
                    f"actual_root = so.{scraper.function_name}({scraper.untyped_param_str})",
                    "    {return_type_changing_code}",
                ]
            )

        scraper.test_function_code = "\r\n".join(
            [
                "",
                (
                    f"def test(testObj: unittest.TestCase, {test_function_parameters}, "
                    f"expected:{scraper.function_return_type}) -> None:"
                ),
                f"    {type_changing_code}so = Solution()",
                f"    {actual_code}",
                "    testObj.assertEqual(actual, expected)",
                "",
            ]
        )
