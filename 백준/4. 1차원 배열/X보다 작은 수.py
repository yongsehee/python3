N,X = map(int,input().split())
A = list(map(int,input().split()))
B = list()
for i in range(N):
    if A[i]<X:
        B.append(A[i])
print(*B)

#print(*를 넣어주면 list 압축 풀어짐)