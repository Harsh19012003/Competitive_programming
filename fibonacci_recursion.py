def fib(n):
    if n == 0:
        # print("0 ")
        return 0
    if n == 1:
        # print("1 ")
        return 1
    
    # print(fib(n) + fib(n-1))
    return fib(n-1) + fib(n-2)




for i in range(10):
    print(fib(i))