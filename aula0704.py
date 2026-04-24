'''

a=True
b=False
c=True
d=False

res= a or b
res2= a or c
res3= b or d

print('\nA = ',a)
print('B = ',b)
print('C = ',c)
print('D = ',d)


print('\nA or B = ',res)
print('A or C = ',res2)
print('B or D = ',res3)



x = 0
y = True
print(bool(x and y))



a=int(input('Digite um numero: '))
print(type(a))

'''

# x = 5
# y = 3

# print(bool(x>y))

# x = 5 
# y = 3
# z = 7
# print(x>y and x<z)


# a = 1
# b = 2

# res=a!=2 or b==1
# res2=a!=1 or b==1
# res3=not(a==1)
# res4=a==2 and b!=1

# print(f'A: {res}, B: {res2}, C: {res3}, D: {res4}.')

# x = 10
# y = 15
# z=25
# print(x == z - y and z != y - x or not y != z - x)

# v=7
# if v>1:
#     if v>7:
#         print('valor alto.')
# else:
#     print('valor igual a ',v)

# valor=int(input('Digite o valor:'))
# if(valor>1):
#     print('caiu no if(>1)')
#     if(valor>7):
#         print('caiu no if(>7)')
#         print('valor alto')
# else: 
#     print('caiu no else')
#     print('valor = ',valor)



# idade=int(input('Quantos anos voce tem?\n'))
# prova=int(input('Quanto voce tirou na prova?\n'))
# if idade>=18 and prova >=7 :
#     print('Pode tirar a carteira.')
# else:
#     print('nao pode tirar a carteira')

# n1=float(input('Digite a primeira nota: '))
# n2=float(input('Digite a segunda nota: '))
# n3=float(input('Digite a terceira nota: '))
# n4=float(input('Digite a quarta nota: '))

# med=(n1+n2+n3+n4)/4
# # print(med)

# if(med>=6):
#     print(f'Média: {med}, Aprovado!')
# elif med<6 and med>=4:
#     print(f'Média: {med}, Exame')
# else:
#     print(f'Média: {med},Reprovado!')


# idade=22
# teste_ps="aprovado"
# pt=8.5

# if (idade>=18):
#     print('tem idade para tirar cnh')
#     if(teste_ps == "aprovado"):
#         print('esta apto a fazer as aulas praticas!')
#     elif(teste_ps == "reprovado" or pt<=7):
#         print('nao esta apto a fazer as aulas praticas.')
# else:
#     print('nao tem idade pra tirar cnh.')


x = 5
res=x % 2 == 0
print(f'\nx=5\nx%2==0 : {res}')
res=x%2==1
print(f'x%2==1 : {res}\n')
x=6
res=x%2==0
print(f'x=6\nx%2==0 : {res}')
res=x%2==1
print(f'x%2==1 : {res}\n')