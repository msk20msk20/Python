array = [34, 67, 121]

n = len(array)
max = array[0]

for x in range (1, n) :
      if array[x] > max :
            max = array[x]

print (max)
