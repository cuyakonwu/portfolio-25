#!/bin/bash

PROJECT_DIR="/root/MLH-Portfolio"
DOCKER_COMPOSE_FILE="docker-compose.prod.yml"

navigate_to_project_directory() {
    cd "$PROJECT_DIR" || { printf "Project directory %s not found.\n" "$PROJECT_DIR" >&2; return 1; }
}

update_git_repository() {
    git fetch && git reset origin/main --hard || { printf "Git fetch or reset failed.\n" >&2; return 1; }
}

docker_compose_down() {
    docker compose -f "$DOCKER_COMPOSE_FILE" down || { printf "Failed to bring down Docker containers.\n" >&2; return 1; }
}

docker_compose_up() {
    docker compose -f "$DOCKER_COMPOSE_FILE" up -d --build || { printf "Failed to bring up Docker containers.\n" >&2; return 1; }
}

main() {
    navigate_to_project_directory || exit 1
    update_git_repository || exit 1
    docker_compose_down || exit 1
    docker_compose_up || exit 1
    printf "Deployment script executed successfully.\n"
}

main "$@"