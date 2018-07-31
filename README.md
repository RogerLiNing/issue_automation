# issue_automation
# Moving issues from project's column to column based on Issues' tags

#### Project language
- Python 3.6+

#### Dependency mangagement
- Pipenv 
```
$ pipe install pipenv 
$ pipenv sync
$ pipenv shell
```

#### Dependency used
```
celery==4.2.1                                                                 
Django==2.0.7                                                              
PyMySQL==0.9.2
redis==2.10.6      
django-celery-results==1.0.1                                                      
```

### Backend database
- MySql
Sync model to database table
```
$ python manage.py migration

$ python manage.py createsuperuser
```
- Redis
- Celery
``` 
celery -A issue_automation worker -l info --pool=solo
```
