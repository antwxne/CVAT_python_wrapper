#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/17/22
import abc

import requests
from requests import Response


class Static:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def download_image(url: str, path: str) -> str:
        response: Response = requests.get(url=url)
        with open(path, "wb+") as f:
            f.write(response.content)
        return response.url

    @staticmethod
    def get_redirect_url(url: str) -> str:
        response: Response = requests.get(url=url)
        return response.url