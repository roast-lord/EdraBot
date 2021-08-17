@ECHO OFF
TITLE Instalador de pacotes EdraBot
ECHO Instalando Pacotes... Por favor aguarde...

pip install selenium
pip install numpy
start octave.bat install.m

pause
exit