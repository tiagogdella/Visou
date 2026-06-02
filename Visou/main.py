import sys
import subprocess
from descriptor import descripting
from translator import translate
from speaker import speak
from playsound import playsound


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
    #MacOS
    subprocess.run("afplay", output_path)
    #Windows
    playsound(output_path)

if __name__ == "__main__":
    main(sys.argv[1])
          