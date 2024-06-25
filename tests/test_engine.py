"""
let's create a test module named test_engine.py to test the functionality of the Engine class:
"""
import unittest
from engine import Engine


class TestEngine(unittest.TestCase):
    def test_start_with_enough_fuel(self):
        """Tests if the engine starts when there is enough fuel"""
        engine = Engine(fuel_level=10)
        result = engine.start()
        self.assertTrue(engine.is_running)
        self.assertEqual(result, "Engine started")

    def test_start_with_low_fuel(self):
        """Tests if the engine doesn't start when the fuel level is too low"""
        engine = Engine(fuel_level=0)
        result = engine.start()
        self.assertFalse(engine.is_running)
        self.assertEqual(result, "Cannot start, fuel level is too low")


if __name__ == "__main__":
    unittest.main()
