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
    captions = webvtt.read(caption_location)
    translator = Translator()
    translated_captions = []
    for caption in captions:
        translated_text = translator.translate(caption.text, src=source_lang, dest=dest_lang).text
        translated_captions.append(translated_text)
        caption.text = translated_text
    captions.save(f"{caption_location[:-4]}_{dest_lang}.vtt")
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