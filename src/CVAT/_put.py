#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22

import abc

from requests import Response

from .Predictions.Interface import IPrediction
from .data_types import Task


class Put:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def upload_predictions(self, task: Task, prediction: IPrediction, display_response: bool = False) -> None:
        """
        It takes a task and a prediction, converts the prediction to JSON, and sends it to the server

        Args:
          task (Task): Task - the task object that you want to upload the prediction to
          prediction (IPrediction): IPrediction - the prediction object that you want to upload
          display_response (bool): bool = False. Defaults to False
        """
        prediction_json: dict = prediction.export(display_response).to_json()
        response: Response = self.session.put(
            url=f'{self.url}/api/tasks/{task.id}/annotations',
            json=prediction_json
        )
        if response.status_code != 200:
            raise Exception(response.content)
