def min_find(a) :
      n = len(a)
      min = a[0]
      for x in range (1, n) :
            if a[x] < min :
                  min = a[x]
      return min

v = [17, 92, 18, 33, 58, 7, 43, 56]

print(min_find(v))
