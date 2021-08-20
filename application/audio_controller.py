from threading import Thread
import vlc
import pafy


class AudioController(object):
    POOL_TIME = 5  # Seconds
    myThread = Thread()

    def __init__(self):
        pass

    def get_url(self, country):
        if country == "United States":
            url = "https://www.youtube.com/watch?v=M1wLtAXDgqg"
        elif country == "Denmark":
            url = "https://www.youtube.com/watch?v=KnjCA-h44QY"
        elif country == "France":
            url = "https://www.youtube.com/watch?v=5g4fhqCSdLQ"
        elif country == "China":
            url = "https://www.youtube.com/watch?v=UctriMuXYS0"
        elif country == "Sweden":
            url = "https://www.youtube.com/watch?v=9LiN57nfjFw"
        elif country == "":
            url = ""
        elif country == "":
            url = ""
        else:
            url = "https://www.youtube.com/watch?v=4V9QQePap9Y"
        video = pafy.new(url)
        best = video.getbest()
        return best.url

    def play_audio(self, country):
        url = self.get_url(country)
        media = vlc.MediaPlayer(url)
        media.play()

    def hacked(self, country):
        self.yourThread = Thread(target=self.play_audio, args=(country,))
        self.yourThread.start()
