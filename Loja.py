#Apresentação da loja
def menu_loja():
    print("Meu nome é Jean Mansano")
    print("Seja muito bem vindo a loja com os melhores preços da cidade !")
    print("\n")
    print("Para começar, preciso fazer uma análise de crédito sua.")
    cliente = int(input("Precisamos de algumas informações"))
    cargo = int(input("Informe seu cargo na empresa em que trabalha atualmente: "))
    salario = int(input("Informe seu salario: "))
    ano_nascimento = int(input("Informe seu ano de nascimento com 4 digitos: "))

    if ano_nascimento > 4 and ano_nascimento < 4:
        print("Número inválido")
        return menu_loja()
    else:
        print("Vamos calcular seu limite de crédito")


    print("\n")

#Apresentação de dados ao usuário

    print("Seu cargo é: ", cargo)
    print("Seu salario é de: R$", salario)
    print("Seu ano de nascimento é: ", ano_nascimento)

    from _datetime import datetime
    data_atual = datetime.now()
    ano_atual = (data_atual.year)

#Calcula a idade do usuário

    idade = ano_atual - ano_nascimento
    print("Sua idade aproximada é: ", idade,"anos")

#Calcula o limite de credito que o usuário terá na loja

    limite_credito = (salario * (idade / 1000)) + 100
    print("Análise de crédito concluida !")
    print("Voce tem o limite de credito liberado no valor de R$", limite_credito, "para gastos em nossa loja")
    return cliente

menu_loja()
