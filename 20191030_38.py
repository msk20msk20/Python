x = int(input("첫 번째 숫자를 입력하세요"))
y = int(input("첫 번째 숫자를 입력하세요"))

def gcd (a, b) :
      i = min(a, b)
      while True :
            if a%i == 0 and b%i == 0 :
                  return i
            i = i - 1

print (gcd(x, y))
