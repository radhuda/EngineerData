from flask import Flask, request, jsonify, render_template, redirect
from database import db_session, engine
import pandas as pd
import boto3
#from models import Zinc

app = Flask(__name__)

s3 = boto3.resource('s3')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        smiles_input = request.form.get('smiles_input')
        #app.logger.info('Input : {}'.format(smiles_input))
        print('Input : {}'.format(smiles_input))
        sql_query = "SELECT * FROM zinc_table WHERE smiles = '{}'".format(str(smiles_input).replace(' ',''))
        print(sql_query)
        df = pd.read_sql_query(sql_query, engine)
        print(df)
        tranche = df.iloc[0]["trache_name"]
        print(tranche)
        file = s3.Object(bucket_name="zincdata", key='frags/catalogs/30/molportbb/tranches/AA/xaaa-AA.ref.mol2')
        file.download_file('static/js/rad.mol2')
        return render_template('base.html') + \
                '''
                <section>
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-sm-3">
                            <script type="text/javascript">
                              jmolApplet0 = Jmol.getApplet("jmolApplet0", Info);
                              Jmol.script(jmolApplet0,"background [0,0,34]; load static/js/rad.mol2; spin on")
                            </script>
                        </div>
                        <div class="col-sm-9">
                            <div class="table-responsive">
                            <h1>Here is your chemical:</h1> {}
                            </div>
                        </div>
                    </div>
                </div>
                </section>'''.format(df.to_html())





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