N = int(input())
a = list(map(int,input().split()))
v = int(input())
cnt=0
for i in range(N):
    if a[i]==v:
     cnt+=1
print(cnt)