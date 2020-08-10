# 7. Faça um algoritmo que leia um vetor de 5 números inteiros, mostre a
# soma, a multiplicação e os números.
vet = []
produto = 1

for n in range(1,6):
    num = int(input('Informe o número: '))
    vet.append(num)
    produto *= num
soma = sum(vet)
print(f'O vetor completo é: {vet}')
print(f'A soma do vetor é: {soma}')
print(f'O produto do vetor é: {produto}')
