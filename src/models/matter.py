class Matter:

    def __init__(self, name: str):
        self.name: str = name

    ###
    # GETTER
    ###
    def getName(self):
         return self.name

    ###
    # SETTER
    ###
    def setName(self, name):
         self.name = name

    ###
    # toString
    ###
    def __str__(self):
        return str(self.name)
