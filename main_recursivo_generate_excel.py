import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import urllib3
from dotenv import load_dotenv
import os
import pandas as pd

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de Jenkins desde variables de entorno
JENKINS_URL = os.getenv('JENKINS_URL')
USER = os.getenv('USER')
API_TOKEN = os.getenv('API_TOKEN')

# Desactivar advertencias de solicitudes HTTPS no verificadas
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Función para obtener datos de una URL de Jenkins sin verificar SSL
def get_jenkins_data(url):
    response = requests.get(url, auth=(USER, API_TOKEN), verify=False)
    response.raise_for_status()
    return response.json()

# Función para obtener trabajos de Jenkins, incluyendo subcarpetas
def get_all_jobs(url):
    jobs_data = get_jenkins_data(url)
    all_jobs = []
    
    for job in jobs_data['jobs']:
        if job['_class'] == 'com.cloudbees.hudson.plugins.folder.Folder':
            # Si es una carpeta, buscar trabajos dentro de ella
            folder_url = f"{job['url']}api/json?tree=jobs[name,url,_class]"
            all_jobs.extend(get_all_jobs(folder_url))
        else:
            # Si es un trabajo, añadirlo a la lista
            all_jobs.append(job)
    
    return all_jobs

# Obtener la lista de todos los trabajos, incluyendo los de subcarpetas
jobs_url = f"{JENKINS_URL}/api/json?tree=jobs[name,url,_class]"
all_jobs = get_all_jobs(jobs_url)

build_times = []

# Definir el rango de tiempo para hoy desde las 00:00 hasta las 09:00
today = datetime(2024, 11, 7)
start_time = today
end_time = today + timedelta(hours=24)

# Obtener detalles de las ejecuciones de cada trabajo
for job in all_jobs:
    job_name = job['name']
    job_url = job['url']
    
    builds_url = f"{job_url}api/json?tree=builds[number,url,timestamp,duration]"
    builds_data = get_jenkins_data(builds_url)
    
    # Verificar si la clave 'builds' está presente en la respuesta
    if 'builds' in builds_data:
        for build in builds_data['builds']:
            build_timestamp = datetime.fromtimestamp(build['timestamp'] / 1000)
            
            # Filtrar por el rango de tiempo especificado
            if start_time <= build_timestamp <= end_time:
                build_times.append({
                    'job_name': job_name,
                    'start_time': build_timestamp,
                    'duration': timedelta(milliseconds=build['duration'])
                })
            else:
                print(f"Build fuera de rango: {build_timestamp} para el trabajo {job_name}")
                print(f"Rango esperado: {start_time} a {end_time}")

# Ordenar los datos por start_time
build_times.sort(key=lambda x: x['start_time'])

# Preparar los datos para el diagrama de Gantt
labels = [bt['job_name'] for bt in build_times]
start_times = [bt['start_time'] for bt in build_times]
durations = [bt['duration'] for bt in build_times]

# Crear el diagrama de Gantt
fig, ax = plt.subplots(figsize=(15, 8))

# Crear barras para el diagrama de Gantt
ax.barh(labels, durations, left=start_times, color='blue', edgecolor='black')

# Formato del eje x
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.set_xlabel('Hora')
ax.set_ylabel('Tareas')
ax.set_title(f'Diagrama de Gantt de ejecuciones de trabajos en Jenkins ({today.strftime("%d/%m/%Y")} de 00:00 a 09:00)')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar la gráfica
plt.show()

# Crear un DataFrame con los datos de las ejecuciones
df = pd.DataFrame(build_times)

# Añadir una columna para la hora de fin
df['end_time'] = df['start_time'] + df['duration']

# Guardar el DataFrame en un archivo Excel
df.to_excel('jenkins_builds.xlsx', index=False, columns=['job_name', 'start_time', 'end_time', 'duration'])
