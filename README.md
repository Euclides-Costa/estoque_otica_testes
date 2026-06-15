# Gerenciamento de Estoque para Óticas

Projeto com objetivo desenvolver um sistema de estoque, aplicando técnicas de teste de software aprendidas na disciplina de Teste de Software.

Este repositório contém a lógica de negócios central, a persistência de dados em ambiente relacional e uma suíte automatizada de testes unitários e de integração.

---

## Funcionalidades Principais

* **Cadastro de Produtos (RF01):** Catalogação detalhada de itens com atributos específicos do setor óptico (SKU, marca, modelo, cor, material e dados de validade/lote para lentes).
* **Entrada e Rastreabilidade de Estoque (RF03):** Incremento de mercadorias integrado a um histórico de auditoria que registra o responsável (usuário) e a justificativa da movimentação.
* **Autenticação de Usuários (RF05):** Controle de acesso seguro utilizando criptografia de ponta a ponta para senhas via hash (`bcrypt`).

---

## Tecnologias e Ferramentas

* **Linguagem:** Python 3.12+
* **Banco de Dados:** SQLite (embutido)
* **Criptografia:** `bcrypt`
* **Framework de Testes:** `pytest` (v9.0+)

---

## Estrutura do Projeto

```text
estoque_otica_testes/
│
├── database/                    # Armazenamento do arquivo físico do banco de dados (ex: banco.db)
│
├── src/                         # Código-fonte da aplicação
│   ├── __init__.py
│   ├── autenticacao.py          # Gerenciamento de sessões, usuários e login seguro
│   ├── banco.py                 # Conexão, criação de tabelas e persistência (SQLite)
│   ├── estoque.py               # Regras de negócio para controle e fluxo de produtos
│   ├── fornecedor.py            # Entidade e regras para gerenciamento de fornecedores
│   ├── movimentacao.py          # Registro e lógica de histórico de entradas/saídas
│   ├── produto.py               # Domínio, atributos e validações do produto
│   ├── sistema.py               # Orquestrador principal / Interface de integração dos módulos
│   └── utils.py                 # Funções utilitárias (conversão de dados e formatos)
│
├── tests/                       # Suíte de testes automatizados
│   ├── conftest.py              # Configurações globais, injeção de paths e fixtures do pytest
│   ├── test_autenticacao.py     # Testes unitários do fluxo de login com uso de Mocks
│   ├── test_integracao_estoque.py      # Testes de integração de persistência de produtos
│   ├── test_integracao_movimentacao.py # Testes de integração do histórico de movimentações
│   ├── test_produto.py          # Testes unitários parametrizados das regras do produto
│   └── test_utils.py            # Testes unitários das funções de conversão
│
├── pytest.ini                   # Configurações de ambiente e pythonpath do Pytest
└── README.md                    # Documentação técnica do projeto
