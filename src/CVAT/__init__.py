#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22

from requests import Response
from requests.sessions import Session, session

from ._delete import Delete
from ._get import Get
from ._patch import Patch
from ._post import Post
from ._put import Put
from ._static import Static
from .data_types import Task


class CVAT(Get, Post, Delete, Patch, Put, Static):
    def __init__(self, username: str = "admin", password: str = "admin", url: str = "http://localhost:8080"):
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
        body: dict = {
            "username": username,
            "password": password
        }
        response: Response = self.session.post(url=f'{self.url}/api/auth/login',
                                               json=body)
        self.session.headers = {"Authorization": f'Token {response.json()["key"]}'}
        if response.status_code != 200:
            raise ValueError("Bad credentials")
