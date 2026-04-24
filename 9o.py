nm=input('Digite seu nome: ')#                                                                                                                                                                          variaveis cm nome e o preço dos 3 produtos
val1=float(input('Digite o valor do primeiro produto: '))
val2=float(input('Digite o valor do segundo produto: '))
val3=float(input('Digite o valor do terceiro produto: '))

total=val1+val2+val3#                                                                                                                                                                                   total dos 3 produtos

media=total/3#                                                                                                                                                                                          média dos 3 produtos

valdesc1=(val1*(5/100))#                                                                                                                                                                                valor dos produtos com 5% de desconto
valdesc2=(val2*(5/100))
valdesc3=(val3*(5/100))

valimp1=(val1*(12/100))#                                                                                                                                                                                valor dos produtos com 12% de imposto
valimp2=(val2*(12/100))
valimp3=(val3*(12/100))

print(f'\n=======================================================================================\n\nO seu nome é:{nm}\nO seu total da conta é: {total:.2f}\nA média dos preços é: {media:.2f}\n')#     começo do extrato, com nome(do cliente), total e e media dos produtos

print(f'O valor do 1o produto: {(val1):.2f}, com 5% de desconto é: {(valdesc1):.2f}, e com 12% de imposto é: {(valimp1):.2f}')#                                                                         valor dos 3 produtos cm imposto e desconto aplicados.;
print(f'O valor do 2o produto: {(val2):.2f}, com 5% de desconto é: {(valdesc2):.2f}, e com 12% de imposto é: {(valimp2):.2f}')
print(f'O valor do 3o produto: {(val3):.2f}, com 5% de desconto é: {(valdesc3):.2f}, e com 12% de imposto é: {(valimp3):.2f}\n')

