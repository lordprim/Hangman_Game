####### Importando a estrutura do jogo:
from Estrutura import forca
## Importanto libraria para número aleatório:
from random import randint

########### Funções do jogo ###################
# Função para a escolha de palavra:
def EscolherPalavra():
    # Aberturado arquivo com as palavras:
    arquivo = open("palavras.txt", "r")
    # Comando para percorrer todo o documento:
    arquivo.seek(0,0)
    # Variavel para sortiar uma palavra do documento:
    sorte = randint(0,15)
    # Variavel auxiliar para a busca da palavra:
    contador = 0

    # Processo para localizar a palavra dentro do documento:
    for linha in arquivo:
        if contador == sorte:
            arquivo.close()
            return linha
        contador += 1
    arquivo.close()

# Função para recomçar o jogo:
def pergunta(questão, erro = "Digite S para sim e N para não!"):
    while True:
        try:
            resposta = input(questão)
            if resposta[0] == "S" or resposta[0] == "s":
                return True
            elif resposta[0] == "N" or resposta[0] == "n":
                return False
            else:
                print(erro)
        except:
            print("Certifique-se de digitar S ou N!")

# Função que altera as letras da palavra por "_":
def PalavrasEmJogo(word):
    temp = []
    for a in range(len(word)):
        temp += ['_']
    for x in temp:
        indece = randint(3, 5)
        temp[indece] = word[indece]
    del (temp[len(temp) - 1])
    return temp

#############################################################

######################### Váriaveis de valor #################
# Contagem de erros:
erros = 0
# Contagem de vítórias:
vitória = 0
# Contagem de derrotas:
derrota = 0
# Contagem de partidas disputadas:
partidas = 0

############################################################

# Requisitar nome do jogador:
print('#'*40)
print("Bem Vindo ao Jogo da Forca!")
print('#'*40)
nome = input('Digite seu nome: ')

# Chamada das funções:
word = EscolherPalavra()
temp = PalavrasEmJogo(word)

################# Inicio da repetição do jogo ###################
# Chamada da variavel da tela de inicio jogo:
TelaInicio = True
# Chamada para a tela do jogo:
TelaJogo = True
while TelaJogo:
    while TelaInicio:
        # Questionamento de inicio de jogo:
        if pergunta("Deseja começar? [S/N]: "):
            print('\n'*10)
            print("Começo de Jogo!")
            TelaInicio = False

    # Buscando a função da estrutura do jogo contida na pasta "Estrutura":
    forca(erros) # imprime desenho da forca

    # Imprime os valores de Vitórias, Derrotas e Partidas jogadas:
    print(f"Número de vitórias: {vitória}")
    print(f"Número de derrotas: {derrota}")
    print(f"Número de partidas disputadas: {partidas}")

    # Imprime o campo para o jogador fazer a tentativa:
    print('\n\nAdivinhe: ', end='')
    for let in temp:
        print(let, end='  ')
    print('\n')

    # Verificação se o jogador perdeu:
    if erros == 6:
        # Cahamada da Tela de fim de jogo:
        TelaDeFim = True
        # Imprime a mensagem de derrota:
        print('\nVOCÊ PERDEU!')
        # Aumenta um na contagem de derrotas:
        derrota += 1
        # Aumenta um na contagem de partida:
        partidas += 1

        # Chama a repetição de fim de jogo:
        while TelaDeFim:
            # Questionamento se deseja continuar jogando:
            if pergunta("Você deseja jogar novamente? [S/N]: "):
                TelaDeFim = False
                # Caso a resposta seja "SIM" o jogo recomeça com uma nova palavra:
                # Chama as funções de geração e zera o jogo:
                word = EscolherPalavra()
                temp = PalavrasEmJogo(word)
                erros = 0
                forca(erros)
                print('\n\nAdivinhe: ', end='')
                for let in temp:
                    print(let, end='  ')
                print('\n')

    # Verificação se o jogador ganhou:
    ganhouJogo = True
    for let in temp:
        if let == '_':
            ganhouJogo = False
    if ganhouJogo:
        # Mensagem de vitória:
        print(f'\nParabéns {nome} você venceu!!!')
        # Aumenta um ponto na contagem de vitória:
        vitória += 1
        # Aumenta um na contagem de partida:
        partidas += 1
        # Chama a repetição de vitória:
        GanhouJogo = True
        # Abre a repetição para recomeço do jogo:
        while GanhouJogo:
            # Questionamento se deseja continuar jogando:
            if pergunta("Você deseja jogar novamente? [S/N]: "):
                GanhouJogo = False
                # Caso a resposta seja "Sim" o jogo recomeça:
                # Chamando as funções para geração de uma nova palavra, jogo zera:
                word = EscolherPalavra()
                temp = PalavrasEmJogo(word)
                erros = 0
                forca(erros)
                print('\n\nAdivinhe: ', end='')
                for let in temp:
                    print(let, end='  ')
                print('\n')

    # Captura a letra do usuario:
    letraDig = input('Informe uma letra: ')

    # Verificação se o jogador acertou alguma letra:
    errouLetra = True
    for i, let in enumerate(word):
        if word[i] == letraDig:
            temp[i] = word[i]
            errouLetra = False
    if errouLetra:
        erros = erros+1

#####################################################################