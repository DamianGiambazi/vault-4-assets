# VAULT-4-INDEX — every file, in order of use

**Vault 4 · The Cognitive Contracts** · *Rescuing the Leviathan: Five Contracts for an AI That Wants to Please* · final package, 10 Nov 2026 · laptop SPOOKY
**Repository:** `github.com/DamianGiambazi/novel-ssot`. `main`: `3c6359b` baseline · `f62b964` seal · `e507f21` rescue · `d2ae5f2` correction. Branches `v4-dr1`, `v4-dr2`, `v4-dr3`: the dress rehearsals.
**Personal data:** none found in the package (scanned for emails, user paths, client IDs, keys). The receipts carry only API message IDs.

## 1. Read
| File | What it is |
|---|---|
| `00-READ-FIRST.md` | the result, the folders, the one step left |
| `reference/Vault 4 — The Cognitive Contracts Reference.pdf` | **the reference guide**: the writer, the checker and the key · the schema and the tiers · the five contracts (with the run diagram) · the checker and the scripts · the fair test · the proof (the take, DR1–DR3, the disclosure) · 21 snags · errata · glossary. The live version is the Claude doc of the same name |
| `VAULT-4-ERRATA.md` | ten corrections to the video (V4-E01–E10), the S19 disclosure, the record, one carry-over to Vault 3 |
| `VAULT-4-DESCRIPTIONS.md` | the video description and the lesson blurb |

## 2. The video (`video/`)
| File | What it is |
|---|---|
| `V4-TRANSCRIPT.txt` | the take's transcript (T + line in the errata) |
| `V4-CAPTURE-LOG.md` | every run (DR1, DR2, DR3, the take): verdicts, rubric before and after, timings, snags S01–S21, words on camera |
| `V4-HANDOVER-TO-MASTER.md` | the take's handover from the support session |

## 3. The evidence (`evidence/TAKE/`)
| File | What it is |
|---|---|
| `b.txt` · `c1.txt` · `c2.json` · `c3.json` · `c4.md` · `c5.json` | the writer's six replies, as written (grabbed from the Raw view) |
| `*.api.json` | the six receipts: model `claude-opus-5-5`, tokens, `stop_reason` (all `end_turn`) |
| `c2-beats.txt` · `ch-04-final.txt` · `fixes.txt` | Contract 2's beats; the author's final beats and fixes `[author]` |
| `ch-04-beats.csv` | Contract 5's CSV, committed as `drafts/ch-04-beats.csv` |
| `pastes.jsonl` · `pastes-audit.txt` | every character pasted to the writer → `KEY_NEVER_PASTED` (6 bundles, 49,225 characters) |
| `seal-check.txt` · `git-log.txt` | `SEALED_BEFORE_CONTRACTS` (seal 13:42:05Z, C1 13:46:42Z); the history at capture |
| `rubric-c2-beats.txt` · `rubric-ch-04-final.txt` | the laptop's evidence before and after: 4/6 → 6/6 (the author ticked the same) |
| `last-bundle.txt` | the last paste (C5) as it went on the clipboard |
| `as-pasted/` | **recovered from the paste log:** each document, exactly as the writer received it. That includes the five contracts, the manifest excerpts, the B prompt and **the cold-open draft** `ch04-c-tier.md` (8,045 characters) |

## 4. Running it again (`docs/`)
| File | What it is |
|---|---|
| `VIDEO 4 — BEAT SHEET v1.1 (DRESS REHEARSAL EDITION, after DR1).md` | the script the take followed: A–L, DO · SEE · SAY, decisions D-V4-1–8 |
| `V4-RUNBOOK-DRESS-REHEARSAL.md` | prep, each run, the take, the door back on, troubleshooting |
| `V4-CARDS.md` | the on-screen cards (v1.1) |
| `V4-SANDBOX-TEST-REPORT.md` | what was tested before the kit reached SPOOKY |
| `reference/` | the book sources of the key (`draft-specs`, `state-tracking-matrix`, `continuity-ledger`). **Never pasted** |
| `history/` | the outline v1.0 and the beat sheet v1.0, superseded |

## 5. The kit (`kit/`)
| File | What it is |
|---|---|
| `KIT-README.md` | **read first:** what changed on SPOOKY, and the one step to complete the kit |
| `collect-kit-from-spooky.ps1` | run on SPOOKY: copies the kit as recorded (v4_check 1.1.1, grab, bundle, the sealed prediction, provenance) → `KIT_COLLECTED` |
| `as-recorded/` | empty until that script runs; then the kit to use |
| `as-shipped-v1.0/` | the kit as built for DR1 (v4_check 1.0.0): `novel-door/`, `v4-paste/`, `v4-preflight/`. Its paste pack is identical to what the take pasted |

**The scripts, in order of use** (verdict words): `door-off` `DOOR_OFF` → `new-run` `RUN_READY` → `tab-header-v4` → `preflight-v4` `PREFLIGHT_V4_OK` → `bundle` / `grab` → `v4_check` (`MOTIF_BREACH` · `CONTRACT2_OK` · `CRITIC_OK` · `MATRIX_OK` · `CONTRACT5_OK` · `RUBRIC_EVIDENCE` · `KEY_NEVER_PASTED`) → `seal-check-v4` `SEALED_BEFORE_CONTRACTS` → `capture-evidence-v4` `EVIDENCE_SAVED` → `door-on` `DOOR_ON`.

## 6. The downloads for viewers (`deliverables/`)
| File | What it is |
|---|---|
| `01-THE-CANONICAL-SCHEMA.md` | the five fields, each with the receiver's question |
| `02-ASK-THE-RECEIVER.md` | the 100% question as the first step of any contract |
| `03-TIER-WORKSHEET.md` | F → S, what lifts a prompt, a fill-in sheet |
| `04-HOSTILE-CRITIC-RUBRIC.md` | what counts as debt; how to judge the critic |
| `05-THE-SEALED-KEY-PATTERN.md` | `PREDICTION-V4.md` as a reusable pattern |
| `novel/` · `templates/` · `originals/` | the five contracts as used (with `CHANGES.md`), as templates for any domain, as first written |

## 7. Diagrams (`diagrams/`)
`V4-FLOW-the-cognitive-contracts.svg` / `.png` (the data flow) · `make_v4_flow.py` + `flowkit.py` (regenerate it).
