# The sealed key — a pattern for checking any AI output

`PREDICTION-V4.md` is the worked example. The pattern fits any contract-driven job: a policy summary, a code migration, a client report.

## Before the run (commit and push it: the timestamp is the proof)
1. **The key:** what a correct output must contain, written by someone who knows, *before* the model runs. In Vault 4: the author's Chapter 4 notes, a reference matrix, a six-line rubric.
2. **What the model is given,** listed, with what each document can support. Say plainly what it is **not** given, and so cannot know.
3. **Predictions,** each with the check that will judge it: a script's verdict word, or a named person ticking a line.
4. **Fair-test conditions:** the settings that stop the model seeing the key (no project, no connectors, no web, no memory, a fresh chat).
5. **What happens if something breaks:** it stays in the record and is named.

## During the run
- Log every input that crosses (Vault 4: `bundle.ps1` → `pastes.jsonl`). Mark the human's own additions.
- Save every reply as it came (`grab.ps1`). Never overwrite the recorded run.

## After the run
- Score against the key, line by line, by the person named in the key.
- Audit the input log: the key never crossed (`KEY_NEVER_PASTED`).
- Check the seal came first (`SEALED_BEFORE_CONTRACTS`).
- Record rehearsal results in the next run's key, so the next prediction is made knowing them, and says so.

## Template
```markdown
# PREDICTION — [job]
**Sealed:** committed and pushed before the first run. Baseline: [commit].
## The key (the model never sees it)
## What the model is given (and what it can't know)
| Given | Contains | Supports key line |
## Predictions
| # | Step | Prediction | Checked by |
## Fair-test conditions
## Rehearsal rows (filled before the real run is sealed)
## If something breaks
```
