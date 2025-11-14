# Gerencie a fila de espera e atendimento

<!-- toch -->
[Intro](#intro) | [Guide](#guide) | [Answers](#answers) | [Shell](#shell) | [Draft](#draft)
-- | -- | -- | -- | --
<!-- toch -->

![cover](../../.tko/cache/poo/base/budega/cover.jpg)

## Intro

Este é um projeto de modelagem e implementação de um mercantil, que simula o funcionamento de caixas de atendimento e uma fila de espera. Para isso, serão implementadas duas classes principais: Pessoa `Person` e Mercado `Market`.

- A classe `Market` representa o estabelecimento, com atributos como caixas de atendimento `counters` e uma fila de espera de clientes `wainting`.
- Os caixas `counters` são modelados como um vetor de clientes de tamanho fixo. Uma posição do caixa terá o valor `null` para indicar que o caixa está vazio ou terá um objeto cliente.
  - typescript: `counters: (Person | null)[]`
  - java: `ArrayList<Person> counters`
  - cpp: `vector<Person*> counters`
- A fila de espera `queue` é uma lista de clientes de tamanho variável. Todo cliente que chega é inserido no final da fila. Todo cliente que é chamado para um caixa é removido do início da fila.
  - typescript: `waiting: Person[]`
  - java: `LinkedList<Person> waiting`
  - cpp: `list<Person*> waiting`
- As operações principais incluem chegar cliente `arrive`, chamar no caixa `call` e finalizar atendimento `finish`.
- As operações "bônus" são furar fila `cutInLine` e abandonar fila de espera `giveup`.

### Comandos

Todos os comandos seguem o modelo `$comando arg1 arg2 ...`. Em caso de erro, uma mensagem adequada deve ser impressa.

- `$show` - Mostra o estado atual do mercantil, incluindo os clientes nos caixas e na fila de espera.
- `$init` - Reinicia o estado do mercantil, definindo a quantidade de caixas e limpando a fila de espera.
- `$enter` - Adiciona um cliente à fila de espera. Deve ser seguido pelo nome do cliente.
- `$call` - Chama o próximo cliente na fila de espera para um caixa disponível. Deve ser seguido pelo número do caixa.
- `$finish` - Finaliza o atendimento de um cliente em um caixa. Deve ser seguido pelo número do caixa.

## Guide

![diagrama](../../.tko/cache/poo/base/budega/diagrama.png)
[![youtube icon](https://raw.githubusercontent.com/qxcodepoo/arcade/master/base/animal/../youguide.png)](https://youtu.be/5-GqCN0VPpQ?si=SkROsibr5OC4tdnZ)

### Parte 1: Classe Cliente

- 

## Answers

[![_](../../.tko/cache/poo/base/budega/../../wiki/images/resolucao.png)](https://youtu.be/Z7karsbg1ok)

## Shell

```sh
#TEST_CASE iniciar

$init 2
$show
Caixas: [-----, -----]
Espera: []

#TEST_CASE arrive

$arrive carla
$arrive maria
$arrive rubia

$show
Caixas: [-----, -----]
Espera: [carla, maria, rubia]

#TEST_CASE call

$call 0
$show
Caixas: [carla, -----]
Espera: [maria, rubia]

#TEST_CASE finish

$finish 0
$show
Caixas: [-----, -----]
Espera: [maria, rubia]

$end

```

```sh
#TEST_CASE iniciar2

$init 3
$show
Caixas: [-----, -----, -----]
Espera: []

$arrive carla
$arrive maria

$show
Caixas: [-----, -----, -----]
Espera: [carla, maria]

#TEST_CASE call

$call 0
$call 0
fail: caixa ocupado
$show
Caixas: [carla, -----, -----]
Espera: [maria]

#TEST_CASE empty waiting

$call 2
$show
Caixas: [carla, -----, maria]
Espera: []

#TEST_CASE empty waiting

$call 1
fail: sem clientes

#TEST_CASE finish

$finish 0
$show
Caixas: [-----, -----, maria]
Espera: []

$finish 2
$show
Caixas: [-----, -----, -----]
Espera: []

#TEST_CASE error

$finish 3
fail: caixa inexistente
$finish 1
fail: caixa vazio

$end

```

## Draft

<!-- links .cache/draft -->
- cpp
  - [shell.cpp](../../.tko/cache/poo/base/budega/.cache/draft/cpp/shell.cpp)
- go
  - [shell.go](../../.tko/cache/poo/base/budega/.cache/draft/go/shell.go)
- java
  - [Shell.java](../../.tko/cache/poo/base/budega/.cache/draft/java/Shell.java)
- ts
  - [shell.ts](../../.tko/cache/poo/base/budega/.cache/draft/ts/shell.ts)
<!-- links -->

