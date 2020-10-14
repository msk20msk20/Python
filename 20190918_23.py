# 다각형을 그리는 함수
import turtle as t

def polygon(n):             # n번 반복합니다.
    for x in range(n):      # 거북이를  50만큼 앞으로 이동합니다.
        t.forward(50)       # 거북이를 360/n만큼 왼쪽으로 이동합니다.
        t.left(360/n)

def polygon2(n, a):         # n번 반복합니다.
    for x in range(n):      # 거북이를  a만큼 앞으로 이동합니다.
        t.forward(a)        # 거북이를 360/n만큼 왼쪽으로 이동합니다.
        t.left(360/n)

polygon(3)                  # 삼각형을 그립니다.
polygon(5)                  # 오각형을 그립니다.

# 그림을 그리지 않고 거북이를 100만큼 이동합니다.
t.up()
t.forward(100)
t.down()

polygon2(3, 75)             # 한 변이 75인 삼각형을 그립니다.
polygon2(5, 100)            # 한 변이 100인 오각형을 그립니다.
