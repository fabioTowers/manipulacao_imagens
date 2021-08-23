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
    imagem_inicial = Image.open("default.jpg")
    arquivo_imagem = st.file_uploader("Carregar imagem...", type=['jpg', 'jpeg', 'png'])


    if arquivo_imagem is not None:
        imagem_inicial = Image.open(arquivo_imagem)

    st.image(imagem_inicial)

if __name__ == '__main__':
    main()