'''print('\nExercicio 6:')
turno=input('Digite o turno que voce estuda: (M - matutino, V - vespertino, N - noturno.) ')
if(turno=='M'):
    print('\nBom dia!')
elif(turno=='V'):
    print('\nBoa tarde!')
elif(turno=='N'):
    print('Boa noite!')
else:
    print('Valor invalido!')


print('\nExercicio 7:')
valaquisicao=float(input('Digite o valor de aquisição: '))
if(valaquisicao<50):
    valvenda=valaquisicao*(145/100)
else:
    valvenda=valaquisicao*(130/100)
print(f'O valor de venda é: R$ {valvenda}.')

print('\nExercício 11:')
num=int(input('Digite um número inteiro (para ver se é par ou impar):'))
if(num==1):
    print('Impar')
else:
    print('Par')

print('\nExercício 13')
print('Verificar se estes números estão em ordem crescente ou não.')
n1=int(input('Digite um número INTEIRO.'))
n2=int(input('Digite um número INTEIRO.'))
n3=int(input('Digite um número INTEIRO.'))
if(n1<n2 and n1<n3):
    menor=n1
    if(n2<n3):
        meio,maior=n3,n2
elif(n2<n1 and n2<n3):
    menor=n2
    if(n1<n3):
        meio,maior=n1,n3
    else:
        meio,maior=n3,n1
else:
    meio,maior=n2,n1
if(n1<n2 and n2<n3):
    print(f'Está em ordem crescente. Ordem: {menor}, {meio}, {maior}.')
else:
    print(f'não está em ordem crescente. Ordem: {menor}, {meio}, {maior}.')
'''
#print(f'\nExercício {ex}:')#Exercício 15
#ex=ex+1
ht=float(input('Digite as horas trabalhadas neste mês: '))
sal=40.50*ht
if(sal>=2500):
    sal=sal-(sal*(11/100))
    print(f'O seu salário é: {sal} (11% foi para o imposto de renda)')
else:
    print(f'O seu salário é: {sal}')


sal=float(input('Digite o seu salário: '))
parc=float(input('Digite o valor das parcelas/prestações: '))
if(parc>=sal*(20/100)):
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')