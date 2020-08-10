# 4. Faça um algoritmo que leia um vetor de 10 caracteres, e diga quantas
# consoantes foram lidas. Imprima as consoantes.
vogal = ['a','e','i','o','u']
consoante = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vet=[]
vet2 = []
for n in range(1,11):
    letra = input('Informe a letra: ')
    vet.append(letra)
    if letra in consoante:
        vet2.append(letra)
qt_consoantes = len(vet2)
print(f'Voce digitou {qt_consoantes} consoantes. São elas: ', vet2)