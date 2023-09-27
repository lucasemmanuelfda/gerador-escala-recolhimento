import random
from datetime import datetime, timedelta
import calendar

def obter_nome_dia_semana(data):
    nomes_dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    return nomes_dias_semana[data.weekday()]

def obter_ultimo_dia_mes(ano, mes):
    return calendar.monthrange(ano, mes)[1]

def escolher_funcionario(funcionarios, historico_funcionarios, ano, mes, dia_mes):
    while True:
        funcionario = random.choice(funcionarios)
        ultima_data_escolha = historico_funcionarios.get(funcionario)
        # Informar com quantos dias minimos o nome do funcionario deve aparece de novo na lista
        if ultima_data_escolha is None or (datetime(ano, mes, dia_mes) - ultima_data_escolha).days >= 15:
            return funcionario

def imprimir_programacao(programacao_mes):
    cont = 0
    for item in programacao_mes:
        print(f"{item['dia']} ({item['data']}): {item['funcionario']}")
        cont += 1
        if cont == 7:
            print("\n")
            cont = 0

def main():
    funcionarios = ["AGNALIA", "ANDREIA", "ANGELA", "BEATRIZ", "DENNER", "EINER", "ELEN", "FELIPE SILVA", "EMMANUEL",
                   "LUAN", "RODRIGO", "SAVIO", "BRENDOW", "JESSIKA", "DEBORA", "GABRIELLA", "ISACC", "LARA", "STEPHANIE"]

    mes_escolhido = int(input("Digite o número do mês desejado (1 a 12): "))
    ano_escolhido = int(input("Digite o ano desejado: "))
    print("\n")

    if mes_escolhido < 1 or mes_escolhido > 12:
        print("Mês inválido. Por favor, escolha um número de mês entre 1 e 12.")
    elif ano_escolhido <= 0:
        print("Ano inválido. O ano deve ser maior que zero.")
    else:
        num_dias_no_mes = obter_ultimo_dia_mes(ano_escolhido, mes_escolhido)

        historico_funcionarios = {}
        programacao_mes = []

        for dia_mes in range(1, num_dias_no_mes + 1):
            funcionario = escolher_funcionario(funcionarios, historico_funcionarios, ano_escolhido, mes_escolhido, dia_mes)

            historico_funcionarios[funcionario] = datetime(ano_escolhido, mes_escolhido, dia_mes)
            data = datetime(ano_escolhido, mes_escolhido, dia_mes)
            dia_semana = obter_nome_dia_semana(data)
            data_formatada = data.strftime("%d/%m")

            programacao_mes.append({'dia': dia_semana, 'data': data_formatada, 'funcionario': funcionario})

        imprimir_programacao(programacao_mes)

if __name__ == "__main__":
    main()
