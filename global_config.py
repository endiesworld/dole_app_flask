import os

basedir = os.path.abspath(os.path.dirname(__file__))
sub_dir = os.path.join(basedir, 'app')
sqlite_db = 'sqlite:///' + os.path.join(sub_dir, 'db','app.db')

# Use In memory database for testing purposes
sqlite_db_test = 'sqlite://'

SYS_SECRET_KEY = os.urandom(16)

class GlobalConfig(object):
    """Global configurations."""
    
    SECRET_KEY =  os.environ.get('SECRET_KEY', SYS_SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', sqlite_db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
class TestingConfig(object):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',sqlite_db_test)
    SECRET_KEY =  os.environ.get('SECRET_KEY', SYS_SECRET_KEY)
    WTF_CSRF_ENABLED = False
