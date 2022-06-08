#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/18/22

from .Interface import IPrediction
from src.CVAT.data_types import LabeledData, Image, PatchedLabel


class Foodvisor(IPrediction):
    def __init__(self, prediction: list[dict], frame_map: dict, label_map: dict):
        self.assets: list[Foodvisor.Asset] = [
            Foodvisor.Asset(asset["jsonResponse"], frame_map[asset["externalId"]], label_map) for asset in prediction if
            asset["externalId"] in frame_map
        ]

    def export(self) -> LabeledData:
        shapes: list[dict] = []
        tags: list[dict] = []
        for asset in self.assets:
            shapes.extend(asset.to_shapes())
            tags.extend(asset.to_tags())
        return LabeledData.from_json({
            "tags": tags,
            "shapes": shapes
        })

    class Asset:
        def __init__(self, json_content: dict, image: Image, label_map: dict):
            self.classe: str = json_content["NOM_CLASSE"]["text"]
            self.image = image
            self.bonne_reponse: PatchedLabel = label_map["Bonne reponse"]
            self.choice: PatchedLabel = label_map["Mon choix"]
            content_type: str = self.get_type(json_content)
            self.annotations: list[Foodvisor.Asset.Annotation] = [
                Foodvisor.Asset.Annotation(annotation, image, label_map) for annotation in
                json_content[content_type]["annotations"]
            ]

        def to_shapes(self) -> list[dict]:
            """
            > This function takes in a list of annotations and returns a list of dictionaries

            Returns:
              A list of dictionaries.
            """
            return [annotation.to_json() for annotation in self.annotations]

        def to_tags(self) -> list[dict]:
            """
            > The function takes a `Question` object as input and returns a list of dictionaries, each of which represents a
            tag

            Returns:
              A list of dictionaries.
            """
            tags = [{
                "frame": self.image.frame_number,
                "label_id": self.choice.id,
                "group": 0,
                "source": "manual",
                "attributes": [
                    {
                        "spec_id": self.choice.attributes[0]["id"],
                        "value": "Je ne sais pas"
                    }
                ]
            }]
            if True:
                tags.append(
                    {
                        "frame": self.image.frame_number,
                        "label_id": self.bonne_reponse.id,
                        "group": 0,
                        "source": "manual",
                        "attributes": [
                            {
                                "spec_id": self.bonne_reponse.attributes[0]["id"],
                                "value": self.classe
                            }
                        ]
                    }
                )
            return tags

        @staticmethod
        def get_type(json_content: dict) -> str:
            """
            It returns the first key of the dictionary that is in the set of keys

            Args:
              json_content (dict): the json file

            Returns:
              The type of the json file.
            """
            ref: set[str] = {"ALIMENTS", "MELANGES", "INGREDIENTS", "INGREDIENTS_PETITS", "INDUSTRIELS_EMBALLES"}
            return next(key for key in json_content.keys() if key in ref)

        class Annotation:
            def __init__(self, annotation: dict, image: Image, label_map: dict):
                self.image: Image = image
                self.points: list[float] = self.get_points(annotation["polyline"], image)
                self.label_id: int = label_map[annotation["categories"][0]["name"]].id

            def to_json(self) -> dict:
                return {
                    "type": "polyline",
                    "occluded": False,
                    "z_order": 0,
                    "rotation": 0.0,
                    "group": 0,
                    "points": self.points,
                    "frame": self.image.frame_number,
                    "label_id": self.label_id,
                    "source": "manual",
                    "attributes": []
                }

            @staticmethod
            def get_points(polylines: list[dict], image: Image) -> list[float]:
                """
                `get_points` takes a list of dictionaries and an image, and returns a list of floats

                Args:
                  polylines (list[dict]): list[dict]
                  image (Image): The image to be processed.

                Returns:
                  A list of floats.
                """
                dest: list[float] = []
                for elem in polylines:
                    dest.extend([elem["x"] * image.width, elem["y"] * image.height])
                return dest
