import re
from typing import Callable


def generator_numbers(text: str):
    # Використовуємо регулярний вираз для пошуку всіх чисел у тексті
    for match in re.findall(r' \d+\.\d+ | \d+ ', text):
        # Генеруємо числа як float
        yield float(match)


def sum_profit(text: str, func: Callable) -> float:
    # Використовуємо передану функцію-генератор для отримання всіх чисел з тексту
    return sum(func(text))

text = "The company reported profits of 200.50, 1500.75 and 800.25 in the first quarter."
print(f"Total profit: {sum_profit(text, generator_numbers)}")