import time
from typing import Callable


def fizzOrBuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    
    return str(n)


def fizzOrBuzzException(n: int) -> str:
    if n == 42:
        raise ValueError("You've hit the secret number of the day")
    
    return fizzOrBuzz(n)


def main_loop(
    thread_name: str,
    func: Callable[[int], str],
):
    while True:
        for i in range(1, 101):
            print(f"{thread_name}: {func(i)}")
            time.sleep(0.1)

        print(f"{thread_name}: finished one fizz buzz iteration")
        time.sleep(0.5)


if __name__ == "__main__":
    main_loop("main", fizzOrBuzzException)
