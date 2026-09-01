from sets import CharacterSet, Line, Song

from playsound import playsound
from threading import Thread

from time import sleep as tsleep
from functools import wraps

from collections.abc import Callable


class ExitEnter(Song):
    def __init__(self) -> None:
        #INTRO
        self._intro_delays: dict[str, int | float] = {} #can't be made a literal due to self-reference

        self._intro_delays['intro default delay'] = 0.1
        self._intro_delays['intro half time'] = self._intro_delays['intro default delay']-0.05
        self._intro_delays['intro default wait lines'] = 2
        self._intro_delays['intro swing'] = self._intro_delays['intro default wait lines']-0.25
        self._intro_delays['intro thirds'] = self._intro_delays['intro swing']-0.05
        self._intro_delays['intro slightly slower'] = self._intro_delays['intro half time']+0.03
        self._intro_delays['intro end'] = 2.2

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

                                                       self._intro_delays['intro thirds'],

                                                       Line([CharacterSet(" ahead", self._intro_delays['intro default delay']),
                                                                  CharacterSet(" of me\n", self._intro_delays['intro default delay']),
                                                                  CharacterSet("The mo", self._intro_delays['intro slightly slower']),
                                                                  CharacterSet("ment flew\n", self._intro_delays['intro half time']),
                                                                  CharacterSet("They al", self._intro_delays['intro slightly slower']),
                                                                  CharacterSet("ways do\n", self._intro_delays['intro slightly slower']),
                                                                  CharacterSet("Seems one", self._intro_delays['intro default delay']),
                                                                  CharacterSet(" is some", self._intro_delays['intro half time']),
                                                                  CharacterSet("times more", self._intro_delays['intro half time']),
                                                                  CharacterSet(" than two", self._intro_delays['intro half time']),],
                                                            self._intro_delays['intro default wait lines']),

                                                       self._intro_delays['intro end']]
        #/INTRO

        #CHORUS0
        self._chorus0_delays: dict[str, int | float] = {}

        self._chorus0_delays['chorus0 default delay'] = 0.15
        self._chorus0_delays['chorus0 default wait lines'] = 2.5

        self._chorus0_lines: list[Line | float | int] = [Line([CharacterSet("Everything is made up", self._chorus0_delays['chorus0 default delay']),
                                                                    CharacterSet("Everything is made up", self._chorus0_delays['chorus0 default delay']),],
                                                            self._chorus0_delays['chorus0 default wait lines'])]
        #/CHORUS0

    @staticmethod
    def async_sound(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> None:
            Thread(target=playsound, args=(args[1],), daemon=True).start()
            func(*args, **kwargs)

        return wrapper

    @async_sound
    def intro(self, filename: str) -> None:
        local_intro_delay: int | float = 20.2

        #self._async_sound(filename)

        tsleep(local_intro_delay)

        for line in self._intro_lines:
            try:
                line.print_delay()
            except AttributeError:
                tsleep(line)

    @async_sound
    def chorus0(self, filename: str) -> None:
        for line in self._chorus0_lines:
            try:
                line.print_delay()
            except AttributeError:
                tsleep(line)

def main():
    ee: ExitEnter = ExitEnter()

    ee.intro('./music/exitenter/intro.mp3')
    ee.chorus0('./music/exitenter/chorus0.mp3')

if __name__ == '__main__':
    main()