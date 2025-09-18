idade = int(input("Digite sua idade: "))
if idade <= 1:
    print("Você é um bebê")
elif idade <= 9:
    print("Você é criança")
elif idade <= 17:
    print("Você é adolescente")
elif idade <= 59:
    print("Você é adulto")
else:
    print("Você é idoso")