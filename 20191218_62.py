def addition(n) :
      if n > 1 :
            result = addition(n-1) + n
      else :
            result = 1
      return result

print (addition(10))
print (addition(100))
#print (addition(1000))
