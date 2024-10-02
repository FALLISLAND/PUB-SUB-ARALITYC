<!DOCTYPE html>
<html lang="es">
<body>

  <h1>Sistema de Mensajería Asíncrona con RabbitMQ</h1>
  <p>Este proyecto implementa un sistema de mensajería asíncrona usando <strong>RabbitMQ</strong>, con un patrón de publicador-suscriptor para procesar y analizar datos en el contexto de ventas retail.</p>

  <h2>Publicadores</h2>
  <ul>
    <li><strong>Publicador POS:</strong> Envía datos de ventas del punto de venta a RabbitMQ.</li>
    <li><strong>Publicador de Recomendaciones de Precios:</strong> Publica ajustes de precios basados en el análisis de tendencias de ventas.</li>
    <li><strong>Publicador de Alertas de Anomalías:</strong> Detecta y publica alertas por caídas en ventas o problemas de inventario.</li>
  </ul>

  <h2>Suscriptores</h2>
  <ul>
    <li><strong>Suscriptor de Análisis de Tendencias:</strong> Recibe datos de ventas y analiza tendencias de consumo.</li>
    <li><strong>Suscriptor de Gestión de Inventario:</strong> Ajusta el inventario en función de las recomendaciones de precios recibidas.</li>
    <li><strong>Suscriptor de Análisis de Anomalías:</strong> Recibe alertas y notifica al equipo sobre problemas detectados.</li>
  </ul>

  <h2>Flujo de Trabajo</h2>
  <p>El flujo del sistema incluye:</p>
  <ol>
    <li>El <strong>Publicador POS</strong> envía datos de ventas.</li>
    <li>El <strong>Suscriptor de Análisis de Tendencias</strong> analiza los datos recibidos.</li>
    <li>El <strong>Publicador de Recomendaciones</strong> ajusta los precios según las tendencias.</li>
    <li>El <strong>Suscriptor de Inventario</strong> ajusta el stock según las recomendaciones.</li>
    <li>El <strong>Publicador de Alertas</strong> monitorea anomalías y las notifica al <strong>Suscriptor de Anomalías</strong>.</li>
  </ol>

  <h2>Tecnologías Utilizadas</h2>
  <ul>
    <li>RabbitMQ</li>
    <li>Python (Pika)</li>
  </ul>

</body>
</html>
