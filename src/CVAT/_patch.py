#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22
import abc

from typing import Optional

import requests
from requests import Response

from src.CVAT.data_types import Task, BasicUser


class Patch:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def assign_user_to_task(self, task: Task, user: BasicUser) -> None:
        """
        It takes a task and a user, and assigns the user to the task

        Args:
          task (Task): Task - the task you want to assign a user to
          user (BasicUser): BasicUser = The user you want to assign to the task.
        """
        body: dict = {"assignee_id": user.id}
        response: Response = self.session.patch(url=f'{self.url}/api/tasks/{task.id}',
                                                json=body)
        if response.status_code != 200:
            raise requests.HTTPError(response.content)
