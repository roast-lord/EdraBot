import subprocess as sub

print("==============Instalando Pacotes Python==============\n")
sub.run("pip install -r requirements.txt",shell= True)

print("==============Instalando Pacotes Octave==============\n")
sub.run("start octave.bat install.m",shell=True)
