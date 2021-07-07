# INTERFACE DO CLIENTE

# transformador de string em dicionário.
from ast import literal_eval


# SAQUE ------------------------------------------------------------------------------------------------------
def saque():
    # ABRINDO O ARQUIVO PARA CONFERIR AS INFORMAÇÕES DO CLIENTE
    arquivo = open('teste.txt', 'r')
    conteudo = arquivo.read()
    dicionario = literal_eval(conteudo)
    arquivo.close()

    # VERIFICANDO O QUE FOI DIGITADE ESTÁ DE ACORDO COM O SISTEMA
    try:
        print("------------------------------------------------------------------")
        conta = int(input('Qual o número da sua conta?\n'))
    except:
        print('Apenas insira números!\n')
        menu()
    try:
        senhacli = str(input('Qual é a senha da sua conta?\n'))
    except:
        print('Apenas insira números!\n')
        menu()
    # CONFERINDO O NÚMERO DA CONTA E A SENHA E SE TUDO ESTIVER CORRETO REALIZAR O SAQUE!
    for nomeCliente in dicionario:
        if dicionario[nomeCliente]['numeroConta'] == conta:
            if dicionario[nomeCliente]["senha"] == senhacli:
                print("------------------------------------------------------------------")
                print('Conta encontrada! Cadastrada no nome de {}.'.format(nomeCliente))
                valor_de_saque = float(input("Digite o valor que deseja-se sacar: "))
                print("------------------------------------------------------------------")
                print("Digite 1 para confirmar ou 2 para cancelar/sair")
                confir = int(input("Digite a opção desejada: "))
                saldoatual = dicionario[nomeCliente]['saldo']
                if confir == 1:
                    if valor_de_saque <= float(saldoatual) and valor_de_saque > 0:
                        saldoatual -= valor_de_saque

                        # ALTERANDO O SALDO ANTIGO PARA O NOVO SALDO COM O SAQUE REALIZADO
                        saldo = saldoatual
                        dicionario[nomeCliente]['saldo'] = saldo
                        arquivo = open('teste.txt', 'w')
                        arquivo.write(str(dicionario))
                        arquivo.close()
                        print("------------------------------------------------------------------")
                        print(f"O valor sacado foi de: {valor_de_saque}")
                        print(f"O valor atual da conta é: {saldoatual}")
                        break
                    else:  # DIGITOU UMA VALOR QUE NÃO PODE
                        print("Este valor não pode ser sacado!\n")
                        break
                elif confir == 2:  # VOLTAR AO MENU PRINCIPAL
                    break
                else:  # DIGITOU UM NÚMERO INVALÍDO PARA CONFIRMAR SE QUER CONTINUAR OU NÃO
                    print("Você digitou um número inválido! Tente novamente mais tarde!")
                    break
            else:  # SENHA INCORRETA
                print("Senha Incorreta! Tente novamente mais tarde!")
                break
        elif nomeCliente == list(dicionario.keys())[-1]:  # CONTA NÃO EXISTENTE NO SISTEMA
            print("\nConta não encontrada! Tente novamente!")
            break


# DEPÓSITO ------------------------------------------------------------------------------------------------------
def deposito():
    # ABRINDO O ARQUIVO PARA CONFERIR AS INFORMAÇÕES DO CLIENTE
    arquivo = open('teste.txt', 'r')
    conteudo = arquivo.read()
    dicionario = literal_eval(conteudo)
    arquivo.close()

    # VERIFICANDO O QUE FOI DIGITADE ESTÁ DE ACORDO COM O SISTEMA
    try:
        print("------------------------------------------------------------------")
        conta = int(input('Qual o número da sua conta?\n'))
    except:
        print('Apenas insira números!\n')
        menu()
    try:
        senhacli = str(input('Qual é a senha da sua conta?\n'))
    except:
        print('Apenas insira números!\n')
        menu()
    # CONFERINDO O NÚMERO DA CONTA E A SENHA E SE TUDO ESTIVER CORRETO REALIZAR O DEPOSITO!
    for nomeCliente in dicionario:
        if dicionario[nomeCliente]['numeroConta'] == conta:
            if dicionario[nomeCliente]["senha"] == senhacli:
                print("------------------------------------------------------------------")
                print('Conta encontrada! Cadastrada no nome de {}.'.format(nomeCliente))
                depo = float(input("Digite o valor que deseja-se depositar: "))
                print("------------------------------------------------------------------")
                print("Digite 1 para confirmar ou 2 para cancelar/sair")
                confir = int(input("Digite a opção desejada: "))
                saldoatual = dicionario[nomeCliente]['saldo']
                if confir == 1:
                    if depo > 0 and depo <= 10000:
                        saldoatual += depo

                        # ALTERANDO O SALDO ANTIGO PARA O NOVO SALDO COM O DEPÓSITO REALIZADO
                        saldo = saldoatual
                        dicionario[nomeCliente]['saldo'] = saldo
                        arquivo = open('teste.txt', 'w')
                        arquivo.write(str(dicionario))
                        arquivo.close()
                        print("------------------------------------------------------------------")
                        print(f"O valor depositado foi de: {depo}")
                        print("O valor atual da conta é de: ", saldoatual)
                        break
                    else:  # DIGITOU UMA VALOR QUE NÃO PODE
                        print("Este valor não pode ser depositado!\n")
                        break

                elif confir == 2:  # VOLTAR AO MENU PRINCIPAL
                    break
                else:  # DIGITOU UM NÚMERO INVALÍDO PARA CONFIRMAR SE QUER CONTINUAR OU NÃO
                    print("Você digitou um número inválido! Tente novamente mais tarde!")
                    break

            else:  # SENHA INCORRETA DA CONTA!
                print("Senha Incorreta! Tente novamente mais tarde!")
                break
        elif nomeCliente == list(dicionario.keys())[-1]:  # CONTA NÃO EXISTENTE NO SISTEMA
            print("\nConta não encontrada! Tente novamente!")
            break


# SALDO ------------------------------------------------------------------------------------------------------
def saldo_cliente():
    # ABRINDO O ARQUIVO PARA CONFIRMAR AS INFORMAÇÕES DO CLIENTE
    arquivo = open('teste.txt', 'r')
    conteudo = arquivo.read()
    dicionario = literal_eval(conteudo)
    arquivo.close()
    # VERIFICANDO SE O QUE FOI DIGITADO ESTÁ DE ACORDO COM O SISTEMA
    try:
        print("------------------------------------------------------------------")
        conta = int(input('Qual o número da sua conta?\n'))
    except:
        print('Apenas insira números!\n')
        menu()
    try:
        senhacli = str(input('Qual é a senha da sua conta?\n'))
    except:
        print('Apenas insira números!\n')
        menu()
    # CONFERINDO O NÚMERO DA CONTA E A SENHA E SE TUDO ESTIVER CORRETO PODERÁ VISUALIZAR O SALDO!
    for nomeCliente in dicionario:
        if dicionario[nomeCliente]['numeroConta'] == conta:
            if dicionario[nomeCliente]["senha"] == senhacli:

                # VISUALIZANDO O SALDO DA CONTA
                print('Conta encontrada! Cadastrada no nome de {}.'.format(nomeCliente))
                saldoatual = dicionario[nomeCliente]['saldo']
                print(f"O número de sua conta é: {conta}.")
                print(f"O seu saldo atual é de: {saldoatual}\n")
                break
            else:  # SENHA INCORRETA DA CONTA!
                print("Senha Incorreta! Tente novamente mais tarde!")
                break
        elif nomeCliente == list(dicionario.keys())[-1]:  # CONTA NÃO EXISTENTE NO SISTEMA
            print("\nConta não encontrada! Tente novamente!")
            break


# INVESTIMENTO -----------------------------------------------------------------------------------------------
def investimento():
    # ABRINDO O ARQUIVO PARA CONFIRMAR AS INFORMAÇÕES DO CLIENTE
    arquivo = open('teste.txt', 'r')
    conteudo = arquivo.read()
    dicionario = literal_eval(conteudo)
    arquivo.close()
    # VERIFICANDO SE O QUE FOI DIGITADO ESTÁ DE ACORDO COM O SITEMA
    try:
        print("------------------------------------------------------------------")
        conta = int(input('Qual o número da sua conta?\n'))
    except:
        print('Apenas insira números!\n')
        menu()
    try:
        senhacli = str(input('Qual é a senha da sua conta?\n'))
    except:
        print('Apenas insira números!\n')
        menu()
    # CONFERINDO O NÚMERO DA CONTA E A SENHA E SE TUDO ESTIVER CORRETO REALIZAR A SIMULAÇÃO DE INVESTIMENTO!
    for nomeCliente in dicionario:
        if dicionario[nomeCliente]['numeroConta'] == conta:
            if dicionario[nomeCliente]["senha"] == senhacli:
                print('Conta encontrada! Cadastrada no nome de {}.'.format(nomeCliente))
                num_meses = int(input("Digite, de forma numérica, a quantidade de meses de investimento: "))
                aporte = float(input("Digite, de forma numérica, o aporte inicial do investimento: "))
                M = aporte * ((1 + 0.015) ** num_meses)  # JUROS COMPOSTO DO BANCO
                print(f"Valor inicial do rendimento do investimento: {M:.2f}")  # O VALOR FINAL SEM A TAXA DO BANCO!
                if num_meses < 60:  # TAXA DO BANCO PARA MENOS DE 5 ANOS
                    D = 1
                    for i in range(0, num_meses, 12):
                        D *= 0.99
                        F1 = M * D
                    print(f"O valor do final do investimento com a taxa do banco: {F1:.2f}")
                elif num_meses >= 60:  # TAXA DO BANCO PARA MAIS DE 5 ANOS DE INVESTIMENTO
                    D2 = 1
                    for i in range(0, num_meses, 12):  # TAXA DO BANCO DE 0.05% NO INVESTIMENTO!
                        D2 *= 0.995
                        F2 = M * D2
                    print(f"O valor final do investimento (5 ou mais anos) com a taxa do banco: {F2:.2f}\n")
                break

            else:  # SENHA INCORRETA!
                print("Senha Incorreta! Tente novamente mais tarde!")
                break
        elif nomeCliente == list(dicionario.keys())[-1]:  # CONTA NÃO EXISTENTE NO SISTEMA
            print("\nConta não encontrada! Tente novamente!")
            break


# INTERFACE CLIENTE (ESCOLHAS)
def menu():
    while True:

        # MENU PRINCIPAL DO CLIENTE

        print("------------------------------------------------------------------")
        print('Bem vindo ao Banco do Brasólia!\n')
        print('1 - SAQUE.\n'
              '2 - DEPÓSITO.\n'
              '3 - VISUALIZAÇÃO DE SALDO.\n'
              '4 - SIMULAÇÃO DE INVESTIMENTO.\n'
              '5 - SAIR.\n')
        # VERIFICANDO SE O QUE FOI DIGITADO ESTÁ DE ACORDO COM O SISTEMA
        try:
            escolhaMenuPrincipal2 = int(input("Digite o número desejado: "))
        except:
            print("Você digitou algo que não podia, tente novamente!")
            menu()
            break

        # DIGITOU OUTROS NÚMEROS DA OPÇÕES
        if escolhaMenuPrincipal2 < 1 or escolhaMenuPrincipal2 > 5:
            print("(Você digitou um número inválido, tente novamente!)")
            menu()  # VOLTAR AO MENU PRINCIPAL

        # ENTRAR NA OPÇÃO 1
        if escolhaMenuPrincipal2 == 1:
            saque()
        # ENTRAR NA OPÇÃO 2
        if escolhaMenuPrincipal2 == 2:
            deposito()
        # ENTRAR NA OPÇÃO 3
        if escolhaMenuPrincipal2 == 3:
            saldo_cliente()
        # ENTRAR NA OPÇÃO 4
        if escolhaMenuPrincipal2 == 4:
            investimento()
        # ENTRAR NA OPÇÃO 5
        if escolhaMenuPrincipal2 == 5:
            break


menu()