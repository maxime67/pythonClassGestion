from typing import List

from src.models.classroom import Classroom
from src.models.matter import Matter
from src.models.rating import Rating
from src.models.people import People

def getByPeople(ratings: List[Rating], people: People):
    """
    :param ratings:
    :param people:
    :return: List[Rating]
    """
    result = []
    for i in enumerate(ratings):
        if(i[1].getPeople() == people.getPeople()):
            result.append(i)
    return result

def getByClassroom(ratings: List[Rating], classroom: Classroom):
    """
    :param ratings:
    :param classroom:
    :return: List[Rating]
    """
    result = []
    for i in enumerate(ratings):
        if(i[1].getPeople().getClassroom() == classroom):
            result.append(i)
    return result

def getAvgByClassroomAndMatter(matter: Matter, ratings: List[Rating], classroom: Classroom):
    """
    :param ratings:
    :param classroom:
    :return: Float
    """
    result = []
    sum = 0
    for i in enumerate(ratings):
        if(i[1].getPeople().getClassroom() == classroom):
            if(i[1].getMatter() == matter):
                result.append(i)
    for i in enumerate(result):
        sum += i[1].getValue()
    return sum / len(result)