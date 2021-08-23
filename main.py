# Pacotes necessários
import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance


def main():
    st.title("Manipulação de imagens com OpenCV")
    st.markdown("Aplicação de filtro em imagens usando o pacote OpenCV do **Python**.")
    st.sidebar.title("Opções")

    # Opções de página
    opcoes_menu = ["Filtros", "Sobre"]
    st.sidebar.selectbox("Selecione...", opcoes_menu)

    # Upload de imagem
    img = st.empty() # Referência da exibição pricipal da imagem
    imagem_inicial = Image.open("default.jpg")
    arquivo_imagem = st.file_uploader("Carregar imagem...", type=['jpg', 'jpeg', 'png'])

    st.sidebar.text("Imagem original:")

    if arquivo_imagem is not None:
        imagem_inicial = Image.open(arquivo_imagem)

    img.image(imagem_inicial)
    st.sidebar.image(imagem_inicial, width=300)

    # Opções de filtros
    filtros = st.sidebar.radio("Filtros", ['Original', 'P & B', 'Gaussian Blur'])

    if filtros == 'P & B':
        imagem_convertida = np.array(imagem_inicial.convert('RGB'))
        pb_img = cv2.cvtColor(imagem_convertida, cv2.COLOR_RGB2GRAY)
        img.image(pb_img)


if __name__ == '__main__':
    main()