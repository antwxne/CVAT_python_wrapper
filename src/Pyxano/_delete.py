#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22
import abc

from requests import Response


class Delete:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def delete_user(self, username: str):
        """
        It deletes a user from the database.

        Args:
          username (str): The username of the user to delete.

        Raises:
            ValueError: if the user isn't in the database
        """
        response: Response = self.session.delete(url=f'{self.url}/users/{username}')
        if response.status_code != 204:
            raise ValueError(response.content)

    def delete_task(self, task_name: str):
        """
        It deletes a task from the database.

        Args:
          task_name (str): The task of the user to delete.

        Raises:
            ValueError: if the task isn't in the database
        """
        response: Response = self.session.delete(url=f'{self.url}/tasks/{task_name}')
        if response.status_code != 204:
            raise ValueError(response.content)
