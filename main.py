#Les importations des packages 
import pymysql
from app import app
from config import mysql
from flask import request, render_template, Flask,flash,jsonify

############-------------############

#Création de la route pour ajouter un employé 
@app.route('/employe/add',methods=['POST']) 
def add_employe(): # debut de la fonction add_employe()
    try: # debut try execption
    
        json = request.json
        #id = json ['id']
        name = json ['name']
        creation_date = json ['creation_date']
        city = json ['city']
        manager = json ['manager']
        max_salary = json ['max_salary']
        mean_salary = json ['mean_salary']
        min_salary = json ['min_salary']

        # La condition pour que la requete soit une methode POST
        if name and creation_date and city and manager and max_salary and mean_salary and min_salary and request.method == 'POST':
            # Varriable qui nou permet de nous connecter à la base de donnée(db-entreprise)
            db_con = mysql.connect()
            # Accéder ou executer les requetes à la base de donnée (db-entreprise)
            cursr = db_con.cursor(pymysql.cursors.DictCursor)
            # Ici on ecrit les requet sql
            requet_db = 'insert into entreprise (name, creation_date, city, manager, max_salary, mean_salary, min_salary)values(%s,%s,%s,%s,%s,%s,%s)'
            # les attributs de la requette dans une variable bind_db
            bind_db = (name, creation_date, city, manager, max_salary, mean_salary, min_salary)
            # Execution de la requette
            # La fonction execute prend en argument la requette(requet_db) et les attributs de la requette (bind_db)
            cursr.execute(requet_db,bind_db)
            # Commettre l'execution
            db_con.commit()
            return 'Valide'
        else:
            return 'error'
    except Exception as e:
        print(e)
        return 'error error' # fin try execption
    # fin try execption
    
    finally:
        cursr.close()
        db_con.close() # debut de la fonction add_employe()
# fin de la fonction add_employe()


# Pour executer le fichier main si l'application app est run 
if(__name__ == '__main__'):
    app.run()