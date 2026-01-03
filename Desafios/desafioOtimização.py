menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuario
[c] Criar Conta
[q] Sair

=> """
valor = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = "0001"


def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): 

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(nome, data_nasc, cpf, endereco):
    cpf_limpo = cpf.replace(".", "").replace("-", "")

    for usuario in usuarios:
        if usuario["cpf"] == cpf_limpo:
            print("Erro: este usuário já existe")
            return

    novo_usuario = {
        "nome": nome,
        "data_nasc": data_nasc,
        "cpf": cpf_limpo,
        "endereco": endereco
    }
    
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

def criar_conta(cpf):
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf_limpo:
            usuario_encontrado = usuario
            break
    
    if not usuario_encontrado:
        print("\nErro: Usuário não encontrado! Cadastre o usuário antes de criar uma conta.")
        return

    numero_conta = len(contas) + 1
    
    nova_conta = {
        "agencia": AGENCIA,
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    }
    
    contas.append(nova_conta)
    print(f"\nConta {numero_conta} criada com sucesso")

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

    elif opcao == "e":
        exibir_extrato(saldo, extrato = extrato)

    elif opcao == "u":
        nome = input("Informe o nome completo: ")
        data_nasc = input("Informe a data de nascimento (ex: 21/01/2000): ")
        cpf = input("Informe o CPF: ")
        endereco = input("Informe o endereço completo (Rua, Número, Bairro, Cidade/UF): ")
        criar_usuario(nome, data_nasc, cpf, endereco)

    elif opcao == "c":
        cpf = input("Informe o CPF do titular: ")
        criar_conta(cpf)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")