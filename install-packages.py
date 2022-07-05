import subprocess as sub
from sys import platform

print("==============Instalando Pacotes Python==============\n")
sub.run("pip install -r requirements.txt", shell=True)

print("==============Instalando Pacotes Octave==============\n")

if platform == "linux":
    sub.run(
        "sudo apt install -y unzip xvfb libxi6 libgconf-2-4 && sudo apt install default-jdk -y && sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && sudo bash -c "
        + "echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list && sudo apt -y update && sudo apt -y install google-chrome-stable",
        shell=True,
    )
    sub.run("sudo apt install liboctave-dev -y", shell=True)
    sub.run("octave install.m", shell=True)
else:
    sub.run("start octave.bat install.m", shell=True)
