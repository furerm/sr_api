from flask import Blueprint, request, send_file, jsonify
import app.services.image_service as image_service

image_controller = Blueprint("image_controller", __name__)

@image_controller.route("/fsrcnn/upscale", methods=["POST"])
def upscale_image_endpoint():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No se encontró ningún archivo"}), 400

        file = request.files['file']

        if not image_service.is_allowed_file(file.filename):
            return jsonify({"error": "file extension is not allowed"}), 400

        buf = image_service.process_image(file, 'fsrcnn')

        return send_file(buf, mimetype='image/jpg', as_attachment=True), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500
