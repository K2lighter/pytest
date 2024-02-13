from src.lesson_1 import Car


def test_first():
    assert Car.model == "Hyundai"
    print(f"Car is : {Car.model}")


def test_second():
    assert 2 == 2
    print("Test passed!!")


def test_5():
    x = 3
    y = 5

#  pytest --alluredir=allure_results
