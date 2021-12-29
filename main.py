# Pacotes necessários
import streamlit as st
import numpy as np
#import cv2
from PIL import Image, ImageEnhance


# Excutar a aplicação: streamlit run main.py


def main():
    st.title("Manipulação de imagens com OpenCV")
    st.markdown("Aplicação de filtro em imagens usando o pacote [OpenCV](https://opencv.org) do **Python**, interface implementada"
                " com [StreamLit](https://streamlit.io).")

    st.sidebar.title("Opções")

    # Opções de página
    options_menu = ["Filtros", "Sobre"]
    page = st.sidebar.selectbox("Selecione...", options_menu)


    if page == 'Filtros':
        # Upload de imagem
        img = st.empty()  # Referência da exibição pricipal da imagem
        default_img = Image.open("default.jpg")
        uploaded_img = st.file_uploader("Carregar imagem...", type=['jpg', 'jpeg', 'png'])

        st.sidebar.text("Imagem original:")

        if uploaded_img is not None:
            default_img = Image.open(uploaded_img)

        img.image(default_img)
        st.sidebar.image(default_img, width=300)

        # Opções de filtros
        filters = st.sidebar.radio("Filtros", ['Original', 'Grayscale', 'Gaussian Blur', 'Sketch',
                                               'Sépia', 'Canny', 'Contraste', 'Brilho'])

        if filters == 'Grayscale':
            converted_img = np.array(default_img.convert('RGB'))
            grayscale_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
            img.image(grayscale_img)
        elif filters == 'Gaussian Blur':
            # Deslizante:  3 a 81, default: 27, step=2 (dimensão do kernel deve ser sempre ímpar)
            k_size = st.sidebar.slider("Kernel (n x n):", 3, 81, 27, step=2)
            converted_img = np.array(default_img.convert('RGB'))
            # Blur é aplicado uniformemente em todos os canais, não necessita conversão p/ BGR
            blurred_img = cv2.GaussianBlur(converted_img, (k_size, k_size), 0)
            img.image(blurred_img)
        elif filters == 'Sketch':
            converted_img = np.array(default_img.convert('RGB'))
            gray_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
            inv_gray_img = 255 - gray_img
            blur_img = cv2.GaussianBlur(inv_gray_img, (21, 21), 0, 0)
            sketch_img = cv2.divide(gray_img, 255 - blur_img, scale=256)
            img.image(sketch_img)
        elif filters == 'Sépia':
            converted_img = np.array(default_img.convert('RGB'))
            kernel = np.array([[0.272, 0.534, 0.131],
                               [0.349, 0.686, 0.168],
                               [0.393, 0.769, 0.189]])
            output_img = cv2.filter2D(converted_img, -1, kernel)
            img.image(output_img)
        elif filters == 'Canny':
            converted_img = np.array(default_img.convert('RGB'))
            blurred_img = cv2.GaussianBlur(converted_img, (11, 11), 0)
            st.sidebar.text('Hysteresis Thresholding: ')
            min_val = st.sidebar.slider("Minimum value:", 10, 300, 100, step=2)
            max_val = st.sidebar.slider("Maximum value:", 10, 300, 150, step=2)
            canny_img = cv2.Canny(blurred_img, min_val, max_val)
            img.image(canny_img)
        elif filters == 'Contraste':
            intensity = st.sidebar.slider("Contraste", 0.0, 2.0, 1.0)
            # Objeto de contraste
            enhancer = ImageEnhance.Contrast(default_img)
            output_img = enhancer.enhance(intensity)
            img.image(output_img)
        elif filters == 'Brilho':
            intensity = st.sidebar.slider("Contraste", 0.0, 2.0, 1.0)
            # Objeto de brilho
            enhancer = ImageEnhance.Brightness(default_img)
            output_img = enhancer.enhance(intensity)
            img.image(output_img)
    elif page == 'Sobre':
        st.subheader("Fabio Mendes")
        st.markdown("Aluno do curso de Análise e Desenvolvimento de Sistemas")
        st.markdown("Para mais conteúdos conheça minhas redes sociais:")
        st.markdown("* [GitHub](https://github.com/fabioTowers)")
        st.markdown("* [Medium](https://medium.com/@fabiomendes_95615)")
        st.markdown("* [LinkedIn](https://www.linkedin.com/in/fabio-mendes-35743b128)")

if __name__ == '__main__':
    main()