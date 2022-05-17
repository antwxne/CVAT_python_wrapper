#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22
import abc
from typing import Optional
from requests import Response
from src.CVAT.data_types import BasicUser, Task


class Get:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def get_user_by_username(self, username: str) -> Optional[BasicUser]:
        response: Response = self.session.get(url=f'{self.url}/api/users?search={username}&limit=10&is_active=true')
        return None if response.json()["count"] < 1 else BasicUser.from_json(response.json()["results"][0])

    def get_task_by_name(self, task_name: str):
        response: Response = self.session.get(url=f'{self.url}/api/tasks?search={task_name}&limit=10&is_active=true')
        return None if response.json()["count"] < 1 else Task.from_json(response.json()["results"][0])
