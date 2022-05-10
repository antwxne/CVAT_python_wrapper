#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22
import json
from typing import Optional

from requests import Response, HTTPError
from requests.sessions import Session, session
from src.Pyxano import constants


class Pyxano:
    def __init__(self, username: str = "admin", password: str = "admin", url: str = "http://localhost:3000/api/v1"):
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

    def get_tasks(self) -> list[dict]:
        response: Response = self.session.get(url=f'{self.url}/tasks')
        return json.loads(response.content)

    def get_task(self, name: str) -> dict:
        response: Response = self.session.get(url=f'{self.url}/tasks/{name}')
        content: dict = json.loads(response.content)
        if response.status_code == 400:
            raise ValueError(content["message"])
        return content

    def get_results(self, task_name: str, first: Optional[int] = None) -> list[dict]:
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
        return results[:stop] if first is None else results[:first]

    def get_labels(self, task_name: str, data_id: str) -> list[dict]:
        response: Response = self.session.get(url=f'{self.url}/tasks/{task_name}/labels/{data_id}')
        content: dict = json.loads(response.content)
        return content["annotations"]

    def add_user(self, username: str, password: str, role: str) -> None:
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
        response: Response = self.session.delete(url=f'{self.url}/users/{username}', )
        if response.status_code != 204:
            raise ValueError(response.content)


API: Pyxano = Pyxano()
