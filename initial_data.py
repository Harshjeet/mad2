from main import app 
from raasan.sec import datastore
from raasan.models import db,Role
from flask_security import  hash_password
from werkzeug.security import generate_password_hash,check_password_hash

with app.app_context():
    db.create_all()
    datastore.find_or_create_role(name ='admin', description = 'current_user is admin role')
    datastore.find_or_create_role(name ='user', description = 'current_user is user role')
    datastore.find_or_create_role(name = 'store_manager', description = 'current_user is store manager role')
    db.session.commit()
    if not datastore.find_user(email = 'admin@admin.com'):
        datastore.create_user(
            username = 'admin',
            email = 'admin@admin.com',
            password = generate_password_hash('1234'),
            roles = ['admin']
        )
    if not datastore.find_user(email = 'user@user.com'):
        datastore.create_user(
            username = 'user',
            email = 'user@user.com',
            password = generate_password_hash('1234'),
            roles = ['user']
        )
    if not datastore.find_user(email = 'store_manager@store_manager.com'):
        datastore.create_user(
            username = 'store_manager',
            email = 'store_manager@store_manager.com',
            password = generate_password_hash('1234'),
            roles = ['store_manager'],
            active = False
        )
    db.session.commit()
    
    
    