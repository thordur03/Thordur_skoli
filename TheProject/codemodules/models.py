from __init__ import db
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import null

class UserModel(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    bio = db.Column(db.String(400), nullable=False,default="")
    
    profile_picture = db.Column(db.String(400),default="n/a")
    
    date_added = db.Column(db.DateTime,default=datetime.utcnow())
    password_hash = db.Column(db.String(128), nullable=False)
    
    clothings = db.relationship("ClothingModel",backref="user")
    posts = db.relationship("PostModel",backref="user")
    

    def __repr__(self):
        return "<Name %r>" % self.name

class ClothingModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    describtion = db.Column(db.String(220))
    type = db.Column(db.String(10), nullable=False)

    image_link = db.Column(db.String(),nullable=False)
    #date_added = db.Column(db.DateTime,default=datetime.utcnow())
    user_id  = db.Column(db.Integer,db.ForeignKey(UserModel.id))

class PostModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id  = db.Column(db.Integer,db.ForeignKey(UserModel.id))
    likes = db.Column(db.Integer,default=0)
    #date_added = db.Column(db.DateTime,default=datetime.utcnow())
    hat = db.Column(db.Integer,db.ForeignKey(ClothingModel.id), default=null)
    shirt = db.Column(db.Integer,db.ForeignKey(ClothingModel.id), default=null)
    jacket = db.Column(db.Integer,db.ForeignKey(ClothingModel.id), default=null)
    gloves = db.Column(db.Integer,db.ForeignKey(ClothingModel.id), default=null)
    pants = db.Column(db.Integer,db.ForeignKey(ClothingModel.id), default=null)
    shorts = db.Column(db.Integer,db.ForeignKey(ClothingModel.id), default=null)
    shoes = db.Column(db.Integer,db.ForeignKey(ClothingModel.id), default=null)
    socks = db.Column(db.Integer,db.ForeignKey(ClothingModel.id), default=null)