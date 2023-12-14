from PIL import Image

image = Image.open('img/image1_NN.jpg')
print('Формат изображения: ',image.format)
print('Размер изображения: ',image.size)
print('Цветовой режим изображения: ',image.mode)
