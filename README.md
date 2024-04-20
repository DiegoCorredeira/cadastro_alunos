

## Pagamentos de Clientes

Este é um aplicativo simples de registro de vendas que permite adicionar informações sobre vendas de produtos de clientes, armazenando-as em um banco de dados SQLite e exibindo os registros na interface gráfica do usuário (GUI) usando a biblioteca Tkinter em Python.

### Funcionalidades:

1. **Adicionar Venda:**
   - Preencha os campos para adicionar uma nova venda.
   - Campos obrigatórios: Nome do cliente, Quantidade adquirida, Saldo devedor do cliente, Data da venda e Data do pagamento.
   - Opção para marcar se o pagamento foi realizado.

2. **Exibir Clientes:**
   - Exibe todas as vendas registradas no banco de dados.
   - Mostra detalhes como nome do cliente, quantidade adquirida, saldo devedor, datas de venda e pagamento, e se o pagamento foi feito ou não.

### Estrutura do Código:

- **create_table():**
  - Função para criar a tabela 'vendas' no banco de dados se ainda não existir.

- **add_venda():**
  - Função para adicionar uma nova venda ao banco de dados.
  - Valida se todos os campos obrigatórios foram preenchidos.
  - Limpa os campos de entrada após adicionar a venda.

- **vendas_output():**
  - Função para exibir todas as vendas registradas no banco de dados na área de texto da GUI.
  - Recupera todas as vendas do banco de dados e as exibe formatadas.

### Componentes da Interface:

- **Labels:**
  - Rótulos para os campos de entrada na GUI, indicando o que cada campo representa.

- **Campos de Entrada:**
  - Entradas de texto para inserir informações sobre a venda, como nome do cliente, quantidade adquirida, saldo devedor, etc.

- **Botões:**
  - 'Adicionar Venda': Executa a função add_venda() para adicionar uma nova venda.
  - 'Exibir Clientes': Executa a função vendas_output() para exibir todas as vendas registradas.
  
- **Checkbox:**
  - Para indicar se o pagamento foi feito ou não.

- **Status Label:**
  - Exibe mensagens de status após adicionar uma venda ou ao realizar outras operações.

- **Área de Texto:**
  - Onde os detalhes das vendas são exibidos após selecionar "Exibir Clientes".

### Dependências:

- Python 3.x
- Tkinter
- SQLite3

### Como Executar:

1. Certifique-se de ter as dependências instaladas.
2. Execute o script Python.
3. Insira os detalhes da venda nos campos de entrada e clique em "Adicionar Venda" para adicionar uma nova venda.
4. Clique em "Exibir Clientes" para ver todas as vendas registradas.
