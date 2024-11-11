from models.ToDoList import ToDoList

class ToDoListManager:
    def __init__(self):
        self._todo_list: list[ToDoList] = list()

    def add_new_todo_list(self, category_name):
        todo = ToDoList(category_name)
        self._todo_list.append(todo)

    # def add_new_todo_list(self, new_todo):
    #     if self._check_todo_exists(new_todo):
    #         self._todo_list.append(new_todo)
    #     else:
    #         print(f'Category: {new_todo.return_category_name()} exist!')

    def remove_todo_list(self, todo):
        self._todo_list.remove(todo)

    def _check_todo_exists(self, new_todo) -> bool:
        new_category_name = new_todo.return_category_name()
        all_categories_name = map(lambda todo: todo.return_category_name(), self._todo_list)
        return new_category_name in all_categories_name
