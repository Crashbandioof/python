class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        '''
        Creates a television that is muted, turned off, at the lowest channel
        ,and at the lowest volume
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
    def power(self) -> None:
        '''
        Turns the TV on if the TV is off
        Turns the TV off if the TV is on
        '''
        if self.__status == True:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        '''
        Mutes the TV if it isn't muted
        Unmutes the TV if it's muted
        '''
        if self.__status:
            if self.muted == True:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        '''
        Increases the channel by one if the channel isn't at the max channel
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Decreases the channel by one if the channel isn't at the min channel
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Increases the volume by one if the volume isn't at the max volume
        '''
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__muted = False
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Decreases the volume by one if the volume isn't at the min volume
        '''
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__muted = False
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Returns the power status, channel, and volume
        :return: tv status.
        '''
        if self.__muted:
            return f'Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

