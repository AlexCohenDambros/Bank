import random
from ast import literal_eval

# Função para guardar as informações do cliente em um dicionario, esse que é uma variável global
def novaConta():
    nome = input('Insira o nome completo do cliente.\n')
    profissao = input('Profissão: \n')
    renda = input('Renda mensal: \n')
    endereco = input('Endereço: \n')
    telefone = input('Telefone para contato: \n')
    senha = input('Senha: \n')
    numero = random.randint(10000, 99999)
    saldo = float(input("Digite o saldo inicial da conta: \n"))
    while True:
        if numero in contasUsadas:
            numero = random.randint(10000, 99999)
        else:
            contasUsadas.append('Nome: ' + str(nome) + ' ;' + ' Numero da conta: ' + str(numero))
            break

    dados[nome] = {'numeroConta': numero,
                   'senha': senha,
                   'profissao': profissao,
                   'renda': renda,
                   'endereco': endereco,
                   'telefone': telefone,
                   'saldo': saldo}


# Função que abre o arquivo em que estão contidas as informações dos clientes e retorna o número da conta do cliente pesquisado
def pesquisaConta():
    arquivoContas = open('teste.txt', 'r')
    escolhaDaConta = input('Qual o nome do usuário que deseja pesquisar?\n')
    conteudoContas = arquivoContas.read()
    dicionarioContas = literal_eval(conteudoContas)

    try:
        numeroConta = dicionarioContas[escolhaDaConta]['numeroConta']
        arquivoContas.close()
        return numeroConta
    except:
        arquivoContas.close()
        return 'Nome não encontrado no sistema, verifique se o digitou corretamente.\n'


# Função que abre o arquivo em que estão contidas as informações e altera a chave senhha, que está dentro da chave que repesenta
# o nome do cliente
def mudarSenha():
    arquivo = open('teste.txt', 'r')
    conteudo = arquivo.read()
    dicionario = literal_eval(conteudo)
    arquivo.close()

    try:
        contaPesquisada = int(input('Qual o número da conta que deseja pesquisar?\n'))

    # try/except para validar que apenas número serão inseridos
    except:
        print('Apenas insira números!\n')

    for nomeCliente in dicionario:
        if dicionario[nomeCliente]['numeroConta'] == contaPesquisada:
            nomeCidadao = nomeCliente
            print('Conta encontrada! Cadastrada no nome de {}'.format(nomeCliente))
            novaSenha = input('Insira uma nova senha, sem caracteres especiais e acentos, de 4 a 8 caracteres.\n')

    return [novaSenha, dicionario, nomeCidadao]


dados = {}
contasUsadas = []
caracteresProibidos = ['´', '^', '~', '`', '@', '#', '$', '_', '-', '&', '*', '%', '!', '?']

# Dicionário para exercer a função de um switch-case, que provém de outras linguagens e não existe no Python de maneira built-in
options = {'1': novaConta,
           '2': pesquisaConta,
           '3': mudarSenha}

# Loop principal, que vai receber o numero digitado e chamar a função corresponde da ação desejada
while True:
    print('Bem vindo ao Banco do Brasólia!\n')
    print('Escolha uma opções para realizar uma ação.\n')
    escolhaMenuPrincipal = input('1 - Cadastrar uma nova conta.\n'
                                 '2 - Procurar uma conta.\n'
                                 '3 - Mudar senha de uma conta.\n'
                                 '4 - Sair.\n')

    if escolhaMenuPrincipal == '4':
        break

    # func armazena o nome da função, declarada no dicionário 'options'
    func = options.get(escolhaMenuPrincipal, lambda: 'Opção Inválida!\n')

    if func == novaConta:
        while True:
            func()

            # Primeiramente ele procura um arquivo existente, caso não seja a primeira execução do programa
            try:
                arquivotxtR = open('teste.txt', 'r')
                conteudoArquivo = arquivotxtR.read()
                if len(conteudoArquivo) > 0:
                    dicionarioArquivo = literal_eval(conteudoArquivo)

                    for nomeCliente in dados:
                        dicionarioArquivo[nomeCliente] = dados[nomeCliente]

                        arquivotxtR.close()
                        arquivotxtW = open('teste.txt', 'w')
                        arquivotxtW.write(str(dicionarioArquivo))
                        arquivotxtW.close()

            # except para caso seja a primeira execução do programa, então um arquivo para armazenamento será criado
            except:
                arquivotxtW = open('teste.txt', 'w')
                arquivotxtW.write(str(dados))
                arquivotxtW.close()
            decider = input('Digite 1 para cadastrar outro cliente, 2 para voltar ao menu principal.\n')
            if decider == '2':
                break

    if func == pesquisaConta:
        while True:
            resultadoPesquisa = func()
            if type(resultadoPesquisa) == int:
                print('Numero da conta é: {}\n'.format(resultadoPesquisa))
            else:
                print(resultadoPesquisa)

            decider2 = input('Digite 1 para pesquisar outra conta, 2 para voltar ao menu principal.\n')
            if decider2 == '2':
                break

    if func == mudarSenha:

        # variável flag muda para True caso haja uma incoerência na senha, não siga as regras para criação de senha
        flag = False
        while True:
            try:
                novaSenha = func()
            except:
                continue

            if len(novaSenha[0]) > 8 or len(novaSenha[0]) < 4:
                print('A senha deve possuir entre 4 e 8 caracteres.')
                continue

            for char in novaSenha[0]:
                if char in caracteresProibidos:
                    flag = True

            if flag == True:
                print('Apenas insira caracteres alfanuméricos, sem acentos ou caracteres especiais.')
                continue

            if flag == False:
                print('Senha alterada com sucesso!\n')

                nome = novaSenha[2]
                senha = novaSenha[0]
                dicionario = novaSenha[1]

                dicionario[nome]['senha'] = senha

                arquivo = open('teste.txt', 'w')
                arquivo.write(str(dicionario))
                arquivo.close()
                break