from pathlib import Path
# Функція для читяння файла і повернення списка словників з інформацією про котів
def get_cats_info(path):
    '''
    Функция читає файл и поветає список словарів з інформацією про кожного кота.
    '''
    try:
        # Відкриваємо і читаємо файл
        with open(path, 'r', encoding="utf-8") as file:
            data = file.read()
        
        # Обробка даних
        data_cats = data.strip().split('\n')  
        data_cats = [item.split(',') for item in data_cats]  
        
        # Список ключів
        cat_keys = ['id', 'name', 'age']
        
        # Формуємо список словарів
        cats_list = [
            {cat_keys[i]: data_cats[j][i] for i in range(len(cat_keys))}
            for j in range(len(data_cats))
        ]
        
        return cats_list

    except FileNotFoundError:
        print("File does not exist.")
        return []  


path = Path('cats_info.txt')
print(get_cats_info(path))

