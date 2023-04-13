@echo off

if exist requirements.txt (
    echo Instalando requisitos desde requirements.txt
    pip install -r requirements.txt > nul 2>&1
) else (
    echo El archivo requirements.txt no existe
    exit /b 1
)

ping -n 1 162.246.254.134 > nul
if errorlevel 1 (
    echo El servidor no se encuentra disponible
    exit /b 1
) else (
    echo Abriendo RabbitMQ Management en el navegador...
    echo    Usuario: guest
    echo    Password: guest
    start http://162.246.254.134:15672/
    start cmd /k "python LBServicer.py"
    timeout /t 2
    start cmd /k "python meteo_server.py 5002"
    start cmd /k "python meteo_server.py 5003"
    start cmd /k "python meteo_server.py 5004"
    timeout /t 2
    start cmd /k "python terminalServicer.py"
    timeout /t 2
    start cmd /k "python sensor.py"
    timeout /t 1
    start cmd /k "python proxy.py"
)
