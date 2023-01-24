from typing import Protocol

from scraping.py_function import PyFunction


class CodeGeneratorProtocol(Protocol):
    code_definition: str
    classname: str
    functions: list[PyFunction]
    test_function_code: str
