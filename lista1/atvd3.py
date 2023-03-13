num = int(input("Digite um número inteiro: "))

# Verifica se o número é primo
primo = True
for i in range(2, num):
    if num % i == 0:
        primo = False
        break

# Exibe o resultado
if primo:
    print("O número é primo")
else:
    print("O número não é primo")


        