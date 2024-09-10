# API Gerenciamento de Usuários - Backend Python com Flask

Este projeto é uma aplicação backend de gerenciamento de usuários desenvolvida com Flask. O aplicativo permite adicionar, buscar, editar e deletar usuários utilizando uma API RESTful.

## Como executar

Certifique-se de que o código do projeto esteja disponível no novo computador. Você pode fazer isso clonando o repositório do GitHub ou baixando os arquivos.  
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo, será necessário ter todas as libs python listadas no requirements.txt instaladas.

Siga os passos abaixo para configurar e rodar o projeto em qualquer computador.

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run
(env)$ flask run --host 0.0.0.0 --port 5000
```
