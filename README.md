### django Local Server
`python manage.py runserver`

### celery worker
`celery -A NotificationEngine worker -l info`

### celery beat
`celery -A NotificationEngine beat -l info -S django`

### redis server
`redis-server`


### Run migrations:
> python manage.py makemigrations

> python manage.py migrate


### Celery Dashboard
* Launch the server and open http://localhost:5555

     `flower -A NotificationEngine --port=5555`
* Ref:
    > http://flower.readthedocs.io/en/latest/config.html


#### Ref:
* https://www.codingforentrepreneurs.com/blog/celery-redis-django/