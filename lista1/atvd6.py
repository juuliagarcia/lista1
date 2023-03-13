num = input("Digite um número inteiro de três dígitos: ")

# Verifica se o número tem três dígitos
if len(num) != 3:
    print("Número inválido")
else:
    # Converte o número para inteiro e calcula a soma dos dígitos
    num = int(num)
    soma = 0
    while num > 0:
        soma += num % 10
        num //= 10

    # Exibe a soma dos dígitos
    print("A soma dos dígitos é:", soma)
