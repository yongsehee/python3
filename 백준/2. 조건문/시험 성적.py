scores= map(int, input().split())

for score in scores:
    # a=90~100
    if score >= 90 and score <= 100:
        print("A")
    # b=80~89
    elif score >= 80 and score <= 89:
        print("B")
    # c=70~79
    elif score >= 70 and score <= 79:
        print("C")
    # d=60~69
    elif score >= 60 and score <= 69:
        print("D")
    else:
        print("F")

