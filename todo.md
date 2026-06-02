# Visou — Todo

## Semana 1 — Configuração

- [ ] Configurar ambiente: criar virtualenv, instalar dependências (transformers, torch, pillow, deep-translator, edge-tts, pygame) e gerar `requirements.txt`
- [ ] Criar estrutura de pastas do projeto: `vozparaver/`, `imagens_teste/`, `saidas/`

## Semana 2 — Pipeline principal

- [ ] Implementar `descritor.py`: carregar modelo BLIP (`Salesforce/blip-image-captioning-base`) e gerar descrição em inglês a partir de uma imagem
- [ ] Implementar `tradutor.py`: receber texto em inglês e retornar tradução para português brasileiro usando `deep-translator`
- [ ] Implementar `narrador.py`: receber texto em português e gerar arquivo de áudio `.mp3` com `edge-tts` (voz `pt-BR-FranciscaNeural` ou `pt-BR-AntonioNeural`)

## Semana 3 — Integração e testes

- [ ] Implementar `audiodescrever.py`: script principal que orquestra o pipeline imagem → descrição → tradução → áudio → reprodução
- [ ] Adicionar imagens de teste variadas em `imagens_teste/` (paisagens, pessoas, animais, objetos, cenas)

## Semana 4 — Validação e entrega

- [ ] Testar pipeline completo com as imagens de teste, verificar qualidade das descrições e do áudio gerado
- [ ] Medir tempo de processamento por imagem e validar se fica abaixo de 10 segundos
- [ ] Escrever `README.md` final com instruções de uso, prints de saída e resultados dos testes
- [ ] Preparar entrega: revisar código e completar documento final da disciplina (CIT7596)

---

**Prazo de entrega: 17/06/2026**
**Disciplina:** Sistemas Multimídia (CIT7596) — UFSC Araranguá
**Professora:** Marina Carradore Sérgio
