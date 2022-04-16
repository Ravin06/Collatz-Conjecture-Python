#Collatz Conjecture
x = int(input())

while True:
   if x == 1:
      break
   elif x % 2 == 0:
      x = (x/2)
      print(x)
   else:
      x = ((x*3)+1)
      print(x)
