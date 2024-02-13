#!/bin/bash

REMOTE_HOST="iv.krak.fvds.ru"
#read -p "Enter your host: " REMOTE_HOST
REMOTE_USER="root"
PROJECT_DIR="$(basename $PWD)"
EXCLUDE_STRING=" --exclude .venv --exclude .git --exclude .idea --exclude .vscode"

rsync -avz --delete --filter='- __pycache__/' -e "ssh" $EXCLUDE_STRING $PWD $REMOTE_USER@$REMOTE_HOST:/root/programming

SSH_COMMAND="ssh $REMOTE_USER@$REMOTE_HOST"

$SSH_COMMAND "cd /root/programming/$PROJECT_DIR && docker-compose up --build -d"
