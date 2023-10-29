import heapq

a = [1,2,3,4,5,6,7,8,9,0,12,123,43,23,32,323,4,322,3,233,45]


# 1 using sorting
a.sort(reverse=True)
print(a)
x = a[0]
for i in range(len(a)):
    if a[i] < x:
        print("2nd largest", a[i])
        break



# 2 using heap
x = []
n = 5 # 5th largest element
for i in a:
    heapq.heappush(x, -i)

print(x)
for i in range(n):
    heapq.heappop(x)
print(-x[0])

