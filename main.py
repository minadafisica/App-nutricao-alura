# app_streamlit.py

import streamlit as st
from PIL import Image
import time
from gemini_agent import analyze_plate_image_with_gemini, analyze_calories_with_gemini

def exibir_resultados_alimentos(resultados_gemini):
    """Exibe os alimentos identificados e permite inserir quantidades, agrupando alimentos iguais com sugestão de unidade."""
    st.subheader("Quantifique os Alimentos")
    quantidades_dict = {}

    if "error" in resultados_gemini:
        st.error(f"Erro na análise dos alimentos: {resultados_gemini['error']}")
        return None
    elif "prato" in resultados_gemini and isinstance(resultados_gemini["prato"], list):
        alimentos_identificados = {}
        for item in resultados_gemini["prato"]:
            if "alimento" in item:
                alimento = item["alimento"].strip()
                unidade_sugerida = item.get("unidade_sugerida", "gramas") # Pega a unidade sugerida, padrão para gramas
                if alimento not in alimentos_identificados:
                    alimentos_identificados[alimento] = {"count": 0, "unidade_sugerida": unidade_sugerida}
                alimentos_identificados[alimento]["count"] += 1

        for i, (alimento, info) in enumerate(alimentos_identificados.items()):
            col1, col2 = st.columns(2)
            with col1:
                quantidade = st.number_input(f"Quantidade de {alimento}", min_value=0.0, step=0.1, key=f"quantidade_{alimento.replace(' ', '_')}")
            with col2:
                unidade = st.selectbox(f"Unidade de {alimento}", ["gramas", "colheres", "xícaras", "pedaços", "porções", "unidade"], index=["gramas", "colheres", "xícaras", "pedaços", "porções", "unidade"].index(info["unidade_sugerida"]) if info["unidade_sugerida"] in ["gramas", "colheres", "xícaras", "pedaços", "porções", "unidade"] else 0, key=f"unidade_{alimento.replace(' ', '_')}")
            quantidades_dict[alimento] = {"quantidade": quantidade, "unidade": unidade, "count": info["count"]}
        return quantidades_dict
    else:
        st.warning("Formato de resultados de alimentos inesperado.")
        st.json(resultados_gemini)
        return None

def exibir_resultado_calorias_gemini(quantidades_alimentos):
    """Calcula e exibe o resultado das calorias usando Gemini."""
    st.subheader("Estimativa de Calorias (via Gemini)")
    total_calorias = 0
    detalhes_calorias = []

    if quantidades_alimentos:
        with st.spinner("Calculando calorias com Gemini..."):
            for alimento, info in quantidades_alimentos.items():
                calorias_result = analyze_calories_with_gemini(alimento, info["quantidade"], info["unidade"])
                if "calorias" in calorias_result:
                    calorias = calorias_result["calorias"]
                    total_calorias += calorias * info["count"]
                    detalhes_calorias.append(f"- {info['quantidade']} {info['unidade']} de {alimento} (x{info['count']}): {calorias * info['count']:.2f} calorias (estimativa Gemini)")
                elif "error" in calorias_result:
                    st.warning(f"Erro ao obter calorias para '{alimento}': {calorias_result['error']}")
                else:
                    st.warning(f"Resposta de calorias inesperada para '{alimento}': {calorias_result}")
            time.sleep(1)

        st.markdown("---")
        st.write(f"**Total estimado de calorias (Gemini):** {total_calorias:.2f}")
        if detalhes_calorias:
            st.write("Detalhes:")
            for detalhe in detalhes_calorias:
                st.write(detalhe)

st.set_page_config(
    page_title="Analisador de Pratos com Gemini e Calorias",
    page_icon="🍽️",
    layout="centered"
)

st.title(f"🍽️ Análise de Pratos com IA e Estimativa de Calorias")
st.markdown("""
    Envie uma foto do seu prato, identifique os alimentos e estime as calorias usando a IA do Gemini!
    """)

st.sidebar.header("⚙️ Upload da Imagem")
uploaded_file = st.sidebar.file_uploader(
    "Selecione uma imagem do seu prato (.jpg, .jpeg, .png)",
    type=["jpg", "jpeg", "png"],
    key="file_uploader"
)

st.sidebar.markdown("---")
st.sidebar.markdown("ℹ️ **Como usar:**")
st.sidebar.markdown("1. Envie a foto do seu prato na barra lateral.")
st.sidebar.markdown("2. Ajuste a quantidade e a unidade de medida para cada alimento (a IA tentará sugerir uma unidade).")
st.sidebar.markdown("3. Clique em 'Calcular Calorias' para obter uma estimativa.")
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido com Streamlit e Google Gemini API.")

if "resultados_gemini" not in st.session_state:
    st.session_state["resultados_gemini"] = None
if "quantidades_alimentos" not in st.session_state:
    st.session_state["quantidades_alimentos"] = None

if uploaded_file is not None:
    image_pil = Image.open(uploaded_file)

    st.subheader("Sua Imagem Carregada")
    st.image(image_pil, caption="Imagem do Prato", use_container_width=True)

    st.markdown("---")
    if st.session_state["resultados_gemini"] is None or st.session_state.get("uploaded_file_name") != uploaded_file.name:
        with st.spinner("Analisando o prato com Gemini..."):
            resultados_gemini = analyze_plate_image_with_gemini(image_pil)
            st.session_state["resultados_gemini"] = resultados_gemini
            st.session_state["quantidades_alimentos"] = None # Limpa as quantidades ao reanalisar
            st.session_state["uploaded_file_name"] = uploaded_file.name # Guarda o nome do arquivo para controle

    if st.session_state["resultados_gemini"]:
        st.session_state["quantidades_alimentos"] = exibir_resultados_alimentos(st.session_state["resultados_gemini"])

        if st.session_state["quantidades_alimentos"]:
            if st.button("Calcular Calorias"):
                exibir_resultado_calorias_gemini(st.session_state["quantidades_alimentos"])

else:
    st.info("Por favor, carregue uma imagem do seu prato na barra lateral para começar.")
