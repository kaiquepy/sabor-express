# Documentação dos testes unitários para o projeto Sabor Express

## Introdução

O objetivo desta atividade foi estudar o repositório **Sabor Express** e elaborar
uma bateria de testes unitários utilizando o framework **pytest**. A
aplicação simula um sistema de pedidos em restaurantes e possui classes
representando itens de cardápio, restaurantes individuais, uma coleção de
restaurantes e a interface principal. A seguir descrevo, em língua
portuguesa, os testes planejados e implementados para cada componente da
aplicação. Os dados necessários para as instâncias de teste foram
concentrados em *fixtures*, conforme recomendado, permitindo reutilização e
isolamento de contexto.

## Descrição geral dos testes

Para cada classe principal da aplicação foi criado um arquivo de teste
independente dentro do diretório `tests`. Os casos de teste têm como
objetivo garantir que:

- As funcionalidades centrais de cada classe comportem‑se de forma
  determinística, mesmo quando confrontadas com entradas variadas.
- Os atributos sejam inicializados e atualizados corretamente, sem
  dependência de interações do usuário.
- As operações de leitura e escrita em arquivos ocorram de forma segura
  quando aplicável.

Nos parágrafos subsequentes, detalho os testes por classe e seus
respectivos comportamentos verificados.

## Testes das classes de cardápio (`Prato`, `Bebida` e `Sobremesa`)

Cada item de cardápio herda de `ItemCardapio` e implementa um método
`aplicar_desconto` com percentuais distintos. Para cada classe foi
criado um arquivo de teste individual para que ficasse claro o escopo
dos testes:

- **Prato** (`test_prato.py`): um teste garante que a conversão para
  `str` devolve apenas o nome do prato e outro confirma que o método
  `aplicar_desconto` reduz o preço em 5%.
- **Bebida** (`test_bebida.py`): de forma análoga, o teste de `str` retorna
  o nome da bebida e `aplicar_desconto` reduz o preço em 8%.
- **Sobremesa** (`test_sobremesa.py`): testa‑se a conversão para
  string e a aplicação de um desconto de 15%.

As instâncias para esses testes são fornecidas por fixtures
(`prato_fixture`, `bebida_fixture` e `sobremesa_fixture`) que criam
itens de cardápio com valores controlados para nome e preço.

## Testes da classe `Restaurante`

A classe `Restaurante` centraliza um conjunto de informações sobre um
estabelecimento e provê métodos para processar seu cardápio, alternar
estado, calcular a média das avaliações e adicionar novos itens. Os
testes implementados cobrem os seguintes aspectos:

- **Normalização de dados**: no construtor, o nome é padronizado com
  `title()` e a categoria em maiúsculas. O teste cria um restaurante
  com letras minúsculas e confere se `_nome` e `_categoria` são
  normalizados.
- **Processamento do cardápio**: a partir da lista de dicionários
  recebida, o método interno `processar_cardapio` deve instanciar
  objetos `Prato`, `Bebida` ou `Sobremesa` conforme o tipo informado.
  O teste verifica se os três itens do cardápio de exemplo são
  convertidos nos tipos corretos e na ordem esperada.
- **Alternância de estado**: inicialmente o restaurante está inativo
  (propriedade `ativo` retorna “❌”). Após uma chamada a
  `alternar_estado`, deve ficar ativo (“✅”). Uma segunda chamada
  retorna ao estado inicial. O teste cobre essa alternância.
- **Cálculo da média das avaliações**: ao adicionar uma nova nota à
  lista de avaliações individuais, o método `calcular_media_avaliacoes`
  deve recalcular a média corretamente. O teste insere uma nova nota
  (5) a uma lista com média 4 e verifica se a nova média é 4,5.
- **Adição ao cardápio**: chamar `adicionar_no_cardapio` com um
  objeto que herda de `ItemCardapio` deve aumentar o tamanho da lista
  `_cardapio`, enquanto a passagem de um tipo incorreto deve ser
  ignorada. O teste insere uma nova instância de `Prato` e confere
  que o cardápio aumenta de tamanho; em seguida tenta adicionar um
  inteiro e garante que a lista não cresce.

## Testes da classe `Restaurantes`

A classe `Restaurantes` atua como um contêiner para múltiplos
restaurantes. Ela recebe um dicionário com a chave `restaurants` e
gera uma lista de objetos `Restaurante`. Dois testes foram escritos:

- **Lista vazia**: se a lista recebida estiver vazia, a propriedade
  `_lista_de_restaurantes` deve ser uma lista vazia.

## Tabela resumida dos testes

| Componente | Teste | Fixtures/Mocks | Resultado esperado |
|-----------|------|----------------|-------------------|
| `Prato` | `__str__` retorna o nome do prato. | `prato_fixture` | A função `str(prato)` devolve “Feijoada”. |
| `Prato` | `aplicar_desconto` reduz o preço em 5%. | `prato_fixture` | O preço passa de 100,0 para 95,0. |
| `Bebida` | `__str__` retorna o nome da bebida. | `bebida_fixture` | `str(bebida)` devolve “Suco”. |
| `Bebida` | `aplicar_desconto` reduz o preço em 8%. | `bebida_fixture` | O preço passa de 50,0 para 46,0. |
| `Sobremesa` | `__str__` retorna o nome da sobremesa. | `sobremesa_fixture` | `str(sobremesa)` devolve “Sorvete”. |
| `Sobremesa` | `aplicar_desconto` reduz o preço em 15%. | `sobremesa_fixture` | O preço passa de 80,0 para 68,0. |
| `Restaurante` | Normalização de nome e categoria no construtor. | `restaurante_data_fixture` | `_nome` recebe `title()` e `_categoria` é convertida para maiúsculas. |
| `Restaurante` | Processamento do cardápio em objetos concretos. | `restaurante_fixture` | `_cardapio` contém um `Prato`, uma `Bebida` e uma `Sobremesa` nesta ordem. |
| `Restaurante` | Alternar estado ativo/inativo. | `restaurante_fixture` | A propriedade `ativo` alterna entre “❌” e “✅”. |
| `Restaurante` | Recalcular média após nova avaliação. | `restaurante_fixture` | Após adicionar uma nota 5 a média passa a 4,5. |
| `Restaurante` | Adicionar item ao cardápio e ignorar tipos inválidos. | `restaurante_fixture` | Tamanho do cardápio aumenta com item válido e permanece igual com tipo inválido. |
| `Restaurantes` | Tratar lista vazia. | Dicionário vazio criado no próprio teste. | `_lista_de_restaurantes` torna‑se uma lista vazia. |

## Considerações finais

Os testes descritos acima cobrem as principais rotas de execução da
aplicação Sabor Express em nível unitário. A utilização de fixtures
facilitou a criação de objetos reutilizáveis e permitiu testar os
métodos sem dependência de arquivos reais ou entrada de usuário. A
organização de um arquivo de teste por classe mantém o código
modularizado e facilita a manutenção futura. Para executar toda a
bateria de testes basta posicionar‑se no diretório `sabor-express/tests`
e rodar o comando `pytest` (após instalar o pacote `pytest`).
