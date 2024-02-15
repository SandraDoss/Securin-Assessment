total=6*6
d=[[0]*6 for _ in range(6)]
p={}

for a in range(1,7):
    for b in range(1,7):
        sums=a+b
        d[a-1][b-1]=sums
for row in d:
    for sums in row:
        if sums not in p:
            p[sums]=1
        else:
            p[sums]+=1
for sums,count in p.items():
    pr=count/total
    print(f"P(Sum={sums}) = {pr:.4f}")
