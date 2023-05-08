print('insira seu nome completo e formatarei')
nc = input()
def fnc(nome):
  nomes = nome.split()
  ln = []
  for x in nomes:
    ln.append(x.capitalize())
  resultado = str(ln[0])
  for x in range(1, len(ln)):
    resultado += ' '
    resultado += ln[x]
  return resultado
print(f'seu nome formatado: {fnc(nc)}') 
