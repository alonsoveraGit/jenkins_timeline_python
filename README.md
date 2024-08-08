# Jenkins Job Execution Timeline

Este proyecto obtiene y visualiza los tiempos de ejecución de los trabajos en Jenkins en un rango de tiempo específico. Utiliza la API de Jenkins para recopilar datos y `matplotlib` para generar una gráfica de dispersión.

## Requisitos

- Python 3.x
- `requests`
- `matplotlib`
- `urllib3`

Puedes instalar las dependencias necesarias con el siguiente comando:

```bash
pip install requests matplotlib urllib3
```

## Configuración

Antes de ejecutar el script, asegúrate de configurar las siguientes variables en el archivo `main.py`:

- `JENKINS_URL`: La URL de tu servidor Jenkins.
- `USER`: Tu nombre de usuario de Jenkins.
- `API_TOKEN`: Tu token de API de Jenkins.

## Uso

El script realiza las siguientes acciones:

1. **Desactiva las advertencias de solicitudes HTTPS no verificadas**: Utiliza `urllib3` para desactivar las advertencias de seguridad cuando se realizan solicitudes HTTPS sin verificación SSL.

2. **Obtiene datos de Jenkins**: Define una función `get_jenkins_data(url)` que realiza una solicitud GET a la URL proporcionada y devuelve los datos en formato JSON.

3. **Obtiene la lista de trabajos**: Utiliza la función `get_jenkins_data` para obtener la lista de todos los trabajos en Jenkins.

4. **Define el rango de tiempo**: Establece un rango de tiempo específico (desde las 00:00 hasta las 09:00 del 08/08/2024).

5. **Obtiene detalles de las ejecuciones de cada trabajo**: Para cada trabajo, obtiene los detalles de las ejecuciones y filtra las ejecuciones que ocurrieron dentro del rango de tiempo especificado.

6. **Ordena los datos**: Ordena los datos de las ejecuciones por timestamp.

7. **Crea la gráfica**: Utiliza `matplotlib` para crear una gráfica de dispersión que muestra los tiempos de ejecución de los trabajos en el rango de tiempo especificado.

8. **Muestra la gráfica**: Muestra la gráfica generada.

## Ejecución

Para ejecutar el script, simplemente corre el siguiente comando en tu terminal:

```bash
python main.py
```

Esto generará y mostrará una gráfica de dispersión con los tiempos de ejecución de los trabajos en Jenkins para el rango de tiempo especificado.
