to_do_list = []
while True:
    print("Добавить новое задание")
    print("Показать задание")
    print("Выход")
    choice = input("Выбор:")
    if choice  == "1":
        name = input("Название задания:")
        to_do_list.append(name) #добавляем задачу в конец списка
        print("Добавлено!")
    elif choice == "2": #при вводе цифры два прога выводит принтом весь список дел
        print(to_do_list)
    elif choice == "3": #при вводе числа 3 программа очищает списк дел, как бы выходим из программы
        break