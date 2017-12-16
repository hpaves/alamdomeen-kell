"""Simple unittest for Countdownpy"""
import unittest
import countdown

class TestCountdown(unittest.TestCase):
    """The class for testing"""

    def test_second_input_larger(self):
        """Compares the times to give True or False"""
        self.assertEqual(countdown.second_input_larger("16:00:00", "8:00"), False)
        self.assertEqual(countdown.second_input_larger("8:00:00", "16:00"), True)

    def test_countdown(self):
        """Note that all results are positive"""
        self.assertEqual(countdown.countdown("16:00:00", "6:00"), "14:00:00")
        self.assertEqual(countdown.countdown("6:00:00", "16:00"), "10:00:00")

if __name__ == '__main__':
    unittest.main()
