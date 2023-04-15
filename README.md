# 1st assignment Distributed Systems
1st assignment ot the subject SD (Distributed Systems) of the degree in Computer Science of the Rovira i Virgili
University. Consists of the implementation of a distributed system using `Python`.

## Content
* [Introduction](#introduction)
    * [Direct communication](#direct)
    * [Indirect communication](#indirect)
    * [Running steps](#run)
      * [Linux](#linux)
      * [Windows](#windows)
* [Authors](#authors)

## Introduction
To implement this system, we've decided to make use of a remote server to simulate a real case where, RabbitMQ and Redis
would be running in a remote server. To do so, we're using two docker containers, one for each, hosted at:
* Redis: 162.246.254.134:8001 (Requires no password)
* RabbitMQ: http://162.246.254.134:15672/
  * User: guest
  * Password: guest

Both containers are always running in detach mode, and containers aren't removed when stopped.<br>
Data in RabbitMQ is set to be kept even if there's a node failure to make sure that any message gets lost.
We've decided to make this implementation to have access to the same data and make a more realistic system.<br>
When it comes to the RPC implementation, we first started using XMLRPC, but ended implementing GRPC due to its safety and speed.
### Direct
* Sensors
* Load balancer
* Server
* Redis storage
* Proxy
* Terminal
### Indirect
* Sensors
* RabbitMQ ( sensor - server communication )
* Server
* Redis storage
* Proxy
* RabbitMQ ( proxy - terminal communication )
* Terminal
### Run

#### Linux
1. 
```bash
pip install -r requirements.txt
```
2.
````bash
./run.sh
````
#### Windows
1. 
```bash
pip install -r requirements.txt
```
2.
````bash
./run.bat
````

## Authors
* Carlos Martínez - [carlosmgv02](https://github.com/carlosmgv02)
* Nil Monfort - [nilm9](https://github.com/nilm9)
