class Match:
    name = None
    participants = []

    def __init__(self, name=None):
        self.name = name
        self.participants = []

    @property
    def name(self):
        return self.name

    def add_participant(self, participant):
        if len(self.participants) < 2:
            self.participants.append(participant)

    @property
    def participants(self):
        return self.participants

