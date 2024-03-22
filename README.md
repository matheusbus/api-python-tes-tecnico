# Teste técnico - API Python

Este é um teste técnico que foi desenvolvido para testar meus conhecimentos em Python e SQL.

### Pré-requisitos para execução
Antes de iniciar, você deve possuir:

- Python: você pode instalar a partir de https://www.python.org/
- Node: você pode obter a partir de https://nodejs.org/en
- Npm: você pode baixar a partir de https://www.npmjs.com/
- Bibliotecas e Dependências do projeto (detalhados abaixo)

### Stack de tecnologia
- Python: linguagem de programação utilizada no back-end (API).
- Django: framework python para desenvolvimento web.
- SQLite: banco utilizado no back-end para armazenar os dados.
- HTML, CSS e JavaScript: utilizado para desenvolvimento dos templates das interfaces gráficas.
- Vue.js: framework front-end utilizado para desenvolvimento das interfaces gráficas do client para consumo da API.

### Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/matheusbus/api-python-tes-tecnico.git
   ```

### Execução da API:
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
   pip install django
   pip install djangorestframework
   pip install django-cors-headers
   
   python manage.py migrate
   ```
5. Iniciar o servidor em desenvolvimento:
   ```bash
   python manage.py runserver
   ```

### Execução da aplicação fron-end:
1. Mova para o diretório da aplicação:
   ```bash
   cd ..
   cd front
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
