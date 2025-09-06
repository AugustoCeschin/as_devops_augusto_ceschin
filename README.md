# as_devops_augusto_ceschin

Repositório criado para a disciplina de **DevOps** no curso de Análise e Desenvolvimento de Sistemas.  
O projeto tem caráter **acadêmico** e serve como base para a realização das atividades formativas e somativas da disciplina.

## Objetivo

O repositório será utilizado para:

- Relembrar conceitos básicos de **Python** e suas configurações iniciais (virtual environment, dependências e execução local).
- Exercitar o uso do **GitHub** e suas funcionalidades (branches, commits, pull requests, GitHub Actions).

## Status Atual

Neste momento, o foco está na configuração inicial do projeto em **Python**, criando um ambiente simples que permita rodar o código localmente e realizar requisições de teste.

## Tecnologias

- Python 3.12
- FastAPI
- Uvicorn

## Como executar localmente

1. Criar e ativar o ambiente virtual:
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1

2. Instalar dependências:
  pip install -r requirements.txt 

3. Executar o servidor FastAPI:
  A aplicação estará disponível em:
  http://127.0.0.1:8000

## ⚠️ Observação

*Este repositório é voltado exclusivamente para fins acadêmicos e de aprendizagem. O foco principal é compreender práticas de versionamento com GitHub, integração contínua (CI), entrega contínua (CD) e, em etapas posteriores, a dockerização da aplicação.*