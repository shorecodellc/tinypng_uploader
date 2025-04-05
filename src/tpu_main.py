#kevin fink
#kevin@shorecode.org
#Fri Oct 18 09:45:28 AM +07 2024
#tpu_main.py

import sys
import os
import tinify
import threading
from tpu_filepaths import Files
#from  import

files = Files()
filepaths = files.get_files_list()
output_dir = filepaths[1]
input_dir = filepaths[2]
input_thumbs_dir = filepaths[3]
INPUT_RESIZE_DIR = filepaths[3]
#log_fp = filepaths[0]

#logger = set_logging('', log_fp)

tinify.key = os.getenv('TINYPNG_API_KEY')

class TinyPngUploader:
    def __init__(self, input_dir, thumb_input_dir, resize_input_dir):
        self.threads = list()
        self.input_dir = input_dir
        self.thumb_input_dir = thumb_input_dir
        self.resize_input_dir = resize_input_dir

    def run(self, thumb_list, convert_list, resize_list):
        for file in input_files:
            thread = threading.Thread(target=lambda: self.compress_img(os.path.join(self.input_dir, file)))
            thread.start()
            self.threads.append(thread)
        for file in thumb_list:
            thread = threading.Thread(target=lambda: self.make_thumb(os.path.join(self.thumb_input_dir, file)))
            self.threads.append(thread)
            thread.start()
        for file in resize_list:
            thread = threading.Thread(target=lambda: self.resize(os.path.join(self.resize_input_dir, file)))
            self.threads.append(thread)
            thread.start()
        for t in self.threads:            
            t.join()
                
    def compress_img(self, img,):    
        source = tinify.from_file(img)  
        converted = source.convert(type=["image/jpg"]).transform(background="#000000")
        output_fp = os.path.join(output_dir, os.path.splitext(os.path.split(img)[-1])[0]) + '.jpg'
        #source.to_file(output_fp)
        converted.to_file(output_fp)
        
    def make_thumb(self, img):    
        source = tinify.from_file(img)
        resized = source.resize(
            method="thumb",
            width=80,
            height=80
        )
        output_fp = os.path.join(output_dir, os.path.split(img)[-1])
        resized.to_file(output_fp)
        
    def resize(self, img, width, height):    
        source = tinify.from_file(img)
        source = source.resize(
            method="thumb",
            width=width,
            height=height
        )      
        output_fp = os.path.join(output_dir, os.path.split(img)[-1])
        resized.to_file(output_fp)    

if __name__ == '__main__':
    input_files = list(os.walk(input_dir))[0][2]
    input_files_for_thumbs =list(os.walk(input_thumbs_dir))[0][2]
    input_files_for_resize =list(os.walk(INPUT_RESIZE_DIR))[0][2]
    png = TinyPngUploader(input_dir, input_thumbs_dir)
    png.run(input_files_for_thumbs, input_files)


