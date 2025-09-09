#!/bin/bash

# Configurações
GITHUB_USER="krebinha"                # Seu usuário GitHub
PROJECT_NAME=$(basename "$PWD")       # Nome da pasta atual como nome do repositório
BRANCH_NAME="main"                     # Branch padrão

# Função para criar repositório no GitHub via API
create_github_repo() {
    echo "Criando repositório $PROJECT_NAME no GitHub..."
    
    # Você precisa gerar um token GitHub com permissão 'repo'
    # Coloque seu token abaixo ou use variável de ambiente GITHUB_TOKEN
    TOKEN=${GITHUB_TOKEN:-"SEU_TOKEN_AQUI"}

    curl -s -H "Authorization: token $TOKEN" \
         -d "{\"name\":\"$PROJECT_NAME\"}" \
         https://api.github.com/user/repos
}

# Inicializa git se necessário
if [ ! -d ".git" ]; then
    echo "Inicializando repositório git..."
    git init
fi

# Adiciona todos os arquivos e faz commit inicial
git add .
git commit -m "Initial commit" 2>/dev/null || echo "Commit já existe"

# Renomeia branch atual para main
git branch -M $BRANCH_NAME

# Configura remoto SSH
REMOTE_URL="git@github.com:$GITHUB_USER/$PROJECT_NAME.git"
git remote remove origin 2>/dev/null
git remote add origin $REMOTE_URL

# Cria o repositório no GitHub (ignora erros se já existir)
create_github_repo

# Faz push para o GitHub
git push -u origin $BRANCH_NAME
