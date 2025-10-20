a, b, c = map(int, input().split())
best = a
if b > best:
    best = b
if c > best:
    best = c
print(best)
