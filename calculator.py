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


if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.add(1, 0.5))
