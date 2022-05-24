#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/17/22
import abc
import json
from pathlib import Path
from typing import Union

import requests
from requests import Response


def create_dir(folder: str):
    Path(folder).mkdir(parents=True, exist_ok=True)


class Static:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def download_image(url: str, path: str) -> str:
        """
        "Download an image from a URL and save it to a path."

        The first line of the function is a docstring. It's a string that describes what the function does. It's a good idea
        to include a docstring in every function you write

        Args:
          url (str): The URL of the image to download.
          path (str): The path to the file you want to save the image to.

        Returns:
          The url of the image
        """
        response: Response = requests.get(url=url)
        path += "." + response.headers["Content-Type"].split("/")[-1]
        try:
            with open(path, "wb+") as f:
                f.write(response.content)
        except FileNotFoundError:
            create_dir("/".join(path.split("/")[:-1:]))
            with open(path, "wb+") as f:
                f.write(response.content)
        return path

    @staticmethod
    def get_redirect_url(url: str) -> str:
        """
        It takes a URL as input and returns the URL that the input URL redirects to

        Args:
          url (str): The URL to be redirected to.

        Returns:
          The url of the page that the url redirects to.
        """
        response: Response = requests.get(url=url)
        return response.url

    @staticmethod
    def get_json_from_file(path: str) -> Union[dict, list[dict]]:
        with open(path, "r") as f:
            return json.loads(f.read())
