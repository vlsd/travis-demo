import unittest
import curses 


class SpewTest(unittest.TestCase):

    def test_spew(self):
        self.assertIn('is', curses.verbs)
