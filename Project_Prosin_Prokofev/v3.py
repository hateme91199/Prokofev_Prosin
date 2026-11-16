to_do_list = []
while True:
    print("1 - Добавить новое задание")
    print("2 - Показать задание")
    print("3 - Удалить дело")
    print("4 - Выход")
    choice = input("Выбор:")
    if choice  == "1":
        name = input("Название задания:")
        to_do_list.append(name) #добавляем задачу в конец списка
        print("Добавлено!")
    elif choice == "2": #при вводе цифры два прога выводит принтом весь список дел
        print(to_do_list)
    elif choice == "3":
        name = input("Какое дело удалить?")
        to_do_list.remove (name)
        print("Удалено")
    elif choice == "4": #при вводе числа 4 программа очищает списк дел, как бы выходим из программы
        break