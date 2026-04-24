'''

a=[88,81,82,82,83]
a.sort()
print(a)
print(a.index(88))
a.insert(1,100)
print(a)
print(a.count(82))
a.pop()
print(a)
a.pop(0)
print(a)
'''
print('\nExercicio:')


#lista.sort(reverse=True)#ordena os valores de ordem reversa

t=[[1,2],[3],[4,5,6]]

print(sum(t[0])+sum(t[1])+sum(t[2]))
print(t[0][0]+t[0][1]+t[1][0]+t[2][0]+t[2][1]+t[2][2])

x=t[0]+t[1]+t[2]
print(x,sum(x))

t=t[0]+t[1]+t[2]

print('\nExercicio2:')

t=[1,2,3]
# a=[int(t[0])]
# b=[a+t[1]]
# c=[b+int(t[2])]

s=[t[0] , t[1]+t[-0] , t[2]+t[-1] ]
print(s)

# print(sum(a,b,c))

print('\nExercicio 3:')


country=['Alemanha','japao','italia']
country.insert(0,'Brasil')
print(country)

print('\nExercicio 4:')
lista=[0,1,2,3,4,5,6,7,8,9,10]
print(lista[1:10])
print(lista[8:])
print(lista[0],lista[2],lista[4],lista[6],lista[8],lista[10])
print(lista[1],lista[3],lista[5],lista[7],lista[9])


lista.sort(reverse=True)#lista reversa
print(lista)
print(sum(lista))
print(len(lista))

print('\nExercicio 5')
lista=[0,1,6,310,11,2,33,4332,123,1221,321321,3123,23123,2,3,4,5,6,7,8,9,1]
print(max(lista),'Maximo')
print(min(lista),'Minimo')

print('\nExercicio 6')
p1=[7.0,8.3,10.0,6.5,9.3]
p2=[8.5,6.9,5.0,7.5,9.8]

m1=(p1[0]+p1[1]+p1[2]+p1[3])/4
print('Média turma 1: ',m1)
m2=(p2[0]+p2[1]+p2[2]+p2[3])/4
print('Média turma 2: ',m2)