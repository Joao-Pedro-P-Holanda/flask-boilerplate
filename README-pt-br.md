# Schema Migration com Flask

Este repositório template fornece a estrutura do projeto para configurar uma aplicação web Flask, usando SQLAlchemy, Flask-Migrate, Flask-Marshmallow e Pytest.

As migrações do Alembic são armazenadas na pasta `migrations` por padrão.

Este projeto foi inspirado e segue a mesma estrutura de outro exemplo feito pelo youtuber Eduardo Mendes. Meu objetivo é expandir com configurações mais avançadas, incluindo Docker e CI/CD.

[Video original](https://youtu.be/WzaKIRJBGXo)

[Canal do Eduardo no youtube](https://www.youtube.com/@Dunossauro)

[Repositório dele](https://github.com/dunossauro/crudzin)

## Estrutura do Projeto

Este template contém uma aplicação Flask, definida como um pacote no arquivo **init**.py, a função _create_app_ atua como uma \_application_factory\* e é detectada automaticamente quando `flask run` é executado (consulte o [tutorial do Flask](https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/) para mais detalhes).

Todas as tabelas do banco de dados são expressas como classes no arquivo models.py, a função para configurar o banco de dados também é definida neste arquivo.

serializer.py contém os esquemas do Marshmallow para serializar cada modelo.

hello_world.py define uma blueprint, que contém suas próprias rotas que podem ser registradas no aplicativo.

Por fim, o HTML que é renderizado na rota inicial está incluído na pasta templates.

## Configurar o projeto

### 1. Definir a variável de ambiente `DATABASE_URI`

- #### Linux

```shell
export DATABASE_URI="uri_do_banco"
```

- #### Windows

```cmd
setx DATABASE_URI="uri_do_banco"
```

### Instalar dependências

```shell
pip install -r dev_requirements.txt
```

### Inicializar a aplicação em modo de desenvolvimento

`flask run --debug`

## TODO

- [ ] Containerizar a aplicação
- [ ] Configurar o dependabot
- [ ] Criar workflow do actions para migrações
- [ ] Configurar logging da aplicação
- [ ] Estilizar a página de hello
