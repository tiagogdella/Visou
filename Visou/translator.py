from deep_translator import GoogleTranslator
#Tradutor do Google

def translate(text):
    return GoogleTranslator(source="en", target="pt").translate(text)
    #faz a trad.