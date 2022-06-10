#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22
from tqdm import tqdm
from src.CVAT import CVAT
from src.CVAT.data_types import Task
from src.CVAT.utils import image_content_from_kili_prediction

API: CVAT = CVAT()

# interface: dict = CVAT.get_json_from_file("../interface_foodvisor.json")
# prediction: IPrediction = API.get_prediction_from_file(task, "foodvisor",
#                                                            "./foodvisor_valid_12_2021_Fromages_gmd_predictions.json")
# API.add_interface_to_project(project=6, interface=interface)
# API.upload_predictions(task, prediction)

if __name__ == "__main__":
    # API.create_user("oui", "oui@gmail.com", "kgjhagkjlhlaegkj", "aaa", "aaaa")
    prediction_json: list[dict] = CVAT.get_json_from_file("./foodvisor_valid_12_2021_Fromages_gmd_predictions.json")
    directory: str = "data/Images/Fromages"
    # interface: dict = CVAT.get_json_from_file("../interface_foodvisor.json")
    images_path: list[str] = image_content_from_kili_prediction(prediction_json, directory)
    # project_id: int = API.create_project("TEST_API2", interface=interface)
    # task: Task = Task("jqefhgfdqf", project_id=project_id)
    # task: Task = API.get_task_by_name("qsfqsfqsf")
    # task = API.create_task(task)
    # API.add_local_images_to_task(task=task, images_path=images_path)
    # prediction: IPrediction = API.get_prediction_from_file(task, "foodvisor",
    #                                                        "./foodvisor_valid_12_2021_Fromages_gmd_predictions.json")
    # API.upload_predictions(task, prediction)

