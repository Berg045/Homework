import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)
        return finishers

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race_usein_nick(self):
        tournament = Tournament(90, self.usein, self.nick)
        self.all_results['test_race_usein_nick'] = tournament.start()
        self.assertTrue(self.all_results['test_race_usein_nick']
        [max(self.all_results['test_race_usein_nick'].keys())] == "Ник")

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        self.all_results['test_race_andrey_nick'] = tournament.start()
        self.assertTrue(self.all_results['test_race_andrey_nick']
        [max(self.all_results['test_race_andrey_nick'].keys())] == "Ник")

    def test_race_usein_andrey_nick(self):
        tournament = Tournament(90, self.usein, self.andrey, self.nick)
        self.all_results['test_race_usein_andrey_nick'] = tournament.start()
        self.assertTrue(self.all_results['test_race_usein_andrey_nick']
        [max(self.all_results['test_race_usein_andrey_nick'].keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()

import unittest