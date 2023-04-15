#!/bin/bash

if test -f "requirements.txt"; then
    echo "Instalando requisitos desde requirements.txt"
    pip install -r requirements.txt > /dev/null 2>&1
else
    echo "El archivo requirements.txt no existe"
    exit 1
fi

ping -c 1 162.246.254.134 > /dev/null
if [ $? -eq 0 ]; then
    echo "Abriendo RabbitMQ Management en el navegador..."
    echo "    Usuario: guest"
    echo "    Password: guest"
    xdg-open "http://162.246.254.134:15672/"

    echo "Compilando archivos .proto..."
    python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./gRPC/PROTO/terminal.proto
    python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./gRPC/PROTO/meteo_utils.proto
    python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./gRPC/PROTO/load_balancer.proto

    echo "Iniciando servicios..."
    gnome-terminal --tab -- bash -c "python LBServicer.py; exec bash"
    sleep 2
    gnome-terminal --tab -- bash -c "python meteo_server.py 5002; exec bash"
    gnome-terminal --tab -- bash -c "python meteo_server.py 5003; exec bash"
    gnome-terminal --tab -- bash -c "python meteo_server.py 5004; exec bash"
    sleep 2
    gnome-terminal --tab -- bash -c "python terminalServicer.py; exec bash"
    sleep 2
    gnome-terminal --tab -- bash -c "python pollution_sensor.py; exec bash"
    gnome-terminal --tab -- bash -c "python meteo_sensor.py; exec bash"
    sleep 1
    gnome-terminal --tab -- bash -c "python proxy.py; exec bash"
else
    echo "El servidor no se encuentra disponible"
    exit 1
fi
