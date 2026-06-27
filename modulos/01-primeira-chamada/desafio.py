"""
DESAFIO 01 — Faça sua própria pergunta

Complete os TODOs. Rode com:
    python modulos/01-primeira-chamada/desafio.py
"""

from mock_anthropic import Anthropic

client = Anthropic()

# TODO 1: crie a chamada à API.
#   Dica: copie a estrutura do exemplo.py
#   Use model="claude-sonnet-4-6" e max_tokens=200
#   Na mensagem, pergunte algo que VOCÊ queira saber.
resposta = None  # <-- substitua isto

# TODO 2: imprima só o texto da resposta.
#   Dica: está em resposta.content[0].text

# TODO 3: imprima quantos tokens de saída foram usados.
#   Dica: resposta.usage.output_tokens