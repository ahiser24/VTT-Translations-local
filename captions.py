def translate_captions(source_lang, dest_lang):
    try:
        import webvtt
    except ModuleNotFoundError:
        print("Please install the 'webvtt' library.")
    from googletrans import Translator

    captions = webvtt.read('C:\\Users\\andre\Downloads\\captions.vtt')
    translator = Translator()
    translated_captions = []

    for caption in captions:
        translated_text = translator.translate(caption.text, src=source_lang, dest=dest_lang).text
        translated_captions.append(translated_text)
        caption.text = translated_text

    captions.save(f'C:\\Users\\andre\\Downloads\\translated_captions_{dest_lang}.vtt')

    return translated_captions

translated_captions_cn = translate_captions('en', 'zh-CN')
translated_captions_es = translate_captions('en', 'es')
translated_captions_es = translate_captions('en', 'pt')