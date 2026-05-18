print("Bem vindo a calculadora de meta!")
historico = []

while True:
    vendas = int(input("Insira o valor de vendas atual: "))
    meta = int(input("Insira o valor da meta de vendas: "))
    dias_restantes = int(input("Insira a quantidade de dias restantes: "))

    if vendas < 0 or meta <= 0 or dias_restantes <= 0:
        print("O valor inserido deve ser maior que zero.")
        continue

    calculo = meta - vendas
    calculo_dias = round(calculo / dias_restantes, 2)
    porcentagem = round((vendas / meta) * 100, 2)

    if porcentagem >= 100:
        print("Você atingiu sua meta com maestria!")
    elif porcentagem > 70:
        print("Você está quase batendo sua meta, não pare agora!")
    elif porcentagem > 30:
        print("Só alcança o objetivo quem não desiste!")
    else:
        print("Você está apenas começando, eu acredito em você!")

    historico.append({
        "Vendas": vendas,
        "Meta": meta,
        "Falta": calculo,
        "Porcentagem": porcentagem,
        "Dias": dias_restantes,
        "Venda_diaria" : calculo_dias,
    })

    if vendas > meta:
        print("O valor de vendas atual é de €" + format(vendas, ',').replace(',','.') + " , você atingiu sua meta de €" + format(meta, ',').replace(',','.') + ". Você atingiu " + str(int(porcentagem)) + "%")
    elif vendas == meta:
        print("O valor de vendas atual é de €" + format(vendas, ',').replace(',','.') + " , você atingiu sua meta de €" + format(calculo, ',').replace(',','.') + ". Você atingiu " + str(int(porcentagem)) + "%")
    else:
        print("O valor de vendas atual é de €" + format(vendas, ',').replace(',','.') + " , para bater a sua meta está faltando €" + format(calculo, ',').replace(',','.') + ". Você atingiu " + str(int(porcentagem)) + "%")

    resposta = input("Quer continuar? [S/N] ")
    if resposta.upper() == "N":
        total = sum(item["Vendas"] for item in historico)
        media = total / len(historico)
        for i, item in enumerate(historico):
            print("--- Cálculo " + str(i + 1) + "---")
            if item["Falta"] > 0:
                print("Falta: €" + format(item["Falta"], ',').replace(',', '.'))
                print("Venda diaria estimada para atingir a meta: €" + format(int(item["Venda_diaria"]), ',').replace(',','.'))
            else:
                print("Meta batida!  🎉")
            print("Vendas: €" + format(item["Vendas"], ',').replace(',','.'))
            print("Meta: €" + format(item["Meta"], ',').replace(',','.'))
            print("Porcentagem atingida: " + str(item["Porcentagem"]) + "%")
            print("Dias restantes: " + str(item["Dias"]))

        print("--- Total de vendas ---")
        print("Total de vendas €" + format(total, ',').replace(',','.'))
        print("--- Média de vendas ---")
        print("A média das vendas é de €" + format(int(media), ',').replace(',','.'))

        with open("historico.txt", "w") as arquivo:
            arquivo.write("Histórico de Vendas\n")
            arquivo.write("-----------------------------\n")
            arquivo.write("O Total de vendas foi de €" + format(int(total), ',').replace(',','.') + "\n")
            arquivo.write("A média das vendas é de €" + format(int(media), ',').replace(',','.') + "\n")
            arquivo.write("-----------------------------\n")
            for i, item in enumerate(historico):
                arquivo.write("--- Cálculo " + str(i + 1) + "---" + "\n")
                if item["Falta"] > 0:
                    arquivo.write("Falta: €" + format(item["Falta"], ',').replace(',', '.') + "\n")
                    arquivo.write("Venda diaria estimada para atingir a meta: €" + format(int(item["Venda_diaria"]), ',').replace(',', '.') + "\n")
                else:
                    arquivo.write("Meta batida!  🎉\n")
                arquivo.write("Vendas: €" + format(item["Vendas"], ',').replace(',', '.') + "\n")
                arquivo.write("Meta: €" + format(item["Meta"], ',').replace(',', '.') + "\n")
                arquivo.write("Porcentagem atingida: " + str(item["Porcentagem"]) + "%\n")
                arquivo.write("Dias restantes: " + str(item["Dias"]) + "\n")
        break


