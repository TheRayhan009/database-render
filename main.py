from flask import request ,redirect ,url_for
from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
import json

with open('config.json','r', encoding='utf-8')  as c:
    paramiters=json.load(c)["paramiters"]
    
panel = Flask(__name__)

panel.config["SQLALCHEMY_DATABASE_URI"] = paramiters['local_uri']
db = SQLAlchemy(panel)
class Sign_in(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    first_nmae = db.Column(db.String(80), unique=False)
    last_name = db.Column(db.String(80), unique=False)
    # password=db.Column(db.String(30), unique=False)
    # phone_num = db.Column(db.String(80), unique=True)
    # email = db.Column(db.String(80), unique=True)
    # birthday = db.Column(db.String(1200), unique=False)
    # age = db.Column(db.String(10), unique=False)
    # country=db.Column(db.String(40), unique=False)

@panel.route("/", methods=["GET", "POST"])
def home():
    names=Sign_in.query.all()
    return render_template("home.html",user=names)

panel.run(debug=True)
