run:
	python3 manage.py runserver

newapp:
	@read -p "Digite o nome do novo app: " appname;\
	python3 manage.py startapp $$appname

migration:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

createsuperuser:
	python3 manage.py createsuperuser