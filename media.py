from abc import ABC, abstractmethod


class Media(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Video(Media):
    def play(self):
        print("Video oynatılıyor.")

    def stop(self):
        print("Video durduruldu.")

class Audio(Media):
    def play(self):
        print("Audio oynatılıyor.")

    def stop(self):
        print("Audio durduruldu.")

video = Video()
video.play()
video.stop()
audio = Audio()
audio.play()
audio.stop()