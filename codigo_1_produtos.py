TAXA_DESCONTO = 0.10


def calcular_total_com_desconto(valor_produto):
    desconto = valor_produto * TAXA_DESCONTO
    total = valor_produto - desconto
    return total


produtos = [100, 200, 300]

for produto in produtos:
    total = calcular_total_com_desconto(produto)
    print(total)
