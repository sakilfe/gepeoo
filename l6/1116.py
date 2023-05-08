n = int(input())

for v in range(n):
  x, y = map(int, input().split())

  if y == 0:
    print('divisao impossivel')
  elif x == 0:
    print('0.0')
  else:
    print(f'{(x/y):.1f}')
