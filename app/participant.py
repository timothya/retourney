class Participant:
    name = None

    def __init__(self, name=None):
        self.name = name

    @property
    def name(self):
        return self.name
