from src.calculate import Calculator
import pytest
from contextlib import nullcontext as no_raise  # нужно вызывать --- no_raise()


class TestCalculator:

    @pytest.mark.parametrize(
        "x, y, res, expect",
        [
            (1, 2, 0.5, no_raise()),
            (4, 2, 2, no_raise()),
            (3, "-1", -5, pytest.raises(TypeError)),
            (10, 0, 0, pytest.raises(ZeroDivisionError))
        ]
    )
    def test_sub(self, x, y, res, expect):
        print("Тест начался")
        with expect:
            assert Calculator().sub(x, y) == res
            print("Тест окончен")

    @pytest.mark.parametrize(
        "x, y, res, expect",
        [
            (1, 2, 3, no_raise()),
            (10, 20, 30, no_raise()),
            (3, "-1", -3, pytest.raises(TypeError))
        ]
    )
    def test_add(self, x, y, res, expect):
        print("Тест начался")
        with expect:
            assert Calculator().add(x, y) == res
            print("Тест окончен")

# pytest tests/test_calculate.py::TestCalculator -v
