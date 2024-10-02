import pika
import json

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('aralityc', 'aralityc')  # Reemplaza con tus credenciales correctas

# Conexión a RabbitMQ con credenciales
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

# Declarar el exchange (debe ser igual al que se usa en el publicador)
channel.exchange_declare(exchange='precio_recomendado', exchange_type='direct')

# Crear una cola exclusiva para el suscriptor
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Vincular la cola al exchange
channel.queue_bind(exchange='precio_recomendado', queue=queue_name)

print(' [*] Esperando recomendaciones de precios...')

# Función de callback para procesar los mensajes recibidos
def callback(ch, method, properties, body):
    recomendacion = json.loads(body)
    
    # Ajuste de inventario basado en la recomendación
    print(f" [x] Ajustando inventario para {recomendacion['producto_id']} con precio sugerido {recomendacion['precio_sugerido']}")

# Iniciar el consumo de mensajes de la cola
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Comenzar a consumir mensajes
channel.start_consuming()
