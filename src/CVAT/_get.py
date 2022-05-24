#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22
import abc
from time import sleep
from typing import Optional, Union

from requests import Response

from .Predictions.Foodvisor import Foodvisor
from .Predictions.Interface import IPrediction
from .data_types import BasicUser, Task, Image, PatchedLabel


class Get:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def get_user_by_username(self, username: str) -> Optional[BasicUser]:
        """
        It takes a username as a string, and returns a BasicUser object if the user exists, or None if the user doesn't
        exist

        Args:
          username (str): The username of the user you want to get.

        Returns:
          A list of BasicUser objects
        """
        response: Response = self.session.get(url=f'{self.url}/api/users?search={username}&limit=10&is_active=true')
        return None if response.json()["count"] < 1 else BasicUser.from_json(response.json()["results"][0])

    def get_task_by_name(self, task_name: str):
        """
        > This function takes a task name as a string and returns a Task object if it exists, otherwise it returns None

        Args:
          task_name (str): The name of the task you want to get.

        Returns:
          A Task object
        """
        response: Response = self.session.get(url=f'{self.url}/api/tasks?search={task_name}&limit=10&is_active=true')
        return None if response.json()["count"] < 1 else Task.from_json(response.json()["results"][0])

    def get_map_external_ids_frame(self, task: Union[Task, str]) -> dict:
        """
        > This function takes a task name or a task object and returns a dictionary of image objects

        Args:
          task (Union[Task, str]): The task you want to get the external ids for.

        Returns:
          A dictionary of Image objects. (name : Image)
        """
        if isinstance(task, str):
            task: Task = self.get_task_by_name(task)
        while True:
            response: Response = self.session.get(url=f'{self.url}/api/tasks/{task.id}/data/meta')
            if response.status_code != 200:
                raise Exception(response.content)
            json_response: dict = response.json()["frames"]
            if json_response:
                break
            sleep(1)  # to wait upload of image
        return {elem["name"].split(".")[0]: Image(elem, idx) for idx, elem in enumerate(json_response)}

    def get_labels_map(self, task: Union[Task, str]) -> dict:
        """
        It takes a task and returns a dictionary of labels

        Args:
          task (Union[Task, str]): The task to get the labels for.
            either class or name

        Returns:
          A dictionary of labels. (label name : PatchedLabel)
        """
        if isinstance(task, str):
            task: Task = self.get_task_by_name(task)
        response: Response = self.session.get(url=f'{self.url}/api/tasks/{task.id}')
        if response.status_code != 200:
            raise Exception(response.content)
        json_response: dict = response.json()["labels"]
        return dict([(elem["name"], PatchedLabel.from_json(elem)) for elem in json_response])

    # Create a prediction by it's name
    PREDICTION_FACTORY: dict = {
        "foodvisor": lambda prediction, frame_map, label_map: Foodvisor(prediction, frame_map, label_map)
    }

    def get_prediction_from_file(self, task: Union[Task, str], prediction_type: str,
                                 prediction_path: str) -> IPrediction:
        """
        > This function takes in a task, a prediction type, and a prediction path, and returns a prediction object

        Args:
          task (Union[Task, str]): The name of the task you want to get the prediction for.
          prediction_type (str): str - the type of prediction.
          prediction_path (str): path to the file with the prediction

        Returns:
          A prediction object
        """
        if isinstance(task, str):
            task: Task = self.get_task_by_name(task)
        if prediction_type not in Get.PREDICTION_FACTORY:
            raise ValueError(
                f'Prediction type must be one of {Get.PREDICTION_FACTORY.keys()}. Actual: {prediction_type}')
        prediction_json: dict = self.get_json_from_file(prediction_path)
        frame_map: dict = self.get_map_external_ids_frame(task)
        labels_map: dict = self.get_labels_map(task)
        return Get.PREDICTION_FACTORY[prediction_type](prediction_json, frame_map, labels_map)

    def get_project_by_name(self, project_name: str) -> int:
        """
        It takes a project name as a string and returns the project ID as an integer

        Args:
          project_name (str): The name of the project you want to get the ID for.

        Returns:
          The project id
        """
        response: Response = self.session.get(url=f'{self.url}/api//projects?search={project_name}')
        if response.status_code != 200:
            raise Exception(response.content)
        for project in response.json()["results"]:
            if project["name"] == project_name:
                return project["id"]
        raise ValueError(f'{project_name}: project not found')
