run:
	python scripts/main.py

docker:
	docker-compose up --build

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down
