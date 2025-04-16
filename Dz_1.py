def caching_fibonacci (cache=None):
    if cache is None:
        cache = {}
    def fibonacci(n):
        if n <=1:
            cache[n]= n
        else:
            cache[n] = fibonacci(n-2) + fibonacci(n-1)
        return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(10))
