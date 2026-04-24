lista1=[10,20,30,40]
lista2=['spam', 'bungee', 'swallow']
print(lista1,lista2)

lista1=['oi',2.0,5,[10,20]]
print(lista1)

print(len(lista1))#len=conta os elementos ( o [10, 20] conta como apenas 1 elemento)

uma_lista=[3,67,'gato',[56,57,'cachorro',],[],3.14,False]
print(len(uma_lista))


num=[17,123,87,34,66,8398,44]

print(sum(num))

print(' ')
print(num[2])
print(num[9-8])
print(num[-2])
print(num[-1])

frutas=['maçã','laranja',['banana','cereja']]
print('maçã' in frutas)
print('banana' in frutas)

frutas=['maçã','laranja',['banana','cereja']]
print([1,2] + [3,4])
print(frutas,'FRutas')

print(['teste']*4)
print([1,2,['ola', 'adeus']]*2)
print([frutas+num])
print('Max Num',max(num))
print('Min Num',min(num))
print('Sum num',sum(num))
#0=a  1=b 2=c 3=d 4=e 5=f
uma_lista=['a','b','c','d','e','f']
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])
print(uma_lista[0:6])
print(uma_lista[4:])