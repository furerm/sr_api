import os
import cv2


cwd = os.getcwd()
model_path = f"{cwd}/app/models_raw/FSRCNN_x4.pb"
sr = cv2.dnn_superres.DnnSuperResImpl().create()
sr.readModel(model_path)
sr.setModel("fsrcnn", 4)


def upscale(image):
    try:
        img_sr = sr.upsample(image)

    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        raise

    return img_sr


