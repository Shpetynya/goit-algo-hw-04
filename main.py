from pathlib import Path
path = Path('name_salary.txt')

# Оброблюємо виключення, якщо такого файла не буде існувати
try:  
# Відкриваємо і зчитуємо файл
      with open(path, 'r', encoding="utf-8") as data:
            data = data.read()           
except FileNotFoundError:
      print("File does not exist.")


def total_salary(path):
      '''
      Функція аналізує файл і повертає загальну та середню суму заробітної плати всіх розробників.
      '''    
# Розбиваємо рядок на список і вибираємо з нього значення із зарплатою розробників, перетворюємо у тип даних float
      data_list = data.replace('\n', ',').split(',')
      salary_list = data_list[1::2]
      salary_list = [float(salary) for salary in salary_list]
# Рахуємо загальне і середнє число всіх зарплат
      all_sallarys = sum(salary_list)
      try:
            middle_salary = round((all_sallarys/len(salary_list)),2)
      except ZeroDivisionError:
            middle_salary = 0
# Створюємо кортеж з отриманими значеннями
      total_and_middle_salarys = (all_sallarys, middle_salary)
      return total_and_middle_salarys  
        
print(total_salary(path))