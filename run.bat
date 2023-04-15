@echo off

if exist requirements.txt (
    echo Instalando requisitos desde requirements.txt
    pip install -r requirements.txt > nul 2>&1
) else (
    echo El archivo requirements.txt no existe
    exit /b 1
)

echo Haciendo ping al servidor para comprobar que estan disponibles los servicios de Redi y RabbitMQ
ping -n 1 162.246.254.134 > nul
if errorlevel 1 (
    echo El servidor no se encuentra disponible
    exit /b 1
) else (
    echo Abriendo RabbitMQ Management en el navegador...
    echo    Usuario: guest
    echo    Password: guest
    start cmd /k "python pollution_sensor.py"
    start cmd /k "python meteo_sensor.py"
    timeout /t 2
    start cmd /k "python meteo_server.py"
    start cmd /k "python meteo_server.py"
    start cmd /k "python meteo_server.py"
    timeout /t 3
    start cmd /k "python proxy.py"
    timeout /t 1
    start cmd /k "python terminal.py"
    start cmd /k "python terminal.py"
)
