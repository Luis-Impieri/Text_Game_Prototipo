import os

def salvar_progresso(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        for chave, valor in dados.items():
            arquivo.write(f"{chave}:{valor}\n")

def carregar_progresso(nome_arquivo):
    dados = {}
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                chave, valor = linha.strip().split(':')
                dados[chave] = valor
    return dados

def encontrar_arma(dados, arma_nome, dano):
    print(f"Você encontrou uma {arma_nome}! Que causa {dano} de dano!")
    dados['arma'] = arma_nome
    dados['dano_arma'] = dano
    return dados

def encontrar_dinheiro(dados, quantidade):
    print(f"Você encontrou {quantidade} moedas de ouro!")
    dados['dinheiro'] += quantidade
    return dados

def reiniciar_progresso():
    nome_arquivo = input("Você deseja reiniciar o progresso (S/N)? ")
    if nome_arquivo.lower() == 's':
        return True
    return False

nome = input('Digite seu nome: ')
nome_arquivo = f'{nome}_progresso.txt'  # Nome do arquivo baseado no nome do jogador

if reiniciar_progresso():
    progresso = {'nome': nome, 'vida': 100, 'dinheiro': 0}
else:
    progresso = carregar_progresso(nome_arquivo)

def jogador(dados):
    print(f"Nome: {dados['nome']}")
    print(f"Vida: {dados['vida']}")
    print(f"Dinheiro: {dados['dinheiro']}")
    
    # Defina os dados da faca quebrada (caso não tenha encontrado outra arma)
    if 'arma' not in dados:
        dados['arma'] = 'Faca Quebrada'
        dados['dano_arma'] = 10
    
    print(f"Arma: {dados['arma']} (Dano: {dados.get('dano_arma', 10)})")
    print()

if progresso:
    print("Progresso carregado:")
    jogador(progresso)

print('Após seu grupo de aventureiros ser emboscado por Orcs, você, um jovem guerreiro, acorda atordoado em uma masmorra, tendo apenas sua adaga quebrada ao seu lado. Ao olhar em volta, você vê dois corredores.')

decisao = input('Digite D para ir para o corredor da direita ou E para ir para o corredor da esquerda: ')

# Atualize os dados do progresso com base na decisão do jogador
if progresso:
    progresso['decisao'] = decisao

# Exiba os dados atualizados do jogador
jogador(progresso)


if decisao == 'D':
    progresso = encontrar_arma(progresso, 'Espada Afiada', 20)  
elif decisao == 'E':
    progresso = encontrar_dinheiro(progresso, 50)  


salvar_progresso(nome_arquivo, progresso)