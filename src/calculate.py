from typing import Union


class Calculator:
    def sub(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        return x / y

    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        return x + y


if __name__ == "__main__":
    calculator = Calculator()

# pytest tests/test_calculate.py -v
# pytest tests/test_calculate.py::test_sub -v -s
