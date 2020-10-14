x = int(input("값을 입력하세요"))
d = 2

while d <= x:
      if x % d == 0:
            print(d)
            x = x / d
      else:
            d = d + 1
