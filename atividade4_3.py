# 3. Faça um algoritmo que leia 4 notas, mostre as notas e a média na tela.
vet =[]
for n in range(1,5):
    nota = float(input(f'Informe a nota {n}'))
    vet.append(nota)
media = sum(vet)/len(vet)
print(media)
