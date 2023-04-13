# API_consultas

Este repositório contém uma API construída com o Django REST Framework, que realiza operações CRUD (Create, Read, Update e Delete) em dois modelos: `PessoaProfissional` e `Consulta`.

## Requisitos

- Python 3.6 ou superior
- Django 3.2 ou superior
- Django REST Framework

## Rodando a aplicação

1. Aplique as migrações do banco de dados:

```bash
python manage.py migrate
```

2. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

3. Acesse a API no navegador ou utilize uma ferramenta como [Postman](https://www.postman.com/) ou [curl](https://curl.se/) para testar as rotas.

Exemplos de rotas:

- `http://localhost:8000/api/pessoas/`: Listar e criar `PessoaProfissional`.
- `http://localhost:8000/api/pessoas/1/`: Recuperar, atualizar e excluir uma pessoa profissional específica pelo ID.
- `http://localhost:8000/api/consultas/`: Listar e criar `Consulta`.
- `http://localhost:8000/api/consultas/1/`: Recuperar, atualizar e excluir uma consulta específica pelo ID.
- `http://localhost:8000/api/consultas/pessoa/1/`: Listar todas as consultas de uma pessoa profissional específica pelo ID.
