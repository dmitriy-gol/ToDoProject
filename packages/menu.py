def menu():
    """ Функция, отображающая меню """

    print('Меню:'
          '\n1 - Добавить задание'
          '\n2 - Отметить задание как выполненное'
          '\n3 - Удалить задание'
          '\n4 - Выход')


def display_task_list(my_todo):
    """ Функция, отображающая список дел """

    print()
    todo_list = {}
    done_list = {}

    for key, value in my_todo.items():
        if value[1]:
            done_list[key] = value
        else:
            todo_list[key] = value
    if todo_list:
        print('----- Задачи в очереди -----')
        for key, value in todo_list.items():
            print(f'{key} - {value[0]}')
    if done_list:
        print('---- Выполненные задачи ----')
        for key, value in done_list.items():
            print(f'{key} - {value[0]}')
    print('----' * 7)
