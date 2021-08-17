@ECHO OFF
TITLE EdraBot
ECHO Bem vindo ao EdraBot, qual seu tipo de simulacao?


:start
set choice=
set /p choice= 'm' para simulacao de curvas de motores, 'b' para baterias.
ECHO.
if '%choice%'=='m' goto motores
if '%choice%'=='b' goto baterias
ECHO Comando nao valido, tente novamente.
ECHO.
goto start


:motores
ECHO =====================Iniciando Simulacao de curvas de motores =====================
python EdraBot.py
start octave.bat Edraplot.m
goto end

:baterias
ECHO =====================Iniciando Simulacao de curvas de baterias=====================
python EdraBot.py
start octave.bat EdraplotB.m
goto end

:end
PAUSE
exit