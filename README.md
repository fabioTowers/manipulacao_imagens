# Web app para processamento de imagens com OpenCV

Aplicativo de processamento digital de imagens usando o pacote OpenCV do Python com interface Web desenvolvida com Streamlit.

É possível ver os efeitos aplicados em uma imagem default como também fazer upload de uma imagem própria em seu computador e aplicar os filtros.

## Filtros

### Canny edges

Esse filtro geralmente é utilizado em etapas intermediárias do processamento de imagens para detecção de objetos. Como uma forma simplista de explicar sua função podemos dizer que o efeito Canny remove boa parte dos ruídos (informações desenecessárias) em uma imagem e deixa apenas as bordas, facilitando assim o processo de detecção de objetos.

Exemplo:

Imagem original:

![Imagem sem filtros](img/original.jpg)

Imagem com efeito Canny:

![Imagem com filtro Canny](img/canny.jpg)

A biblioteca OpenCV facilita a aplicação desse filtro, sendo possível aplicá-lo com uma única linha de código:

```python
canny_img = cv2.Canny(blurred_img, min_val, max_val)
```

Mas na maior parte das vezes o desafio é ajustar os parâmetros dessa função: os limites de histerese mínimo e máximo. Isso porque o ajuste desse parâmetros depende da imagem que está sendo utilizada e não há uma fórmula para todas as imagens. Pensando nisso, esse aplicativo permite o ajuste manual desse parâmetros e o resultado da aplicação do filtro na imagem.

Ajuste dos parâmtros de histerese:

![Ajuste de parâmtros Canny](img/hysteresis_thresholding.jpg)


