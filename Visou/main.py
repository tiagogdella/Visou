import sys
# acessa inf. do sistema: pegar img passada no terminal
import subprocess
#permite rodar outros prog. do SO dentro do python
from descriptor import descripting
from translator import translate
from speaker import speak

def main(img_path):
    print("Descrevendo imagem...")
    description = descripting(img_path)
    print(f"Descrição (EN): {description}")

    print("Traduzindo...")
    translation = translate(description)
    print(f"Tradução (PT-BR): {translation}")

    output_path = "outputs/descricao.mp3"
    print("Gerando áudio...")
    speak(translation, output_path)

    print("Reproduzindo...")
    if sys.platform == "darwin":
        subprocess.run(["afplay", output_path]) # macOS
    elif sys.platform == "win32":
        subprocess.run(["start", output_path], shell=True) # Windows
    else:
        subprocess.run(["mpg123", output_path]) # Linux

if __name__ == "__main__":
    #garante que só execute se for o arq. principal
    #ou seja só roda se importar o arquivo completo
    main(sys.argv[1])
    #pega o primeiro arg. passado no terminal
    #roda assim: python3 main.py (arquivo)
          