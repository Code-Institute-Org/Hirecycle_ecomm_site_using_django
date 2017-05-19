# Hirecycle 

This project is a fictional e-commerce site that I have built using Django. Some of the key features of this web application are:
1.	Account registration, login, logout and profile
2.	Posting adverts for products available for rent
3.	Adding products to a cart
4.	Checking out and paying for products

## Demo

A demo of this site is available [here](https://hirecycle-ecomm-site.herokuapp.com/)

## Hosting

This app is hosted by Heroku – a container-based cloud Platform as a Service (PaaS) that allows you to deploy, manage, 
and scale apps. Heroku sources code from this Github repo and the data is sourced and hosted from an add-on called Heroku Postgres. 
The Procfile declares the first command to be run to start the app: web: gunicorn hirecycle.wsgi:application.


## Getting started / Deployment

* If you wish to deploy this app locally, please clone or download this repo and use the following guidelines:

### Python
You must have Python 2.7 installed on your system. Download the correct version for your operating system and follow the installation instructions.
requirements.txt
Create and activate a local virtual environment and pip install -r requirements.txt

### Local Server
***N.B.: Please note that running this app locally (without connecting to a database) will result in errors. To connect to your own database, you will need to update the database configurations in the settings.py file and in your virtual environment. 
* See line 9 to 14 to configure to a local database
* See line 90 to configure to a hosted database e.g. Heroku Postgres

Once you have re-configured to your own database, head to the command line and enter:
* $python manage.py makemigrations
* $python manage.py migrate
* $python manage.py createsuperuser

Once you have migrated and have created your superuser name, email and password you can run the following command to run the app.
* $ python manage.py runserver

Navigate to http://localhost:8000/ to view your app locally.

*More detailed deployment instructions to deploy into a live environment (using Heroku) are available in the deployment.txt file.

## Built With

* Django: A Python based web application framework  for rapid development
* PostreSQL: a powerful, open source object-relational database system
* Stripe: a web application that allows individuals and business to accept secure credit card payments on their website
* Amazon S3: object storage with a simple web service interface 
* HTML, CSS and JavaScript: Front end languages that give the application structure, style and interactivity

## UX Design

Details of the UX design and research process undertaken as part of this project is available in the 
projectdocumentation folder. This document outlines how I approached the design of this site through the 
5 layers (strategy, scope, structure, skeleton and surface) and describes 
my ideas for further development of this site (beyond the scope of this site as a Stream 3 project).

## Testing

Manual testing was undertaken for this application and satisfactorily passed. A sample of the tests conducted are as follows:
1.	Testing the responsiveness of the application (on desktop and mobile applications)
2.	Testing the register/login/logout processes/workflows
3.	Testing th post/ edit advert
4.	Testing the checkout process
5.	Testing buttons and hyperlinks throughout the site
6.	Validating database entries / data displayed on screen


## Authors

**Nakita McCool** - This project was completed as part of Code Institute’s Web Development bootcamp in May 2017.

## Acknowledgments

* Template by [Bootstrap](https://startbootstrap.com/)

