# Gestion des employés

Une application web de gestion des employées

## La description

Une application web qui permet la gestion des employées dans une entreprise.

Elle permettra de faire des modificatioin sur un employé. Ces modification ne sont rien d'autres que les ajouts, les suppressioins, les selections ou triages, ... 
et de faire des bilans de salariés, des employés permenants, ....  

## Commençons

### Dépendances ou les packages 

* Les prérequis

Avoir python installé sur sa machine 

Posséder d'un editeur de code comme visual stidio code 

Installer **CLIENT REST** dans visual stidio code

Posséder Xamp 

Créer une base de donné avec cette requette sql 
```
CREATE TABLE `db-entreprise`.`entreprise` (`id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(255) NULL , `creation_date` DATE NULL , `city` VARCHAR(255) NULL , `manager` VARCHAR(255) NULL , `max_salary` VARCHAR(255) NULL , `mean_salary` VARCHAR(255) NULL , `min_salary` VARCHAR(255) NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
```

* Les bibliothèques 

Flask avec : 
```
- pip install flask

- pip install flask-cors

- pip install flask-mysql
```


### Installation

* Comment/où télécharger ce programme
```
git clone https://github.com/t-h-e-4-5/flask-employe.git
```
* Toutes les modifications nécessaires à apporter aux fichiers/dossiers

Créer un environnement avec la commande 
```
python -m venv "name_of_environemnt"
```

### Exécution du programme

* Comment exécuter le programme
```
pyhton main.py
```

## Aider

Tout conseil pour les problèmes ou problèmes courants.

Véififer les noms des attributs

Le nom de la base de données

## Auteurs

Noms et coordonnées des contributeurs

[@Theophile](https://wa.me/qr/NFB3M6Z66CMVB1)

## Historique des versions

* 0,1
    * Première version

## Licence

Ce projet est sous licence sous la licence MIT 
