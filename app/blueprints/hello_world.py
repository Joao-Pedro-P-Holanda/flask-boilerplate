
from flask import Blueprint, render_template

hello_world_bp = Blueprint("hello_world",__name__)

@hello_world_bp.route('/',methods=['GET'])
def hello_world():
    return render_template('index.html')
