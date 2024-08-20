def caching_fibonacci():
    '''
    Функція створює та використовує кеш для зберігання і повторного використання 
    вже обчислених значень чисел Фібоначчі
    '''
    # Створюємо порожній словник cache
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        # Обчислюємо та зберігаємо результат у cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        # Повертаємо результат з cache
        return cache[n]

    # Повертаємо функцію fibonacci
    return fibonacci

# Використання
fib = caching_fibonacci()
print(fib(10))  # Повинно вивести 55
print(fib(15))  # Повинно вивести 610