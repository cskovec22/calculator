import os


class Calculator():
    """Калькулятор."""

    def add(self, a: float, b: float) -> float:
        """
        Сложить два числа.

        Параметры:
            a (float): Первое число.
            b (float): Второе число.

        Результат:
            (float): Результат сложения двух чисел.
        """

        return a + b

    def sub(self, a: float, b: float) -> float:
        """
        Вычесть из одного числа другое.

        Параметры:
            a (float): Первое число.
            b (float): Второе число.

        Результат:
            float: Результат вычитания.
        """

        return a - b

    def mul(self, a: float, b: float) -> float:
        """
        Перемножить два числа.

        Параметры:
            a (float): Первое число.
            b (float): Второе число.

        Результат:
            float: Результат умножения двух чисел.
        """

        return a * b

    def div(self, a: float, b: float) -> float | None:
        """
        Поделить одно число на другое.

        Параметры:
            a (float): Первое число.
            b (float): Второе число.

        Результат:
            res (float | str): Результат деления или сообщение об ошибке,
                если произошло деление на ноль.
        """

        try:
            res: float = a / b
        except ZeroDivisionError:
            return "Деление на ноль!"
        return res

    def change_sign(self, a: float) -> float:
        """
        Изменить знак числа.

        Параметры:
            a (float): Число.

        Результат:
            float: Число с измененным знаком.
        """

        return -a


def cls() -> None:
    """Очистить консоль."""

    os.system("cls" if os.name == "nt" else "clear")


def main(calc: Calculator) -> None:
    """
    Функция работы калькулятора.

    Параметры:
        calc (Calculator): Экземпляр калькулятора.
    """

    math_operations = {
        "+": calc.add,
        "-": calc.sub,
        "*": calc.mul,
        "/": calc.div,
        "cs": calc.change_sign
    }
    operation: str | None = None
    number: float | None = None
    current_value: float | None = None

    while True:
        input_item = input(
            "Введите число, операцию (+, -, *, /, cs) или 'q' для выхода: "
        )
        cls()

        if input_item == "q":
            break

        if input_item in math_operations and current_value is not None:
            operation = input_item
            if operation == "cs" and current_value is not None:
                current_value = math_operations[operation](current_value)
            print(current_value)
            continue

        try:
            number = float(input_item)
        except ValueError:
            print("Неправильный ввод числа!")
            continue

        if current_value is None or operation is None:
            current_value = number
        elif operation == "cs":
            current_value = math_operations[operation](current_value)
        else:
            current_value = math_operations[operation](current_value, number)
        operation = None

        print(current_value)


if __name__ == "__main__":
    cls()
    calculator: Calculator = Calculator()
    main(calculator)
