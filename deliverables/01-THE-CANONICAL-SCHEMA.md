# The Canonical Schema — a one-page field guide

Every contract in Vault 4 has the same five fields. Each answers one question the receiver would ask if it could (Vault 1's 100% question: *"Are you 100% ready, or do you need more information?"*).

```xml
<role>          who should I be?                      </role>
<context>       what do I need to know?               </context>
<task>          what exactly do you want?             </task>
<constraints>   what must not happen?                 </constraints>
<output_format> what does done look like?             </output_format>
```

| Field | Write | Avoid | Vault 4 example |
|---|---|---|---|
| `role` | a job with a point of view ("Forensic Auditor") | a flattering adjective ("world-class expert") | Contract 3: *Forensic Auditor*, so the same model stops trying to please |
| `context` | only facts the receiver can't know and needs; say where each comes from | claims you haven't checked ("MCP Server confirmed") | D5, the drawer constant, Chapter 3's crack |
| `task` | one verb, one object, one outcome | three tasks in one | "Revise Chapter 4 beats. The cost must be external." |
| `constraints` | the fences: what is untouchable, what is forbidden, what to do when information is missing | examples that belong to another case ("missing an appointment" is Chapter 5's cost) | "Where the documents do not say, write UNKNOWN." |
| `output_format` | a shape a machine can check: fields that **ask** (`"<true or false>"`) | pre-filled answers (`"window_motif_present": false` invites an echo) | Contract 2's JSON, checked by `v4_check.py contract2` |

**The power is in the constraints, not the length.**

## Three rules that came from the earlier vaults
1. **Ask first.** Send the bare task with the 100% question. What the receiver says it lacks becomes your five fields.
2. **Check, don't trust.** Any field where the model reports on itself (`window_motif_present`, `cost_type`) gets a check outside the model. A model's account of what it did is not a log (Vault 3).
3. **Seal the answer key before you run the contract.** Then the result is the key's verdict, not your impression (Vaults 2–3).

## Original reference
`originals/canonical-prompt.md` is the schema as first written (a software-architecture example); `originals/The_Golden_Rule_of_Prompting.md` is the rule behind it.
