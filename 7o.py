n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
op=int(input('Digite uma operação: \n1 - adição; 2 - subtração; 3 - multiplicação; 4 - divisão; 5 - sair.\n'))
out=0
if(op==1):{
    out==(n1+n2)
    print(out)
}
else{
    if(op==2){
        out==(n1-n2)
        print(out)
    }else{
        if(op==3){
            out=(n1*n2)
            print(out)
        }else{
            if(op==4){
                out=(n1/n2)
                print(out)
            }else{
                if(op==5){
                    print('Saida selecionada, adeus.')
                }
            }
        }
    }
}
