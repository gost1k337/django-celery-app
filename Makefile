dev-build:
	sudo docker-compose build
dev-run:
	sudo docker-compose up
dev-down:
	sudo docker-compose down -v
migration:
	sudo docker-compose exec app python3 manage.py makemigrations
migrate:
	sudo docker-compose exec app python3 manage.py migrate
superuser:
	sudo docker-compose exec app python3 manage.py createsuperuser
