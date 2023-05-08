print('digite a base e a altura do retângulo')
b = float(input())
h = float(input())

a = b * h
p = (2 * b) + (2 * h)
d = (b**2 + h**2) ** 0.5

print(f'área = {a:.2f} - perímetro = {p:.2f} - diagonal = {d:.2f}')
