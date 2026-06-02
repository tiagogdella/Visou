from deep_translator import GoogleTranslator

def translate(text):
    return GoogleTranslator(source="en", target="pt").translate(text)