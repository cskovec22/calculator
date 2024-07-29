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
            res (float | None): Результат деления или None,
                если произошло деление на ноль.
        """

        try:
            res = a / b
        except ZeroDivisionError:   
            print("Деление на ноль!")
            return None
        return res


if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.div(-6, -0))
