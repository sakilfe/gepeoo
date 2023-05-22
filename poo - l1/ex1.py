import math

class Circulo():
  def _init_(self):
    self.r = 0
  def calc_c_a(self):
    a = math.pi * self.r ** 2
    c = 2 * math.pi * self.r
    return f'área = {a:.5f} | circunferência = {c:.5f}'

o = Circulo()
o.r = float(input('digite o valor do raio: '))
print(o.calc_c_a())
