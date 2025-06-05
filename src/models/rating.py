from people import People
from matter import Matter
class Rating:

    ###
    # Constructeur
    ###
    def __init__(self, people: People, matter: Matter, value, note = "pas de note"):
        self.people: People = people
        self.matter: Matter = matter
        self.value: float = value
        self.note: str = note

    ###
    # GETTER
    ###
    def getPeople(self):
        return self.people
    def getMatter(self):
        return self.matter
    def getValue(self):
        return self.value
    def getNote(self):
        return self.note

    ###
    # SETTER
    ###
    def setPeople(self, people):
        self.people = people
    def setMatter(self, matter):
        self.matter = matter
    def setValue(self, value):
        self.value = value
    def setNote(self, note):
        self.note = note


    ###
    # ToString
    ###
    def __str__(self):
        return str(self.people) + " " + str(self.matter) + " " + str(self.value)