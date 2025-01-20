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

    # def __str__(self):
    #     return self.name

class RunnerTest(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()