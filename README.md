# Script de Consulta BSC

Projeto desenvolvido para o desafio técnico BSC + Backend + Grafana.

O objetivo é conectar à Binance Smart Chain usando web3.py e consultar informações de uma carteira pública da Binance.

## Funcionalidades

- Conexão via RPC público BSC
- Consulta do bloco atual
- Consulta saldo BNB nativo
- Consulta saldo BEP20 (USDT)
- Conversão de valores brutos para formato humano
- Configuração via variáveis de ambiente
- Estrutura modular

## Arquitetura

src/

config/
services/
utils/
main.py

### Responsabilidades

config:
carrega variáveis de ambiente

services:
camada de comunicação blockchain

utils:
conversões e formatação

main:
fluxo principal da aplicação

## Tecnologias

- Python 3.11+
- web3.py
- python-dotenv

## Instalação

Clone:

```bash
git clone URL

Crie ambiente:

python -m venv venv
source venv/bin/activate

Instale:

pip install -r requirements.txt

Crie:

cp .env.example .env

Execute:

python src/main.py
Exemplo de saída
========================================
BSC Wallet Balance Checker
========================================

Connected successfully

Current block: 99065035

BNB Balance: 6,238,436.9521 BNB

USDT Balance: 2.8138 USDT
Conceitos estudados
web3.py
RPC
HTTPProvider
BNB nativo
Tokens BEP20
Contratos inteligentes
ABI
Wei
balanceOf()
Próximos passos

Este projeto servirá como base do Projeto 2:

coleta periódica
PostgreSQL
FastAPI
API REST
