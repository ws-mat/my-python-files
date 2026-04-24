dis=float(input('Digite a distancia que deseja percorrer: '))#distancia
cons=int(input('Digite o consumo de combustivel(km/l): '))#consumo(km/l)
comb=float(input('Digite o preço do combustivel: '))#preço do combustivel

ln=dis/cons#litros necessarios

custo=ln*comb#custo total da viagem

print(f'\nDistância: {dis}\nConsumo: {cons}\nPreço do combustível: {comb}\n\nLitros necessários: {ln}\nCusto total da viagem: {custo}')#escrever resultados na tela