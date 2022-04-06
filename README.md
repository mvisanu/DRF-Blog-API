# DRF-Blog-API
Django Rest Framework Blogs API

Django Rest API Framework (DRF) & React - Building a Simple Blog API Series


1. create folder
DRF
py -m venv venv
venv\Scripts\activate
pip install django

2. ---create core project
django-admin startproject core .

3. --- create app blog
py manage.py startapp blog

4. ---create app blog_api
py manage.py startapp blog_api

py manage.py runserver

5. --add models (table to database --
py manage.py makemigrations
py manage.py migrate

6. Install djagorestframework
pip install djangorestframework

7.  Add admin link: http://127.0.0.1:8000/admin/
py manage.py createsuperuser
modify blog/admin.py to add the models

8. Install Test Coverage
pip install coverage
----ignore venv folder
coverage run --omit='#/venv/*' manage.py test
run ----
coverage html

9. Build React Application
CREATE new folder DRF-REACT
cd DRF-REACT
code .

commands----
npx create-react-app blogapi .
cd blogapi .
npm start

10.  Install react Router dom and material UI
npm install react-router-dom
npm install @material-ui/core 
npm install --save --legacy-peer-deps @material-ui/core
material-ui.com
https://mui.com/
https://mui.com/getting-started/templates/

11. Back to API and install CORS
pip install django-cors-headers
add to settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'blog_api',
    'rest_framework',
    'corsheaders',  #---------> Add this
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # ------------> Add this
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
