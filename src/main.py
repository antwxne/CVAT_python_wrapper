#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22
import json

from src.CVAT import CVAT
from src.CVAT.data_types import Task
from src.CVAT.Predictions.Interface import IPrediction
from src.CVAT.Predictions.Foodvisor import Foodvisor

API: CVAT = CVAT()






if __name__ == "__main__":

    API.upload_predictions(task, prediction)
