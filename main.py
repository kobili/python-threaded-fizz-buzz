import atexit
import time
from typing import Callable

from fizz_buzz import (
    fizz_or_buzz,
    exceptional_fizz_or_buzz,
    ThreadSafeFizzBuzzFreqCounter,
    FizzBuzzFrequencyCounter,
)


fizz_buzz_frequencies: FizzBuzzFrequencyCounter = ThreadSafeFizzBuzzFreqCounter()


def main_loop(
    thread_name: str,
    func: Callable[[int], str],
    iterations: int = 100,
    start: int = 1,
):
    try:
        for i in range(start, iterations+1):
            value = func(i)
            print(f"{thread_name}: {i} -> {value}")
            fizz_buzz_frequencies.update(value)

            # time.sleep(0.1)
    except Exception as e:
        print(f"{thread_name}: Failed with exception: {e}")
        raise


def on_exit():
    print(fizz_buzz_frequencies.dict)


atexit.register(on_exit)

# without any exceptions
# for 100 iterations we expect: {'Fizz': 27, 'Buzz': 14, 'FizzBuzz': 6}
# for 200 iterations: {'Fizz': 53, 'Buzz': 27, 'FizzBuzz': 13}

if __name__ == "__main__":
    main_loop("main", fizz_or_buzz, iterations=200)
