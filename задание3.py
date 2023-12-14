from PIL import Image

image = Image.open('img/image1_NN.jpg')

cropped = image.crop((85, 440, 570, 820))
cropped.save('img/image3_NN.jpg')