from PIL import Image


im = Image.open('level_up.jpg')
x, y = im.size
im = im.resize((450, 60))
im.save('level_up.jpg')