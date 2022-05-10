#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22

import json
from typing import Union, Optional


class DbVersion:
    def __init__(self, version: str):
        self.version: str = version

    def to_json(self) -> dict:
        return {
            "version": self.version
        }

    def __repr__(self) -> str:
        return json.dumps(self.to_json())


class DbUser:
    def __init__(self, values: dict):
        self.username: str = values["username"]
        self.role: str = values["role"]
        self.preference: dict = {"preferences": {"theme": "white"}}
        self.curr_assigned_jobs: dict[str:str] = values["curr_assigned_jobs"]
        self.queue: dict[str:list[str]] = values["queue"]

    def to_json(self) -> dict:
        return {
            "username": self.username,
            "role": self.role,
            "preferences": self.preference,
            "curr_assigned_jobs": self.curr_assigned_jobs,
            "queue": self.queue
        }

    def __repr__(self) -> str:
        return json.dumps(self.to_json())


class DbDataset:
    def __init__(self, values: dict):
        self.id: str = values["id"]
        self.path: str = values["path"]
        self.data_type: str = values["data_type"]

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "path": self.path,
            "data_type": self.data_type
        }

    def __repr__(self) -> str:
        return json.dumps(self.to_json())


class DbData:
    def __init__(self, values: dict):
        self.id: str = values["id"]
        self.dataset_id: str = values["dataset_id"]
        self.type: str = values["type"]
        self.path: Union[str, list[str]] = values["path"]
        self.children = values["children"]
        self.thumbnail: Optional[str] = values["thumbnail"] if "thumbnail" in values else None

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "dataset_id": self.dataset_id,
            "type": self.type,
            "path": self.path,
            "children": self.children,
            "thumbnail": self.thumbnail
        }

    def __repr__(self) -> str:
        return json.dumps(self.to_json())
