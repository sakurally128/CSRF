import os
HOSTNAME = "localhost"
POST = "3306"
DATABASE = "app_demo"
USERNAME = "root"
PASSWORD = "123456"

SECRET_KEY = os.urandom (24)

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'.format(
    username=USERNAME,password = PASSWORD,host=HOSTNAME,port=POST,db = DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_COMMIT_TEARDOWN = True

