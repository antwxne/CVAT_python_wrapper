#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22

from src.CVAT import CVAT
from src.CVAT.data_types import Task

API: CVAT = CVAT()

if __name__ == "__main__":
    a = Task(name="OLELE", labels=[
        {
            "name": "Mandatory",
            "attributes": []
        }
    ])
    print(a.to_json())
    API.create_task(a)

