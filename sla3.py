# leia= input()
# input() = dentro dos parenteses será uma string
nome=input("Digite seu nome: ")
print("meu nome é", nome)
print(type(nome))


salario=int(input('Salario = '))
imposto=float(input('Digite o imposto = '))
print(salario," é o seu salário e ",imposto," é o seu imposto.")

sal=int(input('Salario='))
print("o salario digitado foi %s" % sal)

x="ederson"
y="pastel"
valor=3.140000000
print("O nome digitado foi %s e o valor foi %.2f, e ele gosta de %s" %(x,valor,y))
'''
string=(%s)
inteiro(%d)
boleano(%b)
float(%f)

obs: voce pode definir a quantidade de casas decimais adicionando-as logo apos o %. ex: %.2f

'''

nome=input('Digite seu nome: ')
print("Meu nome é %s"%nome)

print(10*nome,'\n')