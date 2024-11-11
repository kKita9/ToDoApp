from models.Task import Task

class ToDoList:
    def __init__(self, category_name):
        self._category_name = category_name
        self._task_list = list()
        self._last_task_id = 0

    def return_category_name(self):
        return self._category_name

    def add_new_task(self, new_task):
        if len(new_task) != 0:
            new_task_id = self._last_task_id + 1
            task = Task(new_task_id, new_task)
            self._task_list.append(task)

    def remove_task(self, task):
        if self._check_task_in_list(task):
            self._task_list.remove(task)

    def show_tasks(self):
        print(f'{self._category_name}:')
        for task in self._task_list:
            print(f'- {task}')

    def _check_task_in_list(self, task):
        return task in self._task_list

    def _check_if_empty(self):
        return True if len(self._task_list) == 0 else False




