# Ask the receiver — the first step of any contract

**Before you write a contract, send the bare task with one question:**

> [your task, as you'd first type it]
>
> Before you start: are you 100% ready to execute this prompt, or do you need more information?

**Then map the answer onto the five fields:**

| If it asks about… | It needs | Put it in |
|---|---|---|
| who it's writing as, for whom, in what voice | a role | `<role>` |
| background, documents, what came before | facts | `<context>` |
| what exactly to produce, how much | a precise job | `<task>` |
| what to avoid, what is fixed, what if information is missing | fences | `<constraints>` |
| length, structure, file type, how you'll use it | a shape | `<output_format>` |

**Then decide what it can't have.** Some of what it asks for is the answer itself (in Vault 4: the author's Chapter 4 notes). Leave that out on purpose, and seal it as the key.

**Why it works:** the Golden Rule says to prompt with the care, clarity and context you'd want if you had to act on incomplete information. The receiver is the one with incomplete information, so it is the best judge of what's missing.

**What it doesn't do:** it doesn't check the output. That's the laptop's job, and the author's.
