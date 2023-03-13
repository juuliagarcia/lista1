idade = int(input("Digite a idade da pessoa: "))

cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))

anos_fumando = idade - 18  # considerando que a pessoa começou a fumar aos 18 anos
total_cigarros = anos_fumando * 365 * cigarros_por_dia
total_minutos_perdidos = total_cigarros * 10
total_dias_perdidos = total_minutos_perdidos / (24 * 60)

print("Essa pessoa perdeu aproximadamente", round(total_dias_perdidos), "dias de vida devido ao hábito de fumar.")

