a = ["a", "b", "c", "d", "e"]

for i in range(len(a)):
    for j in range(i, len(a)):
        for k in range(i, j+1):
            print(a[k], end = "")
        print("\t")