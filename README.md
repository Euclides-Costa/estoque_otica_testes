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
├── src/                        # Código-fonte da aplicação
│   ├── __init__.py
│   ├── autenticacao.py         # Módulo de login e segurança
│   ├── estoque.py              # Regras de negócio e movimentações
│   ├── produto.py              # Domínio e atributos do produto
│   └── utils.py                # Funções utilitárias (conversão de dados)
│
├── tests/                      # Suíte de testes automatizados
│   ├── conftest.py             # Configurações globais e fixtures do pytest
│   ├── test_autenticacao.py    # Testes unitários com Mock
│   ├── test_integracao_estoque.py
│   ├── test_integracao_movimentacao.py
│   ├── test_produto.py         # Testes unitários parametrizados
│   └── test_utils.py           # Testes unitários de utilitários
│
├── pytest.ini                  # Configurações de ambiente do Pytest
└── README.md                   # Documentação do projeto
