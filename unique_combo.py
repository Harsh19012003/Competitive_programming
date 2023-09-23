
# from itertools import combinations

# N, K = map(int, input().split())
# p = list(map(int, input().split()))

# uc = set()

# for r in range(1, N + 1):
#     for c in combinations(p, r):
#         if sum(c) == K:
#             uc.add(tuple(sorted(c)))

# print(len(uc))







def gc(arr, r):
    if r == 0:
        yield []
    elif len(arr) >= r:
        head, *tail = arr
        for comb in gc(tail, r - 1):
            yield [head] + comb
        yield from gc(tail, r)

N, K = map(int, input().split())
p = list(map(int, input().split()))

uc = set()

for r in range(1, N + 1):
    for combo in gc(p, r):
        if sum(combo) == K:
            uc.add(tuple(sorted(combo)))

print(len(uc))