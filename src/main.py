#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22

from src.CVAT import CVAT
from src.CVAT.data_types import Task

API: CVAT = CVAT()

if __name__ == "__main__":
    API.assign_user_to_task(task_name="667", username="admin")

