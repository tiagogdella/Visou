# Visou

Sistema de audiodescrição automática de imagens para acessibilidade visual.
Projeto final da disciplina de Sistemas Multimídia (CIT7596) — UFSC Araranguá, 2026.1.

## Problema

Segundo o IBGE, mais de 6 milhões de brasileiros possuem algum grau de
deficiência visual. No cotidiano digital, essas pessoas enfrentam uma barreira
constante: imagens compartilhadas em redes sociais, aplicativos de mensagem,
sites e documentos raramente vêm acompanhadas de descrições textuais. O
resultado é a exclusão silenciosa de parte significativa da comunicação
contemporânea, que se apoia cada vez mais em conteúdo visual.

A solução manual — pedir que alguém descreva cada imagem — é inviável em
escala. É preciso uma ferramenta automática que torne o conteúdo visual
acessível de forma imediata e independente.

## Solução

Aplicação em Python que recebe uma imagem, gera automaticamente uma descrição
textual de seu conteúdo, traduz a descrição para o português e a converte em
áudio com voz natural. O resultado é um arquivo de áudio que descreve a
imagem, permitindo que pessoas com deficiência visual compreendam seu
conteúdo de forma autônoma.

O pipeline integra três mídias — imagem, texto e áudio — caracterizando um
sistema multimídia completo.

## Tecnologias

- **Python 3.10+**
- **Transformers (Hugging Face)** — carregamento do modelo de legendagem
  pré-treinado BLIP (Salesforce)
- **PyTorch** — backend do modelo de IA
- **Pillow** — manipulação e pré-processamento de imagens
- **deep-translator** — tradução automática da descrição para o português
- **edge-tts** — síntese de voz neural (vozes em português brasileiro de
  alta qualidade)
- **playsound** ou **pygame** — reprodução do áudio gerado

## Metodologia

1. **Carregamento da imagem** — a imagem é lida e convertida para o formato
   esperado pelo modelo (RGB, redimensionada se necessário).
2. **Geração da descrição em inglês** — o modelo BLIP analisa a imagem e
   produz uma frase descritiva em inglês.
3. **Tradução para o português** — a descrição é traduzida automaticamente
   para o português brasileiro.
4. **Síntese de voz** — o texto traduzido é convertido em áudio usando uma
   voz neural em português (Francisca ou Antonio, da Microsoft).
5. **Reprodução** — o áudio é tocado automaticamente ou salvo em arquivo
   para uso posterior.

## Estrutura prevista

```
vozparaver/
├── imagens_teste/                 # imagens para demonstração
├── saidas/                        # áudios gerados
├── audiodescrever.py              # script principal
├── descritor.py                   # módulo de geração da descrição
├── tradutor.py                    # módulo de tradução
├── narrador.py                    # módulo de síntese de voz
├── requirements.txt
└── README.md
```

## Resultados esperados

- Descrições coerentes e relevantes para a maioria das imagens cotidianas
  (paisagens, pessoas, animais, objetos, cenas).
- Áudio em português brasileiro com voz natural, compreensível em uma única
  audição.
- Tempo total de processamento inferior a 10 segundos por imagem em um
  notebook comum, sem necessidade de GPU.
- Funcionamento offline após o download inicial do modelo (com exceção da
  tradução e da síntese de voz, que podem usar conexão).

## Cronograma

| Etapa | Prazo |
|---|---|
| Configuração do ambiente e download do modelo BLIP | Semana 1 |
| Implementação do pipeline imagem → texto → tradução | Semana 2 |
| Integração da síntese de voz e ajustes | Semana 3 |
| Documento final, prints e testes com imagens variadas | Semana 4 |
| **Entrega** | **17/06/2026** |

## Limitações conhecidas

- Imagens muito abstratas, artísticas ou de baixa qualidade podem gerar
  descrições imprecisas.
- Os modelos pré-treinados foram majoritariamente treinados em datasets em
  inglês, o que pode introduzir viés cultural nas descrições.
- A tradução automática pode eventualmente produzir frases pouco naturais.
- O sistema descreve o conteúdo geral da imagem, não identifica pessoas
  específicas nem lê texto presente em imagens (OCR seria uma extensão
  futura).

## Referências

- LI, J. et al. *BLIP: Bootstrapping Language-Image Pre-training for Unified
  Vision-Language Understanding and Generation.* ICML, 2022.
- INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA. *Pessoas com Deficiência:
  Censo Demográfico 2022.* IBGE, 2023.
- Hugging Face Transformers. Documentação oficial. Disponível em:
  https://huggingface.co/docs/transformers
- Microsoft Edge TTS. Documentação. Disponível em:
  https://github.com/rany2/edge-tts

---

**Autor:** Tiago Ghellere Della
**Disciplina:** Sistemas Multimídia (CIT7596)
**Professora:** Marina Carradore Sérgio
