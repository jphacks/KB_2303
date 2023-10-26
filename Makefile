install:
	docker compose run --rm client npm i

add:
	docker compose run --rm client npm i ${PKGS}

up:
	docker compose up -d

down:
	docker compose down

ps:
	docker compose ps

log:
	docker compose logs -f