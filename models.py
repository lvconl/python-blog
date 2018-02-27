#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : models.py
# @Author: lvconl
# @Date  : 18-2-10
#@Software : PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
import datetime

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.String(255),primary_key = True)
    email = db.Column(db.String(255))
    passwd = db.Column(db.String(255))
    admin = db.Column(db.Boolean(),default = False)
    name = db.Column(db.String(255))
    birth = db.Column(db.Date())
    image = db.Column(db.BLOB())
    created_at = db.Column(db.DateTime())

    def __init__(self,id,email,passwd,name):
        self.id = id
        self.email = email
        self.passwd = passwd
        self.name = name
        self.birth = datetime.date.today()
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return "[User] id:`{}`,admin:`{}`,email:`{}`,passwd:`{}`,name:`{}`,birth:`{}`,image:`{}`,created_at:`{}`".format(
            self.id,self.admin,self.email,self.passwd,self.name,self.birth,self.image,self.created_at
        )

class Blogs(db.Model):
    id = db.Column(db.String(255),primary_key = True)
    user_id = db.Column(db.String(255))
    user_name = db.Column(db.String(255))
    user_image = db.Column(db.BLOB())
    name = db.Column(db.String(255))
    summary = db.Column(db.Text())
    content = db.Column(db.Text())
    tag = db.Column(db.String(100))
    created_at = db.Column(db.DateTime())

    def __init__(self,id,user_id,user_name,name,summary,content,tag):
        self.id = id
        self.user_id = user_id
        self.user_name = user_name
        self.name = name
        self.summary = summary
        self.content = content
        self.tag = tag
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return "[Blog] id:`{}`,user_id:`{}`,user_name:`{}`,user_image:`{}`,name:`{}`,summary:`{}`,content:`{}`,tag:`{}`,created_at:`{}`".format(
            self.id,self.user_id,self.user_name,self.user_image,self.name,self.summary,self.content,self.tag,self.created_at
        )

class Comments(db.Model):
    id = db.Column(db.String(255),primary_key = True)
    blog_id = db.Column(db.String(255))
    blog_name = db.Column(db.String(255))
    user_id = db.Column(db.String(255))
    user_name = db.Column(db.String(255))
    user_image = db.Column(db.BLOB())
    content = db.Column(db.Text())
    created_at = db.Column(db.DateTime())

    def __init__(self,id,blog_id,blog_name,user_id,user_name,user_image,content):
        self.id = id
        self.blog_id = blog_id
        self.blog_name = blog_name
        self.user_id = user_id
        self.user_name = user_name
        self.user_image = user_image
        self.content = content
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return "[Content] id:`{}`,blog_id:`{}`,blog_name:`{}`,user_id:`{}`,user_name:`{}`,user_image:`{}`,content:`{}`,created_at:`{}`".format(
            self.id,self.blog_id,self.blog_name,self.user_id,self.user_name,self.user_image,self.content,self.created_at
        )