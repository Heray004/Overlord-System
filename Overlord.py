from Base.Recognition import Recognition, Thread
from time import sleep


class Overlord(Recognition):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_id = 0

    def cycle(self):

            while True:
                data = self.get_voice()
                if data and data[0][2] == "fifine":
                    self.model_recognition(data[0][3])
                    self.executed(voice_id=data[0][0])
                    self.last_id = data[0][0]
                elif data and data[0][2] != "fifine":
                    print(data)
                    self.deny(voice_id=data[0][0])
                sleep(0.1)


if __name__ == "__main__":
    Over = Overlord()
    Over.cycle()
