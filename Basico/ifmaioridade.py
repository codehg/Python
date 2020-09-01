"""
Verifica se o usuário eh maior de idade
"""

idade = int(input("Digite sua idade em anos "))

if idade > 18:
    print("Voce eh menor de idade, entrada negada ")
elif idade <= 18:
    print("Voce eh maior de idade, entrada permitida ")


