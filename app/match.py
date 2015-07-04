class Match:
    def __init__(self, name):
        self.name = name
        self.participants = []

    def getName(self):
        return self.name

    def addParticipant(self, participant):
        if len(self.participants) < 2:
            self.participants.append(participant)

    def getParticipants(self):
        return self.participants

