import unittest
from data.systems import systems
from utils.select_best_heating_system import select_best_heating_system

class TestHeatingSystemSelection(unittest.TestCase):
    def setUp(self):
        self.systems = systems

    def test_select_best_heating_system(self):
        best_system = select_best_heating_system(self.systems)
        self.assertEqual(best_system.name, "Electric Furnace")

# Running the test
test_suite = unittest.TestSuite()
test_suite.addTest(TestHeatingSystemSelection('test_select_best_heating_system'))
test_runner = unittest.TextTestRunner()
test_runner.run(test_suite)
