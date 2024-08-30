from flask import Blueprint, render_template, send_file, redirect, url_for, request
from facade.auth_facade import AuthFacade
from models.client_error import *
from models.credentials_model import *
from utils.loggger import Logger

auth_blueprint = Blueprint("auth_view", __name__)

auth_facade = AuthFacade()

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'GET': return render_template('register.html', active='register', user= {})#if i don't declare empty user variable it'll raise an error that it's not defined (user = err.model)
        #else
        auth_facade.register()
        return redirect(url_for('home_view.home'))
    except ValidationError as err:  #err here has the user object from auth facade
        return render_template('register.html', error = err.message, user= err.model)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error_message = request.args.get('error')  # Retrieve error message from query parameters
    try:
        if request.method == 'GET': return render_template('login.html', active='login', credentials={}, error=error_message) #if i don't declare empty credentials variable it'll raise an error that it's not defined (credentials = err.model)
        #else
        auth_facade.login()
        return redirect(url_for('home_view.home'))
    except(ValidationError, AuthError) as err:  #err here has the credentials object from auth facade
        Logger.log(err.message)
        return render_template('login.html', error= err.message, credentials= err.model)

    # except AuthError as err:
    #     return render_template('login.html', error = err.message)

@auth_blueprint.route('/logout')
def logout():
    auth_facade.logout()
    return redirect(url_for('home_view.home'))