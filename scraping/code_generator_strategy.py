from abc import ABC, abstractmethod

from code_generator_protocol import CodeGeneratorProtocol


class CodeGeneratorStrategy(ABC):
    @abstractmethod
    def generate_test_function_code(self, scraper: CodeGeneratorProtocol):
        ...
