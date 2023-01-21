import re


def fix_type(type: str) -> str:
    """make the type 3.10 style"""
    fixed_type = type
    fixed_type = fixed_type.replace("List[", "list[")
    fixed_type = re.sub(r"Optional\[([A-Za-z]+)\]", r"\1 | None", fixed_type)
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

    @classmethod
    def from_code(cls, parameter_code: str) -> "Parameter":
        parameter_code.strip()
        if parameter_code == "self":
            return Parameter("self", "")
        elif ":" not in parameter_code:
            return Parameter(parameter_code, "any")
        else:
            name, ptype = parameter_code.split(":")
            return Parameter(name, ptype)
