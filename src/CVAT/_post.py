#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22
import abc
import json
from typing import Union

from requests import Response

from src.CVAT import constants
from src.CVAT.data_types import Task


class Post:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def create_task(self, task: Task):
        body: dict = task.to_json()
        response: Response = self.session.post(url=f'{self.url}/api/tasks', json=body)
        if response.status_code != 201:
            raise ValueError(response.content)
