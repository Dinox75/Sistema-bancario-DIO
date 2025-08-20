# 🏦 Sistema Bancário em Python

Este projeto implementa um **sistema bancário simples**, desenvolvido em **Python 3** utilizando conceitos de **Programação Orientada a Objetos (POO)**.  
O sistema foi criado como parte de um desafio da DIO

---

## ✨ Funcionalidades

- Criar clientes (com nome, CPF, data de nascimento e endereço).
- Criar contas bancárias vinculadas a clientes.
- Realizar **depósitos**.
- Realizar **saques** (com limite de valor e limite diário de operações).
- Exibir **extrato** de movimentações.
- Listar todas as contas cadastradas.

---

## 🧩 Estrutura do Código

O projeto está dividido em várias classes que representam as entidades do sistema:

- **Cliente / PessoaFisica** → Representa um cliente do banco.  
- **Conta / ContaCorrente** → Gerencia saldo, limite de saque e histórico de transações.  
- **Transacao (abstract class)** → Classe abstrata para padronizar operações.  
  - **Deposito**  
  - **Saque**  
- **Historico** → Registra todas as transações de uma conta.  

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3.10+** instalado em sua máquina.  
2. Clone este repositório:

   ```bash
   git clone https://github.com/Dinox75/Sistema-bancario-DIO.git
