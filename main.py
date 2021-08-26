# Pacotes necessários
import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance


# Excutar a aplicação: streamlit run main.py


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
    filtros = st.sidebar.radio("Filtros", ['Original', 'Grayscale', 'Gaussian Blur', 'Sketch', 'Sépia', 'Canny', 'Contraste', 'Brilho'])

    if filtros == 'Grayscale':
        imagem_convertida = np.array(imagem_inicial.convert('RGB'))
        pb_img = cv2.cvtColor(imagem_convertida, cv2.COLOR_RGB2GRAY)
        img.image(pb_img)
    elif filtros == 'Gaussian Blur':
        # Deslizante:  3 a 81, default: 27, step=2 (dimensão do kernel deve ser sempre ímpar)
        k_size = st.sidebar.slider("Kernel (n x n):", 3, 81, 27, step=2)
        imagem_convertida = np.array(imagem_inicial.convert('RGB'))
        # Blur é aplicado uniformemente em todos os canais, não necessita conversão p/ BGR
        blurred_img = cv2.GaussianBlur(imagem_convertida, (k_size, k_size), 0)
        img.image(blurred_img)
    elif filtros == 'Sketch':
        imagem_convertida = np.array(imagem_inicial.convert('RGB'))
        gray_img = cv2.cvtColor(imagem_convertida, cv2.COLOR_RGB2GRAY)
        inv_gray_img = 255 - gray_img
        blur_img = cv2.GaussianBlur(inv_gray_img, (21, 21), 0, 0)
        sketch_img = cv2.divide(gray_img, 255 - blur_img, scale=256)
        img.image(sketch_img)
    elif filtros == 'Sépia':
        imagem_convertida = np.array(imagem_inicial.convert('RGB'))
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        output_img = cv2.filter2D(imagem_convertida, -1, kernel)
        img.image(output_img)
    elif filtros == 'Canny':
        imagem_convertida = np.array(imagem_inicial.convert('RGB'))
        blurred_img = cv2.GaussianBlur(imagem_convertida, (11, 11), 0)
        st.sidebar.text('Hysteresis Thresholding: ')
        min_val = st.sidebar.slider("Minimum value:", 10, 300, 100, step=2)
        max_val = st.sidebar.slider("Maximum value:", 10, 300, 150, step=2)
        canny_img = cv2.Canny(blurred_img, min_val, max_val)
        img.image(canny_img)
    elif filtros == 'Contraste':
        intensidade = st.sidebar.slider("Contraste", 0.0, 2.0, 1.0)
        # Objeto de contraste
        enhacer = ImageEnhance.Contrast(imagem_inicial)
        output_img = enhacer.enhance(intensidade)
        img.image(output_img)
    elif filtros == 'Brilho':
        intensidade = st.sidebar.slider("Contraste", 0.0, 2.0, 1.0)
        # Objeto de brilho
        enhancer = ImageEnhance.Brightness(imagem_inicial)
        output_img = enhancer.enhance(intensidade)
        img.image(output_img)


if __name__ == '__main__':
    main()