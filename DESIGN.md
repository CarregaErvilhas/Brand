# A linguagem de design

O que um site do grupo tem de ter para parecer do grupo, e o que fica à escolha de cada um. Um site novo segue tudo o que está marcado como regra.

## Regras técnicas

- **Sem build e sem CDN.** HTML, CSS e JavaScript servidos tal como estão, do próprio domínio. Fontes, scripts e imagens vêm da mesma origem, e a CSP é same-origin. Não há trackers nem scripts de terceiros.
- **Dois idiomas, português primeiro.** O O Carro Elétrico, o ohmigo, o Voltaria e o olh'o'posto põem a língua no URL: português em `/`, inglês em `/en/`. A língua vem do URL, não do browser, e as bandeiras levam à mesma página na outra língua. O Postos PT e o Comparador CEME trocam a língua na própria página. Um site novo põe a língua no URL.
- **Tema claro e escuro.** Sem nada guardado, a página segue o sistema (`prefers-color-scheme`). O botão do tema guarda a escolha em `localStorage`, na chave `<site>.theme` (`oce.theme`, `ohmigo.theme`, `voltaria.theme`). Um script pequeno no `<head>` aplica-a antes da primeira pintura, para não piscar.
- **Movimento reduzido.** Animações só com `prefers-reduced-motion: no-preference`.
- **Instalável.** Manifesto PWA, ícones e o botão "Instalar app" no rodapé, com o `install.js` do kit. Cada página traz o markup do botão e do diálogo na sua língua; o script só decide o que mostrar.

## Cor

- **Cada site tem uma cor, a da sua mascote** (`colour` no `group.json`). É o acento do site: ligações, botões e destaques.
- **Em tema escuro, o acento fica mais claro** para manter o contraste. Por exemplo, o azul do Voltaria `#2f5bd0` passa a `#8eaaff`, e o destaque do olh'o'posto `#2C4A6B` passa a `#93AAD6`.
- **Os neutros não são cinzentos puros.** Puxam para a cor do site ou para azul-ardósia (o escuro das mascotes é `#0f172a`).
- **Contraste WCAG AA** em texto e controlos, nos dois temas.

## Tipografia

- **Nunito** é a fonte do grupo. Vem no kit (`fonts/`, subconjunto latino, com a licença OFL) e é a do O Carro Elétrico, do Voltaria e do Postos PT. O ohmigo usa a fonte arredondada do sistema e cai para Nunito (`ui-rounded, "SF Pro Rounded", "Nunito", …`).
- **Dois sites usam outra fonte.** O Comparador CEME usa Inter e a fonte do sistema. O olh'o'posto usa Space Grotesk, Inter e JetBrains Mono.
- **Um site novo usa Nunito.**

## A página do grupo

Todos os sites têm uma página "O grupo". É o sítio onde o grupo mais se vê, por isso é igual em todos:

- **Os sites pela ordem do `group.json`,** cada um com a sua mascote ao lado de um balão, alternando os lados. O balão tem o nome, o endereço, a descrição e as ligações "Abrir o site" e "Código no GitHub".
- **A cor de cada entrada** é a `colour` desse site, numa variável `--c`.
- **O site em que estás** aparece no seu lugar, com "Estás aqui" no lugar da ligação.
- **O AmpereArchive não tem ligação para um site** (`private`). Mostra a `note` e "GitHub (privado, por agora)".
- **No topo,** a mascote do próprio site fala na primeira pessoa, com título, texto e balão próprios (ver `VOZ.md`).
- **O rodapé de todas as páginas** tem uma ligação para a página do grupo.

O protótipo é a página do O Carro Elétrico. Cada site desenha-a no seu estilo, mas os textos, a ordem, as mascotes e as cores vêm do kit.
