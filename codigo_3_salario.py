TAXA_BONUS = 0.15


def calcular_bonus(salario):
    return salario * TAXA_BONUS


def calcular_novo_salario(salario, bonus):
    return salario + bonus


nome = input("Nome: ")
salario = float(input("Salário: "))

bonus = calcular_bonus(salario)
novo_salario = calcular_novo_salario(salario, bonus)

print("Nome:", nome)
print("Bônus:", bonus)
print("Novo salário:", novo_salario)
