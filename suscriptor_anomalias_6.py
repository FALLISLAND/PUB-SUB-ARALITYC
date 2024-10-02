import pika
import json

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('aralityc', 'aralityc')  # Reemplaza con tus credenciales correctas

# Conexión a RabbitMQ con credenciales
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

# Declarar el exchange de alertas
channel.exchange_declare(exchange='alertas_anomalias', exchange_type='fanout')

# Crear una cola exclusiva para el suscriptor
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Vincular la cola al exchange
channel.queue_bind(exchange='alertas_anomalias', queue=queue_name)

print(' [*] Esperando alertas de anomalías...')

# Función de callback para procesar las alertas recibidas
def callback(ch, method, properties, body):
    alerta = json.loads(body)
    print(f" [x] Alerta recibida: {alerta['tipo_anomalia']} para {alerta['producto_id']}: {alerta['descripcion']}")

# Iniciar el consumo de mensajes de la cola
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Comenzar a consumir alertas
channel.start_consuming()
