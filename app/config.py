import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/database/blackrockdb.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False