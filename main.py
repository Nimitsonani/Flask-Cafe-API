from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


#create db and add all data from that into a list
all_cafe_detail = []
with app.app_context():
    db.create_all()
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafe_obj = result.scalars()
    all_cafe_obj_list = []

    for i in all_cafe_obj:
        all_cafe_obj_list.append(i)

    for j in all_cafe_obj_list:
        cafe_dict = {
            'id': j.id,
            'name': j.name,
            'map_url': j.map_url,
            'img_url': j.img_url,
            'location': j.location,
            'seats': j.seats,
            'has_toilet': j.has_toilet,
            'has_wifi': j.has_wifi,
            'has_sockets': j.has_sockets,
            'can_take_calls': j.can_take_calls,
            'coffee_price': j.coffee_price,
        }
        all_cafe_detail.append(cafe_dict)




#home route
@app.route("/")
def home():
    return render_template("index.html")

random_cafe=random.choice(all_cafe_detail)


#random raoute
@app.route('/random',methods=['GET'])
def random():
    return jsonify(cafe=random_cafe)


#all route
@app.route('/all',methods=['GET'])
def all():
    return jsonify(all_cafes=all_cafe_detail)


#seacrh route
@app.route('/search')
def search():
    loc=request.args.get('loc').title()
    found=False
    for i in all_cafe_detail:
        if i['location']==loc:
            found = True
            return jsonify(cafe=i)
    if not found:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        })

def str_to_bool(value):
    return value.lower()=='true'


#add route
@app.route('/add',methods=['POST'])
def add():
    add_dict=Cafe(
    id=request.form.get('id'),
    name=request.form.get('name'),
    map_url=request.form.get('map_url'),
    img_url=request.form.get('img_url'),
    location=request.form.get('location'),
    seats=request.form.get('seats'),
    has_toilet=str_to_bool(request.form.get('has_toilet')),
    has_wifi=str_to_bool(request.form.get('has_wifi')),
    has_sockets=str_to_bool(request.form.get('has_sockets')),
    can_take_calls=str_to_bool(request.form.get('can_take_calls')),
    coffee_price=request.form.get('coffee_price'),
    )
    db.session.add(add_dict)
    db.session.commit()
    return jsonify(response={
        "success": "Cafe added successfully!"
    })


#update price route
@app.route('/update_price/<cafe_id>',methods=['GET','PATCH'])
def update_price(cafe_id):
    cafe_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe_to_update is not None:
        cafe_to_update.coffee_price=request.args.get('new_price')
        db.session.commit()
        return jsonify(success='successfully updated the price.'),200
    elif cafe_to_update is None:
        return jsonify(error={
            'Not Found':'Sorry a cafe with that id was not found in data base.'
        }),404


#report closed route
@app.route('/report_closed/<cafe_id>',methods=['GET','DELETE'])
def report_closed(cafe_id):
    cafe_to_delete=db.session.execute(db.select(Cafe).where(Cafe.id==cafe_id)).scalar()
    if cafe_to_delete is not None:
        if request.args.get('api_key')=='topsecretkey':
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(done='ok')
        else:
            return jsonify(error='Sorry,thats not allowed. make sure you have the correct api key.')
    else:
        return jsonify(error={
            'Not Found':'Sorry a cafe with that id was not found in data base.'
        })


if __name__ == '__main__':
    app.run(debug=True)
