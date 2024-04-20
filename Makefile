CONTAINER = app

up:
	docker compose up -d

rebuild:
	docker compose up --build -d

down:
	docker compose down

lint:
	black .
	isort .
	mypy .

shell:
	docker exec -it ${CONTAINER} sh

psql:
	docker exec -it db psql -U postgres -d app

make_revision:
	alembic revision --autogenerate -m "$(m)"

