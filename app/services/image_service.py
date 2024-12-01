import app.services.upscale_service as fsrcnn_service
import app.repositories.store_image_repository as img_repository

models = {
    'fsrcnn': fsrcnn_service.upscale
}

def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {"png", "jpg", "jpeg", "gif"}

def process_image(file, mod):
    img = img_repository.read_from_buffer(file) # original image
    img_sr = models[mod](img) # super resol image
    return img_repository.write_to_buffer(img_sr)

