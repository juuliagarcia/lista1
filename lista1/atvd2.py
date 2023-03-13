repita = True 

while repita == True:

    op = int(input("Informe o número do mês desejado: "))

    if op == 1:
        print ("O número inserido corresponde ao mês de Janeiro.")
    elif op == 2:
        print ("O número inserido corresponde ao mês de Fevereiro.")
    elif op == 3:
        print ("O número inserido corresponde ao mês de Março.")
    elif op == 4: 
        print ("O número inserido corresponde ao mês de Abril.")
    elif op == 5:
        print ("O número inserido corresponde ao mês de Maio.")
    elif op == 6:
        print ("O número inserido corresponde ao mês de Junho.")
    elif op == 7:
        print ("O número inserido corresponde ao mês de Julho.")
    elif op == 8:
        print ("O número inserido corresponde ao mês de Agosto.")
    elif op == 9:
        print ("O número inserido corresponde ao mês de Setembro.")
    elif op == 10:
        print ("O número inserido corresponde ao mês de Outubro.")
    elif op == 11:
        print ("O número inserido corresponde ao mês de Novembro.")
    elif op == 12:
        print ("O número inserido corresponde ao mês de Dezembro.")
    else:
        print ("Número de mês inválido, escolha um número de 1-12.")

    op2 = int(input("Deseja repetir?\n1- Sim: \n2- Não: "))

    if op2 == 1:
        repita = True 
    else: 
        repita = False