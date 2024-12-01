import os
import cv2
from flask import Flask
from app.controllers.image_controller import image_controller

def create_app():
    app = Flask(__name__)
    app.register_blueprint(image_controller, url_prefix="/api")
    return app