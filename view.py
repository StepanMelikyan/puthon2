import proc
# from proc import read_csv
# from proc import find_contact
# from proc import find_tell
# from proc import add_all


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input('что Вас интересует? '))
    if choice == 1:
        proc.read_csv()
        show_menu()
    elif choice == 2:
        proc.find_contact()
        show_menu()
    elif choice == 3:
        proc.find_tell()
        show_menu()
    elif choice == 4:
        proc.add_all()
        show_menu()
    elif choice == 5:
        proc.save_txt()
        show_menu()
    elif choice == 6:
        print('работа звершена')

























