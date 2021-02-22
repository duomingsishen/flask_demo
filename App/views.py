# -*- coding:utf-8 -*-
import random

from flask import Blueprint
from flask import current_app
from flask import g
from flask import render_template
from flask import request
from sqlalchemy import and_
from sqlalchemy import not_
from sqlalchemy import or_

from App.ext import db
from App.models import Person, Grade, Student

blue=Blueprint('first_blue',__name__)

def init_first_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    return 'hello flask'

@blue.route('/addperson/')
def add_person():
    person=Person()

    flag=random.randrange(100)

    person.p_name="我打你%d下"%flag

    person.p_age=flag

    db.session.add(person)

    db.session.commit()

    return 'Add Success'

@blue.route('/getpersons/')
def get_persons():
    # persons=Person.query.all()   #查询所有

    # persons=Person.query.filter(Person.p_age.__lt__(50))  #小于
    # persons = Person.query.filter(Person.p_age>50)

    # persons=Person.query.filter(Person.p_name.contains('想'))
    # persons=Person.query.filter(Person.p_name.startswith('想'))

    #常用在级联数据上
    # persons = Person.query.filter_by(p_age=80)

    #order_by 在offset和limit之前    offset和limit不分顺序  offset最先执行
    # persons = Person.query.order_by('p_age').offset(8).limit(4)
    # persons = Person.query.filter(Person.p_age>15).filter(Person.p_age<30)
    # persons = Person.query.filter(and_(Person.p_age>=10,Person.p_age<30))
    # persons = Person.query.filter(or_(Person.p_age>=10,Person.p_age<30)).order_by('p_age')
    persons=Person.query.filter(not_(Person.p_age==80)).order_by('p_age')

    return render_template('PersonList.html',persons=persons)


@blue.route('/getperson/')
def get_person():

    # person=Person.query.get(6)   #获取的没有的时候 返回none

    person = Person.query.order_by("-id").first()

    print(person.p_name)

    return '获取person'

@blue.route('/getpersonswithpage/')
def get_persons_with_page():

    #分页  数据   第几页   每页多少条
    page=request.args.get('page',1,type=int)

    print(page)

    print(type(page))

    per_page=request.args.get('per_page',3,type=int)

    persons=Person.query.limit(per_page).offset(per_page*(page-1))

    return render_template('PersonList.html', persons=persons)

@blue.route('/getpersonsbypaginate/')
def get_persons_by_paginate():

    page = request.args.get('page', 1, type=int)

    per_page = request.args.get('per_page', 4, type=int)

    pagination=Person.query.paginate(page,per_page)  #对象

    # persons=pagination.items   #直接获取数据

    return render_template('PersonListPagination.html',pagination=pagination,per_page=per_page)

@blue.route('/addgrade/')
def add_grade():

    grade=Grade()

    grade.g_name='python%d'%random.randrange(2000)

    db.session.add(grade)

    db.session.commit()

    return 'Grade Add Success'

@blue.route('/addstudent/')
def add_student():

    grade=Grade.query.order_by('-id').first()

    student=Student()

    student.s_name="好程序员%d"%random.randrange(100)

    student.s_grade_id=grade.id

    db.session.add(student)

    db.session.commit()

    return 'Student Add Success'

@blue.route('/getgradebystudent/')
def get_drade_student():

    student=Student.query.order_by('-id').first()

    # grade=Grade.query.get(student.s_grade_id)

    # print(grade)

    # print(student.grade)
    grade=student.grade

    return '班级获取成功%s'%grade.g_name

@blue.route('/getstudentsbygrade/')
def get_students_by_grade():

    grade=Grade.query.order_by('-id').first()
    print(type(grade.g_students))
    print(grade.g_students)

    # students=Student.query.filter(Student.s_grade_id==grade.id)
    students=grade.g_students

    return render_template('StudentList.html', students=students)

@blue.route('/configlist/')
def config_list():

    config=current_app.config

    # print(type(config))
    #
    # print(config)

    # for key in config.keys():
    #     print(key,config.get(key))

    return render_template('ConfigList.html')


@blue.before_request
def process_request():
    print('请求之前')

    g.content='德玛西亚'