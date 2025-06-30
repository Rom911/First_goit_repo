def caching_fibonacci():
    cache = {}  # Dictionary to store calculated Fibonacci numbers

    def fibonacci(n):
        # Base cases
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Check if result is already in cache
        if n in cache:
            return cache[n]

        # Calculate recursively and store in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
