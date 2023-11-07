import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox

def translate_captions(caption_location, source_lang, dest_lang):
    try:
        import webvtt
    except ModuleNotFoundError:
        print("Please install the 'webvtt' library.")
    try:
        import googletrans
    except ModuleNotFoundError:
        print("Please install the 'googletrans' library.")
    from googletrans import Translator
    import re  # Regular expression library

    # Read the file and ignore lines with meeting ID
    with open(caption_location, 'r') as f:
        lines = f.readlines()
    lines = [line for line in lines if not re.search(r'[-/]\d+$', line.strip())]

    # Write the cleaned lines to a new file
    temp_location = caption_location[:-4] + "_temp.vtt"
    with open(temp_location, 'w') as f:
        f.writelines(lines)

    captions = webvtt.read(temp_location)
    translator = Translator()
    translated_captions = []
    for caption in captions:
        translated_text = translator.translate(caption.text, src=source_lang, dest=dest_lang).text
        translated_captions.append(translated_text)
        caption.text = translated_text
        time.sleep(10) # Add a delay of 10 seconds
    captions.save(f"{caption_location[:-4]}_{dest_lang}.vtt")

    # Remove the temporary file
    os.remove(temp_location)

    return translated_captions


root = tk.Tk()
root.withdraw()
caption_location = filedialog.askopenfilename(title='Select captions file', filetypes=[('VTT Files','*.vtt')])
if not caption_location:
    print('No file selected')
    messagebox.showerror('Error', 'No file selected')
    raise SystemExit

translated_captions_cn = translate_captions(caption_location, 'en', 'zh-CN')
translated_captions_es = translate_captions(caption_location, 'en', 'es')
translated_captions_pt = translate_captions(caption_location, 'en', 'pt')
