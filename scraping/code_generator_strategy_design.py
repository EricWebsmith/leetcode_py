from scraping.code_generator_protocol import CodeGeneratorProtocol
from scraping.code_generator_strategy import CodeGeneratorStrategy


class CodeGeneratorDesignStrategy(CodeGeneratorStrategy):

    def __init__(self) -> None:
        super().__init__()

    def generate_test_function_code(self, scraper: CodeGeneratorProtocol):

        cases = "\n"

        for py_func in scraper.functions:
            if py_func.name == "__init__":
                continue

            #fmt: on
            case = ""
            if py_func.returnType == "None":
                case = "\r\n".join([
                    f'            case "{py_func.name}":',
                    f"                obj.{py_func.name}(*params[i])",
                    ""])
            else:
                case = "\r\n".join([
                    f'            case "{py_func.name}":',
                    f"                {py_func.name}_actual = obj.{py_func.name}(*params[i])",
                    f"                testObj.assertEqual({py_func.name}_actual, expected[i])",
                    ""])
            cases += case
            #fmt: off

        scraper.test_function_code = "\r\n".join(
            [
                "def test(testObj: unittest.TestCase, actions:list, params:list , expected:list) -> None:",
                "    n = len(actions)",
                f"    obj = {scraper.classname}(*params[0])",
                "    print('------------test case-----------')",
                "    for i in range(1, n):",
                "        print(i, actions[i], params[i], expected[i])",
                "    print('-------done-------------')",
                "    for i in range(1, n):",
                "        print(i, actions[i], params[i], expected[i])",
                "        match actions[i]:",
                f"            {cases}",
            ]
        )
