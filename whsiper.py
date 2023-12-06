import re
import sys
import os
from pydub import AudioSegment
import whisper

os.chdir(r" ")   # Change this 

dest_dir = (r"  ") # Change this too

d_list = (os.listdir())

model = whisper.load_model("base")

f = open("test.txt", 'w')

for file in d_list:

    if file.endswith('.wav'):


        result = model.transcribe(file)

        f.write('\n')

        f.write(file + ":    "+ result["text"] + "\n")

f.close()
