from flask import Blueprint, render_template, send_file, redirect, url_for, request
from facade.products_facade import ProductsFacade
from utils.image_handler import ImageHandler
from models.client_error import *


products_blueprint = Blueprint("products_view", __name__)

@products_blueprint.route("/products")
def list():
    facade = ProductsFacade()
    all_products = facade.get_all_products()
    return render_template("products.html",active="products", products = all_products) #take all products to the html page to show them on the page


@products_blueprint.route("/products/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)

@products_blueprint.route("/products/details/<int:id>")
def details(id):
    facade = ProductsFacade()
    try:
        one_product = facade.get_one_product(id)
        return render_template("details.html", product = one_product)
    except ResourceNotFoundError as err:
        return render_template('404.html', error=err.message)


@products_blueprint.route("/products/new", methods=["GET", "POST"])
def insert():
    try:
        if(request.method=="GET"): return render_template("insert.html", active="new")
        #else "POST" when u click the button add
        facade = ProductsFacade()
        facade.add_product()
        return redirect(url_for("products_view.list"))
    except ValidationError as err:
        return render_template('insert.html',error=err)

# @products_blueprint.route("/products/save", methods =["POST"])
# def save():
#     facade = ProductsFacade()
#     facade.add_product()
#     return redirect(url_for("products_view.list"))

@products_blueprint.route("/products/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    try:
        facade = ProductsFacade()
        if(request.method=="GET"): 
            one_product = facade.get_one_product(id) 
            return render_template("edit.html", product = one_product )
        
        facade.update_product(id)
        return redirect(url_for("products_view.list"))
    except ValidationError as err:
        return render_template('edit.html', error=err)

@products_blueprint.route("/products/delete/<int:id>")
def delete(id):
    facade = ProductsFacade()
    facade.delete_product(id)
    return redirect(url_for("products_view.list"))


