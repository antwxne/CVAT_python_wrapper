#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/16/22
from typing import Optional, Type, Any

TYPE_REF = [int, str, type(None), list, dict]


def get_key_value(json_response: dict, key: str) -> Optional[Any]:
    return json_response[key] if key in json_response else None


class CVATData:
    def to_json(self) -> dict:
        dest: dict = {}
        for key in self.__dict__:
            if type(self.__dict__[key]) not in TYPE_REF:
                dest[key] = self.__dict__[key].to_json()
            if not isinstance(self.__dict__[key], type(None)):
                dest[key] = self.__dict__[key]
        return dest


class BasicUser(CVATData):
    def __init__(self, username: str):
        self.url: Optional[str] = None
        self.id: Optional[str] = None
        self.username: Optional[str] = username
        self.first_name: Optional[str] = None
        self.last_name: Optional[str] = None
        self.email: Optional[str] = None

    @staticmethod
    def from_json(json_response: dict):
        new_user: BasicUser = BasicUser("")
        new_user.url = get_key_value(json_response, "url")
        new_user.id = get_key_value(json_response, "id")
        new_user.username = get_key_value(json_response, "username")
        new_user.first_name = get_key_value(json_response, "first_name")
        new_user.last_name = get_key_value(json_response, "last_name")
        new_user.email = get_key_value(json_response, "email")
        return new_user


class Task(CVATData):
    def __init__(self, name, labels: Optional[list[dict]] = None, project_id: Optional[int] = None):
        self.name: str = name
        self.labels: list[dict] = labels
        self.project_id: Optional[int] = project_id
        self.url: Optional[str] = None
        self.id: Optional[int] = None
        self.mode: Optional[str] = None
        self.owner: Optional[BasicUser] = None
        self.assignee: Optional[BasicUser] = None
        self.owner_id: Optional[int] = None
        self.assignee_id: Optional[int] = None
        self.bug_tracker: Optional[str] = None
        self.created_date: Optional[str] = None
        self.updated_date: Optional[str] = None
        self.overlap: Optional[int] = None
        self.segment_size: Optional[int] = None
        self.status: Optional[int] = None
        self.segments: Optional[int] = None
        self.data_chunk_size: Optional[int] = None
        self.data_compressed_chunk_type: Optional[str] = None
        self.data_original_chunk_type: Optional[str] = None
        self.size: Optional[int] = None
        self.image_quality: Optional[int] = None
        self.data: Optional[int] = None
        self.dimension: Optional[str] = None
        self.subset: Optional[str] = None
        self.organization: Optional[int] = None

        if self.project_id is None and self.labels is None:
            raise ValueError("Please provide labels or project id")

    @staticmethod
    def from_json(json_response: dict):
        new_task: Task = Task(name="", project_id=0)
        new_task.name = get_key_value(json_response, "name")
        new_task.labels = get_key_value(json_response, "labels")
        new_task.project_id =get_key_value(json_response, "project_id")
        new_task.url = get_key_value(json_response, "url")
        new_task.id = get_key_value(json_response, "id")
        new_task.mode =get_key_value(json_response, "mode")

        owner: Optional[dict] = get_key_value(json_response, "url")
        new_task.owner = BasicUser.from_json(owner) if owner is not None else None

        assignee: Optional[dict] = get_key_value(json_response, "assignee")
        new_task.assignee = BasicUser.from_json(assignee) if assignee is not None else None
        new_task.owner_id = get_key_value(json_response, "owner_id")
        new_task.assignee_id =get_key_value(json_response, "assignee_id")
        new_task.bug_tracker = get_key_value(json_response, "bug_tracker")
        new_task.created_date = get_key_value(json_response, "created_date")
        new_task.updated_date = get_key_value(json_response, "updated_date")
        new_task.overlap = get_key_value(json_response, "overlap")
        new_task.segment_size = get_key_value(json_response, "segment_size")
        new_task.status = get_key_value(json_response, "status")
        new_task.segments = get_key_value(json_response, "segments")
        new_task.data_chunk_size = get_key_value(json_response, "data_chunk_size")
        new_task.data_compressed_chunk_type = get_key_value(json_response, "data_compressed_chunk_type")
        new_task.data_original_chunk_type = get_key_value(json_response, "data_original_chunk_type")
        new_task.size = get_key_value(json_response, "size")
        new_task.image_quality = get_key_value(json_response, "image_quality")
        new_task.data = get_key_value(json_response, "data")
        new_task.dimension = get_key_value(json_response, "dimension")
        new_task.subset = get_key_value(json_response, "subset")
        new_task.organization = get_key_value(json_response, "organization")
        return new_task