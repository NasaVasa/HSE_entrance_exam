N = int(input())
n = list(map(int, input().split()))
K = int(input())
p = list(map(int, input().split()))
for i in p:
    q = 0
    for j in n:
        if i > j:
            q += 1
    print(q)
