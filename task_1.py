from pathlib import Path

def total_salary(path):
    '''
    Функція аналізує файл і повертає загальну та середню суму заробітної плати всіх розробників.
    '''
    try:
        # Відкриваємо і зчитуємо файл
        with open(path, 'r', encoding="utf-8") as file:
            data = file.read()
        
        # Розбиваємо рядок на список і вибираємо з нього значення із зарплатою розробників
        data_list = data.strip().split('\n')
        salary_list = [float(line.split(',')[1]) for line in data_list]
        
        # Рахуємо загальну і середню зарплату
        total_salary = sum(salary_list)
        try:
            average_salary = round(total_salary / len(salary_list), 2)
        except ZeroDivisionError:
            average_salary = 0
        
        # Створюємо кортеж з отриманими значеннями
        total_and_average_salaries = (total_salary, average_salary)
        return total_and_average_salaries

    except FileNotFoundError:
        print("File does not exist.")
        return None

# Приклад використання функції
path = Path('name_salary.txt')
print(total_salary(path))