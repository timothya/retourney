import unittest
from app.participant import Participant

class TestParticipant(unittest.TestCase):

    def setUp(self):
        self.participant = Participant("PartName");

    def testParticipantInit(self):
       self.assertEqual(self.participant.getName(), "PartName")

if __name__ == '__main__':
    unittest.main()
