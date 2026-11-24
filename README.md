# Vault 4 — The Cognitive Contracts: Reference

Nov 10, 2026 · @Damian

## What Vault 4 is

Vault 4 lets the model write, and shows how to stop it writing the wrong thing. A well-written Chapter 4, made with no rules, puts the Figure in the wrong chapter and spends the book's emotional release early. Five contracts, each pasted into a fresh request and each output checked by the laptop, rescue it to the chapter the author's notes describe. The author fixes what the critic finds, types the commit, and scores the result against a key sealed before the first contract.

> **Status (10 Nov 2026): final.** The results below come from the recorded take on SPOOKY, 10 Nov, on `main`. The three dress rehearsals (9–10 Nov) are kept beside them on their own branches.

The method carries beyond novels: ask the receiver what it needs, write that into a contract, seal the answer key before you run it, check every output outside the model, and keep the decision with a person.

- **Laptop** — Lenovo V15-IGL ("SPOOKY"): Intel Celeron N4020, 2 cores, 8 GB RAM, no AVX, Windows 11 Pro 25H2
- **Stack (from Vaults 1–3)** — PowerShell 7.6.9 · git 2.50.1 · all-MiniLM-L6-v2 (snapshot `1110a243...`) · the Vault 2 index (29 passages) · Vault 3's door venv (`sentence-transformers` 6.1.0, `torch` 2.14.1)
- **New this vault** — nothing installed · the checker `v4_check.py` 1.1.1 · the paste and capture scripts (`bundle`, `grab`, `new-run`, `preflight-v4`, `capture-evidence-v4`) · the writer: `claude-opus-5-5` in the Claude Console Playground, no tools
- **Corpus** — the same 24 chapters as Vaults 2–3; the author's Chapter 4 notes are the sealed key
- **Video** — *Rescuing the Leviathan: Five Contracts for an AI That Wants to Please*

## The writer, the checker and the key

Vault 3 ended with a reader that found all four threads. Vault 4 asks the same model to write, and it fails in a way that looks like success: the prose is gorgeous, the pacing is fatal. The answer is a better contract and a check outside the model, not a better model.

The thesis: **"Don't argue with the AI. Change the contract, then check it."**

**The statement in the novel's own words.** Chapter 4 is the refusal: connective tissue that builds tension and resolves nothing. A writer with no contract does what a tired friend would: it gives the scene the release it seems to want. The contract is the fence that keeps Chapter 4 a refusal.

| Who | Job | Built from |
| --- | --- | --- |
| The writer | drafts and revises under each contract; sees nothing but what is pasted | `claude-opus-5-5` in the Console Playground: no tools, no system prompt, one fresh request per contract |
| The checker (the laptop) | audits every output by word and by meaning; checks the writer's account of itself | `v4_check.py`, Vault 2's index and translator, Vault 3's venv |
| The paste log | records every character that crossed to the writer | `bundle.ps1` → `pastes.jsonl` |
| The key | what a correct Chapter 4 is; sealed and pushed before the first contract | the author's ch-04 notes, a reference matrix, a six-line rubric in `PREDICTION-V4.md` |
| GitHub (the record) | holds the seal, the rescued beats and the author's commit | Vault 2's public `novel-ssot` |
| The author | fixes what the critic finds, from their own notes; ticks the rubric; types the commit | you |

## The schema and the tiers

Every contract has the same five fields, and each answers a question the receiver asked when it was told "Write the scene beats for Chapter 4" and asked whether it was 100% ready (Vault 1's question). In the rehearsals it named four of the five, in the take three; it never asked who it should be.

| Field | The receiver's question | Write | Avoid |
| --- | --- | --- | --- |
| `<role>` | who should I be? | a job with a point of view ("Forensic Auditor") | a flattering adjective |
| `<context>` | what do I need to know? | only facts it can't know, with their source | claims you haven't checked |
| `<task>` | what exactly do you want? | one verb, one object, one outcome | three tasks in one |
| `<constraints>` | what must not happen? | the fences; what to do when information is missing (`UNKNOWN`) | examples from another case |
| `<output_format>` | what does done look like? | a shape a machine can check; fields that ask (`<true or false>`) | pre-filled answers, which invite an echo |

**The power is in the constraints, not the length.**

The tiers are a lens, not a score. C is the cold-open draft: functional, flawed. B is context with no enforcement. A is contracts in the schema with checked outputs. S is contracts, laptop checks and the author's decision together, claimed only if all six rubric lines hold and the author commits. The score itself is the sealed key.

## The five contracts

Strip, fence, attack, restructure, derive: each contract does one job, runs in its own fresh request, and its output is checked before the next one starts. Between Contracts 3 and 4 the author fixes the beats from their own notes.

The two accented steps are the author's; every other step ends in a verdict word printed by the laptop.

*the run · the seal, five contracts, two author steps*

| Contract | Role | Job | Pasted with it | Saved as | Checked by | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| C1 Raw Output | Raw Output Generator | strip the prose; keep only physical actions and dialogue | the C-tier draft | `c1.txt` | `v4 beats` | `BEATS_OK` / `BEATS_PROSE` |
| C2 Surgical Fence | Principal Architect | revise the beats inside the SSOT; the cost external; report on itself | SSOT, manifest excerpts, Chapter 3 notes, `c1.txt` | `c2.json` → `c2-beats.txt` | `v4 contract2`: its own `window_motif_present` against the laptop's count | `CONTRACT2_OK` / `SELF_REPORT_WRONG` |
| C3 Hostile Critic | Forensic Auditor | attack the beats: contradictions, hidden assumptions, edge cases, debt, voice | SSOT, manifest excerpts, `c2-beats.txt` | `c3.json` | `v4 critic` | `CRITIC_OK n` |
| the author | — | fix what the critic found, from the ch-04 notes, typed | nothing pasted | `ch-04-final.txt`, `fixes.txt` | `[author]` | the rubric, in J |
| C4 Modality Shift | State Architect | a state-tracking matrix, Chapters 2–6; UNKNOWN where the documents are silent | SSOT, manifest excerpts, Chapter 3 notes, `ch-04-final.txt` | `c4.md` | `v4 matrix`: shape, UNKNOWN cells, the Ch 4 row beside the key | `MATRIX_OK` |
| C5 Derivative Matrix | Multi-Format Generator | three outputs from one source: a synthesis, a CSV, a commit message to retype | `fixes.txt`, `c4.md`, `ch-04-final.txt` | `c5.json` → `ch-04-beats.csv` | `v4 contract5`: the CSV, and no claim the final beats lack | `CONTRACT5_OK` / `UNSUPPORTED_CLAIM` |

What changed from the original contracts, and why: C2 gained the context the writer lacked (D5, the drawer constant, Chapter 3's crack) and lost two errors (a check that never ran, and Chapter 5's cost); its self-report fields ask instead of asserting. C4 gained "write UNKNOWN; do not invent". C5's context is now the author's own list of fixes, so the synthesis can't claim one that wasn't made. C1 and C3 are unchanged.

## The checker and the scripts

`v4_check.py` (build 1.1.1) is the judge: one file, run in Vault 3's door venv, called `v4` on camera. It reads by word and by meaning, prints every sentence it counted, and leaves the verdict on a contract's quality to the author.

| Command | Reads | Prints |
| --- | --- | --- |
| `selftest` | 17 built-in cases: negation, "figure it out", an envelope's window, a heading, "tear" vs tears, "until" vs a clock, messy JSON | `SELFTEST_OK` |
| `draft` | a draft: window and Figure language by word (negations shown, not counted); each paragraph's four nearest chapters by meaning | `MOTIF_BREACH n` / `MOTIF_CLEAR` |
| `beats` | numbered beats: count, lines that read as prose, the motif | `BEATS_OK` / `BEATS_PROSE k` |
| `contract2` | Contract 2's JSON; writes `c2-beats.txt`; the model's claim beside the laptop's count | `CONTRACT2_OK` / `SELF_REPORT_WRONG` |
| `critic` | Contract 3's JSON; which rubric themes it touched | `CRITIC_OK n` |
| `matrix` | Contract 4's table: 5 × 6, UNKNOWN cells, the Ch 4 row beside the sealed key | `MATRIX_OK` |
| `contract5` | Contract 5's JSON; writes and checks the CSV; any claim the final beats lack | `CONTRACT5_OK` / `UNSUPPORTED_CLAIM` |
| `rubric` | the six sealed lines, with the evidence found; the author ticks | `RUBRIC_EVIDENCE n/6` |
| `pastes` | the paste log: did any key phrase cross before the author typed it? | `KEY_NEVER_PASTED` / `KEY_LEAKED` |

Four rules the checker keeps:

1. **Likeness is not proof.** The meaning scan is shown as evidence; the word scan decides, and shows every sentence.
2. **A model's account of what it did is not a log.** Every self-report field is checked outside the model.
3. **Test the judge first:** `selftest` runs in every preflight, on messy input.
4. **Evidence, not verdict:** rubric points; the author decides each line.

The scripts around the take:

| Script | Job | Verdict |
| --- | --- | --- |
| `door-off.ps1` / `door-on.ps1` | `novel_door` out of Claude Desktop's config for Vault 4, back byte for byte after | `DOOR_OFF` / `DOOR_ON` |
| `new-run.ps1 -Run DR1\|DR2\|TAKE` | a rehearsal branch from main (or main itself for the take); archives the last answers, never deletes | `RUN_READY` |
| `preflight-v4.ps1` | the gate: RAM ≥ 2.0 GB, branch, clean tree, no seal yet, the index, the pack, the draft's size and provenance, the door off, the selftest, the warm-up | `PREFLIGHT_V4_OK` |
| `bundle.ps1 B\|C1...C5` | builds one paste, puts it on the clipboard, logs every character; refuses key files | `BUNDLE...` |
| `grab.ps1 <name>` | takes the Playground's Raw response, saves the reply's text exactly and the whole response as a receipt (model, tokens); refuses a rendered copy, a cut-off reply, an overwrite | `GRABBED` |
| `seal-check-v4.ps1` | the pushed seal came before the first contract | `SEALED_BEFORE_CONTRACTS` |
| `capture-evidence-v4.ps1` | the answers, the paste audit, the seal check and both rubric runs, into one folder | `EVIDENCE_SAVED` |

## The fair test, step by step

The writer can read nothing but what is pasted, every paste is logged, and the key is sealed before the first contract. Each step below ends in a verdict word on the laptop's screen.

1. **Make the cold open, before recording.** A long chat with no rules (about 40 turns, the writer agreeing like a tired friend), then `Write the scene beats for Chapter 4.` verbatim. Keep a draft that is good and wrong; record the model, the turns and every follow-up in `PROVENANCE.md`.

2. **Gate.** `new-run.ps1` makes the run's branch from main; `preflight-v4.ps1` prints `PREFLIGHT_V4_OK` and warms the translator on the draft.

3. **B, ask the receiver.** The bare prompt plus Vault 1's question: "are you 100% ready?" It says no, and lists what it lacks. The list is mapped onto the five fields.

4. **C, the laptop audits the draft.** `v4 draft` on the draft and on the author's notes: `MOTIF_BREACH` and `MOTIF_CLEAR` (the notes' one window is negated).

5. **D, seal the key.** `PREDICTION-V4.md` (the ch-04 notes, the reference matrix, the rubric, what the writer is given, P1–P9) and `seal-check-v4.ps1` are committed and pushed; the check prints `SEALED_BEFORE_CONTRACTS` (no contract has been pasted).

6. **E–I, the five contracts.** For each: `bundle Cn`, the Playground's **+ New**, paste, Run, the Raw view copied whole, `grab`, then the `v4` check. In G the author edits `ch-04-final.txt` and `fixes.txt`; in I the author types the commit and pushes.

7. **J, score against the key.** `v4 rubric` before (Contract 2's beats) and after (the author's), ticked by the author; `v4 pastes` → `KEY_NEVER_PASTED`; the seal check again.

8. **After.** `capture-evidence-v4.ps1` → `EVIDENCE_SAVED`.

**The fair-test checklist for the writer (D-V4-8):**

- the Claude Console Playground, model `claude-opus-5-5`, nothing added (no tools), the system prompt empty;
- ⚙: no fallback model, thinking Adaptive, speed Standard, max tokens 20,000; the same in every run;
- a probe before the first run: asked to list its tools, it has none;
- one fresh request per contract, and one for B;
- Claude Desktop closed during the run, with `novel_door` out of its config for all of Vault 4.

**Why the Playground, not a chat.** In rehearsal, a Claude Desktop chat with every connector off still carried web fetch, artifact, docs and repository tools, and it searched the author's artifacts unasked. The repository is public and holds the key. The paste log proves only what crossed the clipboard; a writer with no tools makes that the whole story.

**The record:** three dress rehearsals ran on branches (`v4-dr1`, `v4-dr2`, `v4-dr3`) and stay on GitHub; the take ran on `main`. Nothing is force-pushed.

## The proof

The rescue went from 4 of 6 to 6 of 6 against the sealed key, and the key never crossed to the writer. The take: 10 Nov 2026, `claude-opus-5-5` in the Console Playground, one fresh request per contract, on `main`. Every sealed prediction held. One gap held in every run too: the critic never found the clock.

The seal `f62b964` was pushed at 13:42:05 UTC; the first contract was pasted at 13:46:42 UTC: `SEALED_BEFORE_CONTRACTS`. The contracts ran from 13:46 to 14:21 UTC (35 min).

| # | Chunk | Predicted | The take | DR1 · DR2 · DR3 |
| --- | --- | --- | --- | --- |
| P1 | B | not 100% ready; at least 3 of 5 fields named | held: 3 of 5 (context, task, format; no role, no constraints) | 4 · 4 · 4 |
| P2 | C | `MOTIF_BREACH` on the draft; `MOTIF_CLEAR` on the notes | held: 6 counted; the notes clear, 1 negated | held ×3 |
| P3 | E | the motif survives stripping | held: 2 window beats kept (`BEATS_PROSE 1` of 44) | ✗ · held · held |
| P4 | F | `CONTRACT2_OK` `MOTIF_CLEAR`; the self-report agrees | held: 19 beats; the model said false, the laptop counted 0 | held ×3 |
| P5 | G | the critic names a real gap: the clock, or the joke | held, on the joke ("Humour rule vs beat 5... Sarah laughs"); not the clock. 20 findings | the clock missed in all three |
| P6 | H | `MATRIX_OK`, at least 1 UNKNOWN, no contradiction in Ch 4 | held: 5 × 6, 11 UNKNOWN; Sarah's pressure High against the key's Medium, a difference of degree | held · void · held |
| P7 | I | `CONTRACT5_OK`; nothing unsupported | held: 12 CSV rows; no unsupported claim | held · void · held |
| P8 | J | rubric at least 4/6 before, 6/6 after (the author's ticks) | held: 4/6 → 6/6 | 4→6 · 4→void · 4→6 |
| P9 | J | `KEY_NEVER_PASTED` | held: 6 bundles, 49,225 characters | held ×3 |

**The rubric, before and after.** Contract 2's beats failed two lines. Line 3: the first joke ("raise your premium") lands and Sarah laughs; the second ("Act of God") lands wrong but isn't regretted. Line 5: no clock. Contract 2 also pulled Chapter 5's Wednesday, the stuck drawer, into Chapter 4, in every run. The final beats hold all six: the joke about her new project, too quick, regretted, and "You don't have to do that"; the lock on Tuesday morning, on top of Sarah's tea; the clock, "The Albion, by the station — until Friday"; the silent drive; nothing from Wednesday.

**The critic's blind spot.** In four runs out of four, the Hostile Critic missed the clock. Nothing pasted mentions one, so it could only come from the author's notes. In every run, the only clock in the rescue is the one the author typed.

**Disclosure:** the author's fixes were prepared before the take (V4-S19). To keep the recording moving, the take's fixes came from rehearsal 3. `ch-04-final.txt` is DR3's final beats with one word changed. `fixes.txt` was written against DR3's Contract 2. Some of its lines fit the take as well ("Squatter's rights", the Tuesday-night lock). Others name beats the take's 19-beat Contract 2 doesn't have ("7:31", "I refuse to be the passenger", the laugh at the junction, "old beats 15–27"). And it doesn't mention the take's "raise your premium" or "Act of God". So the notes and the final beats agree (6/6), but the fixes don't answer this run's Contract 2 line by line. The checker tests Contract 5's claims against the final beats, not the fixes against Contract 2: a check for Vault 5.

**What it cost.** $0.69 for the take, from the six receipts. Contract 3 alone used 4,044 tokens in and 13,224 out, 10,084 of them thinking.

**The record on main.** `3c6359b` the baseline (issue #2 adopted) · `f62b964` the seal · `e507f21` the rescue (its message is `commit`, V4-S20) · `d2ae5f2` the Changelog correction to v1.2 (V4-S21). History is kept; nothing is force-pushed. The evidence is in `v4-evidence\TAKE` (the six replies with their receipts, the paste log, the audits).

## What the work taught us

Each snag below was real, found in rehearsal on SPOOKY, diagnosed from its evidence and fixed at its source, one change at a time.

| ID | Snag | Fix | What it teaches |
| --- | --- | --- | --- |
| V4-S01 | The runbook had the cold-open draft made while `novel_door` was still in Claude's config | the door off and the settings set before generating | the fair test starts before the draft |
| V4-S02 | "A charity envelope with a window" counted; a heading glued to the next sentence printed it twice | checker 1.1: envelope windows shown, not counted; headings are their own sentence | a keyword scan shows its sentences for a reason |
| V4-S03 | Vault 3's issue #2 was closed by hand, its commit message posted as a comment; the SSOT never changed | adopted properly: `3c6359b` (`closes #2`) | a closed issue is not a decision; the commit is |
| V4-S04 | 2.02 GB free at the preflight, before OBS | Claude Desktop, VS Code and other apps closed during runs | RAM is the constraint on an 8 GB laptop |
| V4-S05 | A Claude Desktop chat, every connector off, still carried web fetch, artifact, docs and repository tools, and searched the author's artifacts unasked | the writer became a bare model in the Console Playground (D-V4-8) | a fair test is a tool list, not a settings page |
| V4-S06 | The Playground's Raw view is the API response; the rendered copy loses numbering and JSON | `grab` reads Raw, saves the text exactly, keeps the response as a receipt | copy the evidence, not its rendering |
| V4-S07 | "Tear its edge" read as tears | checker 1.1 | test the judge on the trial's own words |
| V4-S08 | The checked zones printed as a raw list | one per line | what's on camera is read, not parsed |
| V4-S09 | A placeholder commit message was copied and committed: `<your own words>` | no copyable message anywhere; the author types it | the author declares, in their own words |
| V4-S10 | `code` returned at once, so the SSOT missed the commit | `code --wait` | a step that waits must say so |
| V4-S11 | Rubric line 5 found a clock in the bare word "until" | checker 1.1: the Albion or Friday | evidence, not verdict: the author ticks |
| V4-S12 | The transcript missed most native output (git, Python) | none: the evidence folder holds it | the record is the files, not the scroll |
| V4-S13 | DR2: no CSV, because Contract 5's check returned `JSON_BAD` | the cause was S15 | follow a failure to its first cause |
| V4-S14 | DR2: after a Ctrl-C, the G step ran again and overwrote the author's edited beats; C4, C5 and the rubric ran on Contract 2's beats | copy only if missing; `bundle` refuses C4/C5 while the final beats equal Contract 2's | a step that can be repeated must be safe to repeat |
| V4-S15 | The checker straightened curly quotes before parsing, breaking valid JSON | checker 1.1.1: read as written first | test the judge on the trial's own words |
| V4-S16 | "Cry" counted as prose in Contract 1, though crying is an action | removed; P3 reworded to "the motif survives" | a prediction says what it tests |
| V4-S17 | DR3: `GRAB_SAME_AS_BUNDLE`, the clipboard still held the paste | none: the guard worked | a guard that fires is a guard that works |
| V4-S18 | DR3: a commit message typed in a hurry | the take sheet shows an example shape to read, then type | the record is read later; write it for that reader |
| V4-S19 | The take's fixes were prepared from DR3: the final beats are DR3's, and `fixes.txt` was written against DR3's Contract 2: some lines fit the take, others name beats it doesn't have | disclosed (The proof, errata); a check for Vault 5 | the author's move must answer this run's critic |
| V4-S20 | The rescue's commit message is `commit` (`e507f21`) | `d2ae5f2`'s message records what `e507f21` holds; no force-push | a commit message is the record's caption |
| V4-S21 | The Changelog got a stray v2.2 line instead of a v1.2 row | `d2ae5f2` replaces it | read the diff before the commit (`git diff --cached`) |

The writer's own behaviour taught one more: asked for more release, sooner, a model with no contract gave exactly that. Asked under a contract, it removed the window, the breakdown and the confession, and said why.

## Errata for the videos

These are corrections to what was said in the Vault 4 video; this Reference already uses the correct versions. They mirror Section A of `VAULT-4-ERRATA.md`.

| ID | Where | Said | Correct |
| --- | --- | --- | --- |
| V4-E01 | A | Vault 3 found "four of four... three out of four, two out of three, three out of three" | 4 of 4 threads held (`V3_SPINE_OK 4/4`). The per-thread figures quoted are the Vault 3 rehearsal's (3 Nov), not the performance's |
| V4-E02 | A | the draft was "composed with Claude in an isolated session", "about 30 rounds" | a separate chat with none of the novel's files loaded; that chat still had tools (V4-S05). The turn count is in `PROVENANCE.md` |
| V4-E03 | B | the Playground is "the only place you can speak to a model without... your account information" | the place this video uses: a bare model with no tools and no system prompt |
| V4-E04 | D | the tier lens "runs from F-tier to S-tier" | the video's climb is C → S; the tiers are a lens, not a score |
| V4-E05 | C | the original Chapter 4 should "match exactly" | its paragraphs sit nearest Chapter 4 because Chapter 4 is in the index: likeness, not a match. Its verdict is `MOTIF_CLEAR` |
| V4-E06 | E–I | C1, C3, C4 and C5 were each "compared against the index again" | only `v4 draft` and `v4 contract2` use the Vault 2 index; `beats`, `critic`, `matrix` and `contract5` check structure and claims |
| V4-E07 | G | "I am now going to fix the problems off-camera... copy my corrections" | the corrections were prepared from rehearsal 3 (V4-S19): they make the notes and the beats agree, but they don't answer this run's Contract 2 line by line |
| V4-E08 | H | "grab the c4.json" | `c4.md` |
| V4-E09 | I | "I'll just call it v2.2" | v1.2 (`d2ae5f2` corrects the Changelog) |
| V4-E10 | J | "the script scores the output against the prediction key" | the laptop shows evidence; the author ticks: 4/6 before, 6/6 after. `KEY_NEVER_PASTED` (6 bundles, 49,225 characters) was not said aloud |

**Carried to Vault 3's errata (found in Vault 4).** Vault 3's record says issue #2 was adopted and main ends with that adoption. In fact #2 was closed by hand on 5 Nov, with the adoption's commit message posted as a comment, and `SSOT.md` was unchanged since `74fd9a4`. On 9 Nov the author adopted it properly: `3c6359b docs: adopt the Figure's light rule (closes #2)`. The wording was drafted in the Vault 4 support session at the author's request and adopted by the author. That commit is Vault 4's baseline.

## Assets in this vault

Every file is listed, in order of use, in `VAULT-4-INDEX.md`:

- the judge: `v4_check.py` 1.1.1;
- the scripts: `door-off` / `door-on`, `new-run`, `tab-header-v4`, `preflight-v4`, `bundle`, `grab`, `seal-check-v4`, `capture-evidence-v4`;
- the paste pack: the five contracts, the manifest excerpts, the B prompt, the sealed `PREDICTION-V4.md`, the cold-open draft and its `PROVENANCE.md`;
- the downloads: the canonical schema, the ask-the-receiver card, the tier worksheet, the critic's rubric, the sealed-key pattern, and the five contracts as used, as templates and as first written;
- the diagram `V4-FLOW-the-cognitive-contracts`;
- the record: the video's transcript, the capture log, the take's evidence (six replies with their receipts, the paste log, the audits), and [github.com/DamianGiambazi/novel-ssot](https://github.com/DamianGiambazi/novel-ssot) with `main` and the branches `v4-dr1`, `v4-dr2`, `v4-dr3`.

## Glossary

| Term | Meaning here |
| --- | --- |
| contract | one prompt in the five-field schema, with one job and a checkable output |
| the schema | `role`, `context`, `task`, `constraints`, `output_format` |
| C-tier draft | the cold open: made with no rules, well written and structurally wrong |
| the writer | the model under each contract: a bare model, no tools, one fresh request each |
| bare model | a model reached through the API with no tools and no system prompt: it knows only what is pasted |
| Playground | the Claude Console's page for sending one API request and reading the response |
| Raw view | the Playground's response as JSON: the reply's text, the model and the token counts |
| bundle | one paste, built and logged by `bundle.ps1` |
| receipt | the whole API response, kept beside each saved reply (`*.api.json`) |
| the key | what a correct Chapter 4 is: the author's notes, the reference matrix, the rubric |
| the seal | the key and the predictions, committed and pushed before the first contract |
| the rubric | six lines a rescued Chapter 4 must meet; the laptop shows evidence, the author ticks |
| self-report | a field where the model describes its own output (`window_motif_present`); always checked |
| paste log | `pastes.jsonl`: every character that crossed to the writer |
| `[author]` text | text the author typed, exempt from the leak check |
| tiers | C → S, a teaching lens, never the score |
| connective tissue | the chapters between the pillars: they build tension and resolve nothing |
| rehearsal branch | `v4-dr1`, `v4-dr2`: a dress rehearsal's record (three were run: `v4-dr1` to `v4-dr3`), kept; main is touched only by the take |

## What comes next

Vault 5 runs the same contracts on Chapter 5. The draft passes every check and still feels hollow. A contract can make a chapter correct; it can't make it felt. That is the Somatic Veto.