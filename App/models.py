# -*- coding:utf-8 -*-
from App.ext import db


class Person(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    p_name=db.Column(db.String(16))
    p_age=db.Column(db.Integer,default=18)

class Grade(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name=db.Column(db.String(16),unique=True)
    #显性属性·隐性属性   级联查询的属性
    g_students=db.relationship('Student',backref='grade',lazy=True)

class Student(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name=db.Column(db.String(16))
    p_age = db.Column(db.Integer, default=16)
    s_grade_id=db.Column(db.Integer,db.ForeignKey('grade.id'),nullable=False)