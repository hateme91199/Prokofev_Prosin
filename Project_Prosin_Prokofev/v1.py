to_do_list = []
while True:
    print("Добавить новое задание")
    print("Показать задание")
    choice = input("Выбор:")
    if choice  == "1":
        name = input("Название задания:")
        to_do_list.append(name) #добавляем задачу в конец списка
        print("Добавлено!")
    elif choice == "2": #при вводе цифры два прога выводит принтом весь список дел
        print(to_do_list)