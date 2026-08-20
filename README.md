# Sistema Genérico de Gerenciamento de Estoque e Vendas

## Identificação

- **Disciplina:** Organização e Abstração na Programação
- **Trabalho:** Sistema genérico de gerenciamento de estoque e vendas
- **Integrante:** Talysson da Costa
- **Instituição:** Universidade Atitus
- **Professor:** Augusto Ortolan

## Descrição do sistema

Este projeto consiste na proposta e implementação de um sistema genérico para
gerenciamento de produtos, clientes, estoque e vendas. A aplicação foi pensada
para atender diferentes tipos de lojas, sem depender de um segmento específico.

Entre as operações previstas estão:

- cadastro, consulta, alteração e remoção de produtos;
- cadastro e consulta de clientes;
- registro de entradas e saídas do estoque;
- identificação de produtos abaixo do estoque mínimo;
- registro de vendas com um ou mais produtos;
- atualização do estoque após uma venda;
- consulta do histórico de movimentações;
- persistência dos dados para uso posterior.

O sistema ainda está em desenvolvimento. Algumas decisões de implementação e
funcionalidades serão definidas durante a evolução do trabalho.

## Instruções de execução

### Requisitos

- Python 3.10 ou superior;
- Terminal ou IDE compatível com Python.

### Execução

Na pasta raiz do projeto, execute:

```bash
python main.py
```

Caso o sistema passe a utilizar dependências externas, elas serão descritas
nesta seção e em um arquivo de requisitos do projeto.

## Estrutura de diretórios

```text
Projeto/
├── algoritimos/
│   ├── busca_binaria.py
│   └── ordenacao.py
├── data/
│   ├── clientes.csv
│   ├── movimentacoes.csv
│   ├── produtos.csv
│   └── vendas.csv
├── estruturas/
│   ├── fila.py
│   ├── lde.py
│   ├── lse.py
│   ├── nodo.py
│   └── pilha.py
├── models/
│   ├── cliente.py
│   ├── item_venda.py
│   ├── movimentacao_estoque.py
│   ├── produto.py
│   └── venda.py
├── repositories/
│   ├── cliente_repository.py
│   ├── produto_repository.py
│   └── venda_repository.py
├── services/
│   ├── cliente_service.py
│   ├── estoque_service.py
│   ├── persistencia_service.py
│   ├── produto_service.py
│   └── venda_service.py
├── main.py
└── README.md
```

## Tecnologias e conceitos

- Python 3;
- programação orientada a objetos;
- listas encadeadas;
- fila e pilha;
- algoritmos de ordenação e busca;
- persistência em arquivos CSV;
- análise de complexidade computacional.

## Status do projeto

Em desenvolvimento.

