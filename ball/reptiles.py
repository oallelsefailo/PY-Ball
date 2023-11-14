from flask import (Blueprint, render_template)
import json

reptiles = json.load(open('reptiles.json', encoding='utf-8'))
print(reptiles)

bp = Blueprint('reptile', __name__, url_prefix="/reptiles")

@bp.route('/')
def index(): 
    return render_template('reptiles/index.html', reptiles=reptiles)

@bp.route('/<int:id>')
def show(id): 
    reptile=reptiles[id - 1]
    return render_template('reptiles/show.html', reptile=reptile)