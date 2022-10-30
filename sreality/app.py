from flask import Flask, render_template
import connection

app = Flask(__name__)


@app.route('/')
def hello():
     return render_template('index.html', items=connection.connect())
     #return render_template('index.html')