import random
from datetime import datetime, timedelta
import calendar
from tinydb import TinyDB, Query

# Crie ou abra o banco de dados
db = TinyDB('funcionarios_db.json')

funcionarios = ["AGNALIA", "ANDREIA", "ANGELA", "BEATRIZ", "DENNER", "EINER", "ELEN", "FELIPE SILVA", "EMMANUEL",
               "LUAN", "RODRIGO", "SAVIO", "BRENDOW", "JESSIKA", "DEBORA", "GABRIELLA", "ISACC", "LARA", "STEPHANIE",
               "SUELLEN", "VERICIO", "RAFAELA", "MARCIO", "ALDENISY"]

# Solicite ao usuário que escolha o mês e o ano desejados
mes_escolhido = int(input("Digite o número do mês desejado (1 a 12): "))
ano_escolhido = int(input("Digite o ano desejado: "))

# Verifique se o mês escolhido é válido
if mes_escolhido < 1 or mes_escolhido > 12:
    print("Mês inválido. Por favor, escolha um número de mês entre 1 e 12.")
elif ano_escolhido <= 0:
    print("Ano inválido. O ano deve ser maior que zero.")
else:
    # Obtenha o número de dias no mês escolhido
    num_dias_no_mes = calendar.monthrange(ano_escolhido, mes_escolhido)[1]

    # Use random.sample se houver funcionários suficientes
    if len(funcionarios) >= num_dias_no_mes:
        semana = random.sample(funcionarios, num_dias_no_mes)
    else:
        # Use random.choices se houver menos funcionários do que dias no mês
        semana = random.choices(funcionarios, k=num_dias_no_mes)

    # Armazene o mapeamento no TinyDB com as datas e os dias da semana correspondentes
    historico_funcionarios = {}  # Armazena as datas em que cada funcionário foi escolhido
    for dia_mes in range(1, num_dias_no_mes + 1):
        funcionario = None

        # Garante que o funcionário escolhido não se repita antes de 7 dias
        while True:
            funcionario = random.choice(funcionarios)
            ultima_data_escolha = historico_funcionarios.get(funcionario)
            if ultima_data_escolha is None or (datetime(ano_escolhido, mes_escolhido, dia_mes) - ultima_data_escolha).days >= 7:
                break

        historico_funcionarios[funcionario] = datetime(ano_escolhido, mes_escolhido, dia_mes)

        data = datetime(ano_escolhido, mes_escolhido, dia_mes)
        dia_semana = data.strftime("%A")  # %A para obter o dia da semana em português
        data_formatada = data.strftime("%d/%m")
        db.insert({'dia': dia_semana, 'data': data_formatada, 'funcionario': funcionario})

    # Recupere e imprima o mapeamento
    for item in db.all():
        print(f"{item['dia']} ({item['data']}): {item['funcionario']}")
