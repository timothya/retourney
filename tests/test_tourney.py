import unittest
from app.tourney import Tourney

class TestTourney(unittest.TestCase):

    def setUp(self):
        self.tourney = Tourney("TourneyName");

    def testTourneyInit(self):
       self.assertEqual(self.tourney.getName(), "TourneyName")

if __name__ == '__main__':
    unittest.main()
