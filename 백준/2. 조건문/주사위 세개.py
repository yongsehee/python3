a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)

#max는 가장 큰 값을 찾아 리턴하는 함수
