from typing import List

from src.models.rating import Rating
from src.models.classroom import Classroom

class People:
    ###
    # Construct
    ###
    def __init__(self, classroom: Classroom, name: str, age: int, ratings: List[Rating] = None):
        self.classroom = classroom
        self.name: str = name
        self.age: int = age
        self.ratings: List[Rating] = ratings

    ###
    # GETTER
    ###
    def getPeople(self):
        return self.name
    def getClassroom(self):
        return self.classroom
    def getAge(self):
        return self.age
    def getRatings(self):
        return self.ratings

    ###
    # SETTER
    ###
    def setClassroom(self, classroom: Classroom):
        self.classroom = classroom
    def setAge(self, age):
        self.age = age
    def setName(self, name):
        self.name = name
    def addRating(self, rating):
        self.ratings.append(rating)

    ###
    # ToString
    ###
    def __str__(self):
        return str(self.name) + " " + str(self.classroom) + " " + str(self.age) + " " + str(self.ratings)


