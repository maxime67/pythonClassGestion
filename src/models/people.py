from typing import List
from xmlrpc.client import DateTime

from src.models.classroom import Classroom

class People:
    ###
    # Construct
    ###
    def __init__(self, classroom: Classroom, name: str, birthDate: DateTime):
        self.classroom = classroom
        self.name: str = name
        self.birthDate: DateTime = birthDate

    ###
    # GETTER
    ###
    def getPeople(self):
        return self.name
    def getClassroom(self):
        return self.classroom
    def getBirthDate(self):
        return self.birthDate

    ###
    # SETTER
    ###
    def setClassroom(self, classroom: Classroom):
        self.classroom = classroom
    def setBirthDate(self, DateTime):
        self.DateTime = DateTime
    def setName(self, name):
        self.name = name

    ###
    # ToString
    ###
    def __str__(self):
        return str(self.name) + " " + str(self.classroom) + " " + str(self.birthDate)


