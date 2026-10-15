import argparse
import json
import pathlib
import re


def tokens(text):
    return set(re.findall(r"[\w-]+", text.lower()))


def search(query, limit=12, library=None):
    root = pathlib.Path(__file__).resolve().parents[1]
    vocabulary = json.loads((root / "references/vocabulary.json").read_text())
    query_tokens = tokens(query)
    ignored = {"find", "a", "an", "the", "with", "that", "and", "or", "for", "ui", "component", "найди", "компонент", "который", "где", "и", "или", "с", "для", "мне"}
    query_tokens -= ignored
    expanded = set(query_tokens)
    for tag, aliases in vocabulary.items():
        phrases = [tag] + aliases["ru"] + aliases["en"]
        if any(tokens(phrase) and tokens(phrase) <= query_tokens for phrase in phrases):
            expanded.add(tag)
    found = []
    for path in sorted((root / "references/libraries").glob("*.jsonl")):
        if library and path.stem != library:
            continue
        for line in path.read_text().splitlines():
            row = json.loads(line)
            name = tokens(row["name"])
            tags = set(row["tags"])
            aliases = tokens(" ".join(row["synonyms_en"] + row["synonyms_ru"]))
            prose = tokens(row["description"])
            matched = expanded & (name | tags | aliases | prose)
            if not matched:
                continue
            score = 5 * len(expanded & tags) + 4 * len(query_tokens & name) + 2 * len(query_tokens & aliases) + len(query_tokens & prose)
            unmatched = query_tokens - (name | tags | aliases | prose)
            found.append({"library": path.stem, "score": score, "matched": sorted(matched), "unmatched_query": sorted(unmatched), **row})
    found.sort(key=lambda item: (-item["score"], item["library"], item["name"]))
    return found[:limit]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read-only, bilingual lexical search of the Find UI catalog.")
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--library")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    print(json.dumps(search(args.query, args.limit, args.library), ensure_ascii=False, indent=2))
