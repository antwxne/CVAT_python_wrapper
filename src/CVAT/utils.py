#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/23/22
import re
import sys
from os import walk
from typing import Optional

from tqdm import tqdm

from . import CVAT


def tryint(s):
    """
    Return an int if possible, or `s` unchanged.
    """
    try:
        return int(s)
    except ValueError:
        return s


def alphanum_key(s):
    """
    Turn a string into a list of string and number chunks.

    #>>> alphanum_key("z23a")
    ["z", 23, "a"]

    """
    return [tryint(c) for c in re.split('([0-9]+)', s)]


def human_sort(l):
    """
    Sort a list in the way that humans expect.
    """
    l.sort(key=alphanum_key)


def get_files_from_path(path: str, to_sort: Optional[bool] = True) -> list[str]:
    """
    It takes a path and returns a list of files in that path

    Args:
      path (str): The path to the directory you want to get the files from.
      to_sort (Optional[bool]): If True, the files will be sorted in a human-friendly way. Defaults to True

    Returns:
      A list of files in the path
    """
    f = next(walk(path), (None, None, []))[2]
    if to_sort:
        human_sort(f)
    return [f'{path}/{file}' for file in f]


def image_content_from_kili_prediction(prediction: list[dict], directory: str) -> list[str]:
    """
    It downloads the images from the Kili API and saves them in the directory you specify

    Args:
      prediction (list[dict]): list[dict]
      directory (str): str = "./images"

    Returns:
      A list of paths to the images.
    """
    paths: list[str] = []
    current_files: list[str] = get_files_from_path(directory)
    files_without_extension: list[str] = [ ]
    for file in current_files:
        splitted:list[str] = file.split(".")
        if splitted[0] != "":
            files_without_extension.append(splitted[0])
        else:
            files_without_extension.append("." + splitted[1])
    print(f'all files {files_without_extension}', file=sys.stderr)
    for elem in tqdm(prediction, unit="Image"):
        path: str = f'{directory}/{elem["externalId"]}'
        if path not in files_without_extension:
            paths.append(CVAT.download_image(elem["content"], path))
            print(f"download {path}...", file=sys.stderr)
        else:
            paths.append(current_files[files_without_extension.index(path)])
    return paths
