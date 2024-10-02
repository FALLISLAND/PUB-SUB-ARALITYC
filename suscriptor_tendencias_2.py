import pika
import json

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('aralityc', 'aralityc')  # Reemplaza con tus credenciales correctas

# Conexión a RabbitMQ con credenciales
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

# Declarar el exchange (debe ser igual al que se usa en el publicador)
channel.exchange_declare(exchange='pos_data', exchange_type='fanout')

# Crear una cola exclusiva para el suscriptor
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Vincular la cola al exchange
channel.queue_bind(exchange='pos_data', queue=queue_name)

print(' [*] Esperando datos de ventas para análisis de tendencias...')

# Procesar los datos de ventas y detectar tendencias
ventas_por_producto = {}

def analizar_tendencias():
    print(f"Tendencias de ventas actuales: {ventas_por_producto}")

# Función de callback para procesar los mensajes recibidos
def callback(ch, method, properties, body):
    datos = json.loads(body)
    producto = datos['producto_id']
    
    # Actualizar las ventas por producto
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += datos['cantidad']
    else:
        ventas_por_producto[producto] = datos['cantidad']
    
    print(f" [x] Recibido {datos}, analizando tendencias...")
    analizar_tendencias()

# Iniciar el consumo de mensajes de la cola
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Comenzar a consumir mensajes
channel.start_consuming()
