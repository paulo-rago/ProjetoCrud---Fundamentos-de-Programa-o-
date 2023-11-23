import csv
import os

# Função para limpar a tela
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Função para adicionar um livro à biblioteca
def adicionar_livro(biblioteca):
    print("Adicionar Livro")
    dados_livro = input("Digite Nome, Autor, Categoria, Custo (separados por vírgula): ").split(",")
    nome, autor, categoria, custo = dados_livro
    custo = float(custo)
    livro = {"Nome": nome, "Autor": autor, "Categoria": categoria, "Custo": custo}
    biblioteca.append(livro)
    print("Livro adicionado à biblioteca.")

# Função para listar todos os livros na biblioteca
def listar_livros(biblioteca):

# Função para atualizar as informações de um livro
def atualizar_livro(biblioteca, livro_id):

# Função para excluir um livro da biblioteca
def excluir_livro(biblioteca, livro_id):

# Função para calcular o total gasto na coleção de livros
def calcular_gastos_totais(biblioteca):

import os
import time

def livro_aleatorio():
    try:
        with open("livros.txt", mode="r", encoding="utf-8") as arquivo:
            livros = arquivo.readlines()

            indice = (len(livros) * int(time.time())) % len(livros)

            livro_aleat = livros[indice].strip()  # Obtém o livro aleatório

            # Separação dos detalhes do livro
            detalhes = livro_aleat.split(",")  # Suponha que o arquivo "livros.txt" esteja no formato: "Título, Autor, Gênero, Custo"
            titulo = detalhes[0]
            autor = detalhes[1]
            genero = detalhes[2]
            preco = detalhes[3]

            # Adiciona os detalhes à sessão "Livros Indicados" no arquivo "biblioteca.csv"
            with open("biblioteca.csv", mode="a", newline="", encoding="utf-8") as arquivo_csv:
                campos = ["Nome", "Autor", "Categoria", "Custo"]
                escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
                escritor.writerow({"Nome": titulo, "Autor": autor, "Categoria": genero, "Custo": preco})

            print("O livro indicado foi adicionado à biblioteca.")
    except FileNotFoundError:
        print("Arquivo 'livros.txt' não encontrado.")

biblioteca = []

if os.path.isfile("biblioteca.csv"):
    with open("biblioteca.csv", mode="r", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        biblioteca = [row for row in leitor]

limpar_tela()
while True:
    # Exibe o menu
    print("Sistema de Gerenciamento de Biblioteca Pessoal")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Atualizar Livro")
    print("4. Excluir Livro")
    print("5. Calcular Gastos Totais")
    print("6. Indique um Livro Aleatório")
    print("7. Sair")

    # Solicita a escolha do usuário
    opcao = input("Escolha uma opção: ")

    # Realiza a ação correspondente à escolha do usuário
    if opcao == "1":
        adicionar_livro(biblioteca)
    elif opcao == "2":
        listar_livros(biblioteca)
    elif opcao == "3":
        listar_livros(biblioteca)
        livro_id = int(input("Digite o ID do livro que deseja atualizar: "))
        atualizar_livro(biblioteca, livro_id)
    elif opcao == "4":
        listar_livros(biblioteca)
        livro_id = int(input("Digite o ID do livro que deseja excluir: "))
        excluir_livro(biblioteca, livro_id)
    elif opcao == "5":
        total_gastos = calcular_gastos_totais(biblioteca)
        print(f"Total gasto em livros: R$ {total_gastos:.2f}")
    elif opcao == "6":
        livro_aleatorio()
    elif opcao == "7":
        # Salva os dados da biblioteca no arquivo CSV antes de sair
        with open("biblioteca.csv", mode="a", newline="") as arquivo:
            campos = ["Nome", "Autor", "Categoria", "Custo"]
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(biblioteca)
        print("Dados salvos. Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
