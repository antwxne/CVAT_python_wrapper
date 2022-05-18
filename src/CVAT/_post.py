#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22

import abc
import json

from requests import Response
from src.CVAT.data_types import Task


class Post:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def create_task(self, task: Task) -> Task:
        """
        It creates a task

        Args:
          task (Task): Task - this is the task object that we want to create.

        Returns:
          A Task object
        """
        body: dict = task.to_json()
        response: Response = self.session.post(url=f'{self.url}/api/tasks', json=body)
        if response.status_code != 201:
            raise ValueError(response.content)
        return Task.from_json(response.json())

    def add_remote_data_to_task(self, task: Task, urls: list[str], image_quality: int = 100) -> None:
        """
        It adds remote data to a task.

        Args:
          task (Task): Task - the task to which you want to add the data
          urls (list[str]): list[str] - a list of urls to add to the task
          image_quality (int): The quality of the image to be uploaded. Defaults to 100
        """
        body: dict = {"image_quality": image_quality}
        self.session.post(url=f'{self.url}/api/tasks/{task.id}/data?Upload-Start=True',
                          json=body)
        body["remote_files"] = urls
        response: Response = self.session.post(
            url=f'{self.url}/api/tasks/{task.id}/data?Upload-Multiple={len(urls) > 1}',
            json=body)
        if response.status_code != 202:
            raise ValueError(response.content)

    def upload_predictions(self, task: Task, format: str, filename: str) -> None:
        """
        Uploads predictions for a given task in a given format to a given filename

        Args:
          task (Task): The task object that you want to upload predictions for.
          format (str): The format of the file you're uploading.
          filename (str): The name of the file to upload.
        """
        # response: Response = self.session.post(
        #     url=f'{self.url}/api/tasks/{task.id}/annotations?format={format}&filename={filename}')
        # if response.status_code != 202:
        #     raise Exception(response.content)
        # response: Response = self.session.post(
        #     url=f'{self.url}/api/tasks/{task.id}/annotations')
        # if response.status_code != 201:
        #     raise Exception(response.content)
        with open(filename, "r") as f:
            body: dict = json.loads(f.read())
        response: Response = self.session.patch(
            url=f'{self.url}/api/tasks/{task.id}/annotations?action=create&format={format}&filename={filename}',
            json=body
        )
        if response.status_code != 204:
            raise Exception(response.content)