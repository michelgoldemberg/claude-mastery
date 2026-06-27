# Módulo 01 — Primeira chamada

## A analogia
Falar com o Claude pela API é como mandar uma carta. Você escreve uma
**mensagem** (`messages`), diz quem está falando (`role`), escolhe o
"cérebro" que vai responder (`model`) e define um limite de tamanho
pra resposta (`max_tokens`). A API devolve a resposta + um recibo
(`usage`) dizendo quanto "custou".

## Por que importa
Tudo no Claude — system prompts, memória, ferramentas, agentes —
é construído em cima dessa única chamada. Domine ela e o resto encaixa.

## Como rodar
python modulos/01-primeira-chamada/exemplo.py

## Experimente quebrar
1. Troque `max_tokens=300` por `max_tokens=5`. O que muda na resposta?
2. Adicione uma segunda mensagem na lista `messages`. O que acontece?
3. Mude o texto da pergunta e veja a resposta refletir isso.