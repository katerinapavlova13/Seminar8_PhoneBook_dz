import View
import Model

def main_menu():
    while True:
        print(  'Главное меню: \n'
                '1. Открыть файл с контактами \n'
                '2. Записать файл с контактами \n'
                '3. Добавить контакт \n'
                '4. Изменить контакт \n'
                '5. Удалить контакт \n'
                '6. Поиск по контактам \n'
                '0. Выход из программы \n')
        choice = int(input('Выберите действие: '))
        match (choice):
            case 1:
                open_book()
                print('Файл с контактами открыт \n')
            case 2:
                save_contact()
                print('Контакт сохранен \n')

            case 3:
                add_contact()
                print('Контакт добавлен\n')
            case 4:
                change_contact()
                print('Контакт изменен\n')
            case 5:
                delete_contact()
                print('Контакт удален\n')
            case 6:
                search_by_contact()
                print('Введите номер контакта, для поиска: ')
            case 0:
                print('Конец работы\n')
                break


#открытие файла с контактами
def open_book():
    with open(Model.path, 'r', encoding='UTF_8') as file:
        contacts = file.read().split('\n')
        Model.phone_book = contacts

#сохранение контакта
def save_contact():
    with open(Model.path, 'w', encoding='UTF_8') as file:
        file.write('\n'.join(Model.phone_book))

# добавление нового контакта
def add_contact():
    index_cont = int(input('Введите индекс контакта: '))
    name = input('')
    surname = input('')
    patronymic = input('')
    phone = input('')
    comment = input('')
    contact = f'{index_cont}; {name}; {surname}; {patronymic}; {phone}; {comment}'
    Model.phone_book.append(contact)
    View.print_file()

# изменение имеющегося контакта
def change_contact():

# удаление контакта
def delete_contact():

# поиск контакта
def search_by_contact():
