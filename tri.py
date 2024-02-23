print("Enter integers")
p = int(input())
q = int(input())

print(p, q)

all_triplets = []
final_triplets = []

for i in range(1, p+1):
    for j in range(1, p+1):
        for k in range(1, p+1):
            all_triplets.append([i, j, k])


#print(all_triplets)
print()
counter = 0

for triplet in all_triplets:
    x = triplet[0]
    y = triplet[1]
    z = triplet[2]
    print()
    print(x, y, z)
    print()

    if ((x+y)%q) == 0 and ((y+z)%q) == 0 and ((x+z)%q) == 0:
        final_triplets.append(triplet)
        counter += 1

#print(final_triplets)
print(f"counter: {counter}")
