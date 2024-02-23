# taking no of test cases
for i in range(int(input())):

    grid=[]
    geometric_progression=[]
    grid.append(int(input()))
    m=max(grid)

    # setting gp numbers
    for i in range(m*m):
        geometric_progression.append(2**i)
    for i in grid:
        n=1
        for x in range(i):
            for y in range(i):
                # printing 1 according to gp
                if (n in geometric_progression):
                    print("1",end=" ")
                    n+=1
                else:
                    print("0",end=" ")
                    n+=1
            print()
