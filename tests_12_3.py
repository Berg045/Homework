import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def get_distance(self):
        return self.distance

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        runner = Runner("Alice")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.get_distance(), 50)

    def test_run(self):
        runner = Runner("Bob")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.get_distance(), 100)

    def test_challenge(self):
        runner1 = Runner("Charlie")
        runner2 = Runner("Dave")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.get_distance(), runner2.get_distance())

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
    is_frozen = True
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
        self.assertTrue(self.all_results['test_race_usein_nick'][max(self.all_results['test_race_usein_nick'].keys())] == "Ник")

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        self.all_results['test_race_andrey_nick'] = tournament.start()
        self.assertTrue(self.all_results['test_race_andrey_nick'][max(self.all_results['test_race_andrey_nick'].keys())] == "Ник")

    def test_race_usein_andrey_nick(self):
        tournament = Tournament(90, self.usein, self.andrey, self.nick)
        self.all_results['test_race_usein_andrey_nick'] = tournament.start()
        self.assertTrue(self.all_results['test_race_usein_andrey_nick'][max(self.all_results['test_race_usein_andrey_nick'].keys())] == "Ник")

def skip_if_frozen(cls):
    def decorator(func):
        if cls.is_frozen:
            return unittest.skip("Тесты в этом кейсе заморожены")(func)
        else:
            return func
    return decorator

for attr_name in dir(RunnerTest):
    if attr_name.startswith('test_') and callable(getattr(RunnerTest, attr_name)):
        setattr(RunnerTest, attr_name, skip_if_frozen(RunnerTest)(getattr(RunnerTest, attr_name)))

for attr_name in dir(TournamentTest):
    if attr_name.startswith('test_') and callable(getattr(TournamentTest, attr_name)):
        setattr(TournamentTest, attr_name, skip_if_frozen(TournamentTest)(getattr(TournamentTest, attr_name)))

if __name__ == '__main__':
    unittest.main()