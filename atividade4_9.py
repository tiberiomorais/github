# 9. Faça um algoritmo que leia um vetor A com 10 números inteiros, calcule e
# mostre a soma dos quadrados dos elementos do vetor.

vet = []
vet_quad = []
for n in range (1,11):
    num  = int(input(f'Informe o {n}º número: '))
    vet.append(num)
    num_quad = num**2
    vet_quad.append(num_quad)
soma = sum(vet_quad)
print(vet)
print(vet_quad)
print(soma)