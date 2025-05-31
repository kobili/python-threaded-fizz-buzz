import time
from typing import Callable
import atexit

from fizz_buzz import fizz_or_buzz, exceptional_fizz_or_buzz


def main_loop(
    thread_name: str,
    func: Callable[[int], str],
    iterations: int = 100,
):
    try:
        for i in range(1, iterations+1):
            print(f"{thread_name}: {func(i)}")
            time.sleep(0.1)
    except Exception as e:
        print(f"{thread_name}: Failed with exception: {e}")
        raise


def on_exit():
    print("goodbye, Cruel World!")


atexit.register(on_exit)


if __name__ == "__main__":
    main_loop("main", fizz_or_buzz)
