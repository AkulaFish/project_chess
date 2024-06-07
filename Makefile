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

shell:
	docker exec -it ${CONTAINER} sh

psql:
	docker exec -it db psql -U postgres -d app

al_revision:
	alembic revision --autogenerate -m "$(m)"

al_upgrade:
	alembic upgrade head


