import Model
import Controller
import time

def main_menu():
    while True:
        print('Главное меню:\n'
            '1. Открыть файл с контактами \n'
            '2. Записать файл с контактами \n'
            '3. Добавить контакт \n'
            '4. Изменить контакт \n'
            '5. Удалить контакт \n'
            '6. Поиск по контактам \n'
            '0. Выход из программы \n')
        choice = int(input('Выберите действие: '))
        match choice:
            case 1:
                print('Открываю телефоную книгу')
                time.sleep(1)
                print('==============================================================')
                Controller.open_book()
                Controller.print_file()
                print('==============================================================')
                time.sleep(1)
            case 2:
                Controller.save_contact()
                print('Файл сохранен \n')
            case 3:
                Controller.add_new_contact()
                print('Контакт добавлен\n')
            case 4:
                Controller.change_contact()
                print('Контакт изменен')
            case 5:
                Controller.delete_contact()
                print('Контакт удален')
            case 6:
                Controller.search_by_contact()
                print('Контакт который вы искали')
            case 0:
                print('Конец работы')
                break
