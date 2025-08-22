<<<<<<< HEAD
# API Sistema de Fichas

API completa para gerenciamento de sistema de fichas de produção, incluindo clientes, pedidos, pagamentos e envios.
=======
# API SGP - Sistema de Gestão de Pacientes

API RESTful desenvolvida com FastAPI para o agendamento de consultas e gestão de pacientes no setor de saúde.

## 🚀 Funcionalidades

- **Clientes**: Cadastro e gerenciamento de pacientes.
- **Consultas**: Agendamento e visualização de compromissos médicos.
- **Envios**: Tipos de envio disponíveis para notificações.
- **Pagamentos**: Métodos de pagamento para serviços médicos.

## 🛠 Tecnologias Utilizadas

- **Backend**: FastAPI
- **Banco de Dados**: SQLModel com SQLite
- **ORM**: SQLAlchemy
- **Testes**: pytest, FastAPI TestClient
- **Documentação**: Swagger UI integrada

## 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/finderbit1/api-sgp.git
   cd api-sgp
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Execução

Para rodar a aplicação localmente:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Acesse a documentação interativa em: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🧪 Testes

Para rodar os testes automatizados:

```bash
pytest
```

## 📚 Estrutura de Diretórios

```
api-sgp/
├── clientes/          # Endpoints e modelos de clientes
├── consultas/         # Endpoints e modelos de consultas
├── envios/            # Tipos de envio
├── pagamentos/        # Métodos de pagamento
├── database/          # Configuração do banco de dados
├── tests/             # Testes automatizados
├── main.py            # Ponto de entrada da aplicação
├── models.py          # Definições dos modelos de dados
├── base.py            # Configurações base
├── requirements.txt   # Dependências do projeto
└── README.md          # Este arquivo
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## 📞 Contato

Para dúvidas ou contribuições, entre em contato através do [GitHub Issues](https://github.com/finderbit1/api-sgp/issues) ou envie um e-mail para [mateuspython3010@gmail.com](mailto:mateuspython3010@gmail.com).
>>>>>>> a90dc900978f6f3f20e86eeb5346dfb5c748d938

## 🚀 Funcionalidades

- **Clientes**: CRUD completo para gerenciamento de clientes
- **Pedidos**: CRUD completo para fichas de pedidos
- **Pagamentos**: CRUD completo para tipos de pagamento
- **Envios**: CRUD completo para tipos de envio
- **Admin**: CRUD completo para usuários administradores
- **Produção**: Sistema de itens de produção (painéis, totens, lonas)

## 🛠️ Tecnologias

- **FastAPI**: Framework web moderno e rápido
- **SQLModel**: ORM moderno baseado em Pydantic e SQLAlchemy
- **SQLite**: Banco de dados (configurável para outros)
- **Pydantic**: Validação de dados
- **Python 3.13+**: Linguagem de programação

## 📋 Pré-requisitos

- Python 3.13 ou superior
- uv (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd api-sistemas-fichas
```

2. Instale as dependências:
```bash
uv sync
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

4. Execute a aplicação:
```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📚 Endpoints da API

### Clientes
- `POST /api/v1/clientes/` - Criar cliente
- `GET /api/v1/clientes/` - Listar clientes
- `GET /api/v1/clientes/{id}` - Obter cliente específico
- `PATCH /api/v1/clientes/{id}` - Atualizar cliente
- `DELETE /api/v1/clientes/{id}` - Deletar cliente

### Pedidos
- `POST /api/v1/pedidos/` - Criar pedido
- `GET /api/v1/pedidos/` - Listar pedidos
- `GET /api/v1/pedidos/{id}` - Obter pedido específico
- `PATCH /api/v1/pedidos/{id}` - Atualizar pedido
- `DELETE /api/v1/pedidos/{id}` - Deletar pedido

### Pagamentos
- `POST /api/v1/tipos-pagamentos/` - Criar tipo de pagamento
- `GET /api/v1/tipos-pagamentos/` - Listar tipos de pagamento
- `GET /api/v1/tipos-pagamentos/{id}` - Obter tipo específico
- `PATCH /api/v1/tipos-pagamentos/{id}` - Atualizar tipo
- `DELETE /api/v1/tipos-pagamentos/{id}` - Deletar tipo

### Envios
- `POST /api/v1/tipos-envios/` - Criar tipo de envio
- `GET /api/v1/tipos-envios/` - Listar tipos de envio
- `GET /api/v1/tipos-envios/{id}` - Obter tipo específico
- `PATCH /api/v1/tipos-envios/{id}` - Atualizar tipo
- `DELETE /api/v1/tipos-envios/{id}` - Deletar tipo

### Admin
- `POST /api/v1/admin/users/` - Criar usuário
- `GET /api/v1/admin/users/` - Listar usuários
- `GET /api/v1/admin/users/{id}` - Obter usuário específico
- `PATCH /api/v1/admin/users/{id}` - Atualizar usuário
- `DELETE /api/v1/admin/users/{id}` - Deletar usuário

## 📖 Documentação da API

Após executar a aplicação, acesse:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testes

Execute os testes com:
```bash
uv run pytest
```

## 📁 Estrutura do Projeto

```
api-sistemas-fichas/
├── admin/           # Módulo de administração
├── clientes/        # Módulo de clientes
├── database/        # Configurações de banco
├── envios/          # Módulo de tipos de envio
├── pagamentos/      # Módulo de tipos de pagamento
├── pedidos/         # Módulo de pedidos
├── tests/           # Testes automatizados
├── main.py          # Arquivo principal da aplicação
├── models.py        # Modelos do banco de dados
├── base.py          # Configurações base
├── config.py        # Configurações centralizadas
└── producoes.py     # Modelos de produção
```

## 🔒 Segurança

- Configure adequadamente as variáveis de ambiente
- Em produção, restrinja o CORS para domínios específicos
- Gere uma chave secreta única para produção
- Implemente autenticação JWT (próximas versões)

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.
