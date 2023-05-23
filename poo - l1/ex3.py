class Viagem():
  def _init_(self):
    self.d = 0
    self.h = 0
    self.m = 0
  def calc_vm(self):
    kmh = self.d/((self.h * 60 + self.m)/60)
    return f'{str(kmh)} km/h'

p = Viagem()
p.d = float(input('insira os quilômetros rodados: '))
p.h = float(input('insira a quantidade de horas da viagem: '))
p.m = float(input('insira a quantidade de minutos da viagem: '))
print(p.calc_vm())
