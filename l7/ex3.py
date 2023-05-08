print('inserir nome completo')
nc = input()
def iniciais(nome):
  p = nome.split()
  r = ''
  for l in p:
    r += l[0]
  return r
print(iniciais(nc))
