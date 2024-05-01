from flask import Flask
from models import db, Product
from schemas import ma
from flask_restful import Resource, Api
from resources import ProductResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db.init_app(app)
ma.init_app(app)

api = Api(app)
api.add_resource(ProductResource, '/products', '/products/<int:product_id>')

with app.app_context():
    try:
        db.drop_all()
        db.create_all()

        chaussure = Product(name='Chaussure', description='Une belle paire de chaussure', price='20.99')
        armoire = Product(name='Armoire', description='Une belle armoire', price='120.99')
        db.session.add(chaussure)
        db.session.add(armoire)
        db.session.commit()

        chaussure_db = db.session.query(Product).filter(Product.name == 'Chaussure').first()
        armoire_db = db.session.query(Product).filter(Product.name == 'Armoire').first()

        print(f"{chaussure_db.id}: {chaussure_db.name} - {chaussure_db.description}")
        print(f"{armoire_db.id}: {armoire_db.name} - {armoire_db.description}")

        app.run()

    except Exception as ex:
        print(ex)
