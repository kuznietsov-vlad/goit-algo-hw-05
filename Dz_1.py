def caching_fibonacci(n, cache=None):
    if cache is None:
        cache = {}
        def fibonacci(n):
            if n <=1:
                cache[n]= n
            else:
                cache[n] = fibonacci(n-2) + fibonacci(n-1)
            return cache[n]
        return fibonacci(n)

print(caching_fibonacci(10))
