"""Модуль арифметических операций."""


def add(a: float, b: float) -> float:
    """Возвращает сумму двух чисел."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Возвращает разность двух чисел."""
    raise NotImplementedError

def subtract(a: float, b: float) -> float:
    """Возвращает разность двух чисел."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Возвращает произведение двух чисел."""
    return a * b

def divide(a: float, b: float) -> float:
    """Возвращает частное двух чисел.

    Raises:
        ZeroDivisionError: если b равно нулю.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return a / b