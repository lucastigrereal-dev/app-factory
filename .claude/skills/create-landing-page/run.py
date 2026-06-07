#!/usr/bin/env python3
"""Wrapper da skill create-landing-page — gera HTML via template local.

Uso:
    python run.py --nome "Pousada X" --oferta "Diaria especial" --preco "R$ 299"
"""
import argparse
import json
import sys
from pathlib import Path
from string import Template

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
TEMPLATE_PATH = REPO_ROOT / "templates" / "landing_page" / "index.html.jinja2"
ARTIFACTS_DIR = REPO_ROOT / "artifacts" / "create-landing-page"


def main():
    parser = argparse.ArgumentParser(description="Gera landing page para hotel")
    parser.add_argument("--nome", required=True, help="Nome do hotel/pousada")
    parser.add_argument("--oferta", default="Pacote exclusivo", help="Titulo da oferta")
    parser.add_argument("--preco", default="R$ 0,00", help="Preco exibido")
    parser.add_argument("--beneficios", default="Wi-Fi,Cafe da manha,Piscina", help="Lista separada por virgula (3 items)")
    parser.add_argument("--depoimento", default="Experiencia inesquecivel!", help="Depoimento de cliente")
    parser.add_argument("--autor", default="Cliente satisfeito", help="Autor do depoimento")
    parser.add_argument("--endereco", default="Natal, RN", help="Endereco do hotel")
    parser.add_argument("--whatsapp", default="+5584999999999", help="WhatsApp com codigo do pais")
    parser.add_argument("--cta", default="Reservar Agora", help="Texto do botao CTA")
    parser.add_argument("--cta-link", default="#oferta", help="Link do botao CTA")
    parser.add_argument("--tagline", default="Sua escapada perfeita comecaa aqui", help="Tagline do hero")
    parser.add_argument("--hero", default="https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1600", help="URL imagem hero")
    args = parser.parse_args()

    # Flat mapping para string.Template
    b = [x.strip() for x in args.beneficios.split(",")]
    mapping = {
        "hotel_nome": args.nome,
        "oferta_principal": args.oferta,
        "preco": args.preco,
        "tagline": args.tagline,
        "hero_imagem": args.hero,
        "cta_texto": args.cta,
        "cta_link": args.cta_link,
        "beneficio1": b[0] if len(b) > 0 else "Beneficio 1",
        "beneficio2": b[1] if len(b) > 1 else "Beneficio 2",
        "beneficio3": b[2] if len(b) > 2 else "Beneficio 3",
        "icone1": "&#9733;",
        "icone2": "&#9733;",
        "icone3": "&#9733;",
        "desc1": "",
        "desc2": "",
        "desc3": "",
        "incluso1": "Cafe da manha incluso",
        "incluso2": "Wi-Fi Premium",
        "incluso3": "Cancelamento gratis",
        "incluso4": "Late check-out",
        "depoimento": args.depoimento,
        "autor_depoimento": args.autor,
        "endereco": args.endereco,
        "whatsapp": args.whatsapp,
    }

    template = Template(TEMPLATE_PATH.read_text(encoding="utf-8"))
    rendered = template.safe_substitute(mapping)

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = ARTIFACTS_DIR / "index.html"
    out_path.write_text(rendered, encoding="utf-8")

    result = {
        "status": "ok",
        "artefato": str(out_path),
        "tamanho_bytes": len(rendered.encode("utf-8")),
        "proxima_acao": "Abra no browser: " + str(out_path),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
