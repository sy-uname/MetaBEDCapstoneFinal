## MetaBEDCapstone
Back-End Developer Capstone


## Urls API

```
restaurant/
restaurant/menu/items/
restaurant/menu/items/<pk>
restaurant/booking/tables/
restaurant/booking/tables/<pk>
restaurant/api-token-auth/
admin/
auth/users/
auth/token/login
```

## DB my.cfg
For MariaDB or MySql
```
[client]
database = <DATABASE_NAME>
user = <DB_USER_NAME>
password = <DB_USER_PASSWORD>
host = <IP_OR_HOSTNAME>
port = <PORT>
```

## DB settings.py 
  DATABASES 

    'TEST' := the test database name

  do not forget to add permissions to the test base for <DB_USER_NAME>


## After download
prepare the virtual environment (pipenv or another) and install all dependencies using the following commands.

```bash
cd <project directory>

pipenv shell

pipenv install -r ./requirements.txt

python manage.py check

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```
