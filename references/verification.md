# Evidence and evaluation notes

Snapshot: 2026-10-15. Catalog membership was checked against the official indexes documented per library. This is not a claim that all 832 entries were manually exercised. It contains 704 primary-library entries, 115 beUI Pro families and 13 Motion-Primitives Pro categories. See individual coverage notes for limits.

## Code changes

- **Planes → Inline Diff**: the strongest catalog candidate for animated code edits. Documentation describes strike-through removals, blurred progressive additions, context folding and Accept/Reject collapse. Replay and intermediate diff states were viewed in Chrome. Accept/Reject and licensed implementation were not verified. Source is **Pro**. Do not call this token-level code morphing without further evidence.
- **beUI → File Diff / Code Block**: public docs/source support progressive row reveal and following scroll. This is a useful free partial match, but rendering red deleted rows does not establish animated deletion between versions.
- **AICSS → File Diff**: inspected as a static diff card. **Beautiful UI → Code Block** and **Magic UI → Code Comparison** are comparison/listing candidates; dynamic edit transitions are unconfirmed.

Find the records using `code diff line-add line-remove version-transition`. Evaluate actual deletion, not merely the presence of red and green lines.

## AI task steps

**interior.dev → Task Steps** exposes `pending`, `active`, `done`, and `error`. The Chrome demo replay showed Queued followed by Building with the previous step checked. Source exposes `steps`, `current`, and `failed`, including reduced-motion handling. Applications must wire real execution events themselves. Consider trove/cn Agent Activity for richer traces and AI Elements Task/Plan for SDK-oriented interfaces.

## Interactive toggle

**Transitions.dev → Toggle** was toggled off → on in Chrome. Its public CSS/React code defines thumb keyframes and a reduced-motion guard. Keyboard behavior and the reduced-motion path were not separately tested. For alternatives, search Fluid Switch, beUI Switch and Bencho Liquid toggle; do not assume they share the same motion or accessibility behavior.

## Failure cases

- No exact match: a request for a volumetric medical image editor has no exact catalog entry. Do not present a generic Image Viewer as equivalent; label a partial match or search externally.
- Unavailable site: actual 404 responses for several `llms.txt`/sitemap endpoints required navigation-based indexing. If a component page itself fails, cite the dated catalog as unverified and try the official repository or another candidate. Never claim its demo was observed.
- Paid source: Planes Inline Diff is a valid candidate with a licensing constraint, not a free implementation. Free alternatives must carry their missing behaviors.
- Search-only scope: the bundled helper uses the Python standard library, reads local JSONL, and writes nothing. It performs no network access or dependency installation. Source/demo inspection also does not authorize implementation in the user's project.
