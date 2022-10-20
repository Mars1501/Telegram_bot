log_file = None


def start_log(file_name):
    global log_file
    log_file_name = 'logs/' + file_name + '.txt'
    log_file = open(log_file_name, 'w')


def write_log(title, date_time, data):
    global log_file
    log_file.write(f'{date_time} — {title} — {data}\n')


def stop_log():
    global log_file
    log_file.close()