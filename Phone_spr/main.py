from logger import input_contact, print_contacts, find_contact, delete_contact, update_contact

def menu():
    text = (
        "Главное меню:\n"
        "1. Добавить контакт\n"
        "2. Посмотреть все контакты\n"
        "3. Найти контакт\n"
        "4. Изменить контакт\n"
        "5. Удалить контакт\n"
    )
    print(text)
    
    while True:
        command = int(input('Введите команду: \n'))
        if command == 1:
            input_contact()
        elif command == 2:
            print_contacts()
        elif command == 3:
            find_contact()
        elif command == 4:
            update_contact()
        elif command == 5:
            delete_contact()
        elif command == 4:
            # Здесь должна быть логика для изменения контакта
            pass
        elif command == 5:
            # Здесь должна быть логика для удаления контакта
            pass
        elif command == 0:
            break
        else:
            print('Неверная команда. Пожалуйста, выберите существующую команду.')
        print('_' * 30)

if __name__ == '__main__':
    menu()