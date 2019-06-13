import PIL
from PIL import Image

# =============================================================================
# Resize larger images to specified width while keeping aspect ratio
# =============================================================================

def resize_image(img):
    new_width = 400
    if(img.size[0] > new_width):
        width_percent = (new_width/float(img.size[0]))
        new_height = int((float(img.size[1])*float(width_percent)))
        new_img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
    else:
        new_img = img
    
    return new_img
