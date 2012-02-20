from mock.tests.base import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_basic_subtraction(self):
        """
        Tests that 5 - 3 always equals 2.
        """
        self.assertEqual(5 - 3, 2)