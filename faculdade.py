# Sistema de Controle de Estoque
# Autor: Matheus Henrique da Silva
# RU: 5331588

import sys
sys.stdout.reconfigure(encoding='utf-8')
# Dicionário para armazenar produtos e quantidades
estoque = {}

# Lista para registrar movimentações
movimentacoes = []

# Função para cadastrar produto
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")

    if nome in estoque:
        print("Produto já cadastrado!")
    else:
        estoque[nome] = 0
        print("Produto cadastrado com sucesso!")

# Função para entrada de produtos
def entrada_produto():
    nome = input("Digite o nome do produto: ")

    if nome not in estoque:
        print("Produto não encontrado!")
        return

    try:
        quantidade = int(input("Digite a quantidade recebida: "))
        data = input("Digite a data (dd/mm/aaaa): ")
        responsavel = input("Responsável: ")

        if quantidade <= 0:
            print("Quantidade inválida!")
            return

        estoque[nome] += quantidade

        movimentacoes.append(f"ENTRADA - Produto: {nome} | Qtd: {quantidade} | Data: {data} | Resp: {responsavel}")

        print("Entrada registrada com sucesso!")

    except:
        print("Erro: digite um número válido!")

# Função para saída de produtos
def saida_produto():
    nome = input("Digite o nome do produto: ")

    if nome not in estoque:
        print("Produto não encontrado!")
        return

    try:
        quantidade = int(input("Digite a quantidade a retirar: "))
        data = input("Digite a data (dd/mm/aaaa): ")
        responsavel = input("Responsável: ")

        if quantidade <= 0:
            print("Quantidade inválida!")
            return

        if estoque[nome] < quantidade:
            print("Estoque insuficiente!")
            return

        estoque[nome] -= quantidade

        movimentacoes.append(f"SAÍDA - Produto: {nome} | Qtd: {quantidade} | Data: {data} | Resp: {responsavel}")

        print("Saída registrada com sucesso!")

    except:
        print("Erro: digite um número válido!")

# Função para mostrar estoque
def mostrar_estoque():
    print("\n=== ESTOQUE ATUAL ===")
    if not estoque:
        print("Nenhum produto cadastrado.")
    else:
        for produto, qtd in estoque.items():
            print(f"{produto}: {qtd}")

# Função para mostrar movimentações
def mostrar_movimentacoes():
    print("\n=== MOVIMENTAÇÕES ===")
    if not movimentacoes:
        print("Nenhuma movimentação registrada.")
    else:
        for mov in movimentacoes:
            print(mov)

# Menu principal
while True:
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar Produto")
    print("2 - Entrada de Produto")
    print("3 - Saída de Produto")
    print("4 - Mostrar Estoque")
    print("5 - Mostrar Movimentações")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        entrada_produto()
    elif opcao == "3":
        saida_produto()
    elif opcao == "4":
        mostrar_estoque()
    elif opcao == "5":
        mostrar_movimentacoes()
    elif opcao == "6":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida!")