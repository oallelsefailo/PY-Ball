from flask import ( Blueprint, render_template, request, redirect ) 
from . import models

bp = Blueprint('add', __name__, url_prefix="/add-reptile")

@bp.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        common_name = request.form['common name']
        scientific_name = request.form['name']
        conservation_status = request.form['status']
        native_habitat = request.form['native habitat']
        fun_fact = request.form['fun fact']

        new_reptile = models.Add(scientific_name=scientific_name, common_name=common_name, conservation_status=conservation_status, native_habitat=native_habitat, fun_fact=fun_fact)
        models.db.session.add(new_reptile)
        models.db.session.commit()

        return redirect('/adds')
    
    results = models.Add.query.all()

    return render_template('adds/index.html', adds=results)

@bp.route('/new')
def new(): 
    return render_template('adds/adds.html')