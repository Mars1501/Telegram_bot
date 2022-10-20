from datetime import datetime as dt
import view
import model
import logger as log


def make_evaluation():
    log.start_log(dt.now().strftime('%Y-%m-%d_%H-%M-%S'))
    while True:
        dt_data = '%Y:%m:%d::%H:%M:%S'
        user_expression = view.get_user_data()
        log.write_log('Данные пользователя', dt.now().strftime(dt_data), user_expression)
        if user_expression == 'stop':
            log.stop_log()
            break
        result = model.evaluate(user_expression)
        log.write_log('Результат', dt.now().strftime(dt_data), result)
        view.view_result(result)