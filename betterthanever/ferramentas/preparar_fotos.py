#!/usr/bin/env python3
"""Prepara as fotos de um produto para o site.

Uso:
  python3 ferramentas/preparar_fotos.py <pasta-com-fotos-originais> <slug> [--sem-corte]

- Gira conforme o celular gravou (EXIF), corta em quadrado (1:1) centralizado
  ou, com --sem-corte, encaixa num quadrado com fundo rosa claro.
- Redimensiona para 1200x1200, salva JPG qualidade 85 em fotos/<slug>-1.jpg, -2.jpg...
- Remove TODOS os metadados (inclusive localização GPS das fotos do celular).
- Aceita JPG, PNG, WEBP e HEIC (HEIC precisa de: pip install pillow-heif).
Imprime a lista de arquivos pronta para colar em `fotos: [...]`.
"""
import sys, pathlib
from PIL import Image, ImageOps

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

LADO, FUNDO = 1200, (251, 246, 247)  # --bg do site (Ever)
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif"}

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(__doc__)
    origem, slug = pathlib.Path(args[0]), args[1]
    sem_corte = "--sem-corte" in sys.argv
    destino = pathlib.Path(__file__).resolve().parent.parent / "fotos"
    destino.mkdir(exist_ok=True)
    arquivos = sorted(p for p in origem.iterdir() if p.suffix.lower() in EXTS)
    if not arquivos:
        sys.exit(f"Nenhuma foto em {origem}")
    nomes = []
    for i, src in enumerate(arquivos, 1):
        img = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        if sem_corte:
            img = ImageOps.pad(img, (LADO, LADO), color=FUNDO)
        else:
            img = ImageOps.fit(img, (LADO, LADO), Image.LANCZOS)
        nome = f"{slug}-{i}.jpg"
        img.save(destino / nome, "JPEG", quality=85, optimize=True, progressive=True)  # sem exif
        nomes.append(nome)
        print(f"{src.name} -> fotos/{nome}")
    print("\nfotos: " + str(nomes).replace("'", '"'))

if __name__ == "__main__":
    main()
