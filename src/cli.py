"""CLI-интерфейс калькулятора."""

import argparse
import sys

from calculator import add, subtract, multiply, divide

OPERATIONS = {
    "add": add,
    "sub": subtract,
    "mul": multiply,
    "div": divide,
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Простой калькулятор")
    parser.add_argument("operation", choices=OPERATIONS.keys())
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    args = parser.parse_args()

    try:
        result = OPERATIONS[args.operation](args.a, args.b)
        print(f"Результат: {result}")
        return 0
    except ZeroDivisionError as e:
        print(f"Ошибка вычисления: {e}. Проверьте введённые значения.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())