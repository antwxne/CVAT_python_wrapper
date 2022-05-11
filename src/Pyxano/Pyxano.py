#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22
import json
from typing import Optional, Union

from requests import Response
from requests.sessions import Session, session
from src.Pyxano import constants
from src.Pyxano.db_classes import DbResult, RestTask


class Pyxano:
    def __init__(self, username: str = "admin", password: str = "admin", url: str = "http://localhost:3000/api/v1"):
        """
        This function takes in a username, password, and url and uses them to log into the Grafana API

        Args:
          username (str): The username of the user you want to log in as. Defaults to admin
          password (str): str = "admin". Defaults to admin
          url (str): The url of the Grafana instance. Defaults to http://localhost:3000/api/v1

        Raises:
            ValueError: if the credentials aren't correct
        """
        self.session: Session = session()
        self.url: str = url
        self.session.headers = {"Content-Type": "application/json"}
        body: dict = {
            "username": username,
            "password": password
        }
        response: Response = self.session.post(url=f'{self.url}/login', data=json.dumps(body))
        if response.status_code != 200:
            raise ValueError("Bad credentials")

    def get_tasks(self, as_dict: bool = True) -> Union[list[dict], list[RestTask]]:
        """
        > This function returns a list of dictionaries or a list of RestTask objects, depending on the value of the as_dict
        parameter

        Args:
          as_dict (bool): bool = True. Defaults to True

        Returns:
          A list of dictionaries or a list of RestTask objects.
        """
        response: Response = self.session.get(url=f'{self.url}/tasks')
        content: list[dict] = json.loads(response.content)
        return content if as_dict else [RestTask(value) for value in content]

    def get_task(self, name: str, as_dict: bool = True) -> Union[dict, RestTask]:
        """
        > This function returns a task object from the server

        Args:
          name (str): str - The name of the task to get.
          as_dict (bool): If True, returns a dictionary of the task. If False, returns a RestTask object. Defaults to True

        Returns:
          A dictionary or a RestTask object.

        Raises:
            ValueError: if the task doesn't exist
        """
        response: Response = self.session.get(url=f'{self.url}/tasks/{name}')
        content: dict = json.loads(response.content)
        if response.status_code == 400:
            raise ValueError(content["message"])
        return content if as_dict else RestTask(content)

    def get_results(self, task_name: str, first: Optional[int] = None, as_dict: bool = True) -> Union[list[dict], list[DbResult]]:
        """
        > This function gets the results of a task from the database and returns them as a list of dictionaries or a list of
        DbResult objects

        Args:
          task_name (str): The name of the task you want to get results for.
          first (Optional[int]): The number of results to return. If None, all results will be returned.
          as_dict (bool): If True, returns a list of dictionaries. If False, returns a list of DbResult objects. Defaults to
        True

        Returns:
          A list of dictionaries or a list of DbResult.
        """
        stop: int = 1
        current: int = 0
        page: int = 1
        results: list[dict] = []
        while current <= stop:
            response: Response = self.session.get(url=f'{self.url}/tasks/{task_name}/results?page={1}&count=100')
            content: dict = json.loads(response.content)
            stop = content["counter"]
            results.extend(content["results"])
            current = len(results)
            page += 1
        results = results[:stop] if first is None else results[:first]
        return results if as_dict else [DbResult(result) for result in results]

    def get_labels(self, task_name: str, data_id: str) -> list[dict]:
        """
        > This function returns a list of dictionaries, each of which contains the label information for a single label

        Args:
          task_name (str): The name of the task you want to get the labels for.
          data_id (str): The id of the data you want to get the labels for.

        Returns:
          A list of dictionaries.
        """
        response: Response = self.session.get(url=f'{self.url}/tasks/{task_name}/labels/{data_id}')
        content: dict = json.loads(response.content)
        return content["annotations"]

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
                                               data=json.dumps(body))
        if response.status_code != 201:
            raise ValueError(f'{username}: {json.loads(response.content)["message"]}')

    def delete_user(self, username: str):
        """
        It deletes a user from the database.

        Args:
          username (str): The username of the user to delete.

        Raises:
            ValueError: if the user isn't in the database
        """
        response: Response = self.session.delete(url=f'{self.url}/users/{username}', )
        if response.status_code != 204:
            raise ValueError(response.content)

