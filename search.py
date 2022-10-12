import csv
def search(element):
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        file_headers = ['id', 'Фамилия', 'Имя', 'Отчество', 'Телефон', ]
        reader = csv.DictReader(file, fieldnames=file_headers)
        for row in reader:
            for key, value in row.items():
                if element == value:
                    print(row)


