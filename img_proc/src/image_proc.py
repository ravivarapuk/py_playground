from PIL import Image, ImageFilter

img = Image.open('./images/616797.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
converted_img = img.convert('L')

filtered_img.save("geryscaleimage.png", 'png')
filtered_img.show()
print(img)
print(img.mode)
print(dir(img))
