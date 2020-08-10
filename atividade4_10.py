# Faça um algoritmo que leia dois vetores com 10 elementos cada. Gere um
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos
# pelos elementos intercalados dos dois outros vetores.

vet_A = []
vet_B = []
vet_C = []
for n in range(1,11):
    num_A = input(f'Informe o {n} elemento do vetor A: ')
    vet_A.append(num_A)

for m in range(1,11):
    num_B = input(f'Informe o {m} elmento do vetor B: ')
    vet_B.append(num_B)
print(f'O vetor A é: {vet_A}')
print(f'O vetor B é: {vet_B}')
for x in range (0,10):
   vet_C.append(vet_A[x])
   vet_C.append(vet_B[x])
print(f'O novo vetor é: {vet_C}')