import random
from datetime import datetime, timedelta
import calendar

funcionarios = ["AGNALIA", "ANDREIA", "ANGELA", "BEATRIZ", "DENNER", "EINER", "ELEN", "FELIPE SILVA", "EMMANUEL",
               "LUAN", "RODRIGO", "SAVIO", "BRENDOW", "JESSIKA", "DEBORA", "GABRIELLA", "ISACC", "LARA", "STEPHANIE",
               ]

# Solicite ao usuário que escolha o mês e o ano desejados
mes_escolhido = int(input("Digite o número do mês desejado (1 a 12): "))
ano_escolhido = int(input("Digite o ano desejado: "))
print("\n")

# Verifique se o mês escolhido é válido
if mes_escolhido < 1 or mes_escolhido > 12:
    print("Mês inválido. Por favor, escolha um número de mês entre 1 e 12.")
elif ano_escolhido <= 0:
    print("Ano inválido. O ano deve ser maior que zero.")
else:
    # Obtenha o número de dias no mês escolhido
    num_dias_no_mes = calendar.monthrange(ano_escolhido, mes_escolhido)[1]

    # Nomes dos dias da semana em português
    nomes_dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

    # Use random.sample se houver funcionários suficientes
    if len(funcionarios) >= num_dias_no_mes:
        semana = random.sample(funcionarios, num_dias_no_mes)
    else:
        # Use random.choices se houver menos funcionários do que dias no mês
        semana = random.choices(funcionarios, k=num_dias_no_mes)

    # Dicionário para armazenar o mapeamento de datas e funcionários
    historico_funcionarios = {}  

    # Lista para armazenar a programação do mês
    programacao_mes = []

    for dia_mes in range(1, num_dias_no_mes + 1):
        funcionario = None

        # Garante que o funcionário escolhido não se repita antes de 15 dias
        while True:
            funcionario = random.choice(funcionarios)
            ultima_data_escolha = historico_funcionarios.get(funcionario)
            if ultima_data_escolha is None or (datetime(ano_escolhido, mes_escolhido, dia_mes) - ultima_data_escolha).days >= 15:
                break

        historico_funcionarios[funcionario] = datetime(ano_escolhido, mes_escolhido, dia_mes)

        data = datetime(ano_escolhido, mes_escolhido, dia_mes)
        dia_semana = nomes_dias_semana[data.weekday()]  # Obtém o nome do dia da semana em português
        data_formatada = data.strftime("%d/%m")
        
        programacao_mes.append({'dia': dia_semana, 'data': data_formatada, 'funcionario': funcionario})

    # Imprima a programação do mês
    cont = 0
    for item in programacao_mes:
        print(f"{item['dia']} ({item['data']}): {item['funcionario']}")
        cont+=1
        if cont == 7:    
            print("\n")
            cont = 0
