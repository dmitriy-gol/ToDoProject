def add_task(task_number, task_list):
    """ Функция, добавляющее задание """

    task_name = input('Введите название задачи: ')

    while len(task_name) < 3:
        task_name = input('Введите название(не менее 3 символов): ')

    task_list[task_number] = [task_name, False]


def task_done(task_list):
    """ Функция, меняющая статус задания с 'очереди' на 'выполнено' """

    if check_task_list(task_list):
        return

    task_number = int(input('Введите номер задачи для отметки: '))
    if task_number in task_list:
        if task_list[task_number][1]:
            print('Задача уже в списке выполненных.')
            return
        task_list[task_number][1] = True
    else:
        print(f'Задачи с номером {task_number} нет в списке.')



def delete_task(task_list):
    """ Функция, удаляющая задание """

    if check_task_list(task_list):
        return
    
    task_number = int(input('Введите номер задачи для удаления: '))
    if task_number in task_list:
        print(f'Задача {task_list.pop(task_number)[0]} удалена из списка!')
    else:
        print(f'Задачи с номером {task_number} нет в списке')


def check_task_list(task_list):
    """ Функция, проверяющая наличие задач в списке """

    if not task_list:
        print('В списке пока нет задач.')
        return True
