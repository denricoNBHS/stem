from PIL import Image
import numpy as np

def to_ascii(infile, width=80, outfile=None, font_ratio=.43):
    
    # ASCII character gradient from light to dark
    gradient =  " .:-=+*#%@"

    # open the image
    img = Image.open(infile)
    
    # determine aspect ratio of image
    aspect = img.width/img.height
    
    # resize image to given width at scale 
    # (rounding height to integer number of pixels and correcting for font dimensions)
    # then convert to B&W and reduce color depth
    img = img.resize((width, int(font_ratio * width/aspect))).convert('L').quantize(colors=10)
    
    # convert to array
    img = np.array(img)
    
    # replace each pixel value with corresponding value from gradient
    # use .join() to store as string
    img_str = '\n'.join([''.join([gradient[p] for p in row]) for row in img])
    
    # if a target file is specified, write the string to that file
    # otherwise return the string
    
    if outfile:
        with open(outfile, 'w') as f:
            f.write(img_str)
    else:
        return img_str