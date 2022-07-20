n=int(input())
subject=input()
subjects=list(map(str,input().split(';')))
sum=0
for i in range (0,n):
    rating = list(map(int, input().split(';')))
    sum+=rating[subjects.index(subject)]
print(f'{sum/n:0.3f}')