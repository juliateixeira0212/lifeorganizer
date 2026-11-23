---
name: descrever-produto
description: Olha as fotos de um desapego (bolsa, relógio, eletrônico...) e escreve o anúncio do site betterthanever.club — nome, descrição, estado, o que acompanha — e a legenda do Instagram. Use quando a Julia mandar fotos de um produto novo ou pedir para descrever/anunciar um item.
argument-hint: "<pasta-das-fotos ou link do Drive> [slug]"
---

# Descrever produto a partir das fotos

Objetivo: transformar fotos cruas em um anúncio honesto e bonito no `betterthanever/index.html`
e numa legenda pronta para o Instagram. Tom: pessoal, leve, confiável — é um desapego de
alguém que cuidou bem da peça, não uma loja.

## 1. Pegar as fotos
- Pasta no repositório ou enviada na conversa: use direto.
- Link/pasta do Google Drive: baixe com as ferramentas do Google Drive para uma pasta nova no
  scratchpad (uma pasta só para isso).
- Defina o `slug` (curto, minúsculo, com hífen: `ysl-loulou-preta`, `apple-watch-s9`).

## 2. Olhar TODAS as fotos com atenção (Read em cada imagem)
Anote o que dá para **ver**:
- Marca, linha/modelo, cor, material, ferragens (dourada/prata), tamanho aparente.
- Etiquetas internas, número de série/código de data (não publique o número completo — só
  "código interno visível nas fotos").
- Estado real: cantos, alças, costuras, interior, riscos na tela/caixa, manchas. Seja
  específica e honesta — isso evita devolução e passa confiança.
- O que acompanha: caixa, dust bag, nota, cartão, carregador, pulseiras extras.
- Apple Watch: geração/tamanho se aparecer em Ajustes > Geral > Sobre; saúde da bateria se
  houver print.

## 3. Perguntar só o que não dá para ver
Em UMA mensagem curta, peça o que faltar: preço em R$ e €, preço de loja (opcional),
saúde da bateria, garantia, se tem nota, medidas se o modelo não for identificável.
Se o usuário já disse ou pediu para não perguntar, marque o campo com `[confirmar]`.
Nunca invente: modelo incerto → escreva o que é certo ("bolsa de ombro em couro
matelassê") e marque `[confirmar modelo]`. Medidas do site oficial podem ser usadas para um
modelo identificado com certeza, indicadas como "medidas do modelo".

## 4. Preparar as fotos
```
python3 betterthanever/ferramentas/preparar_fotos.py <pasta> <slug>
```
(use `--sem-corte` se o produto ficar cortado no quadrado). O script remove localização GPS
e outros metadados — sempre rode antes de publicar. Ordene para que a 1ª foto seja a mais
bonita (frente da peça, fundo limpo); as de defeitos vão por último.

## 5. Escrever no site
Edite o array `PRODUTOS` em `betterthanever/index.html` (adicionar novo item ou substituir
um exemplo). Campos:
- `marca`, `nome` (modelo + tamanho + cor/material, ≤ 55 caracteres)
- `descricao`: 2–3 frases. 1ª: o que é e por que é especial. 2ª: estado honesto, citando
  qualquer sinal de uso ("ver foto 5"). 3ª opcional: motivo do desapego / cuidado.
- `detalhes`: 3–4 pares, ex. `Estado`, `Acompanha`, `Medidas`, `Garantia`, `Bateria`.
  Escala de estado: Novo com etiqueta · Excelente · Muito bom · Bom.
- `fotos`: a lista que o script imprimiu.
- `precoBRL`, `precoEUR`, `precoOriginalEUR` (ou `null`), `parcelas: 0` (ainda não há parcelamento; só pôr 12 quando ela tiver)
- `linkBRL`/`linkEUR`: manter vazios se não houver; nunca inventar link.
- `status: "disponivel"`

## 6. Legenda do Instagram
Entregue no chat, pronta para copiar:
```
✨ desapego: <marca> <modelo>
<1 frase sobre a peça>
Estado: <...> · Acompanha: <...>
R$ <preço> (Pix) · € <preço>
🔗 link na bio → shop.betterthanever.club
```
Mais uma variação curta para stories (≤ 2 linhas).

## 7. Conferir e salvar
- Abra a página no Playwright em tamanho iPhone e veja o card novo (screenshot só para você).
- Resuma em 3–5 linhas o que escreveu e liste tudo marcado `[confirmar]`.
- Commit no branch de trabalho e push.
