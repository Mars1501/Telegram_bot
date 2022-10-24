from os.path import exists
import database as db
import actions as act
import data_provider as dp


def print_separator():
    print('--------')


def show_menu():
    print_separator()
    print('1 — Добавить новый контакт')
    print('2 — Показать контакт')
    print('3 — Изменить контакт')
    print('4 — Удалить контакт')
    print('5 — Экспортировать данные')
    print('6 — Закрыть приложение')
    return int(input('Выберите пункт меню: '))


def add_contact():
    name = dp.get_name()
    if act.is_contact_exists(name):
        print(act.get_duplicate_error(name))
    else:
        phone = dp.get_phone()
        act.set_new_contact(name, phone)


def view_contact():
    name = dp.get_name()
    if act.is_contact_exists(name):
        print(f'{name}: {act.get_phone(name)}')
    else:
        print(act.get_no_contact_error(name))


def change_contact():
    print('Укажите, какой контакт изменить.')
    name = dp.get_name()
    if act.is_contact_exists(name):
        print(f'Текущий номер: {act.get_phone(name)}')
        print('Введите новый номер.')
        phone = dp.get_phone()
        act.change_contact(name, phone)
    else:
        print(act.get_no_contact_error(name))


def delete_contact():
    print('Укажите, какой контакт удалить.')
    name = dp.get_name()
    if act.is_contact_exists(name):
        act.delete_contact(name)
    else:
        print(act.get_no_contact_error(name))


def export_data():
    path = input('Укажите, куда сохранить данные: ')
    act.export_phonebook(path)
    print('Данные экспортированы')


def run_app():
    if exists(db.get_db_path()):
        act.init_phonebook()

    while True:
        match show_menu():
            case 1:
                add_contact()
            case 2:
                view_contact()
            case 3:
                change_contact()
            case 4:
                delete_contact()
            case 5:
                export_data()
            case 6:
                db.update_db(act.get_phonebook())
                break
            case _:
                db.update_db(act.get_phonebook())
                break