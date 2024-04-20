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
        if self.status == True:
            self.status = False
        else:
            self.status = True
    def mute(self):
        if self.muted == True:
            self.muted = False
        else:
            self.muted = True
    def channel_up(self):
        if self.channel < self.MAX_CHANNEL:
            self.channel += 1
    def channel_down(self):
        if self.channel > self.MIN_CHANNEL:
            self.channel -= 1
    def volume_up(self):
        if self.volume < self.MAX_VOLUME:
            self.volume += 1
    def volume_down(self):
        if self.volume > self.MIN_VOLUME:
            self.volume -= 1
    def __str__(self):
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'