def find_max_idx(a) :
      n = len(a)
      max_idx = 0
      for i in range (1, n) :
            if a[i] > a[max_idx] :
                  max_idx = i
      return max_idx
v = [12, 34, 54, 34, 6, 4, 5, 23, 100, 923, 34]
print(find_max_idx(v))
