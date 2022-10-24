import View
import Model

def begin_of_work():
    View.main_menu()

def print_file():
    for item in Model.phone_book:
        print(item)
def open_book():
    with open(Model.path, 'r', encoding='UTF_8') as file:
        contacts = file.read().split('\n')
        Model.phone_book = contacts

def save_contact():
    with open(Model.path, 'w', encoding='UTF_8') as file:
        file.write('\n'.join(Model.phone_book))

def add_new_contact():
    id_cont = int(input('Введите id для нового контакта: '))
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    contact = f'{id_cont}; {name}; {surname}; {patronymic}; {phone}; {comment}'
    Model.phone_book.append(contact)
    View.print_file()

def change_contact():
    open_book()
    View.print_file()
    choice_id = int(input('Введите id контакта, который хотите изменить: '))
    contact = Model.phone_book.pop(choice_id).split('; ')
    print(contact)
    print('Выберите, что хотите поменять: \n '
        '1 - имя, 2 - фамилия, 3 - отчество, '
        '4 - номер телефона, 5 -комментарий ?')
    choice = int(input('Ваш выбор: '))
    contact[choice] = input('Введите новое значение: ')
    print(contact)
    Model.phone_book.insert(choice, ';'.join(contact))

def delete_contact():
    open_book()
    View.print_file()
    choice_id = int(input('Введите id контакта для удаления: '))
    Model.phone_book.pop(choice_id)
    View.print_file()

def search_by_contact():
    open_book()

    choice_id = int(input('Введите id контакта, который хотите найти: '))
    contact = Model.phone_book.pop(choice_id)
    print(contact)
    print('\n')




