from sets import CharacterSet, Line, Song
from winsound import PlaySound, SND_ASYNC
from time import sleep as tsleep

class ExitEnter(Song):
    def __init__(self) -> None:
        self._intro_lines: list[Line] = [Line([CharacterSet], 2.5)]

    def intro(self, filename: str) -> None:
        PlaySound(filename, flags=SND_ASYNC)
        for line in self._intro_lines:
            line.print_delay()

def main():
    ee: ExitEnter = ExitEnter()

    ee.intro('./music/exitenter/intro.mp3')