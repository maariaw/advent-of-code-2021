class OperationFactory:
    @staticmethod
    def get_operation(type):
        operations = [
            Sum(),
            Product(),
            Minimum(),
            Maximum(),
            "literal value",
            GreaterThan(),
            LessThan(),
            EqualTo()
        ]
        return operations[type]

class Sum:
    def calculate(self, values: list):
        total = 0
        for value in values:
            total += value
        return total

class Product:
    def calculate(self, values: list):
        total = 1
        for value in values:
            total *= value
        return total

class Minimum:
    def calculate(self, values: list):
        return min(values)

class Maximum:
    def calculate(self, values: list):
        return max(values)

class GreaterThan:
    def calculate(self, values: list):
        if values[0] > values[1]:
            return 1
        return 0

class LessThan:
    def calculate(self, values: list):
        if values[0] < values[1]:
            return 1
        return 0

class EqualTo:
    def calculate(self, values: list):
        if values[0] == values[1]:
            return 1
        return 0
