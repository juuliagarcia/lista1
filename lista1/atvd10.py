# Lê os três números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

# Verifica a ordem crescente dos números e os exibe
if num1 <= num2 <= num3:
    print(num1, num2, num3)
elif num1 <= num3 <= num2:
    print(num1, num3, num2)
elif num2 <= num1 <= num3:
    print(num2, num1, num3)
elif num2 <= num3 <= num1:
    print(num2, num3, num1)
elif num3 <= num1 <= num2:
    print(num3, num1, num2)
else:
    print(num3, num2, num1)
