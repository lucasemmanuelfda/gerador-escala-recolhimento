import random
from tinydb import TinyDB, Query

# Crie ou abra o banco de dados
db = TinyDB('funcionarios_db.json')

funcionarios = ["AGNALIA", "ANDREIA", "ANGELA", "BEATRIZ", "DENNER", "EINER", "ELEN", "FELIPE SILVA", "EMMANUEL",
               "LUAN", "RODRIGO", "SAVIO", "BRENDOW", "JESSIKA", "DEBORA", "GABRIELLA", "ISACC", "LARA", "STEPHANIE",
               "SUELLEN", "VERICIO", "RAFAELA", "MARCIO", "ALDENISY"]

diasdasemana = ["SEG", 'TER', 'QUA', 'QUI', 'SEX', 'SAB', 'DOM']

# Use random.sample para evitar duplicatas e tornar o código mais eficiente
semana = random.sample(funcionarios, len(diasdasemana))

# Armazene o mapeamento no TinyDB
for dia, funcionario in zip(diasdasemana, semana):
    db.insert({'dia': dia, 'funcionario': funcionario})

# Recupere e imprima o mapeamento
for item in db.all():
    print(f"{item['dia']}: {item['funcionario']}")
