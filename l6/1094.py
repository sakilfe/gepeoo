n = int(input())
c = 0
r = 0
s = 0

for x in range(n):
  q, t = input().split()
  q = int(q)
  t = str(t)
  if t == 'C':
    c += q
  if t == 'R':
    r += q
  if t == 'S':
    s += q

total = c + r + s
pc = (c / total) * 100
pr = (r / total) * 100
ps = (s / total) * 100

print(f'''Total: {total} cobaias
Total de coelhos: {c}
Total de ratos: {r}
Total de sapos: {s}
Percentual de coelhos: {pc:.2f} %
Percentual de ratos: {pr:.2f} %
Percentual de sapos: {ps:.2f} %''')
