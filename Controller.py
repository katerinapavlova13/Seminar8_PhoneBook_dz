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
                print('Файл с контактами открыт \n')
                open_book()
            case 2:
                print('Контакт сохранен \n')
                save_contact()
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
main_menu()

def open_book():
    with open(Model.path, 'r', encoding='UTF_8') as file:
        contacts = file.read().split('\n')
        Model.phone_book = contacts
#
def save_contact():
    with open(Model.path, 'w', encoding='UTF_8') as file:
        file.write('\n'.join(Model.phone_book))

def add_contact():
    

def change_contact():


def delete_contact():


def search_by_contact():
