n = int(input())
vetor = []

for i in range(0,n):
  if i <= 1:
    vetor.append(i)
  else:
    aux = vetor[i-1] + vetor[i-2]
    vetor.append(aux)

for j in range(0, n):
    vetor[j] =str(vetor[j])

vetor = ' '.join(vetor)
print(vetor)
