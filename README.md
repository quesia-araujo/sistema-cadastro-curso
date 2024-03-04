# Plataforma restfull de cursos online

## Sobre o projeto

Este projeto é um sistema de cadastro de cursos implementado em `python`, usando o framework `django` e testado com `pytest` e `postman`, desenvolvido com o intuitode realizar o gerenciamento de cursos online para uma empresa de cursos que oferece diversas opções de aprendizado. O sistema permite que a empresa gerencie os cursos oferecidos na parte administrativa, além de possibilitar a conexão através de outras plataformas para o cadastro de novos cursos e visualização.

### Comandos executados apenas na primeira vez:

#### Instalação do ambiente virtual

    pip install virtualenv

#### Criação do ambiente virtual

    python -m  venv .venv

#### Instalação do Django\_\_

    pip install django

### Comandos para modificar o projeto

#### Ativação do ambiente virtual

    .venv/Scripts/ativate

#### Comando para criação de um projeto django

    django-admin startproject nome_do_projeto .

#### Comando para rodar um projeto django

    python  manage.py  runserver

#### Comando para criação de um app

    python manage.py startapp base
