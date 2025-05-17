# 🍽️ Agente de Análise de Alimentos (Food Analysis Agent)

Um agente simples desenvolvido em Google Colab para analisar imagens de pratos de comida, identificar os alimentos presentes e retornar os resultados em formato JSON. Ideal para quem deseja experimentar análise de imagem com IA sem a necessidade de configuração local complexa.

## ✨ Sobre o Projeto



## 🚀 Como Funciona

O "Agente de Análise de Alimentos" opera da seguinte forma:

1.  Você fornece uma imagem de uma refeição (seja fazendo upload no Colab ou fornecendo uma URL).
2.  O código no Google Colab carrega e pré-processa a imagem.
3.  Um modelo de classificação de imagem pré-treinado (especializado em alimentos) analisa a imagem.
4.  O modelo retorna as probabilidades de diferentes alimentos estarem presentes na imagem.
5.  O código seleciona os alimentos com maior confiança e formata essa informação em uma string JSON.
6.  A string JSON é exibida como saída.

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Google Colab:** Ambiente de execução baseado em notebook, fornecendo acesso a GPUs/TPUs.
* **Hugging Face `transformers`:** Biblioteca para fácil acesso e uso de modelos de ML pré-treinados, incluindo o pipeline de classificação de imagem.
* **`torch`:** Framework de Deep Learning (utilizado pelo modelo via `transformers`).
* **`Pillow` (PIL):** Biblioteca para manipulação básica de imagens.
* **`requests`:** Para baixar imagens de URLs.
* **`json`:** Para formatar a saída.

## 🔗 Acesse e Use no Google Colab

A maneira mais fácil de usar este agente é executá-lo diretamente no Google Colab.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<SEU_USUARIO_GITHUB>/<NOME_DO_SEU_REPOSITORIO>/blob/main/<NOME_DO_SEU_NOTEBOOK>.ipynb)

1.  Clique no botão acima "Open In Colab".
2.  O notebook será aberto no seu ambiente Colab.
3.  Execute as células sequencialmente (clicando no botão de play ou `Shift + Enter`).
4.  A primeira célula instalará as dependências.
5.  A célula seguinte pedirá para você fazer upload de uma imagem do seu computador.
6.  Após o upload, o agente analisará a imagem e imprimirá a resposta JSON na saída da célula.
7.  Alternativamente, você pode descomentar e usar a opção de analisar uma imagem via URL no código.

**Certifique-se de substituir `<SEU_USUARIO_GITHUB>`, `<NOME_DO_SEU_REPOSITORIO>` e `<NOME_DO_SEU_NOTEBOOK>.ipynb` no link do Colab acima para que ele aponte para o seu repositório!**
