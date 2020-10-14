import random
import time

animal = ["cat", "dog", "fox", "monkey", "mouse", "panda", "lion", "tiger", "wolf"]


print("[타자게임]준비되면 엔터(ENTER)")
input()
start = time.time()

q = random.choice(animal)

for x in range (1, 6) :

    print("*문제", x)
    print(q)
    a = input()
    if q == a :
        print("correct")
        x = x + 1
        q = random.choice(animal)
    else :
        print("not correct....try again")


end = time.time()
et = end - start
et = format(et, ".2f")
print("타자시간 :", et, "초")
