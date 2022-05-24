#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22
from tqdm import tqdm
from src.CVAT import CVAT
from src.CVAT.data_types import Task
from src.CVAT.utils import image_content_from_kili_prediction
from src.CVAT.Predictions.Interface import IPrediction

API: CVAT = CVAT()

# interface: dict = CVAT.get_json_from_file("../interface_foodvisor.json")
# prediction: IPrediction = API.get_prediction_from_file(task, "foodvisor",
#                                                            "./foodvisor_valid_12_2021_Fromages_gmd_predictions.json")
# API.add_interface_to_project(project=6, interface=interface)
# API.upload_predictions(task, prediction)

if __name__ == "__main__":
    prediction: list[dict] = CVAT.get_json_from_file("./foodvisor_valid_12_2021_Fromages_gmd_predictions.json")
    directory: str = "data/Images/Fromages"
    interface: dict = CVAT.get_json_from_file("../interface_foodvisor.json")
    # images_path: list[str] = image_content_from_kili_prediction(prediction, directory)
    # API.create_project("TEST_API", interface=interface)
    project_id = API.get_project_by_name("TEST_API")
    # task: Task = Task("TEST_UPLOAD_LOCAL_FILE", project_id=project_id)
    # task = API.create_task(task)
    task = API.get_task_by_name("TEST_UPLOAD_LOCAL_FILE")
    a = 0
    # API.add_local_images_to_task(task=task, images_path=images_path)
