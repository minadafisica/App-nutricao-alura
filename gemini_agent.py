# gemini_agent.py

import google.generativeai as genai
import json
from PIL import Image
import os  # Para acessar variáveis de ambiente

# Configure a API Key
# É RECOMENDADO USAR VARIÁVEIS DE AMBIENTE OU STREAMLIT SECRETS PARA A CHAVE API
# Por exemplo, definir a variável de ambiente GOOGLE_API_KEY
# ou usar st.secrets.gemini_api_key no Streamlit Cloud
try:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    if GOOGLE_API_KEY is None:
        raise ValueError("A variável de ambiente 'GOOGLE_API_KEY' não está definida.")
    genai.configure(api_key=GOOGLE_API_KEY)
except ValueError as e:
    print(f"Erro de configuração da API: {e}")
    print("Por favor, defina a variável de ambiente GOOGLE_API_KEY ou use st.secrets.gemini_api_key no Streamlit.")
    # No ambiente local, você pode descomentar a linha abaixo para testes rápidos, mas não em produção!
    # genai.configure(api_key="SUA_API_KEY_AQUI") # SUBSTITUA PELA SUA CHAVE SE FOR TESTAR LOCALMENTE SEM VARIAVEL DE AMBIENTE


def analyze_plate_image_with_gemini(pil_image: Image.Image) -> dict:
    """
    Analisa uma imagem de um prato de comida usando o Gemini Pro Vision e
    retorna os alimentos identificados com sugestões de unidade em formato de dicionário Python.

    Args:
      pil_image: A imagem do prato no formato PIL.Image.Image.

    Returns:
      Um dicionário Python contendo os alimentos identificados com sugestões de unidade.
      Retorna um dicionário de erro em caso de falha.
    """
    try:
        # Inicializar o modelo Gemini Pro Vision
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Criar a requisição para o modelo
        prompt = """
        Analise a imagem deste prato de comida e identifique os alimentos presentes.
        Para cada alimento identificado, tente sugerir uma unidade de medida comum (gramas, colheres, xícaras, pedaços, porções, unidade).
        Retorne a lista de alimentos e suas sugestões de unidade em formato JSON, seguindo a seguinte estrutura:
        {
          "prato": [
            {"alimento": "Nome do Alimento 1", "unidade_sugerida": "unidade"},
            {"alimento": "Nome do Alimento 2", "unidade_sugerida": "gramas"},
            ...
          ]
        }
        Responda apenas com o JSON.
        """

        # Gerar conteúdo com a imagem PIL
        response = model.generate_content([prompt, pil_image])

        # Tentar analisar a resposta como JSON
        response_text = response.text.strip()

        # Remover possíveis blocos de código markdown se presentes
        if response_text.startswith('```json'):
            response_text = response_text[len('```json'):].strip()
        if response_text.endswith('```'):
            response_text = response_text[:-len('```')].strip()

        json_data = json.loads(response_text)
        return json_data

    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        print(f"Resposta bruta do modelo: {response_text}")
        return {"error": f"Não foi possível analisar a resposta como JSON. Resposta bruta: {response_text}"}
    except Exception as e:
        print(f"Ocorreu um erro na análise do Gemini: {e}")
        return {"error": f"Erro na análise do Gemini: {e}"}


def analyze_calories_with_gemini(alimento: str, quantidade: float, unidade: str) -> dict:
    """
    Analisa a quantidade e unidade de um alimento usando o Gemini Pro e
    retorna uma estimativa das calorias em formato de dicionário Python.

    Args:
        alimento: O nome do alimento (string).
        quantidade: A quantidade do alimento (float).
        unidade: A unidade de medida (string).

    Returns:
        Um dicionário Python contendo a estimativa de calorias.
        Retorna um dicionário de erro em caso de falha.
    """
    try:
        # Inicializar o modelo Gemini Pro
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Criar a requisição para o modelo
        prompt = f"""
        Qual a estimativa de calorias de {quantidade} {unidade} de {alimento}?
        Responda com um JSON contendo apenas o número de calorias, na chave 'calorias'.
        Exemplo de resposta: {{"calorias": 150}}
        """

        response = model.generate_content(prompt)

        response_text = response.text.strip()

        # Remover possíveis blocos de código markdown
        if response_text.startswith('```json'):
            response_text = response_text[len('```json'):].strip()
        if response_text.endswith('```'):
            response_text = response_text[:-len('```')].strip()

        json_data = json.loads(response_text)
        return json_data

    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON de calorias: {e}")
        print(f"Resposta bruta do modelo de calorias: {response.text}")
        return {"error": f"Não foi possível analisar a resposta de calorias como JSON. Resposta bruta: {response.text}"}
    except Exception as e:
        print(f"Ocorreu um erro na análise de calorias com Gemini: {e}")
        return {"error": f"Erro na análise de calorias com Gemini: {e}"}