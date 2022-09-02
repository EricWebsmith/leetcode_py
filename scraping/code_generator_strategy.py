from abc import ABC, abstractmethod
from scraping.scraper_protocol import ScraperProtocol


class CodeGeneratorStrategy(ABC):
    @abstractmethod
    def parse_function_code(self, scraper: ScraperProtocol):
        ...

    @abstractmethod
    def generate_test_function_code(self, scraper: ScraperProtocol):
        ...
