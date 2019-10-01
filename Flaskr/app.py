from flask import Flask, request, jsonify, render_template, redirect
from database import db_session
from models import Zinc

app = Flask(__name__)


@app.route('/')
def index():
    zinc = Zinc.query.all()
    return render_template('index.html', zinc=zinc)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
# run Flask app
if __name__ == "__main__":
    app.run()