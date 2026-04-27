'''

nm=input('Digite o nome do produto: ')#                 variável que lê o nome do produto.
qt=int(input('Digite a quantidade comprada: '))#        variável que lê a quantidade comprada.
vu=float(input('digite o valor unitário: '))#           variável que lê o valor unitário do produto.
des=float(input('Digite o percentual de desconto: '))#  variável que lê o percentual a ser descontado.
val=vu*qt-(des/100)#                                    variável que determina o valor a ser pago.
print('Produto: ',nm,'\nValor: R$ ',val)#               print com resultado do calculo e mostrando o nome do produto.




'''

texto='estafilococos'
textoinvertido=''
for i in texto:
    textoinvertido=i+textoinvertido
print(textoinvertido)

#texto muito maneiro e legal