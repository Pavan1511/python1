from PIL import Image # from pillow we are going to import Image to resize the image

img = Image.open("resize_img.png") # here we are going to use open() to open the Image and store the result in img
resizing_img = img.resize((325, 400)) #here we are going to use resize() to resize the image and store the result in resizing_img
resizing_img.save("resizedimg.png") # here we are going to resizing_img the image and store the result in resizedimg.png