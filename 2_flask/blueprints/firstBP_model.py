from flask import Blueprint

blueprint = Blueprint("bluePrint",__name__)

@blueprint.route("/<string:name>")   # bluePrint/
def home(name):
    return f"{name} welcome to the blueprint world"

