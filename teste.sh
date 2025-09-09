#!/bin/bash

# Configurações
GITHUB_USER="krebinha"                # Seu usuário GitHub
PROJECT_NAME=$(basename "$PWD")       # Nome da pasta atual como nome do repositório
BRANCH_NAME="main"                     # Branch padrão

# Inicializa git se necessário
if [ ! -d ".git" ]; then
    echo "Inicializando repositório git..."
    git init
fi

# Adiciona todos os arquivos e faz commit inicial se ainda não existir
git add .
git commit -m "Initial commit" 2>/dev/null || echo "Commit já existe"

# Renomeia branch atual para main
git branch -M $BRANCH_NAME

# Configura remoto SSH
REMOTE_URL="git@github.com:$GITHUB_USER/$PROJECT_NAME.git"
git remote remove origin 2>/dev/null
git remote add origin $REMOTE_URL

# Faz push para o GitHub (irá criar branch main se repositório já existir)
echo "Fazendo push para $REMOTE_URL..."
git push -u origin $BRANCH_NAME
