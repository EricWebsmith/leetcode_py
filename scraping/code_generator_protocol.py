from typing import Protocol

from parameter import Parameter


class CodeGeneratorProtocol(Protocol):
    code_definition: str
    classname: str
    function_name: str
    function_names: list[str]
    typed_param_str: str
    untyped_param_str: str
    functoin_code: str
    function_params: list[Parameter]
    function_return_type: str = "None"
    test_function_code: str
