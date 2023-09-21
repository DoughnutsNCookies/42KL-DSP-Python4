def callLimit(limit: int):
    """Decorator for limiting the number of calls to a function"""
    count = 0

    def callLimiter(function):
        """Inner function"""

        def limit_function(*args: any, **kwds: any):
            """Limit function"""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} called too many times")
                return None
            count += 1
            return function(*args, **kwds)
        return limit_function
    return callLimiter
