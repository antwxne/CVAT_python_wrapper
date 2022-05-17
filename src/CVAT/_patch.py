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

    def assign_user_to_task(self, task_name: str, username: str) -> None:
        task: Optional[Task] = self.get_task_by_name(task_name)
        user: Optional[BasicUser] = self.get_user_by_username(username)
        if user is None or task is None:
            raise ValueError(f'{username}: user doesn\'t exist.' if user is None else f'{task_name}: task doesn\'t exist.')
        body: dict = {"assignee_id": user.id}
        response: Response = self.session.patch(url=f'{self.url}/api/tasks/{task.id}',
                                                json=body)
        if response.status_code != 200:
            raise requests.HTTPError(response.content)