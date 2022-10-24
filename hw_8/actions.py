import database as db

phonebook = {}


def get_phonebook():
    return phonebook


def init_phonebook():
    database = db.get_data()
    for line in database:
        contact = line.split(' — ')
        phonebook[contact[0]] = contact[1].replace('\n', '')


def is_contact_exists(name):
    return db.format_name(name) in phonebook


def get_no_contact_error(name):
    return f'Контакта {name} не существует'


def get_duplicate_error(name):
    return f'Контакт с именем {name} уже есть в телефонной книге'


def set_new_contact(name, phone):
    phonebook[db.format_name(name)] = db.format_phone(phone)
    print('Контакт сохранен')


def change_contact(name, phone):
    phonebook[db.format_name(name)] = db.format_phone(phone)
    print('Контакт изменен')


def delete_contact(name):
    phonebook.pop(db.format_name(name))
    print('Контакт удален')


def get_phone(name):
    return phonebook[db.format_name(name)]


def export_phonebook(path):
    db.export_db(path, phonebook)