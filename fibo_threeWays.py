# This hopefully computes fibonacci of N
# Recursively, iteratively, and dynamically

def fibo_rec(n):

    if n == 0 or n == 1:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

#print(fibo_rec(10))


def fibo_iter(n):
    start = 0
    second = 1
    for i in range(1, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        total = start + second
        start = second
        second = total
    return total

#print(fibo_iter(23))

cache = [None]*100

def fibo_memo(n):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return n
    else:
        result = fibo_rec(n - 1) + fibo_rec(n - 2)
        cache[n] = result
        return cache[n]

print(fibo_memo(24))