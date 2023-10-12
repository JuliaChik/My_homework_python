import os

def input_contact():
    # f = open('data.txt', 'r')
    # if not f:
    #     f = open('data.txt', 'w')
    #     f.close()
    # else:
    #     f.close()
    if not os.path.isfile('data.txt'):
        f = open('data.txt', 'w')
        f.close()


    with open('data.txt', 'a', encoding='utf-8') as f:
        user = input('Введите имя, фамилию и телефон: ').strip().split()
        f.write(';'.join(user) + '\n')


def print_contacts():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    for contact in contacts:
        print(*contact.strip().split(';'))


def find_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('По каким параметрам ищем контакт?:\n1. Имя\n2. Фамилия\n3. Телефон')
        command_index = int(input('Команда: '))
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break
    data = input('Введите данные: ')
    print('Найденные контакты: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data == full_contact[command_index-1]:
            print(' '.join(full_contact))
            
def delete_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    
    index_to_delete = int(input('Введите номер контакта для удаления: '))
    
    if 1 <= index_to_delete <= len(contacts):
        del contacts[index_to_delete - 1]
        
        with open('data.txt', 'w', encoding='utf-8') as f:
            for contact in contacts:
                f.write(contact)

def update_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    
    index_to_update = int(input('Введите номер контакта для изменения: '))
    
    if 1 <= index_to_update <= len(contacts):
        new_data = input('Введите новые данные (имя, фамилия и телефон): ').strip().split()
        contacts[index_to_update - 1] = ';'.join(new_data) + '\n'
        
        with open('data.txt', 'w', encoding='utf-8') as f:
            for contact in contacts:
                f.write(contact)