import pytest
from television import *
class Test:
    def setup_method(self):
        self.tvl = Television()
    def teardown_method(self):
        del self.tvl
    def test_init(self):
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'
    def test_power(self):
        self.tvl.power()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tvl.power()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'
    def