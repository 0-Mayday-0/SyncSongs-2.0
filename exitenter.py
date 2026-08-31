from sets import CharacterSet, Line, Song
from playsound import playsound
from threading import Thread
from time import sleep as tsleep

class ExitEnter(Song):
    def __init__(self) -> None:
        self._intro_delays: dict[str, int | float] = {}

        self._intro_delays['intro default delay'] = 0.1
        self._intro_delays['intro half time'] = self._intro_delays['intro default delay']-0.05
        self._intro_delays['intro default wait lines'] = 2
        self._intro_delays['intro swing'] = self._intro_delays['intro default wait lines']-0.25
        self._intro_delays['intro thirds'] = self._intro_delays['intro swing']-0.05
        self._intro_delays['intro slightly slower'] = self._intro_delays['intro half time']+0.03

        self._intro_lines: list[Line | float | int] = [Line([CharacterSet("The sun", self._intro_delays['intro default delay']),
                                                                  CharacterSet(" says leave\n", self._intro_delays['intro half time']),
                                                                  CharacterSet("The clock", self._intro_delays['intro default delay']),],
                                                self._intro_delays['intro default wait lines'], cancel_last_delay=True),

                                                       self._intro_delays['intro thirds'],

                                                       Line([CharacterSet(" agrees\n", self._intro_delays['intro default delay']),
                                                                  CharacterSet("My dreams", self._intro_delays['intro half time']),
                                                                  CharacterSet(" have left", self._intro_delays['intro slightly slower']),
                                                                ],
                                                            self._intro_delays['intro swing']),

                                                       self._intro_delays['intro swing'],

                                                       Line([CharacterSet(" ahead", self._intro_delays['intro default delay']),
                                                            CharacterSet(" of me\n", self._intro_delays['intro default delay'])]


    @staticmethod
    def _async_sound(path) -> None:
        Thread(target=playsound, args=(path,), daemon=True).start()

    def intro(self, filename: str) -> None:
        local_intro_delay: int | float = 20.2
        local_intro1_delay: int | float = 0.15

        self._async_sound(filename)

        tsleep(local_intro_delay)

        for line in self._intro_lines:
            try:
                line.print_delay()
            except AttributeError:
                tsleep(line)

        tsleep(1) #debug

def main():
    ee: ExitEnter = ExitEnter()

    ee.intro('./music/exitenter/intro.mp3')

if __name__ == '__main__':
    main()