from pathlib import Path
path = Path('name_salary.txt')

'''
Функція аналізує файл і повертає загальну та середню суму заробітної плати всіх розробників.
'''

def total_salary(path):
  # Оброблюємо виключення, якщо такого файла не буде існувати
    try:  
      # Відкриваємо і зчитуємо файл
        with open('name_salary.txt', 'r', encoding="utf-8") as data:
            data = data.read()
      # Розбиваємо рядок на список і вибираємо з нього значення із зарплатою розробників, перетворюємо у тип даних int
            data_list = data.replace('\n', ',').split(',')
            salary_list = data_list[1::2]
            salary_list = [int(salary) for salary in salary_list]
      # Рахуємо загальне і середнє число всіх зарплат
            all_sallarys = sum(salary_list)
            middle_salary = all_sallarys//len(salary_list)
      # Створюємо кортеж з отриманими значеннями
            total_and_middle_salarys = (all_sallarys, middle_salary)
        return total_and_middle_salarys

    except FileNotFoundError:
        print("File does not exist.")
            
                        
        
print(total_salary(path))