a, b, c = map(int, input().split())
best = a
if b > best:
    best = b
elif c > best:
    best = c
print(best)
