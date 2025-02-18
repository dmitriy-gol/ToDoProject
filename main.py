from packages.menu import menu, display_task_list
from packages.crud import add_task, task_done, delete_task

def main():
    """ Функция, вызывающая другие функции """

    task_list = {}
    task_number = 1

    menu()
    action = input("Выберите действие: ")
    while action != "4":
        if action == "1":
            add_task(task_number, task_list)
            task_number += 1
        elif action == "2":
            task_done(task_list)
        elif action == "3":
            delete_task(task_list)
        display_task_list(task_list)
        menu()
        action = input("Выберите действие: ")


if __name__ == '__main__':
    main()
