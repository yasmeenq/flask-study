from flask import Blueprint, render_template, send_file
from facade.products_facade import ProductsFacade
from utils.image_handler import ImageHandler

products_blueprint = Blueprint("products_view", __name__)

@products_blueprint.route("/products")
def list():
    facade = ProductsFacade()
    all_products = facade.get_all_products()
    return render_template("products.html", products = all_products) #take all products to the html page to show them on the page


@products_blueprint.route("/products/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)

@products_blueprint.route("/products/details/<int:id>")
def details(id):
    facade = ProductsFacade()
    one_product = facade.get_one_product(id)
    return render_template("details.html", product = one_product)


@products_blueprint.route("/products/images/<str:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)