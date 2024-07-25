kill_previous_service() {
    systemctl stop myportfolio || { printf "Failed to stop myportfolio service.\n" >&2; return 1; }
}

navigate_to_project_directory() {
    cd /root/MLH-Portfolio || { printf "Project directory /root/MLH-Portfolio not found.\n" >&2; return 1; }
}

update_git_repository() {
    git fetch && git reset origin/main --hard || { printf "Git fetch or reset failed.\n" >&2; return 1; }
}

activate_virtualenv() {
    source python3-virtualenv/bin/activate || { printf "Virtual environment activation failed.\n" >&2; return 1; }
}

install_dependencies() {
    pip install -r requirements.txt || { printf "Pip install failed.\n" >&2; return 1; }
}

restart_service() {
    systemctl daemon-reload || { printf "Failed to reload systemd manager configuration.\n" >&2; return 1; }
    systemctl restart myportfolio || { printf "Failed to restart myportfolio service.\n" >&2; return 1; }
}

main() {
    kill_previous_service || exit 1
    navigate_to_project_directory || exit 1
    update_git_repository || exit 1
    activate_virtualenv || exit 1
    install_dependencies || exit 1
    restart_service || exit 1
    printf "Deployment script executed successfully.\n"
}

main "$@"