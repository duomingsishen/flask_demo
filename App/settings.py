# -*- coding:utf-8 -*-


def get_db_uri(dbinfo):

    ENGINE=dbinfo.get('ENGINE') or 'mysql'

    DRIVER=dbinfo.get('DRIVER') or 'pymysql'

    USER=dbinfo.get('USER') or 'root'

    PASSWORD=dbinfo.get('PASSWORD') or 'root'

    HOST=dbinfo.get('HOST') or 'localhost'

    PORT=dbinfo.get('PORT') or '3306'

    NAME=dbinfo.get('NAME') or 'jianshu'

    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE,DRIVER,USER,PASSWORD,HOST,PORT,NAME)


class Config:
    DEBUG=False

    TESTING=False

    SECRET_KEY="132132ASDASDSAD"

    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopConfig(Config):

    DEBUG = True

    DATABASE={
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'360361689',
        'HOST':'10.10.3.8',
        'PORT':3306,
        'NAME':'jianshu'
    }

    SQLALCHEMY_DATABASE_URI=get_db_uri(DATABASE)

class TestingConfig(Config):

    TESTING = True

    DATABASE={
        'ENGINE':'mysql',
        'DRIVER': 'pymysql',
        'USER':'root',
        'PASSWORD':'360361689',
        'HOST':'10.10.3.8',
        'PORT':3306,
        'NAME':'testing'
    }

    SQLALCHEMY_DATABASE_URI=get_db_uri(DATABASE)

class StagingConfig(Config):

    TESTING = True

    DATABASE={
        'ENGINE':'mysql',
        'DRIVER': 'pymysql',
        'USER':'root',
        'PASSWORD':'360361689',
        'HOST':'10.10.3.8',
        'PORT':3306,
        'NAME':'test1'
    }

    SQLALCHEMY_DATABASE_URI=get_db_uri(DATABASE)

class ProductConfig(Config):

    TESTING = True

    DATABASE={
        'ENGINE':'mysql',
        'DRIVER': 'pymysql',
        'USER':'root',
        'PASSWORD':'360361689',
        'HOST':'10.10.3.8',
        'PORT':3306,
        'NAME':'Product'
    }

    SQLALCHEMY_DATABASE_URI=get_db_uri(DATABASE)

envs={
    'develop':DevelopConfig,
    'testing':TestingConfig,
    'staging':StagingConfig,
    'product':ProductConfig
}