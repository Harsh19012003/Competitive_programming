x = [10, 20, 20, 60, 50, 25, 40, 40]

def time(x):
    t = []
    for i in range(len(x)):
        t.append(x[i] - (5*i))
    return t

print(time(x))



# edge cases --> incoming time > leaving time --> append 0
#                no person present/ empty list