# check if webvtt is installed
try:
    import webvtt
except ModuleNotFoundError:
    print("Please install the 'webvtt' library.")

from googletrans import Translator

# confirm file path or make relative to current working directory
#Open vtt file
filename = input("Enter filename: ")
captions = webvtt.read(filename)

translator = Translator()
translated_captions = []

for caption in captions:
    print(caption.text)
    translated_text = translator.translate(caption.text, dest='fr').text
    translated_captions.append(translated_text)

    # Replace the original text with the translated text
    caption.text = translated_text

# Save the new VTT file with translated captions
captions.save('C:\\Users\\andre\\Downloads\\translated_captions.vtt')