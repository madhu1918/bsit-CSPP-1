def iterPower(a, b):
   result = 1
   while b > 0:
      result *= a
      b -= 1
   return result