class Cinema():
  def _init_(self):
    self.d = 0
    self.h = 0
    self.m = 0
  def calc_e(self):
    if self.d == 'segunda' or self.d == 'terça' or self.d == 'quinta':
      b = 16
    elif self.d == 'quarta':
      return 'todos pagam R$ 8,00 em qualquer horário!'
    else:
      b = 20
    if self.h >= 17:
      b *= 1.5
    return f'valores da entrada: inteira = R$ {b},00 | meia = R$ {int(b/2)},00'

e = Cinema()
e.d = input('dia da semana da sessão: ')
e.h, e.m = map(int, input('horário da sessão (ex.: 00h00): ').split('h'))
print(e.calc_e())
