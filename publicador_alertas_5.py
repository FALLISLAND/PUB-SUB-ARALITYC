import pika
import json

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('aralityc', 'aralityc')  # Reemplaza con tus credenciales correctas

# Conexión a RabbitMQ con credenciales
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

# Declarar un exchange de tipo 'fanout' para las alertas
channel.exchange_declare(exchange='alertas_anomalias', exchange_type='fanout')

# Simulación de alerta de anomalía (caída en ventas)
alerta_anomalia = {
    'producto_id': 'Producto A',
    'tipo_anomalia': 'Caída en ventas',
    'descripcion': 'Las ventas han caído un 50% en las últimas 24 horas'
}

# Publicar la alerta
channel.basic_publish(exchange='alertas_anomalias', routing_key='', body=json.dumps(alerta_anomalia))
print(f" [x] Alerta enviada: {alerta_anomalia}")

# Cerrar la conexión
connection.close()
