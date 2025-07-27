# 🟩 Jogo 2048 – Trabalho Final de Computação 1  

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)  
![Status](https://img.shields.io/badge/Status-Finalizado-green?style=flat-square)  
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)  

## 📌 **Descrição do Projeto**
Este projeto implementa o clássico jogo **2048** como trabalho final para a disciplina **Computação 1**.  
O objetivo do jogo é combinar números iguais no tabuleiro para formar potências de 2 até atingir o número definido no critério de dificuldade.

---

## 🚀 **Como Executar**
1. Clone ou baixe o repositório.  
2. Certifique-se de que os arquivos estão na mesma pasta.  
3. Execute no terminal:  
   ```bash
   python _2048_jogo_Daniel_Lucas_Rodrigues.py
   ```
4. Siga as instruções exibidas no console para jogar.

---

## 🎮 **Regras do Jogo**
- O jogador escolhe um **nível de dificuldade** (potência de 2 entre 2 e 2048).  
- A cada jogada, surge aleatoriamente um **2** (60%) ou **4** (40%).  
- Controles:  
  - `w` → mover para cima  
  - `a` → mover para a esquerda  
  - `s` → mover para baixo  
  - `d` → mover para a direita  
  - `q` → desistir do jogo  
- O jogo termina quando:
  - ✅ O número objetivo é atingido (**vitória**)  
  - ❌ Não existem mais movimentos possíveis (**derrota**)  

---

## 🛠️ **Estrutura do Código**

### 📄 **1. `_2048_funcoes_Daniel_Lucas_Rodrigues.py`**
Contém as funções principais do jogo:
- `vitoria(tabuleiro, criterio)` → verifica se o objetivo foi alcançado.  
- `dois_ou_quatro(tabuleiro)` → adiciona aleatoriamente um 2 ou 4 no tabuleiro.  
- `mostra_tabuleiro(tabuleiro)` → imprime o tabuleiro formatado.  
- `esquerda(tabuleiro)` → movimenta e combina peças para a esquerda.  
- `direita(tabuleiro)` → movimenta e combina peças para a direita.  

### 📄 **2. `_2048_jogo_Daniel_Lucas_Rodrigues.py`**
Responsável pelo fluxo do jogo:
- `cima(tabuleiro)` → movimento para cima (usa `esquerda` com matriz transposta).  
- `baixo(tabuleiro)` → movimento para baixo (usa `direita` com matriz transposta).  
- `tabuleiro_vazio()` → cria uma matriz 4x4 preenchida com zeros.  
- `derrota(tabuleiro)` → verifica se não existem mais movimentos possíveis.  
- `main()` → controla o jogo, interage com o usuário e verifica condições de vitória/derrota.  

---

## 🧠 **Como Funcionam os Movimentos**

### 🔄 Movimento para a Esquerda (`a`)
Antes:
```
|  2    2    0    4   |
|  4    0    4    0   |
|  0    0    0    0   |
|  2    2    2    2   |
```
Depois:
```
|  4    4    0    0   |
|  8    0    0    0   |
|  0    0    0    0   |
|  4    4    0    0   |
```

### 🔁 Movimento para a Direita (`d`)
Antes:
```
|  2    2    0    4   |
|  4    0    4    0   |
|  0    0    0    0   |
|  2    2    2    2   |
```
Depois:
```
|  0    0    4    4   |
|  0    0    0    8   |
|  0    0    0    0   |
|  0    0    4    4   |
```

### 🔼 Movimento para Cima (`w`)
Antes:
```
|  2    0    2    2   |
|  2    2    2    2   |
|  0    2    4    4   |
|  2    2    0    4   |
```
Depois:
```
|  4    4    4    4   |
|  2    2    4    8   |
|  0    0    0    0   |
|  0    0    0    0   |
```

### 🔽 Movimento para Baixo (`s`)
Antes:
```
|  2    0    2    2   |
|  2    2    2    2   |
|  0    2    4    4   |
|  2    2    0    4   |
```
Depois:
```
|  0    0    0    0   |
|  0    0    0    0   |
|  2    2    4    4   |
|  4    4    4    8   |
```

---


## ✅ **Conceitos Aplicados**
- Estruturas de dados: **listas (matrizes 4x4)**
- Estruturas de controle: **loops, condicionais**
- Modularização: **separação de funções em arquivos distintos**
- Uso da biblioteca `random` para geração aleatória de números

---

## 👨‍💻 **Autores**
- **Daniel dos Santos**  
- **Lucas Rodrigues**
