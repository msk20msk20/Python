def max_find(a) :
      n = len(a)
      max = a[0]
      for x in range (1, n) :
            if a[x] > max :
                  max = a[x]
      return max

v = [17, 92, 18, 33, 58, 7, 43, 56]

print(max_find(v))
