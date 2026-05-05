DESCONTO_VIP = 0.20
DESCONTO_COMUM = 0.05
VALOR_FRETE = 30
VALOR_MINIMO_FRETE_GRATIS = 500


def calcular_desconto(valor_compra, cliente_vip):
    if cliente_vip:
        return valor_compra * DESCONTO_VIP
    return valor_compra * DESCONTO_COMUM


def calcular_frete(total_com_desconto):
    if total_com_desconto > VALOR_MINIMO_FRETE_GRATIS:
        return 0
    return VALOR_FRETE


def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    valor_compra = float(input("Valor da compra: "))
    tipo_cliente = input("Cliente VIP? (s/n): ").lower()

    cliente_vip = tipo_cliente == "s"

    desconto = calcular_desconto(valor_compra, cliente_vip)
    total_com_desconto = valor_compra - desconto
    frete = calcular_frete(total_com_desconto)
    total_final = total_com_desconto + frete

    return {
        "nome": nome,
        "valor_compra": valor_compra,
        "desconto": desconto,
        "frete": frete,
        "total_final": total_final
    }


def exibir_cliente(cliente):
    print("Cliente:", cliente["nome"])
    print("Compra:", cliente["valor_compra"])
    print("Desconto:", cliente["desconto"])
    print("Frete:", cliente["frete"])
    print("Total:", cliente["total_final"])
    print("------------------")


clientes = []
total_geral = 0

while True:
    cliente = cadastrar_cliente()
    clientes.append(cliente)

    total_geral += cliente["total_final"]

    continuar = input("Deseja continuar? (s/n): ").lower()

    if continuar != "s":
        break

for cliente in clientes:
    exibir_cliente(cliente)

print("Faturamento total:", total_geral)
