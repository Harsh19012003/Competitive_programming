# cook your dish here
#print("Enter integers")
x = input().split(' ')
p = int(x[0])
q = int(x[1])


counter = 0

for x in range(1, p+1):
    for y in range(1, p+1):
        for z in range(1, p+1):
            if ((x+y)%q) == 0 and ((y+z)%q) == 0 and ((x+z)%q) == 0:
                counter += 1
print(counter)
