import asyncio
import edge_tts

VOICE = "pt-BR-FranciscaNeural"

def speak(text, output_path):
    async def _generate():
        communication = edge_tts.Communicate(text, VOICE)
        await communication.save(output_path)
    asyncio.run(_generate())