from PIL import Image
#Bib para manipular imagens
from transformers import BlipProcessor, BlipForConditionalGeneration
#transformers Bib da HUgging Face da acesso a APIs de IAs

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
#prepara a img para um formato que a IA entende: numeros e tensores
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
#rende neural em si que gera a descrição

def descripting(img_path):
    img = Image.open(img_path).convert("RGB")
    #abre img e converte para RGB que BLIP trabalho melhor
    inputs = processor(img, return_tensors="pt")
    #transforma a img em tensores(matrizes de num.)
    output = model.generate(**inputs, max_new_tokens=50, repetition_penalty=1.5)
    #gera descr. em ingles | limita a 50 linhas | penaliza rep. palavras
    return processor.decode(output[0], skip_special_tokens=True)
    #decode retorna numeros em Strings legiveis novamente | remove carac. inu.