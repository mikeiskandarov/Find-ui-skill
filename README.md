# Find UI

**Describe the interaction. Find the component. Check how it actually works.**

A Codex skill for finding UI components and interaction references across a curated collection of libraries. Ask in English or Russian; get a small, evidence-backed shortlist with direct links, source availability, and the adaptations you would need.

[Русская версия](README.ru.md) · [Browse the collection](references/index.md) · [Skill instructions](SKILL.md)

```text
$find-ui Find a code component that animates both inserted and removed lines.
```

## What it does

- Searches a local catalog first, using component names, behavior tags, and bilingual aliases.
- Checks promising candidates against current official documentation, source, and live demos when available.
- Recommends 1–3 useful options and distinguishes an exact match from a partial one.
- Separates public demos from public source code, and free components from paid ones.
- Reports what was actually verified and what remains uncertain.

A red-and-green code diff is not necessarily an animated edit transition. Find UI is designed to make distinctions like that before recommending a component.

## Install in Codex

Ask Codex:

```text
$skill-installer Install the skill from https://github.com/mikeiskandarov/Find-ui-skill
```

Or clone it into your personal skills directory (requires Git):

```sh
mkdir -p ~/.agents/skills
git clone https://github.com/mikeiskandarov/Find-ui-skill.git ~/.agents/skills/find-ui
```

If that directory already exists, inspect your existing installation before replacing it. For a project-only installation, use `.agents/skills/find-ui` inside that project instead.

Codex should discover the skill automatically; restart it if the skill does not appear. This skill runs only when explicitly invoked with `$find-ui`. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for installation locations and discovery behavior.

**Requirements:** Python 3 for the bundled local search helper. The helper uses only the standard library and needs no API keys or packages. Full verification needs an agent with web access; checking animation requires browser interaction. Without those tools, results remain catalog-based and must be labeled unverified.

## Try it

```text
$find-ui Найди компонент со стадиями работы AI-агента: ожидание, выполнение, успех и ошибка.

$find-ui Find a tactile toggle with a spring animation and public source.

$find-ui Найди чатовый инпут с вложениями и выбором модели.

$find-ui Find an animated code diff. Check whether deleted lines animate out.
```

The agent should explain why the strongest match fits, link directly to it, state source access and verification status, and describe any necessary adaptation. It can add up to two materially different alternatives.

## The collection

The bundled **2026-10-15 snapshot contains 832 records**: 704 component, example, and variant entries across 13 primary libraries, plus 115 beUI Pro families and 13 Motion-Primitives Pro categories. Records are not all individual components, and the snapshot does not mean every demo has been tested.

| Library | Focus |
| --- | --- |
| prompt-kit | AI chat, composers, reasoning |
| trove/cn | AI workspaces, selection, morphing |
| interior.dev | Microinteractions, task steps, forms |
| AICSS | AI states, diffs, input, approvals |
| Fluid Functionalism | Tactile controls, forms, chat |
| Motion-Primitives | Typography, transitions, springs |
| AI Elements / AI SDK | AI tools, artifacts, voice, workflows |
| Planes | Animated diffs, physics, WebGL, sections |
| beUI | Motion controls, agents, charts |
| Transitions.dev | CSS microinteractions, toggles, AI states |
| Beautiful UI | Compact AI interfaces, tables, code |
| Magic UI | Landing-page effects and typography |
| Bencho | Interactive blocks, physics, gestures |
| beUI Pro | Paid blocks, templates, illustration families |
| Motion-Primitives Pro | Paid landing-page categories |

[Coverage notes and counts](references/index.md) link to each library's sources. [21st and Libraries.dev](references/discovery.md) provide additional discovery maps. If the collection has no suitable match, the skill can search outside it and label those results.

## Search without an agent

From the repository directory:

```sh
python3 scripts/search.py "code diff line-add line-remove" --limit 5
python3 scripts/search.py "переключатель" --limit 5
python3 scripts/search.py "chat input" --library prompt-kit --limit 3
```

The helper prints JSON. It is an offline lexical search, not a semantic search engine or a demo verifier. A low score or an empty result is not proof that a suitable component does not exist.

## Update the catalog

```text
$find-ui update catalog
```

Updates happen only on an explicit request. Ordinary searches do not rewrite the catalog or start background synchronization. The [update procedure](references/update.md) covers source checks, record identities, coverage gaps, and verification dates.

## Scope

Searching is read-only. The skill does not install UI packages, change your project, purchase access, or implement components unless you separately request that work. The local helper performs no network requests and writes no files.

The repository contains discovery metadata and links, not the indexed libraries' implementation code. Each library retains its own license and access terms; public visibility of a demo does not grant rights to its source. This is an independent collection, with no implied affiliation or endorsement.

## Contributing

Found a broken link, stale entry, or useful library? Open an issue or pull request with the official source and the behavior you checked. For catalog changes, follow [the update procedure](references/update.md), preserve English descriptions and Russian/English aliases, and distinguish components from families or categories. Do not add paid source code, credentials, or private browsing data.

## Repository layout

```text
SKILL.md                 Agent workflow and recommendation rules
agents/openai.yaml       Codex metadata and explicit invocation policy
scripts/search.py        Dependency-free local search
references/index.md      Collection overview
references/libraries/    Per-library coverage notes and JSONL catalogs
references/vocabulary.json  Bilingual search vocabulary
references/verification.md Evidence and evaluation notes
references/update.md     Catalog maintenance procedure
```
