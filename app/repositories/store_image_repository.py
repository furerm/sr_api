from io import BytesIO
from PIL import Image
import numpy as np

def read_from_buffer(file):
    # Leer los datos del archivo
    data = file.read()
    if not data:
        raise ValueError("El archivo está vacío o no contiene datos.")

    # Decodificar la imagen usando PIL
    try:
        img_pil = Image.open(BytesIO(data))
        img_pil = img_pil.convert("RGB")  # Asegurarse de que sea RGB
    except Exception as e:
        raise ValueError(f"Error al decodificar la imagen: {e}")

    # Convertir la imagen PIL a un arreglo NumPy
    img_np = np.array(img_pil)
    return img_np

def write_to_buffer(img_sr, format='JPEG'):
    # Validar el formato
    supported_formats = ['JPEG', 'PNG']
    if format.upper() not in supported_formats:
        raise ValueError(f"Formato no soportado: {format}. Use uno de {supported_formats}.")

    # Convertir el arreglo NumPy de vuelta a una imagen PIL
    try:
        img_pil = Image.fromarray(img_sr)
    except Exception as e:
        raise ValueError(f"Error al convertir el arreglo NumPy a PIL: {e}")

    # Escribir la imagen en un buffer
    buf = BytesIO()
    img_pil.save(buf, format=format.upper())
    buf.seek(0)  # Resetear el puntero del buffer
    return buf
