from sets import CharacterSet, Line, Song
from playsound import playsound
from threading import Thread
from time import sleep as tsleep

class ExitEnter(Song):
    def __init__(self) -> None:
        self._default_delay_intro: int | float = 0.1
        self._intro_half_time: int | float = self._default_delay_intro-0.05
        self._default_wait_lines_intro = 2

        self._intro_line0: Line = Line([CharacterSet("The sun", self._default_delay_intro),
                                              CharacterSet(" says leave\n", self._intro_half_time),
                                              CharacterSet("The clock", self._default_delay_intro),],
                                            self._default_wait_lines_intro, cancel_last_delay=True)

        self._intro_line1: Line = Line([CharacterSet(" agrees\n", self._default_delay_intro)],
                                       self._default_wait_lines_intro)

    @staticmethod
    def _async_sound(path) -> None:
        Thread(target=playsound, args=(path,), daemon=True).start()

    def intro(self, filename: str) -> None:
        local_intro_delay: int | float = 20.2
        local_intro1_delay: int | float = 0.15

        self._async_sound(filename)

        tsleep(local_intro_delay)

        self._intro_line0.print_delay()

        tsleep(local_intro1_delay)

        self._intro_line1.print_delay()

        tsleep(1) #debug

def main():
    ee: ExitEnter = ExitEnter()

    ee.intro('./music/exitenter/intro.mp3')

if __name__ == '__main__':
    main()