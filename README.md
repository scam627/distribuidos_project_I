# Proyecto de distribuidos I

## Definiciones:

- Inactividad: Se definira una maquina como inactiva si la cantidad de recursos que posee para ejecutar un proceso supera en un 20% la cantidad de recursos que el proceso solicita de la maquina

## Roles:

- Servidor:

  - Crear y mantener el enlace con el servidor de distribución, en un intervalo de tiempo dado.
  - Recibir la petición con los recursos recursos solicitados y ejecutarla si se puede.

- Cliente:

  - Solicitar la lista de servidores disponibles cuando desee ejecutar un proceso.
  - Recorrer la lista de servidores disponibles hasta encontrar uno que responda su petición, si no hay servidores disponibles esperar un lapso de tiempo 't' y reiniciar el recorrido por la lista de servidores esto se hara una catidad 'x' de veces.

- Distribución:

  - Crea hilo que reciba las direcciones de los servidores en el sistema y las añada a la lista de servidores de ser necesario.
  - Crear hilos que reciban las peticiones de los clientes y como respuesta envie la lista de servidores actualizada en ese momento.

## Estructura de datos

- Comunicación Servidor-Distribución: Distribución recive String "ip port"
- Comunicación Cliente-Distribución: La distribución envia a el cliente la lista de servidores en forma de string "ip port , ip port ...".
- Comunicación Cliente-Servidor: El servidor recibe los recursos que el cliente solicita en el siguiente formato "cpu memory", el servidor responde con un string "0" o "1"
