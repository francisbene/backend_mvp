# Gerenciamento de Usuários - Backend com Flask

Este projeto é uma aplicação backend de gerenciamento de usuários desenvolvida com Flask. O aplicativo permite adicionar, buscar, editar e deletar usuários utilizando uma API RESTful.

## Passos para Rodar o App em Outro Computador

Siga os passos abaixo para configurar e rodar o projeto em qualquer computador.

### 1. Clone ou Baixe o Projeto

Certifique-se de que o código do projeto esteja disponível no novo computador. Você pode fazer isso clonando o repositório do GitHub ou baixando os arquivos.

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

### 2. Instale Python e Pip

Verifique se o Python e o gerenciador de pacotes pip estão instalados na máquina de destino, para isso execute os seguintes comandos:

```bash
python --version
pip --version

Se não estiverem instalados, baixe o Python do site oficial e siga as instruções de instalação para o seu sistema operacional.

### 3. Crie um Ambiente Virtual

No diretório do projeto, crie um ambiente virtual para garantir que todas as dependências do Python sejam isoladas:

```bash
python -m venv venv

#### Windows: Ative o ambiente virtual com o comando:
```bash
venv\Scripts\activate

#### Linux/MacOS: Ative o ambiente virtual com o comando:
```bash
source venv/bin/activate

### 4. Instale as Dependências

Utilize o arquivo requirements.txt para instalar todas as bibliotecas necessárias para o projeto:

```bash
pip install -r requirements.txt

### 5. Execute o Servidor Flask

Com todas as dependências instaladas e o ambiente configurado, você pode iniciar o servidor Flask:

```bash
flask run
