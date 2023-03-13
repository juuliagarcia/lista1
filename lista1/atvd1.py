def soma(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def dividir(a,b):
    return a / b

def multiplicar(a,b):
    return a * b

repita = True 

while repita == True:

    a = int(input("Informe o primeiro número desejado: "))
    b = int(input("Informe o segundo número desejado: "))

    op = int(input("1-Soma\n2-Subtrair\n3-Dividir\n4-Multiplicar\nR:"))

    if op == 1:
        print (soma(a,b))
    elif op == 2:
        print (subtrair(a,b))
    elif op == 3:
        print (dividir(a,b))
    elif op == 4: 
        print (multiplicar(a,b))
    else:
        print ("Número inválido, escolha uma operação (acima) existente.")

    op2 = int(input("Deseja repetir?\n1- Sim\n2- Não"))

    if op2 == 1:
        repita = True 
    else: 
        repita = False