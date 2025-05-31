def fizz_or_buzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    
    return str(n)


def exceptional_fizz_or_buzz(n: int) -> str:
    if n == 42:
        raise ValueError("You've hit the secret number of the day")
    
    return fizz_or_buzz(n)
