# Sabor Express

Este repositório abriga o código de um trabalho prático da disciplina **Engenharia de Software II**, cursada por mim no curso de Sistemas de Informação da UFVJM. O projeto simula o funcionamento de um sistema de pedidos para restaurantes e foi desenvolvido com o propósito de aplicar conceitos de modelagem, organização de código e testes unitários estudados ao longo da matéria.

# Sobre o projeto

O Sabor Express é uma aplicação em Python que permite listar restaurantes, exibir os itens de seus cardápios, calcular preços de pedidos (com ou sem desconto) e registrar avaliações dos clientes. Toda a lógica de negócio está organizada em classes dentro do pacote `components`, separando responsabilidades como itens de cardápio (`Prato`, `Bebida`, `Sobremesa`), manipulação de restaurantes (`Restaurante`, `Restaurantes`) e a interface principal (`SaborExpress`). O arquivo `client_app.py` serve apenas como ponto de entrada para a versão em linha de comando.

# Estrutura do código

O diretório do projeto é organizado da seguinte forma:
- `components/`: contém os módulos de negócios. Inclui subpacotes para itens de cardápio e classes responsáveis por restaurantes.
- `data/`: guarda o arquivo `restaurants_db.json` com dados de exemplo usados pela aplicação.
- `tests/`: reúne a suíte de testes unitários escrita com pytest, bem como fixtures reutilizáveis para construção dos objetos de teste. Cada classe principal possui um arquivo de teste próprio para facilitar a manutenção.
- `client_app.py`: executa a aplicação no terminal.

# Requisitos
- Python 3.10 ou superior.
- O projeto não depende de bibliotecas externas para a execução da aplicação. Para executar a suíte de testes é necessário instalar o pacote `pytest` (`pip install pytest`).

# Como executar a aplicação

1. Clone este repositório ou faça o download dos arquivos.
2. No terminal, acesse a pasta `sabor-express`.
3. Execute o comando:
```bash
python client_app.py
```
4. O programa exibirá um menu de restaurantes disponíveis, permitirá escolher um item do cardápio, aplicar desconto e registrar uma avaliação ao final do pedido.

# Executando os testes

Para validar o comportamento das classes, utilize a suíte de testes localizada no diretório tests. Cada arquivo de teste corresponde a uma classe da aplicação. Para executar todos os testes:
```bash
pytest
```

Os testes criam instâncias a partir de fixtures sem depender de entrada de usuário real e verificam cenários como aplicação de descontos, normalização de dados, alternância de estados e cálculo de médias de avaliações.
