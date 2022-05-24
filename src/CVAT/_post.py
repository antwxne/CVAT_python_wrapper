#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22

import abc
import json
from typing import Optional

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

    def create_project(self, project_name: str, interface: Optional[dict] = None) -> int:
        """
        It creates a project with the name `project_name` and returns the project id

        Args:
          project_name (str): The name of the project you want to create.
          interface (Optional[dict]): dict = {

        Returns:
          The project ID
        """
        try:
            project_id: int = self.get_project_by_name(project_name)
        except ValueError:
            body: dict = {
                "name": project_name
            }
            response: Response = self.session.post(url=f'{self.url}/api/projects',
                                                   json=body)
            if response.status_code != 201:
                raise Exception(response.content)
            project_id: int = response.json()["id"]
            if interface:
                self.add_interface_to_project(project_id, interface)
        return project_id
