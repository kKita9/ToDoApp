from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

from models.ToDoList import ToDoList

class ToDoListManager:
    def __init__(self):
        self._todo_list: list[ToDoList] = list()

    def add_new_todo_list(self, category_name):
        if self._check_category_exist(category_name):
            new_todo_id = self._prepare_new_todo_id()
            new_todo = ToDoList(new_todo_id, category_name)
            self._todo_list.append(new_todo)
        else:
            print(f'Category {category_name} exist!')

    def _prepare_new_todo_id(self):
        if self._check_empty_todo_list():
            return 1
        else:
            return self._todo_list[-1].return_todo_id() + 1

    def _check_empty_todo_list(self):
        return len(self._todo_list) == 0

    def remove_todo_list(self, todo):
        self._todo_list.remove(todo)

    def remove_todo_list_by_id(self, todo_id):
        self._todo_list = list(filter(lambda todo: todo.return_todo_id() != todo_id, self._todo_list))

    def _check_category_exist(self, new_category_name):
        all_categories = map(lambda todo: todo.return_category_name(), self._todo_list)
        return new_category_name not in all_categories

    def _check_todo_exists(self, new_todo) -> bool:
        new_category_name = new_todo.return_category_name()
        all_categories_name = map(lambda todo: todo.return_category_name(), self._todo_list)
        return new_category_name in all_categories_name

    def add_new_task_to_category(self, new_task, category):
        todo = list(filter(lambda td: td.return_category_name() == category, self._todo_list))
        if len(todo) != 0:
           todo = todo[0]
           todo.add_new_task(new_task)
        else:
            print(f'Category: {category} doesn\'t exist!')