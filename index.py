
from PIL import Image
import PIL
import glob
from pathlib import Path
import os

def compressFile(basePath):
    fixed_height = 200
    savingFolder = basePath.split('/')[1]
    if not os.path.exists('afterCompress/'+savingFolder):
        os.makedirs('afterCompress/'+savingFolder)
    savingpath = 'afterCompress'+basePath+'.webp'
    filepath = 'fileSToCompress'+basePath+'.png'
    image = Image.open(filepath)
    height_percent = (fixed_height / float(image.size[1]))
    width_size = int((float(image.size[0]) * float(height_percent)))
    image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)
    image.save(savingpath,quality=80)

FilesToCompress = Path('fileSToCompress').glob('**/*.png')
for path in FilesToCompress:
    basePath = str(path).split('.png')[0].split('fileSToCompress')[1]
    compressFile(basePath)
    
# doc install pip3 pillow install 
# create a folder call fileSToCompress and after compress 