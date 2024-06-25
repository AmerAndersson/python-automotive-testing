"""
A module named engine.py with a 
class Engine that has a method start():

Automotive testing in Python can cover a wide range of activities,
including unit testing, integration testing, and system testing for software components in vehicles. example of how you might approach unit testing for a hypothetical automotive component
using the unittest module in Python.

"""


class Engine:
    def __init__(self, fuel_level):
        self.fuel_level = fuel_level
        self.is_running = False

    def start(self):
        if self.fuel_level > 0:
            self.is_running = True
            return "Engine started"
        else:
            return "Cannot start, fuel level is too low"
