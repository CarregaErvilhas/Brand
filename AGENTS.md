# AGENTS.md

The group's brand: the guides (`VOZ.md`, `MASCOTES.md`, `NOMES.md`, `DESIGN.md`) and the kit (`group.json`, the mascots in `grupo/`, `install.js`, the Nunito font). README.md says what each file is and how the sites consume it.

- English for README, AGENTS, code comments and commits. The four guides are in pt-PT. `group.json` texts are pt-PT (current spelling, "MOBI.E") and British English.
- Write as `VOZ.md` says, here too. The guides describe what the sites do; where a site breaks a rule, say so in the guide rather than hiding it.
- Never invent where a name comes from. A blank in `NOMES.md` stays "(por preencher)" until the maintainer fills it.
- This repo is the owner. A site never edits its copy; it moves its `brand/` submodule pointer.
- After any change: `python3 check.py --write-sums`, then `python3 check.py`. CI runs the same check.
- `install.js` stays ASCII with English comments, byte-identical to what every site serves.
- Only shared facts go in `group.json`. A site's page voice (title, lead, bubble), markup and CSS stay in that site.
- Mascots are brands, outside the MIT licence. Never relicense them, never add a mascot without its site's say.
- Ship a change by tagging `vX.Y.Z` on `main`; untagged commits never reach the sites. Releases are the maintainer's call.
- Commits need `git commit -s` (DCO). Merges are by PR into a protected `main`.
- Public repo: no IPs, resource IDs, emails, account names, people's names or dates of our own changes.
