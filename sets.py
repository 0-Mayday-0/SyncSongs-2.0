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

    def __len__(self) -> int:
        return len(self.characters)

class Line:
    def __init__(self, sets: list[CharacterSet], delay_between: float, cancel_last_delay: bool = False) -> None:
        self._sets = sets
        self._delay_between = delay_between
        self._cancel_last_delay = cancel_last_delay

    def print_delay(self):
        len_sets: int = len(self._sets) - 1
        for i, st in enumerate(self._sets):
            local_index: int = i
            for i, v in enumerate(st):
                print(v, end='', flush=True)

            try:
                assert local_index < len_sets
                tsleep(self._delay_between)

            except AssertionError:
                if self._cancel_last_delay:
                    break

def main() -> None:
    a = Line([CharacterSet("Hello ", 0.2), CharacterSet("World", 0.5)], 5)

    a.print_delay()

if __name__ == '__main__':
    main()