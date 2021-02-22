# -*- coding:utf-8 -*-
from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_first_blue


def create_app():
    app=Flask(__name__,template_folder='../templates')

    #初始化app
    app.config.from_object(envs.get('testing'))

    #初始化蓝图·路由
    init_first_blue(app)

    #初始化第三方库
    init_ext(app)


    return app