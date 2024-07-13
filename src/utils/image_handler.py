from pathlib import Path
from flask import current_app

class ImageHandler:
    @staticmethod
    def get_image_path(image_name):
        image_path = Path(current_app.root_path) / "static/images" / image_name
        return image_path
    
