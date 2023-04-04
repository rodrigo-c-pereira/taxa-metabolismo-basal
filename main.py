input("Vamos calcular sua taxa de metabolismo basal!")
gender = "m"
str(input("Antes de começar, informe 'm' para homem ou 'f' para mulher:"))

if gender=="m":
    kg = int(input("Insira sua massa em kg:"))
    h = int(input("Insira sua altura em cm:"))
    age = int(input("Insira sua idade em anos:"))
    formula= 66 + (13.7*kg) + (5*h) - (6.8*age)
    print("Sua taxa de metabolismo basal é de", formula, "kcal.")


elif gender=='f':
    kg = int(input("Insira sua massa em kg:"))
    h = int(input("Insira sua altura em cm:"))
    age = int(input("Insira sua idade em anos:"))
    formula = 655 + (9.6*kg) + (1.8*h) - (4.7*age)
    print("Sua taxa de metabolismo basal é de", formula, "kcal.")

else:
    print("Não foi possível definir o gênero.")
