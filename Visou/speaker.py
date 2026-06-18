import asyncio
#bib para rodar codigo Assíncrono
import edge_tts
#bib para acessar serviço de voz neural da Microsoft

VOICE = "pt-BR-FranciscaNeural"
#Escolhendo a voz pré-pronta

def speak(text, output_path):
    async def _generate():
        communication = edge_tts.Communicate(text, VOICE)
        #converte o texto com a vóz
        await communication.save(output_path)
        #manda e aguarda até a Microsoft retornar a requisição
    asyncio.run(_generate())