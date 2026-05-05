QUANTIDADE_ALUNOS = 3
MEDIA_APROVACAO = 7
MEDIA_RECUPERACAO = 5


def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def definir_status(media):
    if media >= MEDIA_APROVACAO:
        return "Aprovado"
    elif media >= MEDIA_RECUPERACAO:
        return "Recuperação"
    else:
        return "Reprovado"


def cadastrar_aluno():
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    media = calcular_media(nota1, nota2, nota3)
    status = definir_status(media)

    return {
        "nome": nome,
        "media": media,
        "status": status
    }


def encontrar_melhor_aluno(alunos):
    melhor_aluno = alunos[0]

    for aluno in alunos:
        if aluno["media"] > melhor_aluno["media"]:
            melhor_aluno = aluno

    return melhor_aluno


alunos = []

for i in range(QUANTIDADE_ALUNOS):
    aluno = cadastrar_aluno()
    alunos.append(aluno)

for aluno in alunos:
    print(aluno["nome"], aluno["media"], aluno["status"])

melhor_aluno = encontrar_melhor_aluno(alunos)

print("Melhor aluno:", melhor_aluno["nome"])
