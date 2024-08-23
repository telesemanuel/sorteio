import random

nomes = []

while True:
    print("1 - inserir nome na lista. ")
    print("2 - Sortear. ")
    print("3 - Sair do Programa. ")

    opcao = input("Escolha uma Opção: ")

    match opcao:
        case "1":
            nome = input("Insira o nome: ")
            nomes.append(nome)
            print(f"{nome} inserido com sucesso. ")
            continue
        case "2":
            nome_sorteado = random.randint(0, len(nomes)-1)
            print(f"Nome sorteado: {nomes[nome_sorteado]}.")
            continue
        case "3":
            print("Saindo do Programa...")
        case _:
            print("Opção Inválida.")
            continue