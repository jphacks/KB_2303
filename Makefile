install:
	docker compose run --rm client npm i

add:
	docker compose run --rm client npm i ${PKGS}

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

ps:
	docker compose ps

log:
	docker compose logs -f

generate:
	docker compose run --rm client npm run generate-component
	
build:
	docker compose run --rm client npm run build
revision:
	 docker compose exec server /bin/bash -c "cd /db && alembic revision --autogenerate -m '${NAME}'"

migrate:
	 docker compose exec server /bin/bash -c "cd /db && alembic upgrade head"
