import unittest
from app.match import Match
from app.participant import Participant

class TestMatchObject(unittest.TestCase):

    def setUp(self):
        self.match = Match("MatchName");
        self.participant1 = Participant("Part1")

    def testMatchInit(self):
       self.assertEqual(self.match.getName(), "MatchName")

    def testAddParticipant(self):
        self.match.addParticipant(self.participant1)
        self.assertListEqual(self.match.getParticipants(), [self.participant1])

    def testAddingMoreThanTwoParticipants(self):
        self.match.addParticipant(self.participant1)
        self.match.addParticipant(self.participant1)
        self.match.addParticipant(self.participant1)
        self.assertEqual(len(self.match.getParticipants()), 2)

if __name__ == '__main__':
    unittest.main()
