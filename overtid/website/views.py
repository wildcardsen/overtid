from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from datetime import datetime
from .models import Note, User, UserTime
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    return render_template("home.html", user=current_user)


@views.route('/time', methods=['GET', 'POST'])
@login_required
def time():
    if request.method == 'POST':

        start_dato = request.form.get('start-dato')
        end_dato = request.form.get('end-dato')
        pt = request.form.get('project_type')
        format = "%Y-%m-%dT%H:%M"
        sd = datetime.strptime(start_dato, format)
        ed = datetime.strptime(end_dato, format)
        new_time = UserTime(start_time=sd, end_time=ed,
                            project_type=pt, user_id=current_user.id)
        db.session.add(new_time)
        db.session.commit()

    return render_template("time.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
