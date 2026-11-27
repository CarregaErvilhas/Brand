# As mascotes

Cada site do grupo tem uma mascote: o objeto do seu ofício, com cara. Os desenhos estão em `grupo/`, e o texto alternativo de cada um, em pt e en, está no `group.json` (`mascot.alt`). As mascotes são marcas: ficam fora das licenças (ver o README).

## A gramática comum

As mascotes parecem da mesma família porque seguem as mesmas regras:

- **Corpo:** o objeto, com cantos arredondados, na cor do site (`colour` no `group.json`). Por cima, um brilho branco em gradiente diagonal, do canto de cima à esquerda até ao meio, de opacidade 0,3 a 0,35 até 0.
- **Olhos:** duas elipses verticais `#0f172a`, cada uma com um reflexo branco em cima, à direita. São iguais em todas as mascotes.
- **Bochechas:** duas elipses rosadas por baixo dos olhos, `#fb7185` com opacidade de 0,55 a 0,6. Num corpo cor-de-rosa, usa-se um rosa mais claro (`#fda4af` na calculadora). O pino do Postos PT não tem bochechas.
- **Boca:** um sorriso aberto, traço `#0f172a` com pontas redondas e boca `#7f1d1d`.
- **O raio:** amarelo `#facc15` com contorno `#ca8a04` de 3 px. É a marca do grupo e aparece em todas as mascotes menos no Pic: no corpo, num ecrã ou numa capa.
- **Braços,** quando os há: traços grossos com pontas redondas, num tom mais escuro da cor do corpo, com uma mão em círculo. O Ohmi e o livro acenam.
- **Sombra no chão:** uma elipse achatada por baixo, `#0f172a` com opacidade 0,12.
- **Animação:** só pestanejar (`class="blink"`) e acenar (`arm-wave`, `wave-book`). Mexe só com `prefers-reduced-motion: no-preference`.
- **Tamanho:** o `viewBox` tem cerca de 260 × 300, ao alto. O `group.json` guarda a largura e a altura de cada uma, e o `check.py` confirma que batem certo com o `viewBox`.

## Uma a uma

| Mascote | Site | Como é | Cor |
| --- | --- | --- | --- |
| O carrinho repórter | O Carro Elétrico | Carro laranja com chapéu de imprensa e microfone: vai entrevistar e explica | `#ff6b4a` |
| O Ohmi | ohmigo | Ficha elétrica verde com dois pinos cinzentos e o cabo atrás, a acenar | `#22c55e` |
| O livro | Voltaria | Livro azul de capa dura, páginas creme, marcador amarelo e o raio na capa, a acenar | `#2f5bd0` |
| A calculadora | Comparador CEME | Calculadora cor-de-rosa com o raio no ecrã | `#db2777` |
| O pino | Postos PT | Pino de mapa azul com cara e um raio | `#0284c7` |
| O Pic | olh'o'posto | Ficha Type 2 âmbar com os 7 pinos, a objetiva no pino de terra, o obturador e o flash no topo | `#f2b33d` |
| A caixa de arquivo | AmpereArchive | Caixa de arquivo roxa, de óculos, com um cronómetro | `#8b5cf6` |
| (logótipo) | Panoramax | O logótipo do projeto Panoramax, sem cara: não é nosso e não se mexe | `#8f2a85` |

**O Pic é a exceção.** Tem paleta própria (corpo `#F2B33D`, face `#15201C`, destaque `#2C4A6B`, objetiva `#E6E9EE`) e, em vez do raio, os raios do flash. Em tema escuro, o destaque passa a `#93AAD6`. As versões, os ícones e as regras dele estão em `Design/marca/LEIA-ME.md` no repositório do olh'o'posto.

## Uma mascote nova

1. Escolhe o objeto do ofício do site, que se reconheça em 32 px.
2. Aplica a gramática comum: corpo na cor do site, olhos, bochechas, sorriso e o raio.
3. Escolhe uma cor que não se confunda com as da tabela, nos dois temas.
4. Escreve o texto alternativo em pt e en, no molde "O/A <objeto> do <site>, <cor>, com <o que a distingue>".
5. Junta o ficheiro a `grupo/`, a entrada ao `group.json` e corre o `check.py`.
