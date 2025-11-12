# Imagen base, partimos de una imagen ligera de Python
FROM python:3.12.3-alpine

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requisitos al contenedor
COPY . .

# Creamos un entorno virtual para aislar las dependencias
RUN python -m venv env_fastapi

# Activamos el entorno virtual
RUN source env_fastapi/bin/activate

# Actualizamos pip a la última versión
RUN pip install --upgrade pip

# Instalamos las dependencias necesarias
RUN pip install -r requirements.txt

# Exponemos el puerto 8080 para acceder a la aplicación
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]