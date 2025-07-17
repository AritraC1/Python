# LRU Cache
# Stands for Least Recently Used (LRU) cache. Caches the results of function calls to avoid recomputation. Ideal for recursive or expensive functions.

from functools import lru_cache

@lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# Test with caching
print("Fibonacci(10):", fib(10))  # 55

# View cache stats
print(fib.cache_info())