# API Sistema de Fichas

API completa para gerenciamento de sistema de fichas de produção, incluindo clientes, pedidos, pagamentos e envios.

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
