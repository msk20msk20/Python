import random

def make_question() :
    a = random.randint(1, 40)
    b = random.randint(60, 100)
    op = random.randint(1, 3)

    q = str(a)                                     #string 문자열

    if op == 1 :
        q = q + "+"
    if op == 2 :
        q = q + "-"
    if op == 3 :
        q = q + "*"

    q = q + str(b)

    return q


sc1 = 0
sc2 = 0


for x in range (5) :
    q = make_question()
    print(q)                                        # "a+b"  "a-b"  "a*b"
    answer = input("=")
    r = int(answer)

    if eval(q) == r :
        print ("정답")
        sc1 = sc1 + 1
    else :
        print ("오답")
        sc2 = sc2 + 1

print ("정답 : ",sc1, "오답 : ",sc2)

if sc2 == 0 :
    print ("당신은 천재입니다!")
