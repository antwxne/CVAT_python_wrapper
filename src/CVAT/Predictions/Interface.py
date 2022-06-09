#!/bin/python3
import abc
from typing import Union

from ..data_types import LabeledData


# This class is an interface for a prediction object.
# You need to inherit from this class to create a new prediction class.
# You also need to reimplement the abstract methods.
class IPrediction:
    @abc.abstractmethod
    def __init__(self, prediction: Union[list[dict], dict], frame_map: dict, label_map: dict):
        """
        This function takes in a prediction, a frame_map, and a label_map and returns a list of tuples of the form
        (frame_id, label_id, confidence)

        Args:
          prediction (Union[list[dict], dict]): The prediction returned by the model.
          frame_map (dict): A dictionary mapping frame names to frame ids.
          label_map (dict): A dictionary mapping the label names to their corresponding integer values.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def export(self, display_response: bool = False) -> LabeledData:
        """
        > This function takes in a boolean value and returns a LabeledData object

        Args:
          display_response (bool): If True, the response will be displayed in the output. Defaults to False
        """
        raise NotImplementedError
