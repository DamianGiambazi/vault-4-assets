# VAULT-4-ERRATA

**Scope:** what was said in the Vault 4 video, checked against the transcript (T + line), the take's evidence (`evidence\TAKE\`), the capture log and the repository. **None of these corrections changes a result.** The Reference already uses the correct versions.
**Use:** section A goes in the video description, or as captions. Sections B–D are for the record.

## A. Video corrections
| ID | Video | Where | Type | Said (T line) | Correct |
|---|---|---|---|---|---|
| V4-E01 | Full | A | Precision | Vault 3 "found four of four threads. It passed with finding three out of four, two out of three, and three out of three" (T10–13) | 4 of 4 threads held in the Vault 3 performance (`V3_SPINE_OK 4/4`). The per-thread figures quoted are the Vault 3 **rehearsal's** (3 Nov), for the lie, the cost and the door |
| V4-E02 | Full | A | Fact | the draft was "composed with Claude in an isolated session that had no access to… the SSOT"; "about 30 rounds" (T16–20) | a separate chat with none of the novel's files loaded, but that chat still had tools (V4-S05). The number of turns is the one `PROVENANCE.md` records |
| V4-E03 | Full | B | Fact | the Playground "is the only place you can speak to a model without having any of your account information… influencing the answers" (T29–31) | it is the place this video uses: a bare model, no tools, no system prompt, nothing but what is pasted |
| V4-E04 | Full | D | Precision | the tier lens "runs from F-tier to S-tier" (T52–53) | the tiers run F → S, but the video's climb is C → S, and they are a lens, not a score |
| V4-E05 | Full | C | Precision | "We would expect the original to match exactly" (T84–85) | the author's notes sit nearest Chapter 4 because Chapter 4 is in the index: likeness, not a match. Their verdict is `MOTIF_CLEAR` (one window, negated) |
| V4-E06 | Full | E–I | Fact | the C1, C3, C4 and C5 outputs were each "compared against the index" (T136–137, T176, T189–190, T203–204) | only `v4 draft` (C) and `v4 contract2` (F) use the Vault 2 index. `beats`, `critic`, `matrix` and `contract5` check structure and claims, not meaning |
| V4-E07 | Full | G | Omission | "I am now going to fix the problems off-camera… copy my corrections" (T179–186) | the corrections were prepared from rehearsal 3 (V4-S19): the final beats are DR3's, one word changed. They make the notes and the beats agree (6/6), but they don't answer this run's Contract 2 line by line (section B) |
| V4-E08 | Full | H | Fact | "grab the c4.json file" (T194) | `c4.md` (Contract 4's output is a Markdown table) |
| V4-E09 | Full | I | Fact | "I'll just call it v2.2" (T207–208) | v1.2. The take's commit `e507f21` left a stray `v 2.2` line; `d2ae5f2` replaced it with the v1.2 Changelog row |
| V4-E10 | Full | J | Omission | "the script scores the output against the prediction key" (T209–210) | the laptop shows evidence; **the author ticks** each line: 4/6 before the fixes, 6/6 after. `KEY_NEVER_PASTED` (6 bundles, 49,225 characters) was not said aloud |

**Checked and correct:** "No, I am not ready" (T66) · `MOTIF_CLEAR` and the breaches (T94–97) · sealed before the contracts (T112–116) · "1 out of the 44 lines reading as prose" (T138–139) · the model said the window was absent and the laptop agreed (T158–159) · Chapters 2 to 6 as a table (T194) · three outputs from one source (T198–200).

## B. Disclosure (V4-S19): the author's fixes in the take
The take's fixes (G) were prepared off camera from dress rehearsal 3, to keep the recording moving.
- **`ch-04-final.txt`** is DR3's final beats with one word changed. It holds all six rubric lines against the author's notes (the author's ticks: 6/6).
- **`fixes.txt`** was written against DR3's Contract 2. Some of its lines fit the take as well ("Squatter's rights", the Tuesday-night lock). Others name beats the take's 19-beat Contract 2 doesn't have ("7:31", "I refuse to be the passenger", the laugh at the junction, "old beats 15–27"). And it doesn't mention the take's "raise your premium" or "Act of God". (Checked word by word against `evidence\TAKE\c2-beats.txt`.)
- **What the checker did and didn't test:** `v4 contract5` checked that Contract 5's synthesis claims nothing the final beats lack: none unsupported. Nothing checked that the fixes answer *this run's* Contract 2. That check is carried into Vault 5's design.

## C. The record
| Commit on `main` | What it is |
|---|---|
| `3c6359b` | the baseline: issue #2 adopted (closes #2), 9 Nov |
| `f62b964` | the seal, pushed 13:42:05 UTC; the first contract followed at 13:46:42 UTC |
| `e507f21` | the rescue: `drafts/ch-04-beats.csv` and `SSOT.md`. Its message is `commit` (V4-S20), and its Changelog row was a stray `v 2.2` line (V4-S21) |
| `d2ae5f2` | the correction: the v1.2 Changelog row; its message records what `e507f21` holds |

History is kept; nothing is force-pushed. The rehearsals stay on `v4-dr1`, `v4-dr2` and `v4-dr3`.

## D. Carried to Vault 3's errata (found in Vault 4)
Vault 3's record said issue #2 was adopted and that `main` ended with that adoption. In fact #2 was closed by hand on 5 Nov, with the adoption's commit message posted as a comment, and `SSOT.md` was unchanged until `3c6359b` (9 Nov). The wording was drafted in the Vault 4 support session at the author's request, and adopted by the author. **Add as V3-E09 in `VAULT-3-ERRATA.md`.**

## E. Documents changed after the take
| Document | Change |
|---|---|
| *Vault 4 — The Cognitive Contracts: Reference* | final: the take's proof, the disclosure, snags S13–S21, errata E01–E10, assets |
| this file | new |
| `VAULT-4-INDEX.md`, `00-READ-FIRST.md` | final |
| `kit\` | the as-shipped v1.0 kit, and a script that collects the as-recorded kit from SPOOKY |
