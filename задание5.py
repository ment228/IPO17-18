from PIL import Image, ImageFont, ImageDraw

image = Image.open('img/image1_NN.jpg')
print('Формат изображения: ',image.format)
print('Размер изображения: ',image.size)
print('Цветовой режим изображения: ',image.mode)

img = Image.new('RGBA', (200, 200), 'white')
idraw = ImageDraw.Draw(image)
idraw.rectangle((400, 750, 800, 850), fill='BLACK')
#
idraw2 = ImageDraw.Draw(image)
text = "Данишевского Даниила"
font = ImageFont.truetype("arial.ttf", size=18)
idraw2.text((420, 770), text, font=font)
image.save('img/image5_NN.jpg')
