repita = True 

while repita == True:

    a = int(input("Informe a primeira nota: "))
    b = int(input("Informe a segunda nota: "))
    c = int(input("Informe a terceira nota: "))

    media = (a+b+c)

    if media >= 7:
        print ("Você está aprovado.")
    elif media >= 5 and media <= 6.9:
        print("Você está de recuperação.")
    else:
        print("Você está reprovado.")

    op2 = int(input("Deseja repetir?\n1- Sim\n2- Não: "))

    if op2 == 1:
        repita = True 
    else: 
        repita = False