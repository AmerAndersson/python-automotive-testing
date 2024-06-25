import unittest

from module import Math


class TestModule(unittest.TestCase):
    def test_add_two_number(self):
        modules = Math(20, 10)
        result = modules.add()
        self.assertEqual(result, 30)

    def test_subtract_two_number(self):
        modules = Math(20, 10)
        differencece = modules.subtract()
        self.assertEqual(differencece, 10)

    def test_multiply_two_number(self):
        modules = Math(20, 5)
        multiply = modules.multiply()
        self.assertEqual(multiply, 100)

    def test_divide_two_number(self):
        modules = Math(20, 5)
        divided = modules.divide()
        self.assertEqual(divided, 4)

        with self.assertRaises(ValueError):
            modules = Math(20, 0)
            modules.divide()
            


if __name__ == "__main__":
    unittest.main()
