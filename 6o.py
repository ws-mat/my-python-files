nm=input('Digite seu nome: ')
id=int(input('Digite sua idade: '))
sx=input('Digite seu sexo: ')
n1=float(input('Digite uma nota: '))
n2=float(input('Digite mais uma nota: '))
nt=(n1+n2)/2
print('\nSeu nome é {0}, você tem {1} anos de idade, seu sexo é {2}, e sua nota é {3:.2f}.'.format(nm,id,sx,nt))