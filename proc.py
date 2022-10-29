

# создание списка
def create_lst():
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open("phonebook.csv", 'r', encoding='utf-8') as file:
        for line in file:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    file.close()
    return data


# чтение списка
def read_csv():
    my_str = ''
    count = 0
    for i in create_lst():
        my_str = str(i)
        my_str2 = my_str.replace(":", '-', -1)
        my_str3 = my_str2.replace("'", '', -1)
        my_str4 = my_str3.replace("{", '', -1)
        my_str5 = my_str4.replace("}", '', -1)
        count += 1
        print(f'{count}: {my_str5}')
        print("_" * (5 + len(my_str5)))


# какую фамилию ищем
def what_contact():
    wf = str(input("введите фамилию: ").title())
    return wf


# поиск контакта по фамилии
def find_contact():
    for i in create_lst():
        if i['Фамилия'] == what_contact():
            print(i)
            break
        else:
            print('такой фамилии нет в справочнике')
            break


# какой номер телефона нужно найти
def what_tel():
    wt = str(input("введите номер телеофна: "))
    return wt


# поиск по номеру телефона
def find_tell():
    for i in create_lst():
        if i['Телефон'] == what_tel():
            print(i)
            break
        else:
            print('такого телефона нет в справочнике')
            break


# добавление абонента в справочник
def add_all():
    new_family = str(input("Введите фамилию: ").title())
    new_name = str(input("Введите имя: ").title())
    new_tell = str(input("Введите телефон: "))
    new_description = (input("Введите описание: "))
    new_all = new_family + ',' + new_name + ',' + new_tell + ',' + new_description
    with open("phonebook.csv", "a", encoding="utf-8") as file:
        file.write('\n')
        file.write(new_all)
        file.close()
    print('Готово')


# Сохранение файла в формате txt
def save_txt():
    my_file = open("Output.txt", "w+")
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open("phonebook.csv", 'r', encoding='utf-8') as file:
        for line in file:
            record = dict(zip(fields, line.strip().split(',')))
            create_lst().append(record)
            my_file.write(line)
    my_file.close()
    file.close()
    print('Готово')





