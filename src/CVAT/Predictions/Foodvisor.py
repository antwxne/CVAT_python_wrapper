#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/18/22

from src.CVAT.Predictions.Interface import IPrediction
from src.CVAT.data_types import LabeledData


class Foodvisor(IPrediction):
    def __init__(self, prediction: list[dict], frame_map: dict, label_map: dict):
        self.assets: list[Foodvisor.Asset] = [
            Foodvisor.Asset(asset, frame_map[asset["externalId"]], label_map) for asset in prediction if
            asset["externalId"] in frame_map
        ]

    def export(self) -> LabeledData:
        data: list[dict] = []
        for asset in self.assets:
            data.extend(asset.to_json())
        return LabeledData.from_json({
            "shapes": data
        })

    class Asset:
        def __init__(self, json_content: dict, frame: int, label_map: dict):
            self.classe: str = json_content["NOM_CLASSE"]["text"]
            self.category: str = json_content["CLASSE"]["categories"][0]["name"]
            self.annotations: list[Foodvisor.Asset.Annotation] = [
                Foodvisor.Asset.Annotation(annotation, frame, label_map) for annotation in json_content["annotations"]
            ]

        def to_json(self) -> list[dict]:
            return [annotation.to_json() for annotation in self.annotations]

        class Annotation:
            def __init__(self, annotation: dict, frame: int, label_map: dict):
                self.frame: int = frame
                self.points: list[float] = self.get_points(annotation["polyline"])
                self.category: int = label_map[annotation["categories"][0]["name"]]

            def to_json(self) -> dict:
                return {
                    "type": "polyline",
                    "occluded": False,
                    "z_order": 0,
                    "rotation": 0.0,
                    "points": self.points,
                    "frame": self.frame,
                    "label_id": self.category,
                    "source": "manual",
                    "attributes": []
                }

            @staticmethod
            def get_points(polylines: list[dict]) -> list[float]:
                dest: list[float] = []
                for elem in polylines:
                    dest.extend([elem["x"], elem["y"]])
                return dest
