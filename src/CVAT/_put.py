#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/12/22
import abc
import json
from typing import Union

from requests import Response


class Put:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError