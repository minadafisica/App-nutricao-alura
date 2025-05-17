# 🍽️ Nutri.AI - Seu agente de análise de alimentos 

Seu agente de bolso para analisar suas refeições, identificando os alimentos presentes e te ajudando a controlar a caloria da refeição. 

---

## Sobre o Nutri.AI

A preocupação com a saúde e a nutrição tem ganhado cada vez mais destaque, e no Brasil, um país com um histórico rico em políticas de segurança alimentar e nutricional, esse cuidado se manifesta de diversas formas. No entanto, transformar a orientação nutricional em prática diária ainda é um grande desafio para muitas pessoas.

Minha própria jornada com aplicativos de acompanhamento nutricional sempre esbarrou na frustração de ter que inserir manualmente cada alimento consumido. Esse processo, muitas vezes tedioso e demorado, desencorajava o uso contínuo e dificultava seguir as recomendações de um nutricionista de forma consistente.

Essa dificuldade pessoal ganhou um novo significado ao observar a luta da minha mãe contra o sobrepeso ao longo dos anos. Ver a complexa relação dela com a comida e os desafios em manter uma alimentação saudável me motivou a buscar soluções que pudessem simplificar esse dia a dia, tornando a organização e o acompanhamento do plano nutricional menos onerosos. Iniciativas como cozinhar para a semana ou preparar marmitas já ajudam, mas a ponte entre a refeição pronta e o registro no plano nutricional ainda era um obstáculo.

Foi assim que surgiu a ideia deste projeto: utilizar a Inteligência Artificial para facilitar essa prática. Ao permitir que uma simples foto da refeição (como uma marmita preparada para a semana) seja analisada para identificar os alimentos, buscamos remover uma barreira significativa no acompanhamento nutricional. Este "Agente de análise de alimentos" é um primeiro passo para tornar o processo de seguir uma planilha nutricional mais intuitivo e menos frustrante, ajudando pessoas como a minha mãe – e tantas outras – a ter uma relação mais fácil e organizada com a alimentação saudável e alcançar seus objetivos de saúde.

---

## Como Funciona

O "Agente de análise de alimentos" opera da seguinte forma:

1.  Você fornece uma imagem de uma refeição.
2.  Um agente analisa a imagem.
3.  O modelo retorna as probabilidades de diferentes alimentos estarem presentes na imagem.
4.  Você indica a quantidade e a unidade de medida de cada alimento (a IA tentará sugerir uma unidade).
5. O modelo retorna o cálculo de estimativa.

---

[Visualização](https://imgur.com/a/m3vCXt3)

---
## 🔗 Acesse

A maneira mais fácil de usar este agente é através: https://app-nutricao-alura-8tnccannmw7xuvf8k6ob6b.streamlit.app/#analise-de-pratos-com-ia-e-estimativa-de-calorias-gemini
---
## Tecnologias 
* **Python:** Linguagem de programação principal.
* **Google Gemini** 
* **Streamlit**
* **Github**

* **Pillow (PIL)**
Usado em: Ambos arquivos
Função: Abrir e manipular a imagem carregada pelo usuário antes de enviar para análise com IA (formato PIL.Image.Image).
Por que: Necessário para lidar com imagens de forma compatível com Streamlit e a API do Gemini.

* **Google Generative AI (Gemini)**
Usado em: gemini_agent.py
Função: Análise da imagem do prato com o Gemini Pro Vision para identificar alimentos e sugerir unidades.
Estimativa de calorias com o Gemini Pro com base em alimento, quantidade e unidade.
Por que: Permite análise de conteúdo multimodal (texto + imagem) e gera respostas estruturadas em JSON.

* **[JSON (builtin)]**
Usado em: gemini_agent.py
Função: Converter texto gerado pelo Gemini em dicionários Python para posterior uso e exibição.
Por que: Gemini responde com strings que precisam ser transformadas em dados utilizáveis (JSON → dict).

* **[time (builtin)]**
Usado em: main.py
Função: Inserção de pequenas pausas (time.sleep) após processamento, possivelmente para UX ou controle de chamadas.
Por que: Ajuda a simular tempo de carregamento ou evitar chamadas rápidas em sequência.

* **[os (builtin)]**
Usado em: gemini_agent.py
Função: Capturar a variável de ambiente GOOGLE_API_KEY para autenticação com a API do Gemini.
Por que: Boa prática de segurança — evita hardcode de chaves sensíveis no código.

* **[st.session_state (Streamlit)]**
Usado em: app_streamlit.py
Função: Manter estado entre interações do usuário (ex: imagem analisada, resultados salvos).
Por que: Evita reprocessar tudo a cada interação, melhorando performance e UX.

---
## Documentação e pesquisa

- [Gemini API](https://ai.google.dev/gemini-api/docs/get-started/rest?hl=pt-br) para entender como aplicar no projeto;
- [GitHub do Google Gemini](https://github.com/google-gemini/generative-ai-js) para escrever o código de teste no Google Colab usando python.
- [Imersão ALura e Google Gemini]

---
  
## Status do projeto (dentro dos meus conhecimentos de iniciante):
- [x] Interface principal;
- [x] Funcionalidade de selecionar imagens da galeria;
- [x] Gerar a descrição da imagem com a IA;
- [x] Funcionalidade para indicar a quantidade e unidade de medida;
- [x] Gerar a estimativa de calorias com a IA.

## Próximos Passos 
Este projeto é um ponto de partida! Futuras melhorias planejadas incluem:


- [] Sugestão de Complementos: A IA poderá sugerir complementos para a refeição analisada, visando balanceamento nutricional ou variedade.
- [] Emojis na Saída: Substituir nomes de utensílios ou indicadores de quantidade por emojis para uma visualização mais intuitiva (ex: "1 🥄 de açúcar", "uma 🥣 de sopa").
- [] Integração com Plano Nutricional:
- [] Permitir que o usuário configure seu plano nutricional (importando dados desenvolvidos por um nutricionista).
- [] A IA analisará a refeição e indicará se ela se alinha ou se desvia do plano nutricional do usuário.
- [] Fornecer dicas personalizadas sobre como ajustar futuras refeições para se manter no plano ou como compensar um "desvio"

### Para um futuro
- [] Conectar com os dados do smartwatch e valores de bioimpedânica para ter um acompanhamento mais completo.

## Conecte-se comigo
<p> Caso tenha alguma dúvida, queira mandar o seu feedback ou só bater um papo mesmo, conecte-se comigo por meio dessas redes:</p>

- [LinkedIn](https://www.linkedin.com/in/gabriela-oliveira42/)
-Instagram/Tiktok: @minadafisica
