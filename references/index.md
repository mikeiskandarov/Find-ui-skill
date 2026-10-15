# Curated UI collection

Verified: 2026-10-15. The 13 primary libraries contain 704 component, example and variant records. Additional coverage includes 115 beUI Pro families and 13 Motion-Primitives Pro categories. 21st and Libraries.dev have discovery maps rather than recursive component inventories.

| Library | Best for | Records |
|---|---|---:|
| [prompt-kit](libraries/prompt-kit.md) | AI chat, messages, composers, reasoning | 23 |
| [trove/cn](libraries/trove.md) | AI workspaces, controls, selection, morph | 31 |
| [interior.dev](libraries/interior.md) | Microinteractions, task steps, forms, navigation | 54 |
| [AICSS](libraries/aicss.md) | AI states, diff, input, approvals | 18 |
| [Fluid Functionalism](libraries/fluid.md) | Forms, tactile controls, chat, sidebar | 55 |
| [Motion-Primitives](libraries/motion-primitives.md) | Transitions, typography, morph, spring, hover | 33 |
| [AI Elements / AI SDK](libraries/ai-elements.md) | AI apps, tools, artifacts, voice, workflows | 49 |
| [Planes](libraries/planes.md) | AI, animated diff, WebGL, physics, sections | 142 |
| [beUI](libraries/beui.md) | Motion controls, agents, charts, blocks | 107 |
| [Transitions.dev](libraries/transitions.md) | CSS microinteractions, toggle, AI states | 43 |
| [Beautiful UI](libraries/beautiful-ui.md) | Compact AI interfaces, tables, code | 21 |
| [Magic UI](libraries/magic-ui.md) | Landing pages, decorative effects, typography | 78 |
| [Bencho](libraries/bencho.md) | Interactive blocks, physics, gestures, controls | 50 |
| [beUI Pro](libraries/beui-pro.md) | Paid blocks, pages, templates, illustrations | 115 |
| [Motion-Primitives Pro](libraries/motion-pro.md) | Paid landing page sections | 13 |

[21st and Libraries.dev](discovery.md). [Bilingual query vocabulary](vocabulary.json). [Verification notes](verification.md).

## Favorite direct links

- [interior.dev — Task Steps](https://www.interior.dev/docs/task-steps)
- [AICSS — File Diff](https://www.aicss.dev/components/file-diff)
- [Magic UI — Marquee](https://magicui.design/docs/components/marquee): preserved as a favorite; the library itself is deduplicated.
- [AI SDK](https://ai-sdk.dev/): discover UI in AI Elements and consult the SDK for integration.

The collection originated in a personal bookmark folder named DE. The ChatGPT conversation bookmark was excluded. No personal chats, browser history, account data or machine-specific paths are part of the catalog.

## Record format

`name`, `section`, `description`, `tags`, `synonyms_ru`, `synonyms_en`, `url`, `source`, `evidence` are required. `source.access` is `public` or `pro`; read `source.availability` for per-item uncertainty. A public demo does not imply publicly available code. `source.url` points to the code-bearing documentation/registry or, for paid entries, the public access page. `evidence.index` identifies the inventory source; `evidence.checked` dates the snapshot and `evidence.note` limits what was actually verified. `kind` distinguishes families/categories from individual components. Fluid's `registry_id` distinguishes variants sharing a title or URL.
