ex=1
print(f'Exercício {ex}:')#Exercício 1
ex=ex+1
n1=int(input('Digite um numero inteiro: '))
n2=int(input('Digite outro numero inteiro: '))
n3=float(input('Digite um numero real: '))
print(f'\n{n1*(n2/2)}\n{n1*3+n3}\n{n3**3}') #1o Exercicio.

print(f'\nExercício {ex}:')#Exercício 2
ex=ex+1
n1=int(input('Digite um numero inteiro: '))
if(n1>=10):
    print('é igual ou maior q dez.')
else:
    print('é menor que 10.')

print(f'\nExercício {ex}:')#Exercício 3
ex=ex+1
n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
if(n1>=n2):
    print(f'O maior é: {n1}')
elif(n2>n1):
    print(f'O maior é: {n2}')

print(f'\nExercício {ex}:')#Exercício 4
ex=ex+1
n1=int(input('Digite um numero:'))
n2=int(input('Digite outro: '))
n3=int(input('Digite outro: '))

if(n1<=n2 and n1<=n3):
    menor = n1
    if(n2<=n3):
        meio,maior=n2,n3
    else:
        meio,maior=n3,n2
elif(n2<=n1 and n2<=n3):
    menor=n2
    if(n1<=n3):
        meio,maior=n1,n3
    else:
        meio,maior=n3,n1
else:
    meio,maior=n2,n1

print(f'Ordem crescente: {menor}, {meio}, {maior}')

print(f'\nExercício {ex}:')#Exercício 5
ex=ex+1
gen=input('Digite M para Masculino e F para Feminino:')
if(gen=='M'):
    print('Masculino selecionado.')
elif(gen=='F'):
    print('Feminino Selecionado.')
else:
    print('Sexo invalido.')

print(f'\nExercício {ex}:')#Exercício 6
ex=ex+1
turno=input('Digite o turno que voce estuda: (M - matutino, V - vespertino, N - noturno.) ')
if(turno=='M'):
    print('\nBom dia!')
elif(turno=='V'):
    print('\nBoa tarde!')
elif(turno=='N'):
    print('Boa noite!')
else:
    print('Valor invalido!')

print(f'\nExercício {ex}:')#Exercício 7
ex=ex+1
valaquisicao=float(input('Digite o valor de aquisição: '))
if(valaquisicao<50):
    valvenda=valaquisicao*(145/100)
else:
    valvenda=valaquisicao*(130/100)
print(f'O valor de venda é: R$ {valvenda:.2f}.')

print(f'\nExercício {ex}:')#Exercício 8
ex=ex+1
num=float(input('Digite um número POSITIVO, para calcular sua raíz quadrada.'))
if(num>0):
    res=num**0.5
    print(f'Resultado: {res:.2f}')
else:
    print('número invalido, tente novamente.')

print(f'\nExercício {ex}:')#Exercício 9
ex=ex+1
num=float(input('Digite um número. Se for positivo, irá calcular a raíz quadrada.\nSe for negativo, irá calcular o número ao quadrado.'))
if(num>0):
    res=num**0.5
    print(f'Resultado (raíz quadrada do número): {res:.2f}')
else:
    if(num<0):
        res=num**2
        print(f'Resultado (número ao quadrado): {res:.2f}')
    else:
        print('O número digitado foi 0 ou um número não inválido.')

print(f'\nExercício {ex}:')#Exercício 10
ex=ex+1
num=float(input('Digite um número POSITIVO para ser calculado ao quadrado e em raíz quadrada.'))
if(num>0):
    res1=num*2
    res2=num**0.5
    print(f'Resultado (elevado ao quadrado): {res1}\nResultado (em raíz quadrada): {res2:.3f}')
else:
    print('Número inválido.')

print(f'\nExercício {ex}:')#Exercício 11
ex=ex+1
num=int(input('Digite um número inteiro (para ver se é par ou impar):'))
if(num==1):
    print('Impar')
else:
    print('Par')

print(f'\nExercício {ex}:')#Exercício 12
ex=ex+1
num1=int(input('Digite um número INTEIRO e POSITIVO: '))
num2=int(input('Digite outro número INTEIRO E POSITIVO (para comparar com o outro número): '))
if(num1>0 and num2>0):
    if(num1>num2):
        maior=num1
        menor=num2
    else:
        maior=num2
        menor=num1
    res=maior-menor
    if(num1==num2):
        print('Números iguais')
    else:
        print(f'O maior número é {maior}, e o menor é {menor}.\nA diferença dos dois é: {res}.')
else:
    print('Número inválido.')

print(f'\nExercício {ex}:')#Exercício 13
ex=ex+1
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

print(f'\nExercício {ex}:')#Exercício 14
ex=ex+1
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
if((n1>=0 and n2>=0) and (n1<=10 and n2<=10)):
    print('Notas válidas.')
    med=n1+n2/2
    print(f'Média: {med:.2f}')
else:
    print('Nota inválida.')

print(f'\nExercício {ex}:')#Exercício 15
ex=ex+1
ht=float(input('Digite as horas trabalhadas neste mês: '))
sal=40.50*ht
if(sal>=2500):
    sal=sal-(sal*(11/100))
    print(f'O seu salário é: {sal:.2f} (11% foi para o imposto de renda)')
else:
    print(f'O seu salário é: {sal:.2f}')


print(f'\nExercício {ex}:')#Exercício 16
ex=ex+1
sal=float(input('Digite o seu salário: '))
parc=float(input('Digite o valor das parcelas/prestações: '))
if(parc>=sal*(20/100)):
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')

print(f'\nExercício {ex}:')#Exercício 17
ex=ex+1
alt=float(input('Digite a sua altura: '))
gen=input('Digite o seu sexo: (M - MASC, F - FEM) ')
if(gen=='M'):
    res=(72.7*alt)-58
    print(f'Seu peso ideal (masculino) é: {res:.2f}')
elif(gen=='F'):
    res=(62.1*alt)-44.7
    print(f'Seu peso ideal (feminino) é: {res}')

print(f'\nExercício {ex}:')#Exercício 18
ex=ex+1
num=int(input('Digite um número INTEIRO E POSITIVO (n>0): '))
if(num>0):
    print(f'')