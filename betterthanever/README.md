# betterthanever.club

Site estático de uma página (só `index.html`) para os desapegos.

## Editar
Abra `index.html` e mexa só no bloco **EDITE AQUI**:
- `CONTATO.instagram` / `CONTATO.whatsapp`
- cada produto: nome, preços (R$ e €), descrição, detalhes, `fotos` (arquivos na pasta `fotos/`), `linkBRL`, `linkEUR`, `status` (`disponivel` | `reservado` | `vendido`).

Os botões "Pagar" só aparecem quando o link correspondente está preenchido.
Fotos: quadradas (1:1), ~1200px, JPG. `fotos/capa.jpg` vira a imagem de prévia no Instagram/WhatsApp.

## Publicar no domínio
Opção mais simples: Netlify ou Cloudflare Pages → arrastar esta pasta → adicionar o domínio
`betterthanever.club` e apontar o DNS conforme o painel indicar. O arquivo `CNAME` já está pronto
caso prefira GitHub Pages.
