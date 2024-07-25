from flask import Blueprint, render_template, send_file, redirect, url_for, request
from facade.auth_facade import AuthFacade
from models.client_error import *

auth_blueprint = Blueprint("auth_view", __name__)

auth_facade = AuthFacade()

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'GET': return render_template('register.html', active='register')
        #else
        auth_facade.register()
        return redirect(url_for('home_view.home'))
    except ValueError as err:
        return render_template('register.html', error = err.message)
