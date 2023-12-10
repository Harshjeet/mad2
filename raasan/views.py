from flask import current_app as app, jsonify ,request,render_template
from flask_security import auth_required, roles_required
from .models import User,db, Role
from .sec import datastore
from werkzeug.security import generate_password_hash, check_password_hash


@app.get("/")
def index():
    return render_template('index.html')

@app.get('/admin')
@auth_required('token')
@roles_required('admin')
def admin():
    return 'hello admin created hua hai'

@app.get('/activate/store_manager/<int:store_id>')
@auth_required('token')
@roles_required('store_manager')
def activate_store_manager(store_id):
    store_mgr = User.query.get(store_id)
    if not store_mgr or 'store_manager' not in store_mgr.roles:
        return jsonify({"message":"store manager not found"}), 404   
    
    store_mgr.active = True
    db.session.commit()
    return jsonify({"message":"store manager activated"})

@app.post('/user-login')
def user_login():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({"message": "email is required"}), 400
    
    user = datastore.find_user(email=email)
    if not user:
        return jsonify({"message": "user not found"}), 404
    
    if check_password_hash(user.password, data.get('password')):
        return user.get_auth_token
    else:
        return jsonify({"message": "password galat hai bhai"}), 401

    
    
    