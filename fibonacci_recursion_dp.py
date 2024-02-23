# DYNAMIC PROGRAMMING APPROCH FOR FIBONACCI SERIES

memo = {}

def fib(n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]




for i in range(1, 11):
    print(fib(i, memo))







# FIBONACCI SERIES TRADITIONAL APPROCH

def fib_traditional(n):
    if n == 1 or n == 2:
        return 1
    
    return fib_traditional(n-1) + fib_traditional(n-2)


print(fib_traditional(10))