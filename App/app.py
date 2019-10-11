from flask import Flask, request, jsonify, render_template, redirect
from database import db_session, engine
import pandas as pd
import boto3
from appfunctions import purchase_classifier
from post import postresult

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        smiles_input = request.form.get('smiles_input')
        sql_query = "SELECT * FROM zinc WHERE smiles = '{}'".format(str(smiles_input).replace(' ',''))
        df = pd.read_sql_query(sql_query, engine)
        if df.empty:
            smiles = str(smiles_input).replace(' ', "")
            zinc = 'N/A'
            purchase = 'Purchase information not available'
            mwt = 'n/a'
            logp = 'n/a'

        else:
            smiles = df['smiles'][0]
            zinc = df['zinc_id'][0]
            purchase = purchase_classifier(df['purchasable'][0])
            mwt = (df['mwt'][0])
            logp = (df['logp'][0])
            tranche =(df['filename'][0])
            #file = s3.Object(bucket_name="zincdata", key='zincmol' + mol_file)
        template = postresult(smiles,zinc,purchase,mwt,logp)
    else:
        template = '''
                     <div id="smiles">
                    <form method="POST">
                          <input type="text" name="smiles_input" placeholder="input smiles"><br>
                    </form>
                    </div>
                    </div>
                    </section>
                    '''
    return render_template('base.html') + template

# run Flask app
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, use_reloader=True)
