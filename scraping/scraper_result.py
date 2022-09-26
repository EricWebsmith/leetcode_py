from typing import List
from dataclasses import dataclass


@dataclass
class ScraperResult:
    id: str = '0'
    title_slug: str = ''
    title: str = ''
    code_definition: str = ''
    test_cases: List[str] = None

    def __init__(self) -> None:
        self.test_cases = []

    def __repr__(self) -> str:
        s = f"""{self.id}. {self.title} ({self.title_slug})\r\n{self.code_definition}"""
        for tc in self.test_cases:
            s += "\r\n"+tc

        return s
