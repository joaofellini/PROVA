#MENU

while True:
    menu = int(input("Bem vindo ao menu de controle de suas finanças."
                     "\n0 - Sair;"
                     "\n1 - Informar Salário;"
                     "\n2 - Alterar Salário;"
                     "\n3 - Excluir Salário;"
                     "\n4 - Listar Salários;"
                     "\n5 - Informar Despesa;"
                     "\n6 - Alterar Despesa;"
                     "\n7 - Remover Despesa;"
                     "\n8 - Listar Despesas;"
                     "\n9 - Acompanhamento;"
                     "\nSelecione a sua opção : "))
    if menu == 0:
        break

# 1 - Informar rendimento
    elif menu == 1:
        def obter_numero(mensagem):
            while True:
                try:
                    numero = float(input(mensagem))
                    return numero
                except ValueError:
                    print("Valor inválido, por favor insira um número.")

        mes = input("Informe o mês: ")
        salario = obter_numero("Informe o salário mensal: ")

        with open("rendimento_mensal.txt", "a") as arquivo:
            arquivo.write(f"{mes};{salario:.2f}\n")

        print("Informações de rendimento salvas!")

# 2 - Alterar Salário
    elif menu == 2:
        mes = input("Informe o mês do salário que deseja alterar: ")

        with open("rendimento_mensal.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for i, linha in enumerate(linhas):
            if linha.startswith(mes):
                valor_atual = float(linha.split(";")[1])

                novo_valor = obter_numero(f"Informe o novo valor do salário de {mes}: ")

                linhas[i] = f"{mes};{novo_valor:.2f}\n"

                with open("rendimento_mensal.txt", "w") as arquivo:
                    arquivo.writelines(linhas)

                print(f"Salário de {mes} alterada de R${valor_atual:.2f} para R${novo_valor:.2f} com sucesso!")
                break
        else:
            print("Mês não encontrado.")

# 3 - Remover Salário
    elif menu == 3:
        mes = input("Informe o mês do salario que deseja remover: ")

        with open("rendimento_mensal.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        encontrou = False
        for i, linha in enumerate(linhas):
            if linha.startswith(mes):
                encontrou = True
                del linhas[i]
                print(f"Salario de {mes} removida com sucesso!")
                break

        if not encontrou:
            print("Mês não encontrado.")

        with open("rendimento_mensal.txt", "w") as arquivo:

            arquivo.writelines(linhas)

# 4 - Listar Rendimentos
    elif menu == 4:
        with open("rendimento_mensal.txt", "r") as arquivo:
            salario_por_mes = {}
            for linha in arquivo:
                mes, valor = linha.strip().split(";")
                valor = float(valor)
                if mes in salario_por_mes:
                    salario_por_mes[mes].append(valor)
                else:
                    salario_por_mes[mes] = [valor]
            soma_salarios = 0
            for mes, salario in salario_por_mes.items():
                soma_mes = sum(salario)
                soma_salarios += soma_mes
                print(f"{mes}: R$ {soma_mes:.2f}")
            print(f"Soma total dos salários: R$ {soma_salarios:.2f}")

# 5 - Informar despesas
    elif menu == 5:
        mes = input("Digite o mês desejado (ex: 'jan'): ")
        with open("rendimento_mensal.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                mes_arquivo = dados[0]
                salario_arquivo = float(dados[1])
                if mes_arquivo == mes:
                    while True:
                        def obter_numero(mensagem):
                            while True:
                                try:
                                    numero = float(input(mensagem))
                                    return numero
                                except ValueError:
                                    print("Valor inválido, por favor insira um número.")
                        despesa = obter_numero("Informe a despesa do mês: ")
                        if despesa <= salario_arquivo:
                            break
                        else:
                            print("Valor de despesa maior que o salário, por favor insira um valor menor.")

                    with open("despesas_mensais.txt", "a") as arquivo_despesas:
                        arquivo_despesas.write(f"{mes_arquivo};{despesa:.2f}\n")

                    saldo = salario_arquivo - despesa
                    print(f"Restante do mês {mes_arquivo}: R${saldo:.2f}")
                    break
            else:
                print("Mês não encontrado nas informações de rendimento mensal.")

# 6 - Alterar as despesas
    elif menu == 6:
        mes = input("Informe o mês da despesa que deseja alterar: ")

        with open("despesas_mensais.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for i, linha in enumerate(linhas):
            if linha.startswith(mes):
                valor_atual = float(linha.split(";")[1])

                novo_valor = obter_numero(f"Informe o novo valor da despesa de {mes}: ")

                linhas[i] = f"{mes};{novo_valor:.2f}\n"

                with open("despesas_mensais.txt", "w") as arquivo:
                    arquivo.writelines(linhas)

                print(f"Despesa de {mes} alterada de R${valor_atual:.2f} para R${novo_valor:.2f} com sucesso!")
                break
        else:
            print("Mês não encontrado.")

#7 - Remover despesa
    elif menu == 7:

        mes = input("Informe o mês da despesa que deseja remover: ")

        with open("despesas_mensais.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        encontrou = False
        for i, linha in enumerate(linhas):
            if linha.startswith(mes):
                encontrou = True
                del linhas[i]
                print(f"Despesa de {mes} removida com sucesso!")
                break

        if not encontrou:
            print("Mês não encontrado nas despesas.")

        with open("despesas_mensais.txt", "w") as arquivo:

            arquivo.writelines(linhas)

# 8 - Listar as despesas
    elif menu == 8:
        with open("despesas_mensais.txt", "r") as arquivo:
            despesas_por_mes = {}

            for linha in arquivo:
                mes, valor = linha.strip().split(";")
                valor = float(valor)

                if mes in despesas_por_mes:
                    despesas_por_mes[mes].append(valor)
                else:
                    despesas_por_mes[mes] = [valor]

            soma_total = 0
            for mes, despesas in despesas_por_mes.items():
                soma_mes = sum(despesas)
                soma_total += soma_mes
                print(f"{mes}: R$ {soma_mes:.2f}")

            print(f"Soma total das despesas: R$ {soma_total:.2f}")

# 9 - Extrato
    # 9 - Calcular saldo com juros
    elif menu == 9:
        with open("rendimento_mensal.txt", "r") as arquivo:
            saldo_por_mes = {}
            saldo_acumulado = 0
            for linha in arquivo:
                mes, salario = linha.strip().split(";")
                salario = float(salario)
                despesa = 0
                with open("despesas_mensais.txt", "r") as arquivo_despesas:
                    for linha_despesa in arquivo_despesas:
                        mes_despesa, valor_despesa = linha_despesa.strip().split(";")
                        valor_despesa = float(valor_despesa)
                        if mes_despesa == mes:
                            despesa = valor_despesa
                            break
                saldo_anterior = saldo_acumulado
                saldo_acumulado = (saldo_anterior + salario - despesa) * 1.01
                saldo_por_mes[mes] = saldo_acumulado
            for mes, saldo in saldo_por_mes.items():
                print(f"Extrato mensal acumulado {mes}: R$ {saldo:.2f}")
        with open("rendimento_mensal.txt", "r") as arquivo:
            salario_por_mes = {}
            for linha in arquivo:
                mes, valor = linha.strip().split(";")
                salario_por_mes[mes] = float(valor)

        with open("despesas_mensais.txt", "r") as arquivo:
            despesas_por_mes = {}
            for linha in arquivo:
                mes, valor = linha.strip().split(";")
                despesas_por_mes[mes] = float(valor)

        meses = sorted(set(salario_por_mes.keys()) | set(despesas_por_mes.keys()))

        print("\nAcompanhamento das Finanças\n")

        total_rendimentos = sum(salario_por_mes.values())
        total_despesas = sum(despesas_por_mes.values())

        print(f"Total de Rendimentos: R${total_rendimentos:.2f}")
        print(f"Total de Despesas: R${total_despesas:.2f}")







