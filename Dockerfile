# Usamos una imagen base oficial de Python
# Podemos usar otra imagen en base a requerimientos no funcionales, seguridad, tamaño, etc.
FROM python:3.10-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Instalamos dependencias del sistema necesarias para OpenCV y otras herramientas
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Instalamos Poetry
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false

# Copiamos los archivos de configuración de Poetry
COPY pyproject.toml poetry.lock /app/

# Instalamos las dependencias del proyecto
RUN poetry install --no-dev --no-interaction --no-ansi

# Copiamos el resto de la aplicación
COPY app /app/app

# Instalamos Gunicorn para producción
RUN pip install gunicorn

# Exponemos el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para correr Gunicorn con Flask
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app.__main__:app", "--timeout", "120"]

