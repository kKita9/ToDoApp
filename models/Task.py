from enum import Enum

class TaskStatus(Enum):
    ACTIVE = 1
    INACTIVE = 1

class Task:
    def __init__(self, task_id, task):
        self._task_id = task_id
        self._task = task
        self._status = TaskStatus.ACTIVE

    def return_task_id(self):
        return self._task_id

    def __str__(self):
        return self._task