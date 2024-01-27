#declarando variaveis
lista = []
par =[]
impar =[]
#usuario preenchendo a lista
for i in range(10):
    a = int(input(f'Digite o {i+1}º da lista: '))
    lista.append(a)
#dividindo a par e impar
for i in lista:
    if i%2 == 0:
        par.append(i)
    else:
        impar.append(i)


#colocando em tupla
par_tuple = tuple(par)
impar_tuple = tuple(impar)
#printando 
print('Lista de todos os elementos',lista)
print('Os numeros pares em formato tupla',par_tuple)
print('Os numeros impares em formato tupla',impar_tuple)

print('O numero de elementos pares eh:',len(par_tuple))
print('O numero de elementos impares eh:',len(impar_tuple))

print('A soma de todos os numeros pares eh:',sum(par_tuple))
print('A soma de todos os numeros impares eh:',sum(impar_tuple))