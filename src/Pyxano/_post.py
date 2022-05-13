#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22
import abc
import json
from typing import Union

from requests import Response

from src.Pyxano import constants
from src.Pyxano.db_classes import RestTask, DbDataset, DbSpec


class Post:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def add_user(self, username: str, password: str, role: str) -> None:
        """
        This function adds a user to the database

        Args:
          username (str): The username of the user you want to add.
          password (str): The password for the user.
          role (str): str - The role of the user. Can be one of the following:
        Raises:
            ValueError: if the user is already in the database
        """
        if role not in constants.ROLES:
            raise ValueError(f'Role <{role}> value error, please select one of the following: {constants.ROLES}')
        body: dict = {
            "username": username,
            "password": password,
            "role": role,
            "preferences": {
                "theme": "white"
            }
        }
        response: Response = self.session.post(url=f'{self.url}/users',
                                               json=body)
        if response.status_code != 201:
            raise ValueError(f'{username}: {json.loads(response.content)["message"]}')

    def create_task(self, name: str, dataset: Union[dict, DbDataset], spec: Union[dict, DbSpec],
                    as_dict: bool = True) -> Union[dict, RestTask]:
        """
        This function creates a task with the given name, dataset, and spec

        Args:
          name (str): The name of the task.
          dataset (Union[dict, DbDataset]): The dataset to use for the task.
          spec (Union[dict, DbSpec]): The spec is the specification of the task. It contains the following fields:
          as_dict (bool): bool = True. Defaults to True

        Returns:
          A dictionary or a RestTask object.
        """
        body: dict = {
            "name": name,
            "dataset": dataset if isinstance(dataset, dict) else dataset.json(),
            "spec": spec if isinstance(spec, dict) else spec.json()
        }
        response: Response = self.session.post(url=f'{self.url}/tasks',
                                               json=body)
        if response.status_code != 201:
            raise ValueError(response.content)
        return json.loads(response.content) if as_dict else RestTask(json.loads(response.content))
