# Code here 

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)  #defining flask


# connecting db=sqlalchemy to API

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///drinks.db'  #configuring 
db=SQLAlchemy(app)

class Drink(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    description=db.Column(db.String(120),unique=True,nullable=False)

    def __repr__(self):
        return f"{self.name} - {self.description}"


# GET method to display hello
@app.route('/')
def index():
    return 'Hello'

# app to store drinks 
@app.route('/drinks')
def get_drinks():
    drinks=Drink.query.all()
    output=[]
    for drink in drinks:
        drink_data={'name':drink.name,'description':drink.description}
        output.append(drink_data)
    return {"drinks":output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink=Drink.query.get_or_404(id)
    return {"name":drink.name,"description":drink.description}

@app.route('/drinks',methods=['POST'])
def add_drink():
    drink=Drink(name=request.json['name'],description='A milky coffee')
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

@app.route('/drinks/<id>',methods=['DELETE'])
def delete_drink(id):
    drink=Drink.query.get_or_404(id)
    if drink is None:
        return {"message": "Drink not found"}, 404
    db.session.delete(drink)
    db.session.commit()
    return {"message": "Drink deleted successfully"}

if __name__=="__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)