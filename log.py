from datetime import datetime as dt

def get_log(operation):
    time = dt.now()
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'Операция {operation} выполнена в {time}\n')
