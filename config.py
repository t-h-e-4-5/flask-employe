#Les importations des packages 
from app import app
from flaskext.mysql import MySQL

mysql = MySQL() ## Crer une instanse mysql

####Les routes pour la connexion avec la base de données 
app.config['MYSQL_DATABASE_USER']= "root"
app.config['MYSQL_DATABASE_HOST']= "localhost"
app.config['MYSQL_DATABASE_PASSWORD']= ""
app.config['MYSQL_DATABASE_DB']= "db-entreprise"

#pranché
mysql.init_app(app)