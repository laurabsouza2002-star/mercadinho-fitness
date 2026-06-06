Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> Enter "help" below or click "Help" above for more information.
KeyboardInterrupt
>>> 
>>> #Inicialização:
... import time
... 
... def linhas():
...     print("=" *50)
... 
... linhas()
... print('SEJA BEM-VINDO AO SUPER FITNESS!'.center(90))
... linhas()
... 
... #Solicitação de dados ao usuário:
... print('PARA PERSONALIZAR SUA EXPERIÊNCIA. INFORME SEU PESO E ALTURA ABAIXO:'.center(90))
... linhas()
... 
... nome=(input('Digite o seu nome: '.upper()))
... altura=float(input('Digite sua altura: '.upper()))
... peso=(input('Digite o seu peso: '.upper()))
... peso = peso.replace("kg", "")
... peso = float(peso)
... linhas()
... 
... #Cálculo de IMC:
... imc = peso / (altura ** 2)
... 
... if imc <18.5:
...     print(f"{nome}, seu índice de Massa Corporal está abaixo do recomendável!".upper())
...     
... elif imc <25:
...     print(f"{nome}, seu índice de Massa Corporal está normal!".upper())
...     
... elif imc < 30:
...     print(f"{nome} , seu índice de Massa Corporal está acima do recomendável!".upper())
else:
    print(f"{nome}, você está na obesidade!".upper())

#Define os produtos conforme o IMC:
time.sleep(2)

if imc < 18.5:
    produtos = {
        1: ("Hipercalórico", 99.90),
        2: ("Aveia", 11.00),
        3: ("Pasta de Amendoim", 24.90),
        4: ("Banana", 5.00)
    }

elif imc < 25:
    produtos = {
        1: ("Frango", 25.00),
        2: ("Arroz Integral", 18.00),
        3: ("Ovos", 20.00),
        4: ("Frutas", 12.00)
    }

elif imc < 30:
    produtos = {
        1: ("Salada", 15.00),
        2: ("Iogurte Natural", 8.00),
        3: ("Whey", 120.00),
        4: ("Legumes", 10.00)
    }

else:
    produtos = {
        1: ("Salada", 15.00),
        2: ("Iogurte Natural", 8.00),
        3: ("Legumes", 10.00),
        4: ("Água", 3.00)
    }


total = 0

while True:
    print("\nPRODUTOS DISPONÍVEIS")

    for codigo, (produto, preco) in produtos.items():
        print(f"{codigo} - {produto} - R$ {preco:.2f}")

    print("0 - Finalizar compra")

    opcao = int(input("\nEscolha um produto: "))

    if opcao == 0:
        break

    if opcao in produtos:
        produto, preco = produtos[opcao]
        total += preco
        print(f"{produto} adicionado ao carrinho!")
    else:
        print("Produto inválido!")

linhas()
print(f"TOTAL DA COMPRA: R$ {total:.2f}")

#Sorteio:

def linhas():
    print('=' *95)

linhas()
print('🎉 HORA DO SORTEIO! 🎉!SE VOCÊ TIRAR UM NÚMERO PAR , GANHARÁ UM DESCONTO ESPECIAL NA SUA COMPRA!')
linhas()

import random

numero_usuario=int(input('Digite um número inteiro:'))
numero = random.randint(1, 10)

soma=numero_usuario + numero
time.sleep(2)

print(f"O seu número é {numero_usuario} + {numero} sorteado do sistema! O total é: {soma}!")
if soma % 2 == 0:
    print('PARABÉNS! VOCÊ RECEBEU O DESCONTO 10%!')
    desconto = total * 0.10
    valor_final = total - desconto
    print(f'TOTAL COM DESCONTO: R${valor_final:.2f}')
    
else: 
    print('TENTE NOVAMENTE DA PRÓXIMA VEZ!')
