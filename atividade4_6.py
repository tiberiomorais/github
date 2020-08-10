# 6. Faça um algoritmo que peça as quatro notas de 10 alunos, calcule e
# armazene num vetor a média de cada aluno, imprima o número de alunos
# com média maior ou igual a 7.0.

nota = []
vet_media = []
aprovados = []

for n in range (1,11): #número de alunos
    #media = 0
    soma = 0
    input(f'Informe as notas do {n}º aluno')
    for n in range (1,5): #notas das 4 unidades
        nota = float(input(f'nota {n}: '))
        soma +=nota
    media = soma / 4
    if media >= 7:
        aprovados.append(media)
    print(media)
    vet_media.append(media)
print(vet_media)
print(aprovados)
print(f'O número de alunos aprovados foi {len(aprovados)}')