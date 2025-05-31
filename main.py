import time
from typing import Callable
import atexit

from fizz_buzz import fizz_or_buzz, exceptional_fizz_or_buzz, FizzBuzzFrequencyCounter


fizz_buzz_frequencies = FizzBuzzFrequencyCounter()


def main_loop(
    thread_name: str,
    func: Callable[[int], str],
    iterations: int = 100,
):
    try:
        for i in range(1, iterations+1):
            value = func(i)
            print(f"{thread_name}: {i} -> {value}")
            fizz_buzz_frequencies.update(value)

            time.sleep(0.1)
    except Exception as e:
        print(f"{thread_name}: Failed with exception: {e}")
        raise


def on_exit():
    print(fizz_buzz_frequencies.dict)


atexit.register(on_exit)


if __name__ == "__main__":
    main_loop("main", exceptional_fizz_or_buzz)
