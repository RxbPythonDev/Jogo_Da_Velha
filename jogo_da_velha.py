import os

#Função para mostrar a tabela do jogo
def mostra_jogo():
    print(f' {posicoes[0]} | {posicoes[1]} | {posicoes[2]}')
    print('-----------')
    print(f' {posicoes[3]} | {posicoes[4]} | {posicoes[5]}')
    print('-----------')
    print(f' {posicoes[6]} | {posicoes[7]} | {posicoes[8]}')
    print()

#Funções para verificar se a condição de vitória foi atingida

#Função que verifica as linhas
def verifica_linha(posicoes):
    combinacao = ''
    for linha in range(0,7,3):
        for lugar in range(3):
            combinacao += posicoes[linha + lugar]
        if combinacao == 'XXX' or combinacao == 'OOO':
            return True
        else:
            combinacao = ''

#Função que verifica as colunas
def verifica_coluna(posicoes):
    combinacao = ''
    for coluna in range(3):
        for lugar in range(0,7,3):
            combinacao += posicoes[coluna + lugar]
        if combinacao == 'XXX' or combinacao == 'OOO':
            return True
        else:
            combinacao = ''

#Função que verifica as diagonais
def verifica_diagonal(posicoes):
    combinacao = ''
    for lugar in range(0,9,4):
        combinacao += posicoes[lugar]
    if combinacao == 'XXX' or combinacao == 'OOO':
        return True
    combinacao = ''
    for lugar in range(2,7,2):
        combinacao += posicoes[lugar]
    if combinacao == 'XXX' or combinacao == 'OOO':
        return True

#Função que verifica se alguma das condições de vitória retorna verdadeira
def verifica_vitoria(posicoes):
    if verifica_linha(posicoes):
        return True
    elif verifica_coluna(posicoes):
        return True
    elif verifica_diagonal(posicoes):
        return True
    else:
        return False

#Criação do tabuleiro e inicialização dos jogadores
posicoes = []
for i in range(1,10):
    posicoes.append(str(i))
jogador = 'Jogador 1'
jogadas = 9

#Execução do código do jogo
while True:
    print('Bem-vindo ao jogo da velha para 2 jogadores. \n')
    mostra_jogo()
    print(f'Vez do {jogador}.')
    jogada = int(input('Escolha um número para fazer uma jogada na posição. '))
    while jogada > 9 or jogada < 1 or posicoes[jogada - 1] == 'X' or posicoes[jogada - 1] == 'O':
        jogada = int(input('Jogada inválida! Escolha uma posição para fazer sua jogada.'))
    os.system('cls')
    if jogador == 'Jogador 1':
        posicoes[jogada - 1] = 'X'
    elif jogador == 'Jogador 2':
        posicoes[jogada - 1] = 'O'
    jogadas -= 1
    if verifica_vitoria(posicoes):
        mostra_jogo()
        print(f'Vitória do {jogador}!')
        break
    elif jogadas == 0:
        mostra_jogo()
        print('Deu Velha!!!')
        break
    jogador = 'Jogador 2' if jogador == 'Jogador 1' else 'Jogador 1'

print('FIM DE JOGO!')