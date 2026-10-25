"""Python Programs Collection: factorial, Fibonacci and structure-to-dictionary."""


def factorial(n):
    """Return n! using a loop. Raises ValueError for negative numbers."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """Return n! using recursion (same result as factorial)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci(count):
    """Return the first `count` numbers of the Fibonacci series."""
    if count < 0:
        raise ValueError("Count cannot be negative.")
    series = []
    a, b = 0, 1
    for _ in range(count):
        series.append(a)
        a, b = b, a + b
    return series


def pairs_to_dict(pairs):
    """Convert a list of (key, value) tuples into a dictionary."""
    result = {}
    for key, value in pairs:
        result[key] = value
    return result


def lists_to_dict(keys, values):
    """Convert two lists (keys and values) into a dictionary."""
    if len(keys) != len(values):
        raise ValueError("keys and values must have the same length.")
    return dict(zip(keys, values))


class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course


def object_to_dict(obj):
    """Convert a simple object (its attributes) into a dictionary."""
    return dict(vars(obj))


if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Factorial of 5 (recursive):", factorial_recursive(5))
    print("First 10 Fibonacci numbers:", fibonacci(10))

    print("Tuples to dict:", pairs_to_dict([("name", "Nishant"), ("year", 2)]))
    print("Lists to dict:", lists_to_dict(["a", "b", "c"], [1, 2, 3]))
    print("Object to dict:", object_to_dict(Student("Nishant", 101, "B.Tech CSE")))
