from flask import Flask, request, jsonify, render_template, redirect
from database import db_session
#from models import Zinc

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        smiles_input = request.form.get('smiles_input')
        zinc = db_session.execute("SELECT * FROM zinc_table WHERE smiles='{}'".format(smiles_input))
        return (render_template('index.html'), zinc)


    else:
        return render_template('index.html') + \
        '''<form method="POST">
              <input type="text" name="smiles_input"><br>
              <input type="submit" value="Submit"><br>
          </form>'''




@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
# run Flask app
if __name__ == "__main__":
    app.run()