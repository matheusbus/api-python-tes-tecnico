# Teste técnico - API Python

Este é um teste técnico que foi desenvolvido para testar meus conhecimentos em Python e SQL.

### :large_orange_diamond: Descrição do problema
Uma Organização possui um cadastro de empresas clientes. Cada empresa possui dados provenientes da Receita Federal (RF) e outros que são manualmente inseridos pelo usuário. Para criar uma nova empresa na base, o usuário informa o identificador do Cadastro Nacional de Pessoas Jurídicas (CNPJ) e o sistema busca os dados necessários na RF. Após a inserção da empresa no Banco de Dados, o usuário pode alterar dados como Número de Funcionários, Faturamento Anual Estimado e o nome de um Vendedor Responsável.
Os vendedores nessa Organização devem ter acesso a uma consulta que retorna os seguintes dados das empresa: CNPJ, Situação (Ativa/Inativa), Tipo (Matriz/Filial), Razão Social, Nome Fantasia, Estado, Município, Endereço, Natureza Jurídica, Porte, Atividade Principal, Telefone, Número de Funcionários, Faturamento Anual Estimado e o Vendedor Responsável. Nessa consulta, o usuário pode ver todas as empresas cadastradas ou filtrar de acordo com o nome de um vendedor.

---

### :large_orange_diamond: Pré-requisitos para execução
Antes de iniciar, você deve possuir:

- Python: você pode instalar a partir de https://www.python.org/
- Node: você pode obter a partir de https://nodejs.org/en
- Npm: você pode baixar a partir de https://www.npmjs.com/
- Bibliotecas e Dependências do projeto (detalhados abaixo)

---

### :large_orange_diamond: Stack de tecnologia
- Python: linguagem de programação utilizada no back-end (API).
- Django: framework python para desenvolvimento web.
- SQLite: banco utilizado no back-end para armazenar os dados.
- HTML, CSS e JavaScript: utilizado para desenvolvimento dos templates das interfaces gráficas.
- Vue.js: framework front-end utilizado para desenvolvimento das interfaces gráficas do client para consumo da API.

---

### :large_orange_diamond: Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/matheusbus/api-python-tes-tecnico.git
   ```

### :large_orange_diamond: Execução da API:
1. Mova para o diretório da API:
   ```bash
   cd api
   ```
2. Entre no ambiente virtual:
   Windows:
   ```bash
   venv\Scripts\activate
   ```
   MacOS e Linux:
   ```bash
   source venv/bin/activate
   ```
4. Executar a instalação das dependências e em seguida as migrações do Django:
   ```bash
   pip install requests
   pip install django
   pip install djangorestframework
   pip install django-cors-headers
   
   python manage.py migrate
   ```
5. Iniciar o servidor em desenvolvimento:
   ```bash
   python manage.py runserver
   ```
6. URL da API: [http://localhost:8000/api/clientes](http://localhost:8000/api/clientes/)

---

### :large_orange_diamond: Execução da aplicação fron-end:
1. Mova para o diretório da aplicação:
   ```bash
   cd ..
   cd front/carteira-clientes
   ```
2. Instalar as dependências do projeto:
   ```bash
   npm install
   ```
3. Iniciar o servidor em desenvolvimento:
   ```bash
   npm run dev
   ```
5. Acessar via navegador: http://localhost:5173
