# boas vindas ao cliente.
print("Oii, seja bem vindo(a) a lojinha virtual da Sabrina 🌷💗")

# input do valor e da quantidade de produtos.
valorunitario = float(input("Qual o valor unitário do produto?: "))
quantidade = int(input("Qual será a quantidade que você irá levar?: "))

#calculo do valor e quantidade.
valorsemdesconto = valorunitario * quantidade

# exigencia dos comandos, com if, elif e else.
if valorsemdesconto < 2500:  
    desconto = 0
elif valorsemdesconto >= 2500 and valorsemdesconto < 6000:  
    desconto = 0.04
elif valorsemdesconto >= 6000 and valorsemdesconto < 10000:
    desconto = 0.07
else:
    desconto = 0.11

# calculo do valor com desconto.
valorcomdesconto = valorsemdesconto * (1 - desconto)

# print 
print(f"Valor total sem desconto: R${valorsemdesconto:.2f}")
print(f"Valor total com desconto: R${valorcomdesconto:.2f}")

# pedido com desconto
if valorsemdesconto >= 2500:
    print("Eba! Você irá levar esse produto com um descontinho. 😉")
else:
    print("Seu pedido não atingiu o valor mínimo para desconto. 😢")
