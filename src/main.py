#!/bin/python3
# Created by antoine.desruet@epitech.eu at 5/10/22

from src.Pyxano.Pyxano import Pyxano

API: Pyxano = Pyxano()

if __name__ == "__main__":
    # API.add_user("toto", "popo", "user")
    # API.delete_user("popdsdqddo")
    # API.add_user("popo", "popo", "user")
    result = API.get_tasks(as_dict=False)
    print(result)
