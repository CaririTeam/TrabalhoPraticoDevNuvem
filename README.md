# Projeto Docker Compose com Aplicação Web e Banco de Dados na Nuvem

Este projeto consiste na implementação de uma aplicação web e um banco de dados em containers Docker, utilizando o **docker-compose** para orquestrar os serviços. A aplicação web faz uma consulta a um banco de dados e exibe o resultado em uma página web. Este exemplo é baseado no nosso Projeto Integrado (PI), utilizando uma abordagem simplificada.

## Equipe

- **Francisco Eudo da Silva** - Matrícula: 2023011967
- **Gabriel Vasconcelos Andrade da Silva** - Matrícula: 2023009898
- **Wagner Fernando Lavandoski Padilha** - Matrícula: 2023012089

## Descrição do Projeto

O projeto é composto por dois serviços principais:

1. **Serviço 1: Aplicação Web**
   - Desenvolvido com **Flask**.
   - A rota padrão da aplicação (`/`) faz uma consulta ao banco de dados e exibe o resultado em formato HTML.
   - A consulta recupera dados de uma tabela que contém pelo menos três linhas de informações.
  
2. **Serviço 2: Banco de Dados**
   - O banco de dados utilizado é **MySQL**.
   - Contém uma tabela com pelo menos três registros de dados, representando uma parte simplificada do projeto de PI da equipe.

## Pré-requisitos

- Conta na **AWS** para configurar a instância EC2.
- **Docker** e **docker-compose** instalados na instância EC2.
- Chave SSH configurada para acesso à instância EC2.

## Estrutura do Projeto

- **`app/app.py`:** Contém o código principal da aplicação Flask, incluindo as rotas e a lógica para interagir com o banco de dados.
- **`app/Dockerfile`:** Especifica como a imagem Docker para a aplicação Flask será construída.
- **`app/requirements.txt`:** Lista as dependências necessárias para rodar a aplicação Flask.
- **`app/templates/`:** Diretório contendo os arquivos HTML usados pela aplicação.
  - **`home.html`:** Página inicial da aplicação.
  - **`add_employee.html`:** Formulário para adicionar um novo empregado ao banco de dados.
  - **`employee_data.html`:** Exibe os dados dos empregados cadastrados.
- **`db/init.sql`:** Script SQL para criar a tabela no banco de dados e inserir dados iniciais.
- **`docker-compose.yml`:** Arquivo de configuração do Docker Compose, que define os serviços da aplicação web e do banco de dados.
- **`README`:** Este arquivo.

  ## Como Executar o Projeto

### 1. Configurar a Instância EC2

Conecte-se à sua instância EC2 via SSH utilizando a chave SSH configurada.
```bash
ssh -i "sua-chave.pem" ubuntu@<IP-da-instancia>
```
Obs: em alguns SO talvez seja necessário inserir /o/caminho/completo/da/sua/chave.pem em "sua-chave.pem".

### 2. Clonar o Repositório

Clone este repositório na instância EC2.

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```
### 3. Subir os Serviços com Docker Compose

Execute o comando abaixo para iniciar a aplicação e o banco de dados dentro do repositório do projeto, caso não tenha feito o passo 2 completamente.

```bash
sudo docker compose up --build -d
```
### 4. Verificar o Status dos Containers

Após executar o docker compose up, você pode verificar se os serviços estão rodando corretamente com o comando:
```bash
docker compose ps
```
Esse comando lista todos os containers e seus estados, permitindo garantir que ambos os serviços estão funcionando como esperado.

### 5. Acessar a Aplicação

Após verificar que os serviços estão rodando, a aplicação web estará acessível através do IP público da instância EC2 no navegador. Utilize o seguinte formato:
```bash
http://<IP-da-instancia>:5000
```
