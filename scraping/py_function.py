from scraping.parameter import Parameter


class PyFunction:
    def __init__(self, name: str, parameters: list[Parameter], return_type: str) -> None:
        self.name: str = name
        self.parameters: list[Parameter] = parameters
        self.returnType: str = return_type

    def get_argument_list_code(self) -> str:
        return ", ".join([p.name for p in self.parameters[1:]])

    def get_parameter_list_code(self, with_self=True):
        parameter_code = ""
        for p in self.parameters:
            if p.name == "self":
                if with_self:
                    parameter_code += "self, "
            else:
                parameter_code += f"{p.name}: {p.type}, "
        parameter_code = parameter_code[:-2]
        return parameter_code

    def code(self, indent=4):
        parameter_code = self.get_parameter_list_code()
        prefix = " " * indent
        return "\r\n".join([f"{prefix}def {self.name}({parameter_code}) -> {self.returnType}:" f"{prefix}    ..."])

    def __repr__(self) -> str:
        return self.code()

    def __str__(self) -> str:
        return self.code()

    @classmethod
    def from_code(cls, line: str):
        if "def" not in line:
            return None
        def_at = line.find("def")
        open_parenthesis = line.find("(")
        name = line[def_at + 4: open_parenthesis]
        close_parenthesis = line.rfind(")")

        # return type
        return_type = "None"
        arrow = line.find("->")
        if arrow > 0:
            return_type = line[arrow + 2:]
            return_type = return_type.replace(":", "")
            return_type = return_type.strip()

        # parameters
        parameters_code = line[open_parenthesis + 1: close_parenthesis]
        previous_splitor = 0
        parentheses = 0
        parameters = list[Parameter]()
        for i, c in enumerate(parameters_code + ","):
            if c == "[":
                parentheses += 1
            elif c == "]":
                parentheses -= 1

            if c == "," and parentheses == 0:
                parameter_code = parameters_code[previous_splitor:i]
                parameters.append(Parameter.from_code(parameter_code))
                previous_splitor = i + 1

        return PyFunction(name, parameters, return_type)
