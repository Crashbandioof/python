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
    def test_muted(self):
        self.tvl.power()
        self.tvl.volume_up()
        self.tvl.mute()
        assert self.tvl.__str__() == 'Volume = 0'

        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 1' #tests when tv is on and unmuted

        self.tvl.mute()
        self.tvl.power()
        assert self.tvl.__str__() == 'Volume = 0' #Off and muted

        self.tvl.power()
        self.tvl.mute()
        self.tvl.power()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 1'#off and unmuted

    def test_channel_up(self):
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0' #off, increase

        self.tvl.power()
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 1, Volume = 0' #on, increase

        self.tvl.channel_up()
        self.tvl.channel_up()
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'#increase when channel at maximum
    def test_channel_down(self):
        self.tvl.channel_down()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0' #decrease when tv is off

        self.tvl.power()
        self.tvl.channel_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 3, Volume = 0'# decrease when channel at minumum
    def test_volume_up(self):
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0' #off and vol increased

        self.tvl.power()
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 1' #tuned on an vol increased

        self.tvl.mute()
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 2'#muted and vol increased

        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 2'#vol increased past max
    def test_volume_down(self):
        self.tvl.power()
        self.tvl.volume_up()
        self.tvl.power()
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 1'#tv off and volumed decreased

        self.tvl.power()
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'#tv on and volume decreased

        self.tvl.volume_up()
        self.tvl.volume_up()
        self.tvl.mute()
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 1' #tv muted and volume decreased

        self.tvl.volume_down()
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'#vol decreased past min

