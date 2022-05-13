#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22

import json
from typing import Union, Optional, Any


class DbVersion:
    def __init__(self, version: str):
        self.version: str = version

    def json(self) -> dict:
        return {
            "version": self.version
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


class DbUser:
    def __init__(self, values: dict):
        self.username: str = values["username"]
        self.role: str = values["role"]
        self.preference: dict = {"preferences": {"theme": "white"}}
        self.curr_assigned_jobs: dict[str:str] = values["curr_assigned_jobs"]
        self.queue: dict[str:list[str]] = values["queue"]

    def json(self) -> dict:
        return {
            "username": self.username,
            "role": self.role,
            "preferences": self.preference,
            "curr_assigned_jobs": self.curr_assigned_jobs,
            "queue": self.queue
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


class DbDataset:
    def __init__(self, values: dict):
        self.id: str = values["id"]
        self.path: str = values["path"]
        self.data_type: str = values["data_type"]

    def json(self) -> dict:
        return {
            "id": self.id,
            "path": self.path,
            "data_type": self.data_type
        }

    @staticmethod
    def from_json(json_obj: dict):
        return DbDataset(json_obj)

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


class DbData:
    def __init__(self, values: dict):
        self.id: str = values["id"]
        self.dataset_id: str = values["dataset_id"]
        self.type: str = values["type"]
        self.path: Union[str, list[str]] = values["path"]
        self.children: list[DbFrame] = [DbFrame(value) for value in values["children"]]
        self.thumbnail: Optional[str] = values["thumbnail"] if "thumbnail" in values else None

    def json(self) -> dict:
        return {
            "id": self.id,
            "dataset_id": self.dataset_id,
            "type": self.type,
            "path": self.path,
            "children": self.children,
            "thumbnail": self.thumbnail
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


class DbFrame:
    def __init__(self, values: dict):
        self.timestamp: int = values["timestamp"]
        self.path: Union[str, list[str]] = values["path"]

    def json(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "path": self.path,
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


# Custom Label Specifications
class DbSpec:
    def __init__(self, values: dict):
        self.id: str = values["id"]
        self.plugin_name: str = values["plugin_name"]
        self.data_type: str = values["data_type"]
        self.label_schema: str = values["label_schema"]

    def json(self) -> dict:
        return {
            "id": self.id,
            "plugin_name": self.plugin_name,
            "data_type": self.data_type,
            "label_schema": self.label_schema
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


# An annotation task consists of label specifications and a dataset
class DbTask:
    def __init__(self, values: dict):
        self.name: str = values["name"]
        self.spec_id: str = values["spec_id"]
        self.dataset_id: str = values["dataset_id"]

    def json(self) -> dict:
        return {
            "name": self.name,
            "spec_id": self.spec_id,
            "dataset_id": self.dataset_id
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


class DbJob:
    def __init__(self, values: dict):
        self.id: str = values["id"]
        self.task_name: str = values["task_name"]
        self.data_id: str = values["data_id"]
        self.objective: str = values["objective"]
        self.assigned_to: str = values["assigned_to"]
        self.start_at: int = values["start_at"]
        self.duration: int = values["duration"]
        self.last_update_at: int = values["last_update_at"]

    def json(self) -> dict:
        return {
            "id": self.id,
            "task_name": self.task_name,
            "data_id": self.data_id,
            "objective": self.objective,
            "assigned_to": self.assigned_to,
            "start_at": self.start_at,
            "duration": self.duration,
            "last_update_at": self.last_update_at
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


# Annotation jobs summary for a data item
class DbResult:
    def __init__(self, values: dict):
        self.task_name: str = values["task_name"]
        self.data_id: str = values["data_id"]
        self.finished_job_ids: list[str] = values["finished_job_ids"]
        self.current_job_id: str = values["current_job_id"]
        self.status: str = values["status"]
        self.cumulated_time: int = values["cumulated_time"]
        self.annotator: str = values["annotator"]
        self.validator: str = values["validator"]
        self.in_progress: bool = values["in_progress"]

    def json(self) -> dict:
        return {
            "task_name": self.task_name,
            "data_id": self.data_id,
            "finished_job_ids": self.finished_job_ids,
            "current_job_id": self.current_job_id,
            "status": self.status,
            "cumulated_time": self.cumulated_time,
            "annotator": self.annotator,
            "validator": self.validator,
            "in_progress": self.in_progress
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


# Labels for an image
class DbLabel:
    def __init__(self, values: dict):
        self.task_name: str = values["task_name"]
        self.data_id: str = values["data_id"]
        self.annotations: Any = values["annotations"]

    def json(self) -> dict:
        return {
            "task_name": self.task_name,
            "data_id": self.data_id,
            "annotations": self.annotations
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


# Labels statistic for an image
class DbLabelStatistics:
    def __init__(self, values: dict):
        self.task_name: str = values["task_name"]
        self.data_id: str = values["data_id"]
        self.value: Any = values["value"]

    def json(self) -> dict:
        return {
            "task_name": self.task_name,
            "data_id": self.data_id,
            "value": self.value
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


# User info
class RestUser:
    def __init__(self, values: dict):
        self.id: str = values["id"]
        self.username: str = values["username"]
        self.password: str = values["password"]
        self.role: str = values["role"]
        self.preferences: dict = values["preferences"]

    def json(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "preferences": self.preferences
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


class RestTask:
    def __init__(self, values: dict):
        self.name: str = values["name"]
        self.dataset: DbDataset = DbDataset(values["dataset"])
        self.spec: DbSpec = DbSpec(values["spec"])

    def json(self) -> dict:
        return {
            "name": self.name,
            "dataset": self.dataset.json(),
            "spec": self.spec.json()
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


class RestJobUpdate:
    def __init__(self, values: dict):
        self.objective: str = values["objective"]
        self.comments: Any = values["comments"]

    def json(self) -> dict:
        return {
            "objective": self.objective,
            "comments": self.comments
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)


class RestBatchJobUpdate:
    def __init__(self, values: dict):
        self.job_ids: list[str] = values["job_ids"]
        self.objective: str = values["objective"]

    def json(self) -> dict:
        return {
            "job_ids": self.job_ids,
            "objective": self.objective
        }

    def __repr__(self) -> str:
        return json.dumps(self.json(), indent=2)
