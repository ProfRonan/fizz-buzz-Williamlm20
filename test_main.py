"""Test file for testing the main.py file"""

import unittest
from unittest.mock import patch
import io # for capturing the output
import sys # for restoring the stdout and removing the main module from the cache
import importlib # for importing the main.py file

class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Sets up the test environment by removing the main module from the cache"""
        super().setUp()
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="3")
    def test_prints_fizz_3(self, _mock_input):
        """Testa se o programa imprime Fizz quando o usuário digita 3"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Fizz", captured_output.getvalue().strip())
        self.assertNotIn("Buzz", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="6")
    def test_prints_fizz_6(self, _mock_input):
        """Testa se o programa imprime Fizz quando o usuário digita 6"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Fizz", captured_output.getvalue().strip())
        self.assertNotIn("Buzz", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="9")
    def test_prints_fizz_9(self, _mock_input):
        """Testa se o programa imprime Fizz quando o usuário digita 9"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Fizz", captured_output.getvalue().strip())
        self.assertNotIn("Buzz", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="5")
    def test_prints_buzz_5(self, _mock_input):
        """Testa se o programa imprime Buzz quando o usuário digita 5"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Buzz", captured_output.getvalue().strip())
        self.assertNotIn("Fizz", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="10")
    def test_prints_buzz_10(self, _mock_input):
        """Testa se o programa imprime Buzz quando o usuário digita 10"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Buzz", captured_output.getvalue().strip())
        self.assertNotIn("Fizz", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="20")
    def test_prints_buzz_20(self, _mock_input):
        """Testa se o programa imprime Buzz quando o usuário digita 20"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Buzz", captured_output.getvalue().strip())
        self.assertNotIn("Fizz", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="0")
    def test_prints_fizz_buzz_0(self, _mock_input):
        """Testa se o programa imprime FizzBuzz quando o usuário digita 0"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("FizzBuzz", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="15")
    def test_prints_fizz_buzz_15(self, _mock_input):
        """Testa se o programa imprime FizzBuzz quando o usuário digita 15"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("FizzBuzz", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="30")
    def test_prints_fizz_buzz_30(self, _mock_input):
        """Testa se o programa imprime FizzBuzz quando o usuário digita 30"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("FizzBuzz", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="1")
    def test_prints_1(self, _mock_input):
        """Testa se o programa imprime 1 quando o usuário digita 1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("1", captured_output.getvalue().strip())
        self.assertNotIn("Fizz", captured_output.getvalue().strip())
        self.assertNotIn("Buzz", captured_output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
