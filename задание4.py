from PIL import ImageFilter
from PIL import Image

image = Image.open('img/image3_NN.jpg')

blurred = image.filter(ImageFilter.BLUR)
blurred.save('img/image4_NN.jpg')

contour = image.filter(ImageFilter.CONTOUR)
contour.save('img/image4_1_NN.jpg')

detail = image.filter(ImageFilter.DETAIL)
detail.save('img/image4_2_NN.jpg')
