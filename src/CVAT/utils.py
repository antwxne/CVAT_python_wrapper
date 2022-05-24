#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/23/22
from pathlib import Path

from tqdm import tqdm

from src.CVAT import CVAT


def image_content_from_kili_prediction(prediction: list[dict], directory: str) -> list[str]:
    paths: list[str] = []
    for elem in tqdm(prediction, unit="Image"):
        path: str = f'{directory}/{elem["externalId"]}'
        paths.append(CVAT.download_image(elem["content"], path))
    return paths
