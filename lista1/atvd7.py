repita = True 

while repita == True:

    a = int(input("Informe seu salário atual: "))

    if a <= 1500:
        novosalario = a*1.10

    else:
        novosalario = a*1.05

    print(str(a) +", este é seu salário antigo")
    print(str(novosalario) +", e este é seu novo salário")
    print(str(novosalario - a) +", esta é o aumento salarial")


    op2 = int(input("Deseja repetir?\n1- Sim\n2- Não"))

    if op2 == 1:
         repita = True 
    else: 
         repita = False