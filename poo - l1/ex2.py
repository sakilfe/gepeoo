class Disciplina():
  def _init_(self):
    self.nome = 0
    self.n1 = 0
    self.n2 = 0
    self.n3 = 0
    self.n4 = 0
    self.nf = 0
  def calc_media(self):
    mp = (self.n1 * 2 + self.n2 * 2 + self.n3 * 3 + self.n4 * 3) / 10
    if mp >= 60:
      return f'média parcial = {mp:.1f}'
    else:
      mf = (mp + self.nf) / 2
      return f'média parcial = {mp:.1f} | média final = {mf:.1f}'

b = Disciplina()
b.nome = input('nome da disciplina: ')
b.n1 = int(input(f'digite a nota do primeiro bimestre de {b.nome}: '))
b.n2 = int(input(f'digite a nota do segundo bimestre de {b.nome}: '))
b.n3 = int(input(f'digite a nota do terceiro bimestre de {b.nome}: '))
b.n4 = int(input(f'digite a nota do quarto bimestre de {b.nome}: '))
b.nf = int(input(f'digite a nota da prova final de {b.nome}: '))
print(b.calc_media())
