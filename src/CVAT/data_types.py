#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/16/22
from typing import Optional

TYPE_REF = [int, str, type(None), list, dict]


class CVATData:
    def to_json(self) -> dict:
        dest: dict = {}
        for key in self.__dict__:
            if type(self.__dict__[key]) not in TYPE_REF:
                dest[key] = self.__dict__[key].to_json()
            if type(self.__dict__[key]) != type(None):
                dest[key] = self.__dict__[key]
        return dest


class BasicUser(CVATData):
    def __init__(self, username: str):
        self.url: Optional[str] = None
        self.id: Optional[str] = None
        self.username: Optional[str] = username
        self.first_name: Optional[str] = None
        self.last_name: Optional[str] = None


class Task(CVATData):
    def __init__(self, name, labels: list[dict], owner: Optional[BasicUser] = None,
                 assignee: Optional[BasicUser] = None):
        self.name: str = name
        self.url: Optional[str] = None
        self.id: Optional[int] = None
        self.project_id: Optional[int] = None
        self.mode: Optional[str] = None
        self.owner: Optional[BasicUser] = owner
        self.assignee: Optional[BasicUser] = assignee
        self.owner_id: Optional[int] = None
        self.assignee_id: Optional[int] = None
        self.bug_tracker: Optional[str] = None
        self.created_date: Optional[str] = None
        self.updated_date: Optional[str] = None
        self.overlap: Optional[int] = None
        self.segment_size: Optional[int] = None
        self.segment_size: Optional[int] = None
        self.status: Optional[int] = None
        self.labels: list[dict] = labels
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
