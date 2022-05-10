#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22

ROLES: list[str] = ["admin", "user"]

OBJECTIVES: list[str] = ["to_annotate", "to_validate", "to_correct"]

LABELLING_STATUS: list[str] = OBJECTIVES + ["done", "discard"]

DATA_TYPES: list[str] = ["image", "pcl", "pcl_image", "sequence_pcl", "sequence_image", "sequence_pcl_image"]

SORT_PARAM: list[str] = ["status", "assigned"]
