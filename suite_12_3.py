import unittest
import tests_12_3

# Создание TestSuite и добавление тестов
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)