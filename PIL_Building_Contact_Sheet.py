import PIL
from PIL import Image
from PIL import ImageEnhance, ImageFont, ImageDraw
# from IPython.display import display

# read image and convert to RGB
img=Image.open("msi_recruitment.png").convert('RGB')
image = PIL.Image.new(img.mode, (img.width,img.height+60))
image.paste(img, (0,0))
display(image)

lut = (0.1, 0.5, 0.9)
font = ImageFont.truetype("readonly/fanwood-webfont.ttf",55)
# build a list of 9 images which have different brightnesses
images = list()
ch = 0
while ch < 3:    # iterate on 3 channels
    for x in lut:
        newimg = image.copy() # As we don't need to overwrite the old "txt"
        draw = ImageDraw.Draw(newimg)
        txt = 'channel {} intensity {}'.format(ch,x)
        draw.text((0,img.height+5), txt, font=font)
        del draw # Kill drawing context
        
        band = newimg.split() #return 'R','G' and 'B' bands of image
        # multiply each pixel by intensity
        temp = band[ch].point(lambda pixel:pixel*x)
        band[ch].paste(temp)
        #display(temp)
        temp = Image.merge(image.mode, band)
                
        images.append(temp)
        del temp #kill image_temp context
    ch += 1

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
#display(contact_sheet)
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)


