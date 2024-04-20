import unittest
from television import *
class Mytestclass(unittest.TestCase):
    def test_power(self):
        tv_1 = Television()
        self.assertEqual(tv_1.power(), True)
        self.assertEqual(tv_1.power().power(), False)
    def test_mute(self):
        tv_1 = Television()
        self.assertEqual(tv_1.mute(), True)
        self.assertEqual(tv_1.mute().mute(), False)


