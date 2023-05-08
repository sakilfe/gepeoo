e = input().split()
a = float(e[0])
b = float(e[1])
c = float(e[2])

n = 'Impossivel calcular'

delta = (b **2) - 4 * a * c

if a == 0:
  print(n)
elif delta < 0:
  print(n)

else:
  x1 = (-b + delta ** (1/2)) / (2 * a)
  x2 = (-b - delta ** (1/2)) / (2 * a)
  print(f'R1 = {x1:.5f}')
  print(f'R2 = {x2:.5f}')
  
