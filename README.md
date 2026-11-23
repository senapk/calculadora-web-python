# Calculadora web em Python

Projeto de uma calculadora web simples. A interface em HTML envia as operações para um servidor HTTP escrito em Python, que chama as funções matemáticas do módulo `teste.py`.

## Requisitos

- Python 3.10 ou superior

O projeto usa apenas a biblioteca padrão do Python.

## Executar localmente

Na raiz do projeto, execute:

```bash
python3 servidor.py
```

Abra <http://localhost:8000> no navegador. Para encerrar o servidor, use `Ctrl+C`.

## API

O servidor recebe operações por `POST /api/calcular`, em JSON:

```json
{
  "operacao": "multiplicacao",
  "a": 6,
  "b": 7
}
```

As operações aceitas são `soma`, `subtracao`, `multiplicacao` e `divisao`. O resultado é devolvido como JSON; entradas inválidas e divisão por zero retornam erro HTTP 400.

## GitHub Codespaces

O arquivo `.devcontainer/devcontainer.json` encaminha a porta `8000` e inicia o servidor quando o Codespace é iniciado. Depois que a criação terminar, abra a aba **Ports** e acesse a porta encaminhada.

## Arquivos

- `index.html`: interface da calculadora e chamadas à API.
- `servidor.py`: servidor HTTP que serve a página e processa as requisições.
- `teste.py`: funções matemáticas e calculadora interativa de terminal.
- `.devcontainer/devcontainer.json`: configuração do ambiente e da porta no Codespaces.
