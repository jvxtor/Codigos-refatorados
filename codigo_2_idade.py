def classificar_idade(idade):
    if idade < 18:
        return "Menor de idade"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"


idade = int(input("Idade: "))
classificacao = classificar_idade(idade)

print(classificacao)
