N = int(input())
a = list(map(int, input().split()))
K = int(input())
x = []
for i in range(0, K):
    x.append(int(input()))
for i in x:
    count = 0
    res = []
    for j in a:
        if j % i == 0:
            count += 1
            res.append(j)
    print(count)
    print(*res)
