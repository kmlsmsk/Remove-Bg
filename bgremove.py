from rembg import remove
from PIL import Image

def rbg(url):
    out_url = url+".png"
    input=Image.open(url)
    output=remove(input)
    output.save(out_url)


