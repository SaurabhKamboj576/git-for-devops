"""This script defines and runs a simple function."""


def myfunction():
    """Performs a calculation and returns the result."""
    a = 4
    b = 6
    d = a + b
    return d


if __name__ == "__main__":
    result = myfunction()
    print("Result:", result)
