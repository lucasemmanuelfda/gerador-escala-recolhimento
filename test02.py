import random

funcionarios = ["AGNALIA", "ANDREIA", "ANGELA", "BEATRIZ", "DENNER", "EINER", "ELEN", "FELIPE SILVA", "EMMANUEL",
               "LUAN", "RODRIGO", "SAVIO", "BRENDOW", "JESSIKA", "DEBORA", "GABRIELLA", "ISACC", "LARA", "STEPHANIE",
               "SUELLEN", "VERICIO", "RAFAELA", "MARCIO", "ALDENISY"]

diasdasemana = ["SEG", 'TER', 'QUA', 'QUI', 'SEX', 'SAB', 'DOM']

# Use random.sample para evitar duplicatas e tornar o código mais eficiente
semana = random.sample(funcionarios, len(diasdasemana))

for dia, funcionario in zip(diasdasemana, semana):
    print(f"{dia}: {funcionario}")
