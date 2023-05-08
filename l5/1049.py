a = input()
b = input()
c = input()

if a == 'vertebrado' and b == 'ave' and c == 'carnivoro':
  x = 'aguia'
if a == 'vertebrado' and b == 'ave' and c == 'onivoro':
  x = 'pomba'
if a == 'vertebrado' and b == 'mamifero' and c == 'onivoro':
  x = 'homem'
if a == 'vertebrado' and b == 'mamifero' and c == 'herbivoro':
  x = 'vaca'
if a == 'invertebrado' and b == 'inseto' and c == 'hematofago':
  x = 'pulga'
if a == 'invertebrado' and b == 'inseto' and c == 'herbivoro':
  x = 'lagarta'
if a == 'invertebrado' and b == 'anelideo' and c == 'hematofago':
  x = 'sanguessuga'
if a == 'invertebrado' and b == 'anelideo' and c == 'onivoro':
  x = 'minhoca'

print(x)
