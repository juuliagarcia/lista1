num = input("Digite um número inteiro: ")

# Calcula a soma dos cubos dos dígitos do número
soma = 0
for digito in num:
    soma += int(digito) ** 3

# Verifica se o número é um número de Armstrong
if int(num) == soma:
    print(num, "é um número de Armstrong")
else:
    print(num, "não é um número de Armstrong")
