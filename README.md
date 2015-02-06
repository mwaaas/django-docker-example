This is a basic starter django app with a Dockerfile and a fig.yml file for setting up a development environment in a docker containter. 


##Development Environment Instructions 

it has been tested with ubuntu 14.04 only

Clone this repository.

`cd django-docker-example`

### install fig
sudo pip install -U fig

### docker and fig requires root permission
`sudo su`

`fig up` or `fig up -d` to run as daemon

`fig run web python manage.py migrate`

then visit localhost:8080 in your browser. 

##Running management commands

examples:

`fig run web python manage.py migrate`

`fig run web python manage.py createsuperuser`













