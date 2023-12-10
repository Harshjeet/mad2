from flask_restful import Resource,Api,reqparse,marshal_with,fields
from .models import db,User,Product

api = Api(prefix='/api')
parser = reqparse.RequestParser()

                                # ============================
                                #    Product API Section     #
                                # ============================
# this is for product
parser.add_argument('name',type = str, help = 'name should be required and be string')
parser.add_argument('description',type = str, help = 'description should be string')
parser.add_argument('price',type = float, help = 'price should be required and be float')
parser.add_argument('product_quantity',type = int, help = 'quantity should requried and be int')



# Here, we are creating a resource for products means converting json data to python object so that
product_fields ={
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'price': fields.Float,
    'product_quantity': fields.Integer 
} 
class Products(Resource):
    @marshal_with(product_fields)
    def get(self):
        all_products = Product.query.all()
        return all_products
        
# ----------------------------
#     CRUD Operations on Product
# ----------------------------
    def post(self):
        args = parser.parse_args()
        product = Product(name = args['name'], description = args['description'], price = args['price'], product_quantity = args['product_quantity'])
        db.session.add(product)
        db.session.commit()
        return {"product": product.name , "message": 'product added'}
    
    def delete(self, product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return {"product": product.name,"message": "product deleted"}
        else:
            return {"message": "product not found"}
        
    def patch(self, product_id):
        args = parser.parse_args()
        product = Product.query.get(product_id)
        
        if product:
            for key, value in args.items():
                if value is not None:
                    setattr(product, key, value)
                    
            db.session.commit()
            return({"product": product.name, "message": "product updated"})
        else:
            return {"message": f"Product with ID {product_id} not found"}, 404
    


                                # ============================
                                #    Category API Section     #
                                # ============================
                                
api.add_resource(Products, '/products', '/products/<int:product_id>')

