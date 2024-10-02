import unittest
import script

class TestMain(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = script.run_guess_number(guess, answer)
        self.assertEqual(result)

    def test_input_wrong_guess(self):
        answer = 5
        guess = 0
        result = script.run_guess_number(guess, answer)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        answer = 5
        guess = 11
        result = script.run_guess_number(guess, answer)
        self.assertFalse(result)

    def test_input_wrong_dtype(self):
        answer = 5
        guess = '11'
        result = script.run_guess_number(guess, answer)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
