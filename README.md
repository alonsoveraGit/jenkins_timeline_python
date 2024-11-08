# Jenkins Job Execution Timeline

Este proyecto obtiene y visualiza los tiempos de ejecución de los trabajos en Jenkins en un rango de tiempo específico. Utiliza la API de Jenkins para recopilar datos y `matplotlib` para generar una gráfica de dispersión.

## Requisitos

- Python 3.x
- `requests`
- `matplotlib`
- `urllib3`
- `pandas`
- `python-dotenv`

Puedes instalar las dependencias necesarias con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Configuración

Antes de ejecutar los scripts, asegúrate de configurar las siguientes variables en un archivo `.env`:

- `JENKINS_URL`: La URL de tu servidor Jenkins.
- `USER`: Tu nombre de usuario de Jenkins.
- `API_TOKEN`: Tu token de API de Jenkins.

## Scripts

### `main_recursivo_generate_excel.py`

Este script es el punto de entrada principal del proyecto. Realiza las siguientes acciones:

1. **Carga de variables de entorno**: Utiliza `python-dotenv` para cargar las variables de entorno desde un archivo `.env`.
2. **Obtención de datos de Jenkins**: Llama a funciones para obtener datos de Jenkins.
3. **Generación de Excel**: Procesa los datos obtenidos y los guarda en un archivo Excel utilizando `pandas`.
4. **Visualización de datos**: Genera y muestra una gráfica de dispersión de los tiempos de ejecución de los trabajos.

### `data_fetcher.py`

Este script contiene funciones para interactuar con la API de Jenkins:

- **`get_jenkins_data(url)`**: Realiza una solicitud GET a la URL proporcionada y devuelve los datos en formato JSON.
- **Funciones adicionales**: Podría incluir funciones para filtrar y procesar los datos obtenidos.

### `plotter.py`

Este script se encarga de la visualización de los datos:

- **Generación de gráficas**: Utiliza `matplotlib` para crear gráficas de dispersión que muestran los tiempos de ejecución de los trabajos.
- **Configuración de gráficos**: Configura aspectos visuales de las gráficas, como etiquetas y formatos de fecha.

## Ejecución

Para ejecutar el script principal, simplemente corre el siguiente comando en tu terminal:

```bash
python main_recursivo_generate_excel.py
```

Esto generará un archivo Excel con los datos de ejecución y mostrará una gráfica de dispersión con los tiempos de ejecución de los trabajos en Jenkins para el rango de tiempo especificado.
