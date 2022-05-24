#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22
import abc
from typing import Union

from requests import Response

from src.CVAT.data_types import Task


class Delete:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def delete_task(self, task: Union[Task, int]):
        """
        It deletes a task.

        Args:
          task (Union[Task, int]): Union[Task, int]
        """
        task = task.id if isinstance(task, Task) else task
        response: Response = self.session.delete(url=f'{self.url}/api/tasks/{task}')
        if response.status_code != 204:
            raise Exception(response.content)

    def delete_project(self, project_id:int):
        """
        This function deletes a project from the database

        Args:
          project_id (int): The ID of the project you want to delete.
        """
        response: Response = self.session.delete(url=f'{self.url}/api/projects/{project_id}')
        if response.status_code != 204:
            raise Exception(response.content)
