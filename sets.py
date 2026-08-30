from collections.abc import Iterable
from time import sleep as tsleep

class CharacterSet:
    def __init__(self, chars: Iterable, delay: float | int) -> None:
        self.characters: Iterable = chars
        self.delay = delay

    def yield_delay(self):
        for character in iter(self.characters):
            yield character
            tsleep(self.delay)

    def __iter__(self):
        yield from self.yield_delay()


class Line:
    def __init__(self, sets: list[CharacterSet], delay_between: float, cancel_last_delay: bool = False) -> None:
        self.sets = sets
        self.delay_between = delay_between

    def print_delay(self):
        for st in self.sets:
            for i in st:
                print(i, end='', flush=True)




def main() -> None:
    a = Line([CharacterSet("Hello ", 0.2), CharacterSet("World", 0.5)])

    a.print_delay()

if __name__ == '__main__':
    main()