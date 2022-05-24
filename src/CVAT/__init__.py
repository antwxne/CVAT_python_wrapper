#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22
import json
from copy import copy
from typing import Optional

import requests
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

    def add_interface_to_project(self, project: int, interface: dict):
        response: Response = self.session.patch(url=f'{self.url}/api/projects/{project}',
                                                json=interface)
        if response.status_code != 200:
            raise Exception(response.content)

    def add_local_images_to_task(self, task: Task, images_path: list[str], quality: int = 100):
        body: dict = {
            "image_quality": (None, 1),
            "use_zip_chunks": (None, "true"),
            "use_cache": (None, "true"),
            "sorting_method": (None, "lexicographical"),
        }
        files: dict = {}
        # files = {'client_files[{}]'.format(i): open(f, 'rb') for i, f in enumerate(resources)}
        for index, image in enumerate(images_path):
            files[f'client_files[{index}]'] = (image.split("/")[-1], open(image, "rb"), "image/jpeg")

        response: Response = self.session.post(url=f'{self.url}/api/tasks/{task.id}/data',
                                               json=body,
                                               files=files)
        a = 0

    def get_project_by_name(self, project_name: str) -> int:
        response: Response = self.session.get(url=f'{self.url}/api//projects?search={project_name}')
        if response.status_code != 200:
            raise Exception(response.content)
        for project in response.json()["results"]:
            if project["name"] == project_name:
                return project["id"]
        raise ValueError(f'{project_name}: project not found')
