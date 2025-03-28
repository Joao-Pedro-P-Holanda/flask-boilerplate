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

1. Definir as variáveis de ambiente 

Você pode utilizar um arquivo `.env` para definir todas as variáveis, ou criá-las para a sua sessão do terminal.

Para gerar uma chave secreta segura você pode utilizar o seguinte comando:

```console
 openssl rand -hex 64
```

Depois escreva no arquivo .env:

```.env
DATABASE_URI="<uri_do_banco>"
SECRET_KEY="<chave_segura>"
```

Ou exporte apenas em uma sessão do terminal:

- **Linux**

```shell
export DATABASE_URI="<uri_do_banco>"
export SECRET_KEY="<chave_segura>"
```

- **Windows**

```cmd
setx DATABASE_URI="<uri_do_banco>"
```

2. Instalar dependências

```shell
pip install -r dev_requirements.txt
```

3. Atualizar o banco para a última migração

`flask db upgrade`

4. Criar seu certificado ssl auto-assinado para o ambiente de desenvolvimento

Para criar seu certificado auto-assinado você pode utilizar o seguinte comando do openssl:

```shell
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 
```

Você pode responder às questões que são feitas com . (para um valor vazio) ou qualquer outro que você prefira, já que serão utilizados apenas no desenvolvimento.

5. Inicializar a aplicação em modo de desenvolvimento

`flask run --debug --cert cert.pem --key key.pem`

## TODO

- [x] Containerizar a aplicação
- [x] Configurar o dependabot
- [ ] Configurar docker compose com Nginx
- [ ] Configurar logging da aplicação
- [ ] Estilizar a página de hello
