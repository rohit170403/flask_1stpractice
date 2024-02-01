from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///practice.db"
app.config['SQLAlchemy_TRACK_MODIFICATION'] = False
db=SQLAlchemy(app)

class Practice(db.Model):
    sno = db.Column(db.Integer , primary_key =True)
    fn = db.Column(db.String(200) , nullable=False)
    sn = db.Column(db.String(200) , nullable=False)
    ln = db.Column(db.String(200) , nullable=False)
    gen = db.Column(db.String(200) , nullable=False)
    cor = db.Column(db.String(200) , nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.fn}"

@app.route('/',methods=['GET','POST'])
def hellow_world():
    if request.method =='POST':
        sno = request.form['sno']
        fn = request.form['fn']
        sn = request.form['sn']
        ln = request.form['ln']
        gen = request.form['gen']
        cor = request.form['cor']
        print(sno,fn,sn,ln,gen,cor)

        practice = Practice(sno=sno,fn=fn,sn=sn,ln=ln,gen=gen,cor=cor)
        db.session.add(practice)
        db.session.commit()
    return render_template('index.html')

if __name__=="__main__" :
    app.run(debug=True)