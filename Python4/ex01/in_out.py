def square(x: int | float) -> int | float:
    """Return the square of x"""
    return x * x


def pow(x: int | float) -> int | float:
    """Return the power of x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return the function of x"""
    count = 0
    num = x

    def inner() -> float:
        """inner function"""
        nonlocal count
        count += 1
        res = num
        for _ in range(count):
            res = function(res)
        return res

    return inner
