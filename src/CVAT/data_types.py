#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/16/22
from typing import Optional, Any

TYPE_REF = {int, str, type(None), list, dict, bool, float}


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


class PatchedLabel(CVATData):
    def __init__(self):
        self.id: Optional[int] = None
        self.name: Optional[str] = None
        self.color: Optional[str] = None
        self.attributes: list[dict] = []
        self.deleted: bool = False

    @staticmethod
    def from_json(json_response: dict):
        new_obj: PatchedLabel = PatchedLabel()
        new_obj.id = get_key_value(json_response, "id")
        new_obj.name = get_key_value(json_response, "name")
        new_obj.color = get_key_value(json_response, "color")
        new_obj.attributes = get_key_value(json_response, "attributes")
        new_obj.deleted = get_key_value(json_response, "deleted")
        return new_obj


class Task(CVATData):
    def __init__(self, name, labels: Optional[list[PatchedLabel]] = None, project_id: Optional[int] = None):
        self.name: str = name
        self.labels: list[PatchedLabel] = labels
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

        labels: Optional[list[dict]] = get_key_value(json_response, "labels")
        new_task.labels = [PatchedLabel.from_json(label) for label in labels] if labels is not None else None
        new_task.project_id = get_key_value(json_response, "project_id")
        new_task.url = get_key_value(json_response, "url")
        new_task.id = get_key_value(json_response, "id")
        new_task.mode = get_key_value(json_response, "mode")

        owner: Optional[dict] = get_key_value(json_response, "owner")
        new_task.owner = BasicUser.from_json(owner) if owner is not None else None

        assignee: Optional[dict] = get_key_value(json_response, "assignee")
        new_task.assignee = BasicUser.from_json(assignee) if assignee is not None else None
        new_task.owner_id = get_key_value(json_response, "owner_id")
        new_task.assignee_id = get_key_value(json_response, "assignee_id")
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


class Image(CVATData):
    def __init__(self, json_response: dict, frame: int):
        self.width: int = json_response["width"]
        self.height: int = json_response["height"]
        self.name: str = json_response["name"]
        self.frame_number: int = frame

class LabeledImage(CVATData):
    def __init__(self):
        self.id: Optional[int] = None
        self.frame: Optional[int] = None
        self.label_id: Optional[int] = None
        self.group: Optional[int] = None
        self.source: Optional[str] = None
        self.attributes: list[dict] = []

    @staticmethod
    def from_json(json_response: dict):
        new_labeled_image: LabeledImage = LabeledImage()
        new_labeled_image.id = get_key_value(json_response, "id")
        new_labeled_image.frame = get_key_value(json_response, "frame")
        new_labeled_image.label_id = get_key_value(json_response, "label_id")
        new_labeled_image.group = get_key_value(json_response, "group")
        new_labeled_image.source = get_key_value(json_response, "source")
        new_labeled_image.attributes = get_key_value(json_response, "attributes")
        return new_labeled_image


class LabeledShape(CVATData):
    def __init__(self):
        self.type: Optional[str] = None
        self.occluded: Optional[bool] = None
        self.z_order: Optional[int] = None
        self.rotation: Optional[float] = None
        self.points: Optional[list[float]] = None
        self.id: Optional[int] = None
        self.frame: Optional[int] = None
        self.label_id: Optional[int] = None
        self.group: Optional[int] = None
        self.source: Optional[str] = None
        self.attributes: list[dict] = []

    @staticmethod
    def from_json(json_response: dict):
        new_obj: LabeledShape = LabeledShape()
        new_obj.type = get_key_value(json_response, "type")
        new_obj.occluded = get_key_value(json_response, "occluded")
        new_obj.z_order = get_key_value(json_response, "z_order")
        new_obj.rotation = get_key_value(json_response, "rotation")
        new_obj.points = get_key_value(json_response, "points")
        new_obj.id = get_key_value(json_response, "id")
        new_obj.frame = get_key_value(json_response, "frame")
        new_obj.label_id = get_key_value(json_response, "label_id")
        new_obj.group = get_key_value(json_response, "group")
        new_obj.source = get_key_value(json_response, "source")
        new_obj.attributes = get_key_value(json_response, "attributes")
        return new_obj


class TrackedShape(CVATData):
    def __init__(self):
        self.type: Optional[str] = None
        self.occluded: Optional[bool] = None
        self.z_order: Optional[int] = None
        self.rotation: Optional[float] = None
        self.points: Optional[list[float]] = None
        self.id: Optional[int] = None
        self.frame: Optional[int] = None
        self.outside: Optional[bool] = None
        self.attributes: list[dict] = []

    @staticmethod
    def from_json(json_response: dict):
        new_obj: TrackedShape = TrackedShape()
        new_obj.type = get_key_value(json_response, "type")
        new_obj.occluded = get_key_value(json_response, "occluded")
        new_obj.z_order = get_key_value(json_response, "z_order")
        new_obj.rotation = get_key_value(json_response, "rotation")
        new_obj.points = get_key_value(json_response, "points")
        new_obj.id = get_key_value(json_response, "id")
        new_obj.frame = get_key_value(json_response, "frame")
        new_obj.outside = get_key_value(json_response, "outside")

        new_obj.attributes = get_key_value(json_response, "attributes")
        return new_obj


class LabeledTrack(CVATData):
    def __init__(self):
        self.id: Optional[int] = None
        self.frame: Optional[int] = None
        self.label_id: Optional[int] = None
        self.group: Optional[int] = None
        self.source: Optional[str] = None
        self.shapes: list[TrackedShape] = []
        self.attributes: list[dict] = []

    @staticmethod
    def from_json(json_response: dict):
        new_obj: LabeledTrack = LabeledTrack()
        new_obj.id = get_key_value(json_response, "id")
        new_obj.frame = get_key_value(json_response, "frame")
        new_obj.label_id = get_key_value(json_response, "label_id")
        new_obj.group = get_key_value(json_response, "group")
        new_obj.source = get_key_value(json_response, "source")
        shapes = get_key_value(json_response, "shapes")
        new_obj.attributes = [TrackedShape.from_json(shape) for shape in
                              shapes] if shapes is not None else []
        new_obj.attributes = get_key_value(json_response, "attributes")
        # new_obj.attributes = [AttributeVal.from_json(attribute) for attribute in
        #                       attributes] if attributes is not None else []
        return new_obj


class LabeledData(CVATData):
    def __init__(self):
        self.version: int = 0
        self.tags: list[LabeledImage] = []
        self.shapes: list[LabeledImage] = []
        self.tracks: list[LabeledImage] = []

    @staticmethod
    def from_json(json_response: dict):
        new_obj: LabeledData = LabeledData()
        tags: Optional[dict] = get_key_value(json_response, "tags")
        new_obj.tags = [LabeledImage.from_json(tag) for tag in tags] if tags is not None else []
        shapes: Optional[dict] = get_key_value(json_response, "shapes")
        new_obj.shapes = [LabeledShape.from_json(shape) for shape in shapes] if tags is not None else []
        tracks: Optional[dict] = get_key_value(json_response, "tracks")
        new_obj.tracks = [LabeledTrack.from_json(track) for track in tracks] if tracks is not None else []
        return new_obj

    def to_json(self) -> dict:
        return {
            "version": self.version,
            "tags": [elem.to_json() for elem in self.tags],
            "shapes": [elem.to_json() for elem in self.shapes],
            "tracks": [elem.to_json() for elem in self.tracks]
        }
