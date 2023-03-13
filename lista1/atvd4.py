repita = True 

while repita == True:

    a = input("Senhor(a), abaixo informe o seu nome: ")
    b = int(input("Informe a sua atual idade: "))

    if b < 18:
        print (a +", você é menor de idade.")
    elif b >= 18 and b < 65:
        print(a +", você é adulto.")
    else:
        print(a +", você é idoso.")

    op2 = int(input("Deseja repetir?\n1- Sim\n2- Não: "))

    if op2 == 1:
        repita = True 
    else: 
        repita = False