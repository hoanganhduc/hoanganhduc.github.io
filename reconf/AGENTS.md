# Editing `core.bib`

This file documents the structure observed in the complete `core.bib` corpus and gives local rules for future edits. It applies to `core.bib` only. Do not change unrelated entries while adding or updating a record.

## Current corpus snapshot

The snapshot inspected on 2026-09-14 contains one leading `@comment` block followed by 715 bibliography entries:

| Entry type | Count |
|---|---:|
| `@article` | 462 |
| `@inproceedings` | 246 |
| `@incollection` | 7 |

No other bibliography entry type occurs in the file. The comment block records the collection description, its update date, and contributors. Update its `Last Updated` date when changing the bibliography.

## Mandatory safety rules

- Before modifying `core.bib`, create a timestamped, byte-for-byte backup in `reconf/`, for example `core.bib.backup-YYYYMMDD-HHMMSS`.
- Never overwrite an existing backup. Record the backup path and verify that its SHA-256 hash matches the pre-edit `core.bib` hash before making the first change.
- Keep the backup until the user has accepted the result. If an edit or validation fails, stop and report the failure; the backup is the restore source.
- Never merge, delete, or otherwise resolve suspected duplicate papers automatically. Report the evidence and proposed resolution, then wait for the user's explicit instruction.
- Treat `core.bib` as important data: make the smallest requested change and validate the complete file afterward.

## File-wide syntax and layout

Use these rules for every new or edited entry:

- Save the file as UTF-8 with LF line endings.
- Start an entry with `@type{key,` and close it with `}` on its own line.
- Put exactly one field on each line. Do not wrap long field values.
- Indent every field with one tab. Pad field names so every `=` is in column 16.
- Use lowercase entry types and field names.
- Enclose every field value in braces.
- Put a comma after every field except the last field in an entry.
- Do not insert blank lines between adjacent entries.
- Use `{{...}}` for a new or changed `title` so BibTeX preserves capitalization. This is the form used by 711 of 715 titles; the four single-braced titles are legacy exceptions.
- Keep the first three fields in the fixed order `title`, `author`, `year`.
- Put `journal` or `booktitle` next, followed by the available publication metadata. The usual remaining order is `publisher`, `series`, `volume`, `number`, `pages`, `doi`, `note`, `url`, `editor`, other uncommon fields, `archiveprefix`, and `eprint`.
- Preserve the current global entry order. The file is not globally sorted by key or year, so do not reorder unrelated entries.

The common shell is:

```bibtex
@entrytype{key,
	title         = {{Title with Protected Capitalization}},
	author        = {Family, Given and Family, Given},
	year          = {2026},
	field         = {value}
}
```

## Citation keys

The dominant key forms are:

- Journal article or arXiv record: `journals/<venue-code>/<AuthorCode><YY>`
- Conference paper: `conf/<venue-code>/<AuthorCode><YY>`
- Book chapter: `books/<publisher-or-series-code>/<AuthorCode><YY>`

`<AuthorCode>` normally consists of the first author's surname followed by initials for additional authors; `<YY>` is normally the two-digit year. Existing keys include legacy deviations and year mismatches. Preserve an existing key because pages and `note` fields may cite it.

Citation keys must be unique. If $$n$$ entries would otherwise have exactly the same key `<key>`, rename all members of that collision group in file order as `<key>-1`, `<key>-2`, ..., `<key>-n`. Do not leave the first member unsuffixed. Before applying the suffixes, confirm that none of the target keys already belongs to another entry, and update any unambiguous internal `\cite{...}` reference to the renamed key. Keys may also be referenced outside `core.bib`; inspect or edit external consumers only when the user's requested scope permits it, and otherwise report that those references remain unchecked.

Key collisions and duplicate papers are different problems. Renaming a citation key does not resolve a duplicate paper.

## Duplicate papers and versions of one work

### Duplicate-paper rule

Two entries represent a duplicate paper if either of these non-empty identifiers is identical:

- the `doi` value; or
- the arXiv `eprint` value.

Duplicate papers must not remain in `core.bib`. When a duplicate is detected, do not choose or apply a repair. Stop and report:

1. both citation keys and entry types;
2. the shared DOI or arXiv eprint ID;
3. the titles, authors, and years;
4. the locations of both entries; and
5. the possible actions, such as retaining one entry, merging metadata, or deleting one entry.

Wait for the user's explicit decision before changing either entry. Back up `core.bib` again immediately before performing the approved repair.

### Version-family rule

Entries with the same title and the same authors are versions of the same work when their publication status or venue differs. They are related versions, not automatically interchangeable records.

- If a standalone arXiv entry has a matching published entry, propose attaching the arXiv metadata to the nearest matching published version by adding `archiveprefix = {arXiv}` and its `eprint` value to that published entry.
- After that merge, the standalone arXiv entry may be deleted, but only after the user explicitly approves both the target published entry and the deletion.
- If several conference or journal entries are plausible published targets, report all candidates and ask the user which one is the nearest version. Do not select one automatically.
- If the selected published entry already has a different `eprint` or `archiveprefix`, report the conflict and do not overwrite either value.
- If no published version exists, keep the standalone arXiv entry.
- Conference and journal versions may coexist as separate entries. The journal version should cite the conference version in `note` using `Conference Version: \cite{<conference-key>}`. If the journal entry also has an article identifier, preserve the combined `note` form documented below.

## `@article`

Every one of the 462 article entries has these four fields:

```bibtex
@article{journals/<venue-code>/<AuthorCode><YY>,
	title         = {{Article Title}},
	author        = {Family, Given and Family, Given},
	year          = {2026},
	journal       = {Journal Name}
}
```

Observed optional fields are `publisher`, `volume`, `number`, `pages`, `doi`, `note`, `url`, `editor`, `organization`, `hal_id`, `archiveprefix`, and `eprint`. Include metadata that is known; do not add empty fields.

A published article commonly has this structure:

```bibtex
@article{journals/<venue-code>/<AuthorCode><YY>,
	title         = {{Article Title}},
	author        = {Family, Given and Family, Given},
	year          = {2026},
	journal       = {Journal Name},
	volume        = {42},
	number        = {3},
	pages         = {101--125},
	doi           = {10.xxxx/xxxxx}
}
```

An arXiv-only article normally has this structure:

```bibtex
@article{journals/corr/<AuthorCode><YY>,
	title         = {{Preprint Title}},
	author        = {Family, Given and Family, Given},
	year          = {2026},
	journal       = {arXiv preprint},
	archiveprefix = {arXiv},
	eprint        = {2601.01234}
}
```

When a published article also has an arXiv version, retain the journal metadata and append `archiveprefix` and `eprint` at the end.

## `@inproceedings`

All 246 conference entries have `title`, `author`, and `year`; 245 also have `booktitle`. Treat `booktitle` as required for a new conference entry.

```bibtex
@inproceedings{conf/<venue-code>/<AuthorCode><YY>,
	title         = {{Paper Title}},
	author        = {Family, Given and Family, Given},
	year          = {2026},
	booktitle     = {Proceedings Title},
	publisher     = {Publisher},
	series        = {Series},
	volume        = {12345},
	pages         = {101--112},
	doi           = {10.xxxx/xxxxx},
	editor        = {Family, Given and Family, Given},
	archiveprefix = {arXiv},
	eprint        = {2601.01234}
}
```

Observed optional fields are `publisher`, `series`, `volume`, `number`, `pages`, `doi`, `editor`, `url`, `journal`, `note`, `organization`, `hal_id`, `archiveprefix`, and `eprint`. Omit unavailable optional fields rather than inventing placeholders. The `editor` field appears after `doi` in the established layout.

## `@incollection`

All seven book-chapter entries have `title`, `author`, `year`, `booktitle`, `publisher`, `pages`, and `doi`. Six also have `editor`.

```bibtex
@incollection{books/<publisher-or-series-code>/<AuthorCode><YY>,
	title         = {{Chapter Title}},
	author        = {Family, Given and Family, Given},
	year          = {2026},
	booktitle     = {Book Title},
	publisher     = {Publisher},
	series        = {Series},
	volume        = {42},
	pages         = {101--125},
	doi           = {10.xxxx/xxxxx},
	editor        = {Family, Given and Family, Given}
}
```

Observed optional fields are `editor`, `series`, `volume`, `edition`, `chapter`, `archiveprefix`, and `eprint`. Include `editor` when known. The small number of existing entries makes their current field set descriptive rather than a universal BibTeX requirement.

## Field conventions

- `author` and `editor`: separate people with the BibTeX keyword `and`. Existing records use both `Family, Given` and `Given Family`; preserve existing names and use one form consistently within a new entry. Keep braces around compound surnames and LaTeX accents where needed.
- `title`: use double braces around the complete title. Preserve intentional capitalization and LaTeX mathematics such as `$k$`, `$P_4$`, or `$(2K_2,K_4)$`.
- `year`: use a four-digit braced value.
- `pages`: use a BibTeX double dash for a range, for example `{101--125}`. A single page or article number remains a single value.
- `doi`: store a bare DOI beginning with `10.`, not a `https://doi.org/` URL. Use `url` for a web address.
- `archiveprefix` and `eprint`: for a new arXiv record, use them as the pair `archiveprefix = {arXiv}` and `eprint = {<arXiv-id>}`.
- `note`: the established components are an article identifier, `(article <number>)`, and a conference link, `Conference Version: \cite{<key>}`. They may occur separately or together; 14 current entries use the combined form `{(article <number>). Conference Version: \cite{<key>}}`. Preserve both components when present, and make sure a cited key exists.
- Empty fields are not part of the current structure. Omit them.

## Known legacy deviations

These deviations exist in the inspected snapshot. Do not copy them into new entries, and do not repair them as a side effect of an unrelated edit:

- Four titles use only one pair of braces.
- Two `eprint` fields lack `archiveprefix`.
- One `@inproceedings` entry, `conf/sofsem/GuptaKM19`, lacks `booktitle`.
- Two `doi` values are URLs instead of bare DOI strings.
- A few keys use legacy prefixes such as `journal/`, `book/`, or no path prefix, and some key year suffixes differ from the `year` field.
- Three entries place `eprint` before `archiveprefix`; the dominant order is `archiveprefix` followed by `eprint`.

## Edit checklist

Before finishing an edit to `core.bib`:

1. Confirm that the required pre-edit backup exists, has a unique timestamped name, and was hash-verified before editing began.
2. Limit the diff to the requested records and, when applicable, the header update date.
3. Parse the complete file as BibTeX, not merely the changed lines.
4. Confirm all citation keys in the complete file are unique. Resolve every collision with the numbered-suffix rule above.
5. Check the complete file for repeated non-empty DOI values and repeated non-empty arXiv `eprint` values. If any are found, stop and report them; do not resolve them automatically.
6. Check matching title-and-author pairs for arXiv, conference, and journal version relationships. Report ambiguous merge targets instead of choosing one.
7. Confirm each new DOI is a bare DOI and each new arXiv record has the `archiveprefix`/`eprint` pair.
8. Confirm required observed fields for the selected entry type are present.
9. Confirm braces are balanced, every field is on one line, field alignment is preserved, and only the final field lacks a comma.
10. Confirm every `\cite{...}` target introduced in a `note` exists.
11. Do not normalize, reorder, rename, merge, delete, or repair unrelated entries.
