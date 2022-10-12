def get_operation():
    return int(input('введите номер операции: \n1 - добавить данные \n2 - редактирование данных \n3 - поиск данных \n'))

def get_element_search():
    return input('Введите элемент для поиска - ')

def get_edit():
    return input('Введите элемент для редактирования - ')

def get_edit_2():
    return input('Введите заменяющий текст - ')


def get_dict():
    keys = ['Фамилия', 'Имя', 'Отчество', 'Телефон', ]
    user_dict = {}
    for i in range(4):
        user_dict[keys[i]] = input(f'введите {keys[i]} - ')
    return user_dict

def print_result(result):
    print(f'{result}')
    pass
