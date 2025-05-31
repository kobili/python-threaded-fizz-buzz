import atexit
import threading
from typing import Callable

from fizz_buzz import (
    fizz_or_buzz,
    # exceptional_fizz_or_buzz, # used to demonstrate what happens when a thread pops an unhandled exception
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
        for i in range(start, start + iterations):
            value = func(i)
            print(f"{thread_name}: {i} -> {value}")
            fizz_buzz_frequencies.update(value)
    except Exception:
        print(f"{thread_name}: Failed with exception")
        raise


def on_exit():
    print(fizz_buzz_frequencies.dict)


atexit.register(on_exit)


if __name__ == "__main__":
    iterations = 203
    n_threads = 2

    iterations_per_thread = iterations // n_threads
    remainder_iterations = iterations % n_threads

    starting_iteration = 1

    threads: list[threading.Thread] = []
    for i in range(0, n_threads):
        # distribute remaining iterations evenly
        iterations_for_this_thread = iterations_per_thread + (1 if i < remainder_iterations else 0)

        threads.append(
            threading.Thread(
                target=main_loop,
                args=(f"thread{i}", fizz_or_buzz),
                kwargs={
                    "start": starting_iteration,
                    "iterations": iterations_for_this_thread,
                }
            )
        )

        starting_iteration += iterations_for_this_thread

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
