from datetime import datetime as dt

def get_logger(operation, result):
    time = dt.now()
    with open('log.txt', 'a') as file:
        file.write(f'операция {operation} выполнена, в {time}, результат {result} \n')