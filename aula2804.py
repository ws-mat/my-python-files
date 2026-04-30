#aula 28/04
'''
while True:
    valor=int(input('Digite o valor 1 ou 0 para encerrar'))
    if valor<=1:
        print('maior que um')
        continue
    if valor>1:
        print('maior que um')

contador = 0
numero=100
while numero>0:
    numero=(numero-1)
    print(numero)
    contador=contador+1
    print(contador)
'''
op=9
num1=1#primeiro numero da operação
num2=0#segundo numero da operação



'''
while True:
    op=input('\nSelecione uma operação:\n1-Multiplicação\n2-Divisão\n3-Adição\n4-Subtração\n0-Sair')
    
    if op=='':
        print('numero incorreto.')
    elif op=='1':
        # int(op)
        print('\nMultiplicação selecionada.')
        num1=float(input('Digite o primeiro número da operação: '))
        num2=float(input(f'Digite o segundo número da operação: {num1} * '))
        mult=num1*num2
        print(f'\nO resultado da operação é: {mult}')
    elif op=='2':
        # int(op)
        print('\nDivisão selecionada.')
        num1=float(input('Digite o primeiro número da operação: '))
        num2=float(input(f'Digite o segundo número da operação: {num1} / '))
        div=num1/num2
        print(f'\nO resultado da operação é: {div}')
    elif op=='3':
        # int(op)
        print('\nAdição selecionada.')
        num1=float(input('Digite o primeiro número da operação: '))
        num2=float(input(f'Digite o segundo número da operação: {num1} + '))
        adi=num1+num2
        print(f'\nO resultado da operação é: {adi}')
    elif op=='4':
        # int(op)
        print('\nSubtração selecionada.')
        num1=float(input('Digite o primeiro número da operação: '))
        num2=float(input(f'Digite o segundo número da operação: {num1} / '))
        subt=num1-num2
        print(f'\nO resultado da operação é: {subt}')
    elif (op=='0'):
        # int(op)
        print('\nSaída selecionada.')
        break
'''
#atividade 2:

cand1=0
cand2=0
cand3=0
cand4=0
branco=0
nulo=0
while True:
    op=input('\nDigite o codigo do candidato: 1,2,3,4. Para finalizar a entrada de dados = 0.\nQualquer outro numero é voto nulo, e um voto vazio é um voto em branco. ')

    if(op=='1'):
        print(f'\nCandidato {op} selecionado.')
        cand1=cand1+1
    elif(op=='2'):
        print(f'\nCandidato {op} selecionado.')
        cand2=cand2+1
    elif(op=='3'):
        print(f'\nCandidato {op} selecionado.')
        cand3=cand3+1
    elif(op=='4'):
        print(f'\nCandidato {op} selecionado.')
        cand4=cand4+1
    elif op=='0':
        print('\nEntrada de dados finalizada.')
        break
    elif op=='':
        print('\nVoto em branco selecionado.')
        branco=branco+1
    else:
        print('\nVoto nulo selecionado.')
        nulo=nulo+1
total=cand1+cand2+cand3+cand4+branco+nulo

maior=max(cand1,cand2,cand3,cand4)
if cand1==maior:
    maior='Candidato 1'
elif cand2==maior:
    maior='Candidato 2'
elif cand3==maior:
    maior='Candidato 3'
elif cand4==maior:
    maior='Candidato 4'


print('\nResultados:')
print(f'Total de votos POR CANDIDATO =\nCandidato 1 = {cand1}\nCandidato 2 = {cand2}\nCandidato 3 = {cand3}\nCandidato 4 = {cand4}\nTotal de votos nulos = {nulo}\nTotal de votos em branco = {branco}\nTotal de votos = {total}\nGanhador = {maior}')


listanome=[]
#atividade 3:
while True:
    op=input('\nDigite a operação desejada:\n\nCadastro - 1\nConsulta - 2\nExclusão - 3\nSair - 0\n')

    if op=='1':
        addnm=input('\nCadastro selecionado. Digite o nome que deseja inserir: ')#
        listanome.insert(0,addnm)
        
    elif op=='2':
        print(f'\nConsulta selecionado.\n')
    elif op=='3':
