class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL
    def power(self):
        '''
        Turns the TV on if the TV is off
        Turns the TV off if the TV is on
        '''
        if self.status == True:
            self.status = False
        else:
            self.status = True
        return self.status
    def mute(self):
        '''
        Mutes the TV if it isn't muted
        Unmutes the TV if it's muted
        '''
        if self.muted == True:
            self.muted = False
        else:
            self.muted = True
        return self.muted
    def channel_up(self):
        '''
        Increases the channel by one if the channel isn't at the max channel
        '''
        if self.channel < self.MAX_CHANNEL:
            self.channel += 1
        return self.channel
    def channel_down(self):
        '''
        Decreases the channel by one if the channel isn't at the min channel
        '''
        if self.channel > self.MIN_CHANNEL:
            self.channel -= 1
        return self.channel
    def volume_up(self):
        '''
        Increases the volume by one if the volume isn't at the max volume
        '''
        if self.volume < self.MAX_VOLUME:
            self.volume += 1
        return self.volume
    def volume_down(self):
        '''
        Decreases the volume by one if the volume isn't at the min volume
        '''
        if self.volume > self.MIN_VOLUME:
            self.volume -= 1
        return self.volume
    def __str__(self):
        '''
        Returns the power status, channel, and volume
        '''
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'