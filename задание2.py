from PIL import Image

image = Image.open('img/image1_NN.jpg')

rotated = image.rotate(30)
rotated.save('img/image2_NN.jpg')