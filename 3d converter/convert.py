from PIL import Image, ImageChops
import os
origin = []
red = []
cyan = []
Product = Image.open(os.path.join('Images','image ('+raw_input(':')+').jpg'))
ProductR = Image.new('RGB',Product.size, color=(0, 0, 0))
ProductC = Image.new('RGB',Product.size, color=(0, 0, 0))
ProductO = Image.new('RGB',Product.size, color=(0, 0, 0))
width, height = Product.size
for e in range(height):
    for s in range(width):
        pixr, pixg, pixb = Product.getpixel((s, e))
##        if s is 0:
##            origin.append([pixr, pixg, pixb])
##            red.append([pixr, 0, 0])
##            cyan.append([0, pixg, pixb])
##        if s > 0:
##            origin[e].append([pixr, pixg, pixb])
##            red[e].append([pixr, 0, 0])
##            cyan[e].append([0, pixg, pixb])
        ProductR.putpixel((s, e), (pixr, 0, 0, 255))
        ProductC.putpixel((s, e), (0, pixg, pixb, 255))
        ProductO.putpixel((s, e), (pixr, pixg, pixb, 255))
##for s in range(height):
##    for e in range(width):
##        ProductR = ProductR.putpixel((e, s), (pixr, 0, 0, 255))
##        ProductC = ProductC.putpixel((e, s), (0, pixg, pixb, 255))
ProductC.putalpha(128)
ProductR.putalpha(128)
ProductO.putalpha(255)
ProductC = ImageChops.offset(ProductC, -10, 0)
ProductR = ImageChops.offset(ProductR, 10, 0)
#Production = Product
image1 = Image.alpha_composite(ProductC, ProductR)
image2 = Image.alpha_composite(ProductO, image1)
#image2 = Image.alpha_composite(image1, Product)
#Production = Image.alpha_composite(ProductC, ProductR)
#Production = Image.alpha_composite(Production,Product)
#Production.paste(ProductC, (10, 0))
#Production.paste(ProductR, (-10, 0))
#Produce = ImageChops.blend(Product, ProductC, alpha=0.5)
#Final = ImageChops.blend(ProductR, Produce, alpha=0.5)
file_string = ''
cfiles = os.listdir(os.path.join('Images','Production'))
file_string = 'Product'+str(len(cfiles))+'.png'
image2.save(os.path.join('Images','Production',file_string))
