import csv
file_headers = ['id', 'Фамилия', 'Имя', 'Отчество', 'Телефон', ]

def add_record(user_dict):
    global file_headers
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        max_id = 1
        reader = csv.DictReader(file, fieldnames=file_headers)
        for row in reader:
            if max_id < int(row['id']):
                max_id = int(row['id'])

    with open('phonebook.csv', 'a', encoding='utf-8') as file:
         writer = csv.DictWriter(file, fieldnames=file_headers)
         writer.writerow({'id': max_id + 1, 'Фамилия': user_dict["Фамилия"],
                         'Имя': user_dict["Имя"],
                         'Отчество': user_dict["Отчество"],
                         'Телефон': user_dict["Телефон"]})
