# 5. Faça um algoritmo que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no
# vetor impar. Imprima os três vetores.

vet = []
vet_par = []
vet_impar = []
for n in range(1,20):
    num = int(input('Informe o número: '))
    vet.append(num)
    if num%2 == 0:
        vet_par.append(num)
    else:
        vet_impar.append(num)
print(f'O vetor completo é: {vet}')
print(f'O vetor de números pares é: {vet_par}')
print(f'O vetor de números ímpares é: {vet_impar}')
