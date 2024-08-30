from flask import Blueprint, render_template, send_file, redirect, url_for, request, session
from facade.products_facade import ProductsFacade
from utils.image_handler import ImageHandler
from models.client_error import *
from facade.auth_facade import *
from models.role_model import *
from utils.loggger import Logger

products_blueprint = Blueprint("products_view", __name__)

auth_facade = AuthFacade()
products_facade = ProductsFacade()

@products_blueprint.route("/products")
def list():
    all_products = products_facade.get_all_products()
    return render_template("products.html",active="products", products = all_products) #take all products to the html page to show them on the page


@products_blueprint.route("/products/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)


@products_blueprint.route("/products/details/<int:id>")
def details(id):
    try:
        
        one_product = products_facade.get_one_product(id)
        return render_template("details.html", product = one_product, current_user = session.get('current_user'), admin=RoleModel.Admin.value)
    except ResourceNotFoundError as err:
        Logger.log(err.message)
        return render_template('404.html', error=err.message)


@products_blueprint.route("/products/new", methods=["GET", "POST"])
def insert():
    try:
        auth_facade.block_anonymous()
        auth_facade.block_non_user()
        if(request.method=="GET"): return render_template("insert.html", active="new")
        #else "POST" when u click the button add
        products_facade.add_product()
        return redirect(url_for("products_view.list"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error= err.message, credentials={}))  #if anonymous not logged in return him to login page if he wants to insert stuff
    except ValidationError as err:
        return render_template('insert.html', error= err.message, model = err.model)

# @products_blueprint.route("/products/save", methods =["POST"])
# def save():
#     facade = ProductsFacade()
#     facade.add_product()
#     return redirect(url_for("products_view.list"))

@products_blueprint.route("/products/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    try:
        auth_facade.block_non_admin()
        if(request.method=="GET"): 
            one_product = products_facade.get_one_product(id) 
            return render_template("edit.html", product= one_product )
        products_facade.update_product(id)
        return redirect(url_for("products_view.list"))
    except AuthError as err:
        all_products = products_facade.get_all_products() 
        return render_template("products.html", error=err.message, products = all_products)
    except ValidationError as err:
        return render_template("edit.html",error=err.message)


@products_blueprint.route("/products/delete/<int:id>")
def delete(id):
    try:
        auth_facade.block_non_admin()
        products_facade.delete_product(id)
        return redirect(url_for("products_view.list"))
    except AuthError as err:
        all_products = products_facade.get_all_products() 
        return render_template("products.html", error=err.message, products = all_products)
