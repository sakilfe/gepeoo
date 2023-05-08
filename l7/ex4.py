print('insira a nota dos dois bimestres')
n1 = int(input())
n2 = int(input())
def aprovado(n1, n2):
  m = (n1 + n2)//2
  if m >= 60:
    aprovado == True
    print('aprovado')
  else:
    aprovado == False
    print('prova final')
  return m
print('média:', aprovado(n1, n2))
