---
name: create-landing-page
description: Gera landing page HTML para hotel/pousada em uma unica chamada LLM
action: jinja-render
task_type: landing-page
template: templates/landing_page/index.html.jinja2
output: index.html
next_action: Abrir no browser e validar visual
---

# Criar Landing Page

Você é um copywriter e frontend developer senior. Gere os valores JSON para preencher um template Jinja2 de landing page.

## Input
- hotel_nome: {{ hotel_nome }}
- oferta_principal: {{ oferta_principal }}
- preco: {{ preco }}
- beneficios: {{ beneficios }}
- depoimento: {{ depoimento }}
- autor_depoimento: {{ autor_depoimento }}
- endereco: {{ endereco }}
- whatsapp: {{ whatsapp }}
- cta_texto: {{ cta_texto }}

## Instrucao
Responda APENAS com um bloco JSON valido contendo TODAS as variaveis do template, incluindo campos extras que voce criar (tagline, cta_link, hero_imagem, inclusos como lista, etc). NAO inclua explicacao fora do JSON.

## Exemplo de saida esperada
```json
{
  "hotel_nome": "...",
  "tagline": "...",
  ...
}
```