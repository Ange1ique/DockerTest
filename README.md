# Practice
Small RSSfeed web app with sqlite3 db running with Docker Compose

## Prerequisites
* Installation of Docker
* Installation of Docker Compose

## Installation instructions
* Download or clone this repository
* Go to "DockerTest" folder
* Enter the following commands in terminal (with or without sudo): 
> sudo docker-compose up -d

> sudo docker-compose exec web python manage.py migrate
* Visit the web app in your browser with:
> localhost:8000

## Notes
* a superuser needs to be made manually