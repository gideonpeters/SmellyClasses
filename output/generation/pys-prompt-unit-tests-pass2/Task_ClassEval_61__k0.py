class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_song = None
        self.volume = 50

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)

    def play(self):
        if self.current_song in self.playlist:
            return self.current_song
        else:
            return None

    def stop(self):
        if self.current_song in self.playlist:
            return True
        else:
            return False

    def switch_song(self):
        if self.current_song in self.playlist:
            index = self.playlist.index(self.current_song)
            if index < len(self.playlist) - 1:
                self.current_song = self.playlist[index + 1]
                return True
            else:
                return False
        else:
            return False

    def previous_song(self):
        if self.current_song in self.playlist:
            index = self.playlist.index(self.current_song)
            if index > 0:
                self.current_song = self.playlist[index - 1]
                return True
            else:
                return False
        else:
            return False

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume = volume
            return None
        else:
            return False

    def shuffle(self):
        if self.playlist:
            random.shuffle(self.playlist)
            return True
        else:
            return False
