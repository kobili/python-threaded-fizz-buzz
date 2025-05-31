import threading


FIZZ_BUZZ_VALUE_FIZZ = "Fizz"
FIZZ_BUZZ_VALUE_BUZZ = "Buzz"
FIZZ_BUZZ_VALUE_FIZZ_BUZZ = "FizzBuzz"


class FizzBuzzFrequencyCounter:
    def __init__(self):
        self.fizz = 0
        self.buzz = 0
        self.fizz_buzz = 0

    def update(self, value: str):
        if value == FIZZ_BUZZ_VALUE_FIZZ:
            self.fizz += 1
        elif value == FIZZ_BUZZ_VALUE_BUZZ:
            self.buzz += 1
        elif value == FIZZ_BUZZ_VALUE_FIZZ_BUZZ:
            self.fizz_buzz += 1

    @property
    def dict(self) -> dict[str, int]:
        return {
            FIZZ_BUZZ_VALUE_FIZZ: self.fizz,
            FIZZ_BUZZ_VALUE_BUZZ: self.buzz,
            FIZZ_BUZZ_VALUE_FIZZ_BUZZ: self.fizz_buzz,
        }


class ThreadSafeFizzBuzzFreqCounter(FizzBuzzFrequencyCounter):
    def __init__(self):
        super().__init__()
        self.thread_lock = threading.Lock()

    def update(self, value: str):
        with self.thread_lock:
            super().update(value)

    @property
    def dict(self) -> dict[str, int]:
        with self.thread_lock:
            return super().dict


def fizz_or_buzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return FIZZ_BUZZ_VALUE_FIZZ_BUZZ
    if n % 3 == 0:
        return FIZZ_BUZZ_VALUE_FIZZ
    if n % 5 == 0:
        return FIZZ_BUZZ_VALUE_BUZZ
    
    return str(n)


def exceptional_fizz_or_buzz(n: int) -> str:
    if n == 42:
        raise ValueError("You've hit the secret number of the day")
    
    return fizz_or_buzz(n)
