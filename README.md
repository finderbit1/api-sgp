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


## Comandos

uvicorn main:app --reload --host 0.0.0.0 --port 8000
