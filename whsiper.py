import re
import sys
import os
from pydub import AudioSegment
import whisper
import torch

devices = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

os.chdir(r" ") # Change this

dest_dir = (r" ") # Change this

d_list = (os.listdir())

model = whisper.load_model("base", device =devices)

f = open("test.txt", 'w', encoding='utf-8')

for file in d_list:

    if file.endswith('.wav'):


        result = model.transcribe(file)

        f.write('\n')

        f.write(file + ":    "+ result["text"] + "\n")

f.close()
