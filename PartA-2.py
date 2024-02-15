c={}
for a in range(1,7):
    for b in range(1,7):
        sums=a+b
        c.setdefault(sums,[]).append((a,b))
for s,pairs in c.items():
    print(f"Sum = {s}, combinations: {pairs}")
