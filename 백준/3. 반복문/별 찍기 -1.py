N = int(input())
for i in range(N):
    print('*'* (i+1), sep='')

# sep = seperation : 구분하다.
# sep = '?' ('?')에 따라 공백 안에 채워짐
# 없을 경우, 공백이 아무것도 없으니깐 사라지는 것처럼 보임
# 즉 (공백 지워짐)