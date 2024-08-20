# Функціонал бота помічника, котрий приймає, записує та виводить контакти від користувача


def input_error(func):
    # Функція,яка оброблює помилки вводу користувача.
    # Використовується як декоратор для всіх функцій, що приймають дані від користувача
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments provided."
    return inner


def parse_input(user_input):
    # Функція котра приймає дані від користувача і нормалізує їх
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    # Функція для додавання нового контакту користувачем
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    # Функція для внесення змін у вже існуючий контакт
    if len(args) != 2:
        return "Error: Please provide exactly 2 arguments: username and phone."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    else:
        return f"Error: Contact {name} does not exist."

@input_error
def get_phone(args, contacts):
    # Функція для виводу контакту по запиту користувача
    if len(args) != 1:
        return "Error: Please provide exactly 1 argument: username."
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}."
    else:
        return f"Error: Contact {name} not found."


def show_all_contacts(contacts):
    # Функція для виводу всього списку контактів
    if not contacts:
        return "No contacts found."
    
    result = "All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()




def main():
    # Функція, котра запускає в дію всі попередні функції, виконує безпосередній функціонал бота
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:    #Нескінченний цикл для постійного запиту даних у користувача
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
    # Перевірка запитів користувача, в залежності від їх модіфікацій активується визначена функція
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


