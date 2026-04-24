pr1=float(input('Digite o valor de produto 1: '))#valores dos 5 produtos
pr2=float(input('Digite o valor de produto 2: '))
pr3=float(input('Digite o valor de produto 3: '))
pr4=float(input('Digite o valor de produto 4: '))
pr5=float(input('Digite o valor de produto 5: '))

pa1=pr1-(pr1*(10/100))#valores com desconto a vista
pa2=pr2-(pr2*(10/100))
pa3=pr3-(pr3*(10/100))
pa4=pr4-(pr4*(10/100))
pa5=pr5-(pr5*(10/100))

pc1=pr1-(pr1*(5/100))#valores com desconto a cartao
pc2=pr2-(pr2*(5/100))
pc3=pr3-(pr3*(5/100))
pc4=pr4-(pr4*(5/100))
pc5=pr5-(pr5*(5/100))


# fpg=int(input('Digite a forma de pagamento: (1-deb, 2-cred, 3-pix, 4-dinheiro) '))
# print('Produto 1:\nÀ vista ====== 10% de desconto(',pr1*(10/100),' - {0})\ncartão ======= 5% de desconto ',pr1*(5/100),' - {1})\nparcelado ==== sem desconto (0 - {2})\n'.format(pa1,pc1,pr1))

print(f'Produto 1:\nÀ vista ====== 10% de desconto({(pr1*(10/100)):.2f} - {pa1:.2f})\ncartão ======= 5% de desconto({(pr1*(5/100)):.2f} - {pc1:.2f}\nparcelado ==== sem desconto (0 - {pr1:.2f})')
print(f'Produto 2:\nÀ vista ====== 10% de desconto({(pr2*(10/100)):.2f} - {pa2:.2f})\ncartão ======= 5% de desconto({(pr2*(5/100)):.2f} - {pc2:.2f}\nparcelado ==== sem desconto (0 - {pr2:.2f})')
print(f'Produto 3:\nÀ vista ====== 10% de desconto({(pr3*(10/100)):.2f} - {pa3:.2f})\ncartão ======= 5% de desconto({(pr3*(5/100)):.2f} - {pc3:.2f}\nparcelado ==== sem desconto (0 - {pr3:.2f})')
print(f'Produto 4:\nÀ vista ====== 10% de desconto({(pr4*(10/100)):.2f} - {pa4:.2f})\ncartão ======= 5% de desconto({(pr4*(5/100)):.2f} - {pc4:.2f}\nparcelado ==== sem desconto (0 - {pr4:.2f})')
print(f'Produto 5:\nÀ vista ====== 10% de desconto({(pr5*(10/100)):.2f} - {pa5:.2f})\ncartão ======= 5% de desconto({(pr5*(5/100)):.2f} - {pc5:.2f}\nparcelado ==== sem desconto (0 - {pr5:.2f})')