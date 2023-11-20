a,b = map(int,input().split())
c =int(input())
b+=c
while True:
    if b>=60:
        a+=1
        b-=60
        if a>=24:
            a-=24
    else:
        print(a,b)
        break




