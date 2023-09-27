import random
from datetime import datetime, timedelta
import calendar
import tkinter as tk
from tkinter import ttk

# Base de dados para dias de folga dos funcionários (adapte conforme necessário)
folgas_funcionarios = {
    "AGNALIA": ["2023-09-28", "2023-09-30"],
    "ANDREIA": ["2023-09-25"],
    # Adicione os outros funcionários e suas datas de folga aqui
}

# Defina a lista de funcionários no escopo global
funcionarios = ["AGNALIA", "ANDREIA", "ANGELA", "BEATRIZ", "DENNER", "EINER", "ELEN", "FELIPE SILVA", "EMMANUEL",
               "LUAN", "RODRIGO", "SAVIO", "BRENDOW", "JESSIKA", "DEBORA", "GABRIELLA", "ISACC", "LARA", "STEPHANIE"]

def esta_de_folga(funcionario, data):
    if funcionario in folgas_funcionarios:
        return data.strftime("%Y-%m-%d") in folgas_funcionarios[funcionario]
    return False

def obter_nome_dia_semana(data):
    nomes_dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    return nomes_dias_semana[data.weekday()]

def obter_ultimo_dia_mes(ano, mes):
    return calendar.monthrange(ano, mes)[1]

def escolher_funcionario(funcionarios, historico_funcionarios, ano, mes, dia_mes):
    while True:
        funcionario = random.choice(funcionarios)
        ultima_data_escolha = historico_funcionarios.get(funcionario)
        data = datetime(ano, mes, dia_mes)
        
        # Verificar se o funcionário está de folga no dia
        if esta_de_folga(funcionario, data):
            continue

        # Informar com quantos dias mínimos o nome do funcionário deve aparecer de novo na lista
        if ultima_data_escolha is None or (data - ultima_data_escolha).days >= 15:
            return funcionario

def imprimir_programacao(programacao_mes):
    programacao_texto = ""
    for item in programacao_mes:
        programacao_texto += f"{item['dia']} ({item['data']}): {item['funcionario']}\n"
        if item['dia'] == 'Sábado':
            print('\n')
    return programacao_texto

def gerar_programacao():
    mes_escolhido = int(combo_mes.get())
    ano_escolhido = int(entrada_ano.get())

    if mes_escolhido < 1 or mes_escolhido > 12:
        resultado_texto.set("Mês inválido. Por favor, escolha um número de mês entre 1 e 12.")
    elif ano_escolhido <= 0:
        resultado_texto.set("Ano inválido. O ano deve ser maior que zero.")
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

        resultado = imprimir_programacao(programacao_mes)
        resultado_texto.set(resultado)

# Configuração da interface gráfica usando Tkinter
root = tk.Tk()
root.title("Programação de Escala")
root.geometry("500x500")

frame = ttk.Frame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

ttk.Label(frame, text="Escolha o mês (1 a 12):").grid(row=0, column=0, padx=10, pady=5)
combo_mes = ttk.Combobox(frame, values=list(range(1, 13)))
combo_mes.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame, text="Digite o ano:").grid(row=1, column=0, padx=10, pady=5)
entrada_ano = ttk.Entry(frame)
entrada_ano.grid(row=1, column=1, padx=10, pady=5)

gerar_botao = ttk.Button(frame, text="Gerar Programação", command=gerar_programacao)
gerar_botao.grid(row=2, columnspan=2, padx=10, pady=10)

resultado_texto = tk.StringVar()
resultado_label = ttk.Label(frame, textvariable=resultado_texto, wraplength=350)
resultado_label.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
