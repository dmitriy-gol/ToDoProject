def add_task(task_number, task_list):
    """ Функция, добавляющее задание """

    task_name = input('Введите название задачи: ')

    while len(task_name) < 3:
        task_name = input('Введите название(не менее 3 символов): ')

    task_list[task_number] = [task_name, False]


def task_done(task_list):
    """ Функция, меняющая статус задания с очереди на выполнено """

    if not task_list:
        print('В списке пока нет задач')
        return

    task = int(input('Введите номер задачи для отметки: '))
    if task in task_list:
        task_list[task][1] = True
    else:
        print(f'Задачи с номером {task} нет в списке')



def delete_task(task_list):
    """ Функция, удаляющая задание """

    if not task_list:
        print('В списке пока нет задач')
        return
    
    task = int(input('Введите номер задачи для удаления: '))
    if task in task_list:
        deleted = task_list.pop(task)
        print(f'Задача {deleted[0]} удалена!')
    else:
        print(f'Задачи с номером {task} нет в списке')
