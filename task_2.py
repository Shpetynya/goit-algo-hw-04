import re

def generator_numbers(text):
    # Використовуємо регулярний вираз для пошуку всіх чисел у тексті
    for match in re.findall(r'\b\d+\.\d+|\b\d+', text):
        # Генеруємо числа как float
        yield float(match)


def sum_profit(text):
    # Використовуємо функцію generator_numbers для отримання всіх чисел з тексту
    return sum(generator_numbers(text))

text = "The company reported profits of 200.50, 1500.75 and 800.25 in the first quarter."
print(f"Total profit: {sum_profit(text)}")