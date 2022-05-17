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

    def add_remote_data_to_task(self, task_id: int, urls: list[str], image_quality: int = 100) -> None:
        body: dict = {"image_quality": image_quality}
        self.session.post(url=f'{self.url}/api/tasks/{task_id}/data?Upload-Start=True',
                          json=body)
        body["remote_files"] = urls
        response: Response = self.session.post(
            url=f'{self.url}/api/tasks/{task_id}/data?Upload-Multiple={len(urls) > 1}',
            json=body)
        if response.status_code != 202:
            raise ValueError(response.content)
