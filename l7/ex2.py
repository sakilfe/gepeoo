print('insira três valores e te direi o maior entre eles')
x = int(input())
y = int(input())
z = int(input())
def maior(x, y, z):
  maior = max(x, y, z)
  return maior
print(maior(x, y, z))
