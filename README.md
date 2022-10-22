# Projet 12 - Développez une architecture back-end sécurisée en utilisant Django ORM

## Introduction

Ce projet a pour but la création d’une application CRM (Customer Relationship Management)

 - Postgresql
 - Django framework 
 - Django REST framework

# 1. Postgresql

### Installation et création d’une base de donnée.

Windows >  [https://www.veremes.com/installation-postgresql-windows#installation_PostgreSQL](https://www.veremes.com/installation-postgresql-windows#installation_PostgreSQL)  
Linux >  [https://www.linuxtricks.fr/wiki/debian-10-installer-et-utiliser-postgresql](https://www.linuxtricks.fr/wiki/debian-10-installer-et-utiliser-postgresql)

# 2. Epic Events API

### Installation et configuration.

#### Cloner ce dépôt :

```
git clone https://github.com/batshanti/Projet12.git
cd Projet12/

```

#### Créer un environnement virtuel pour le projet :

(Linux or Mac)

```
 python3 -m venv venv
 source venv/bin/activate

```

(Windows)

```
 python -m venv env
 env\Scripts\activate

```

#### Installer les packages :

```
pip install -r requirements.txt

```

#### Création d’un super utilisateur :

```
python manage.py createsuperuser

```

#### Ajouter les informations de connexion à la base de donnée PostgreSQL dans le fichier  **[settings.py](http://settings.py)**  de l’application :

```
DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<Nom de la base de donnée>',
        'USER': '<Utilisateur>',
        'PASSWORD': '<Mot de passe>',
        'HOST': '',
        'PORT': '',
    }
}

```

#### Démarrer le serveur :

```
python manage.py runserver

```

## Lancement de l’application web
