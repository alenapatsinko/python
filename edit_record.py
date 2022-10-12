import csv
def edit(element_edit, new_element):
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        file_headers = ['id', 'Фамилия', 'Имя', 'Отчество', 'Телефон', ]
        reader = csv.DictReader(file, fieldnames=file_headers)
        # for row in reader:
        #     for key, value in enumerate(row):
        #         if value == element_edit:
        #             new_value = key
        #
        # with open('phonebook.csv', 'w', encoding='utf-8') as file:
        #     writer = csv.DictWriter(file, fieldnames=file_headers)
        #     for row in reader:
        #         if
        #     value = new_element
        #     writer.writerow(value)



        #
        for index, row in enumerate(reader):
            for value in row.values():
                if value == element_edit:
                    row_number = index
        file.seek(0)

        with open('phonebook_2.csv', 'w', encoding='utf-8') as file_w:
            writer = csv.DictWriter(file_w, fieldnames=file_headers)
            for index, row in enumerate(reader):
                if index != row_number:
                    writer.writerow(row)
                else:
                    x = []
                    for key, value in enumerate(row):
                        x.append(new_element)
                        writer.writerow(x[value])


