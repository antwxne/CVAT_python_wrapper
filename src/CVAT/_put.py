#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22

import abc

from requests import Response
from src.CVAT.data_types import Task
from src.CVAT.Predictions.Interface import IPrediction


class Put:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def upload_predictions(self, task: Task, prediction: IPrediction) -> None:
        a = prediction.export().to_json()
        response: Response = self.session.put(
            url=f'{self.url}/api/tasks/{task.id}/annotations',
            json=a
        )
        if response.status_code != 200:
            raise Exception(response.content)
