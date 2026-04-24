# frutas=['maçã','banana','tomate','abacaxi']
# for item in frutas:
#     print(item)

# lista=[99,12,14,16,15,88,72,27,30]
# for element in lista: 
#     print(element)

# for i in range(0,101,5):
#     print(i)

num=int(input('digite um numero.'))
if(num>0):
    for i in range(1,11):
        res=num*i
        print(f'{num} X {i} = {res}')