# Brand

The O Carro Elétrico group's brand: how the sites speak, look and name things, and the shared web furniture (the group page's text and site order, the mascots, the "Instalar app" script and the Nunito font). One copy here; every site serves its own copy from its own origin, because their content security policies are same-origin and none of them has a build step that could fetch from elsewhere.

## The guides

In European Portuguese, like the sites:

| File | What |
| --- | --- |
| [`VOZ.md`](VOZ.md) | The voice: who speaks, the rules, the mascot speaking in the first person, spelling and names, what is banned |
| [`MASCOTES.md`](MASCOTES.md) | How the mascots are drawn (the shared grammar), each one described, and how to make a new one |
| [`NOMES.md`](NOMES.md) | Where each site's and mascot's name comes from, and how it is written |
| [`DESIGN.md`](DESIGN.md) | The design language: technical rules, colour, type, the group page |

## The files

| Path | What | Used by |
| --- | --- | --- |
| `group.json` | The group's sites in page order: id, pt/en name, host, site and repo URL, `private` flag, colour (the mascot's, the site's accent), pt/en description (`desc`), short line (`short`), note (`note`), mascot file, name (where it has one), size and pt/en alt text. Also the four shared labels (`open`, `here`, `code`, `private`) | Every group page |
| `grupo/*.svg` | One mascot per site, plus `pano.svg`, the Panoramax logo | Every group page |
| `install.js` | "Instalar app": puts the site on the home screen as a PWA. Each page brings its own markup; the script only decides what to show | The sites with an install button |
| `fonts/nunito-latin.woff2`, `fonts/OFL-Nunito.txt` | Nunito, latin subset, with its licence | The sites set in Nunito |
| `SHA256SUMS` | sha256 of every file above | `check.py` |
| `check.py` | Checks the kit, or a site's copy of it | CI here and in each site |

A site's own voice stays in the site: the group page's title, lead and speech bubble, its markup and its CSS. `group.json` holds only what must read the same everywhere.

## How a site uses it

1. Add this repo as a submodule at `brand/`, and a `gitsubmodule` entry in the site's `.github/dependabot.yml`.
2. Serve the files at the paths the site already uses, laid out like this repo (`grupo/`, `install.js`, `fonts/`). Where the site has a build or deploy step, copy them from `brand/` there; otherwise keep a committed copy.
3. In CI, check out with submodules and run `python3 brand/check.py --against <served dir> <parts>`, where parts are any of `grupo`, `install`, `fonts`. It fails on a missing or different file and names it.
4. Read the texts and the order from `brand/group.json` instead of writing them into the page.

The check compares against the submodule's pinned commit, never against this repo's latest, so a release here never turns a site red. A site moves when its submodule pointer moves.

## Releases

A release is a `vX.Y.Z` tag on `main`. Dependabot's `gitsubmodule` updater proposes the newest semver tag on the tracked branch, not the branch head, so a site's weekly update PR moves only between releases.

- Once any tag exists, commits on `main` after the last tag never reach the sites. Tag to ship.
- Major: removing or renaming a file, or a breaking change to `group.json` (bump its `schema`). Minor: a new site, mascot or field. Patch: text and drawing fixes.

## Changing something

1. Edit the file. For a new site: add its mascot to `grupo/` and its entry to `group.json`, in page order.
2. `python3 check.py --write-sums`, then `python3 check.py`.
3. Commit with `git commit -s` (see [Contributing](#contributing)).

`install.js` stays ASCII with English comments, so it is byte-identical on every site.

## Licences

- Code and text (`install.js`, `check.py`, `group.json`, the docs): [MIT](LICENSE).
- **The mascots are not licensed.** Each file in `grupo/` is the brand of its own site of the group and may not be reused apart from a link to that site. `grupo/pano.svg` is the logo of the [Panoramax](https://panoramax.fr/) project, under that project's terms.
- Nunito: [SIL Open Font License 1.1](fonts/OFL-Nunito.txt), shipped next to the font. A site that serves the font serves the licence with it.

## Contributing

Every commit carries a `Signed-off-by` line ([Developer Certificate of Origin](https://developercertificate.org/)); `git commit -s` adds it. CI checks it with the group's shared DCO workflow.
