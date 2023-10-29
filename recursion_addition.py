def fun(sum, a):
    print(a)
    if a == 0:
        print(sum)
        return sum
    
    last = a%10
    sum += last

    answer = fun(sum, int(a/10))
    return answer
    

if __name__ == "__main__":
    global sum
    sum = 0
    print(f"final answer using recursion is: {fun(sum, 12345)}")
