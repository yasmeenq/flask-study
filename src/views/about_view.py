from flask import Blueprint, render_template

about_blueprint = Blueprint("about_view", __name__)

@about_blueprint.route("/about")
def about():
    return render_template("about.html", active="about")
