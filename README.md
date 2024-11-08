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

### `main.py`

Este script es el punto de entrada principal del proyecto. Realiza las siguientes acciones:

1. **Carga de variables de entorno**: Utiliza `python-dotenv` para cargar las variables de entorno desde un archivo `.env`.
2. **Obtención de datos de Jenkins**: Llama a funciones para obtener datos de Jenkins.
3. **Visualización de datos**: Genera y muestra una gráfica de dispersión de los tiempos de ejecución de los trabajos.

### `main_recursivo.py`

Este script es una variante del script principal que implementa un enfoque recursivo para obtener y procesar los datos:

1. **Obtención recursiva de datos**: Utiliza un enfoque recursivo para navegar por los datos de Jenkins.
2. **Procesamiento de datos**: Filtra y organiza los datos obtenidos.
3. **Visualización de datos**: Genera y muestra una gráfica de dispersión similar a `main.py`.

### `main_recursivo_generate_excel.py`

Este script extiende la funcionalidad de `main_recursivo.py` para incluir la generación de un archivo Excel:

1. **Carga de variables de entorno**: Similar a los otros scripts, carga las variables de entorno necesarias.
2. **Obtención y procesamiento de datos**: Utiliza un enfoque recursivo para obtener y procesar los datos de Jenkins.
3. **Generación de Excel**: Procesa los datos obtenidos y los guarda en un archivo Excel utilizando `pandas`.
4. **Visualización de datos**: Genera y muestra una gráfica de dispersión de los tiempos de ejecución de los trabajos.

## Ejecución

Para ejecutar cualquiera de los scripts, simplemente corre el siguiente comando en tu terminal, reemplazando `<script_name>` con el nombre del script que deseas ejecutar:

```bash
python <script_name>.py
```

Esto generará y mostrará una gráfica de dispersión con los tiempos de ejecución de los trabajos en Jenkins para el rango de tiempo especificado, y en el caso de `main_recursivo_generate_excel.py`, también generará un archivo Excel con los datos.
