install:
	pip install --upgrade pip
	
run:
	python manage.py runserver 0.0.0.0:8000

mig:
	python manage.py makemigrations && \
	python manage.py migrate

delmig:
		rm -rf ./users/migrations/00*.py
		rm -rf ./chefs/migrations/00*.py
		rm -rf ./dishes/migrations/00*.py
		rm -rf ./landing/migrations/00*.py
		
