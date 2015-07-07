import unittest
from app.match import Match
from app.participant import Participant

class TestMatchObject(unittest.TestCase):

    def setUp(self):
        self.match = Match("MatchName");
        self.participant1 = Participant("Part1")

    def testMatchInit(self):
       self.assertEqual(self.match.name, "MatchName")

    def testAddParticipant(self):
        self.match.add_participant(self.participant1)
        self.assertListEqual(self.match.participants, [self.participant1])

    def testAddingMoreThanTwoParticipants(self):
        for i in range(3):
            self.match.add_participant(self.participant1)
        self.assertEqual(len(self.match.participants), 2)

if __name__ == '__main__':
    unittest.main()
