import subprocess as sub


print("====================Bem-Vindo ao EdraBot====================\n")

print("Escolha um tipo de simulação: Simulação de Baterias (B) ou Simulação de Motores (M) ?\n")

r =  str( input() )

print("\n")

if (r == "B" or r == "b"):
    print("=====================Iniciando Simulação com Curvas de Motores =====================\n")
    sub.run("python EdraBot.py",shell = True)
    sub.run("start octave.bat EdraplotB.m",shell = True)
elif(r == "M" or r == "m"):
    print("=====================Iniciando Simulacao com Curvas de Baterias=====================\n")
    sub.run("python EdraBot.py",shell = True)
    sub.run("start octave.bat EdraplotB.m",shell = True)
else:
    print("Erro: Resposta Inesperada\n")
    exit()