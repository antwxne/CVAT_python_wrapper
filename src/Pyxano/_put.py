#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22
import abc
import json
from typing import Union

from requests import Response

from src.Pyxano import constants
from src.Pyxano.db_classes import DbLabel


class Put:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def add_prediction(self, prediction: DbLabel):
        response: Response = self.session.put(url=f'{self.url}/tasks/{prediction.task_name}/labels/{prediction.data_id}',
                                              json=prediction.json())
        if response.status_code != 204:
            raise ValueError(response.content)