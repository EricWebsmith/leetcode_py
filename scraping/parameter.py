import re


def fix_type(type: str) -> str:
    """make the type 3.10 style"""
    print(type)
    fixed_type = type
    fixed_type = fixed_type.replace('List[', 'list[')
    fixed_type = re.sub(r'Optional\[([A-Za-z]+)\]', r'\1 | None', fixed_type)
    return fixed_type


class Parameter:
    def __init__(self, name: str, type: str) -> None:
        self.name: str = name
        self._type: str = fix_type(type)

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        self._type = fix_type(type)
