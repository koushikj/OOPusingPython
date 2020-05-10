from abc import *


class Songs:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    @abstractmethod
    def play(self):
        pass


class Devotional(Songs):
    def play(self):
        print("played devotional songs")


class Jazz(Songs):
    def play(self):
        print("played Jazz songs")


class MusicPlayer:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.songList = []

    def playlist(self):
        pass

    def addSong(self, song):
        song.play()
        self.total = self.total + song.duration
        self.songList.append(song)

    def getTotalDuration(self):
        print("total minutes played %s :" % (self.total))

    def playAll(self):
        for x in self.songList:
            x.play()


p1 = MusicPlayer("group1")
p1.addSong(Devotional("a", 10))
p1.addSong(Jazz("b", 15))
p1.getTotalDuration()
p1.playAll()
