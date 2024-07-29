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


if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.sub(1, 55))
