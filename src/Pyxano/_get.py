#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22
import abc
import json
from typing import Union, Optional

from requests import Response

from src.Pyxano.db_classes import RestTask, DbResult, DbDataset


class Get:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

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
        content: list[dict] = response.json()
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
        content: dict = response.json()
        if response.status_code == 400:
            raise ValueError(content["message"])
        return content if as_dict else RestTask(content)

    def get_results(self, task_name: str, first: Optional[int] = None, as_dict: bool = True) -> Union[
        list[dict], list[DbResult]]:
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
            content: dict = response.json()
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

    def get_datasets(self, as_dict: bool = True) -> Union[list[dict], list[DbDataset]]:
        response: Response = self.session.get(url=f'{self.url}/datasets')
        return response.json() if as_dict else [DbDataset(elem) for elem in response.json()]
