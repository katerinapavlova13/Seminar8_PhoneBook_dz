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


#начало работы
def begin_of_work():
    open_book()       #открываем файл
    View.print_file()  #печатаем
    main_menu()         #выводим главное меню

#открытие файла с контактами
def open_book():
    with open(Model.path, 'r', encoding='UTF_8') as file:
        contacts = file.read().split('\n')
        Model.phone_book = contacts

#записать файл с контактами
def save_contact():
    with open(Model.path, 'w', encoding='UTF_8') as file:
        file.write('\n'.join(Model.phone_book))

# добавление нового контакта
def add_contact():
    index_cont = int(input('Введите индекс контакта: '))
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий')
    contact = f'{index_cont}; {name}; {surname}; {patronymic}; {phone}; {comment}'
    Model.phone_book.append(contact) #производим запись нового контакта в книгу
    View.print_file()

# изменение имеющегося контакта
def change_contact():
    choice_index = input('Введите номер контакта для изменения: ')


# удаление контакта
def delete_contact():
    choice_index = input('Введите номер контакта для удаления: ')
    Model.phone_book.pop(choice_index) #попом удаляем контакт с выбраным индексом из книги
    View.print_file()


# поиск контакта
def search_by_contact():
