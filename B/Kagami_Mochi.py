

N = int(input())

Ds = {}
for i in range(0, N):
    d = int(input())
    if d in Ds.keys():
        Ds[d] = Ds[d] + 1
    else:
        Ds[d] = 1

print(len(Ds.keys()))
