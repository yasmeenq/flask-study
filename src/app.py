from flask import Flask, render_template
from views.home_view import home_blueprint
from views.about_view import about_blueprint
from views.products_view import products_blueprint
from logging import getLogger, ERROR


app = Flask(__name__)

app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(products_blueprint)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html") 


getLogger("werkzeug").setLevel(ERROR)