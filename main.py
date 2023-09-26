import random
funcionarios = ["AGNALIA",
"ANDREIA",
"ANGELA",
"BEATRIZ",
"DENNER",
"EINER",
"ELEN",
"FELIPE SILVA",
"EMMANUEL",
"LUAN",
"RODRIGO",
"SAVIO",
"BRENDOW",
"JESSIKA",
"DEBORA",
"GABRIELLA",
"ISACC",
"LARA",
"STEPHANIE",
"SUELLEN",
"VERICIO",
"RAFAELA",
"MARCIO",
"ALDENISY"]
diasdasemana = ["SEG",'TER','QUA', 'QUI', 'SEX', 'SAB', 'DOM']
cont = 0
semana = []

while True:
    funcionariodia = funcionarios[random.randint(0,23)]
    if funcionariodia in semana:
        funcionariodia = funcionarios[random.randint(0,23)]
    else:
        semana.append(funcionariodia)
        cont+=1
    if cont == 7:
        break
cont = 0    
for dia in diasdasemana:
    print(f"{dia}: {semana[cont]}")
    cont+=1
