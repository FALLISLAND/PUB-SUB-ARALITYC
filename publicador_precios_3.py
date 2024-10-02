import pika
import json

# Configuración de credenciales de RabbitMQ
credentials = pika.PlainCredentials('aralityc', 'aralityc')  # Reemplaza con tus credenciales correctas

# Conexión a RabbitMQ con credenciales
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

# Declarar un exchange de tipo 'direct'
channel.exchange_declare(exchange='precio_recomendado', exchange_type='direct')

# Simulación de recomendación de precio basado en demanda
def generar_recomendacion_precio(producto, ventas):
    if ventas > 10:
        precio_sugerido = 5000  # Subir precio si hay alta demanda
        motivo = 'Alta demanda'
    else:
        precio_sugerido = 4000  # Bajar precio si hay baja demanda
        motivo = 'Baja demanda'
    
    return {
        'producto_id': producto,
        'precio_sugerido': precio_sugerido,
        'motivo': motivo
    }

# Ejemplo de recomendación de precio para Producto A
ventas_producto_a = 15  # Simulación de ventas
recomendacion_precio = generar_recomendacion_precio('Producto A', ventas_producto_a)

# Publicar la recomendación
routing_key = recomendacion_precio['producto_id']
channel.basic_publish(exchange='precio_recomendado', routing_key=routing_key, body=json.dumps(recomendacion_precio))
print(f" [x] Recomendación enviada: {recomendacion_precio}")

# Cerrar la conexión
connection.close()
