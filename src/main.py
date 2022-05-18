#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22

from src.CVAT import CVAT
from src.CVAT.data_types import Task

API: CVAT = CVAT()

if __name__ == "__main__":
    task: Task = API.get_task_by_name("Test api")
    API.assign_user_to_task(task, task.owner)
    API.upload_predictions(task, format="COCO+1.0", filename="../new_annotations.json")
