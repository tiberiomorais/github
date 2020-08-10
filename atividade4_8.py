# 8. Faça um algoritmo que peça a idade e a altura de 5 pessoas, armazene
# cada informação no seu respectivo vetor. Imprima a idade e a altura na
# ordem inversa a ordem lida.

vet_alt = []
vet_idade = []

for n in range (1,6):
    altura = float(input(f'Informe a altura da {n}ª pessoa: '))
    idade = int(input(f'Informe a idade da {n}ª pessoa: '))
    vet_alt.append(altura)
    vet_idade.append(idade)
print(f'A idade foi lida na seguinte ordem: {vet_idade}')
print(f'A altura foi lida na seguinte ordem: {vet_alt}')
vet_alt.reverse()
vet_idade.reverse()
print(f'A idade na ordem inversa é: {vet_idade}')
print(f'A altura na ordem inversa é: {vet_alt}')