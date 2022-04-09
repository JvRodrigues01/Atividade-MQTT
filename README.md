João Vitor Carrijo - RA 591009
Emily Stephanie - RA 557137

COMO USAR:

1- Instalar o paho (biblioteca de conexão mqtt):

Abrir o terminal e digitar: pip3 install paho-mqtt
Abrir o terminal e digitar: pip3 install flask
Abrir o terminal e digitar: pip3 install flask_cors
Abrir o terminal e digitar: pip3 install flask_socketio

2- Rodar o mqtt:

Abrir o terminal e digitar: python mqtt.py

3- Rodar a api:

Abrir o terminal e digitar: python api.py

4- Rodar o mosquitto:

No terminal entrar na pasta C:\Program Files\mosquitto

Digitar o comando: mosquitto_pub.exe -h mqtt.eclipseprojects.io -p 1883 -m "SUA MENSAGEM" -t "MQTT"

5- Para visualizar o Historico de mensagens:

No Postman:
Method: GET , Url: http://localhost:8000/

Obrigado :)
