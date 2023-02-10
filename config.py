from app import app
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
import pymysql




app.config['SECRET_KEY']='root'

#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://%s:%s@%s/%s'%('root','5637','localhost','3306','sqlqlchemy-db')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/order-dba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)


#db.init_app(app)