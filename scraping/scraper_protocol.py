from typing import Protocol

from typing import List
from scraping.parameter import Parameter

class ScraperProtocol(Protocol):
    code_definition: str
    classname: str
    function_name: str
    function_names: List[str]
    typed_param_str: str
    untyped_param_str: str
    functoin_code: str
    function_params: List[Parameter]