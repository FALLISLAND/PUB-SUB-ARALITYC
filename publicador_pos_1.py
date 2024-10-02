import pika
import json
import time
import random

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('aralityc', 'aralityc')  # Reemplaza con tus credenciales correctas

# Conexión a RabbitMQ con credenciales
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

# Declarar un exchange de tipo 'fanout'
channel.exchange_declare(exchange='pos_data', exchange_type='fanout')

# Simulación de datos de ventas (mejorados con más detalles)
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
clientes = ['Cliente 1', 'Cliente 2', 'Cliente 3']

for _ in range(5):  # Generar 5 transacciones
    datos_venta = {
        'producto_id': random.choice(productos),
        'cantidad': random.randint(1, 5),
        'precio': random.randint(1000, 5000),
        'cliente': random.choice(clientes),
        'fecha': time.strftime('%Y-%m-%d %H:%M:%S'),
        'tienda': 'Tienda A'
    }

    # Publicar el mensaje en el exchange
    channel.basic_publish(exchange='pos_data', routing_key='', body=json.dumps(datos_venta))
    print(f" [x] Datos enviados: {datos_venta}")
    time.sleep(1)

# Cerrar la conexión
connection.close()
