from flask import Blueprint, jsonify, make_response
from facade.products_facade import ProductsFacade
from utils.loggger import Logger
from models.client_error import *
from models.status_code import StatusCode

api_blueprint = Blueprint("api_view", __name__)
products_facade = ProductsFacade()

@api_blueprint.route("/api/products")
def products():  # i want a function that will publish all my products as api for further use
    products = products_facade.get_all_products()
    return jsonify(products)

@api_blueprint.route("/api/products/<int:id>")
def product(id):
    try:
        product = products_facade.get_one_product(id)
        return jsonify(product)
    except ResourceNotFoundError as err:
        Logger.log(err.message)
        json = jsonify({"error": err.message})
        return make_response(json, StatusCode.NotFound.value)