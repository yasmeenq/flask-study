from pathlib import Path
from flask import current_app
from uuid import uuid4

class ImageHandler:
    @staticmethod
    def save_image(image): #image is a file
        suffix = Path(image.filename).suffix  #the ending(suffix) of image - egg.png suffix is png
        image_name = str(uuid4())+ suffix  #create unique name 12312-fwq13-f214af
        image_path = ImageHandler.get_image_path(image_name) #static/images/12312-fwq13-f214af.png
        image.save(image_path) #save image on the server side(to my project to disc) on static/images/12312-fwq13-f214af.png
        return image_name  #so we can save its name to mysql database 
 
    @staticmethod
    def get_image_path(image_name):
        image_path = Path(current_app.root_path) / "static/images" / image_name
        return image_path
    
