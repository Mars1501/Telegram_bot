db_path = 'database/db.txt'


def get_db_path():
    return db_path


def format_name(name):
    return name


def format_phone(phone):
    return phone


def get_data():
    return open(db_path, 'r')


def export_db(path, phonebook):
    db = open(path, 'w')
    for name, phone in phonebook.items():
        db.write(f'{name} — {phone}\n')
    db.close()


def update_db(phonebook):
    export_db(db_path, phonebook)