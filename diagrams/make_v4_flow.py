"""make_v4_flow.py: the Vault 4 data flow (1600x900 SVG), in the same visual system as the Vault 1-3 diagrams.
Run next to flowkit.py:  python make_v4_flow.py   ->  V4-FLOW-the-cognitive-contracts.svg"""


from flowkit import Svg, H, W

s = Svg("Vault 4 · The Cognitive Contracts: data flow", "a C-tier draft, five contracts, a laptop that checks, an author who decides",
        thesis=["Don't argue with the AI.", "Change the contract, then check it."])

# --- top: the cold open, the question, the audit, the seal
s.band(40, 120, 1520, 190, "BEFORE ANY CONTRACT")
s.box(70, 165, 250, 120, "The C-tier draft", ["`ch04-c-tier.md`", "made before recording", "no SSOT"], "file")
s.box(360, 165, 250, 120, "v4_check draft", ["by word: window, Figure", "by meaning: Vault 2 index"], "tool")
s.box(650, 180, 220, 90, "MOTIF_BREACH", ["the fault, shown"], "verdict")
s.arrow([(320, 225), (358, 225)]); s.arrow([(610, 225), (648, 225)])
s.box(910, 165, 260, 120, "B: ask the receiver", ["\"are you 100% ready?\"", "→ the five fields"], "human")
s.box(1210, 165, 320, 120, "The key, sealed and pushed", ["`PREDICTION-V4.md`", "ch-04 notes · matrix · rubric", "SEALED_BEFORE_CONTRACTS"], "human", sub=14)

# --- middle: the five contracts, each in a fresh chat
s.band(40, 335, 1520, 330, "ONE CONTRACT, ONE FRESH CHAT · every paste logged by bundle.ps1 · every reply saved by grab.ps1")
xs = [60, 310, 560, 810, 1060, 1310]
names = [("C1 Raw Output", ["strip the prose", "keep the skeleton"], "tool"),
         ("C2 Surgical Fence", ["SSOT + manifest", "untouchable zones"], "tool"),
         ("C3 Hostile Critic", ["same model", "paid to disappoint"], "tool"),
         ("The author", ["fills the gap", "from their own notes", "`fixes.txt`"], "human"),
         ("C4 Modality Shift", ["prose → matrix", "UNKNOWN, not invented"], "tool"),
         ("C5 Derivative Matrix", ["synthesis · CSV", "commit message draft"], "tool")]
checks = ["BEATS_OK", "CONTRACT2_OK", "CRITIC_OK", "ch-04-final.txt", "MATRIX_OK", "CONTRACT5_OK"]
for i, (x, (title, lines, kind)) in enumerate(zip(xs, names)):
    s.box(x, 380, 230, 125, title, lines, kind, size=20)
    if i < len(xs) - 1:
        s.arrow([(x + 230, 442), (xs[i + 1] - 2, 442)])
    k = "file" if checks[i].endswith(".txt") else "verdict"
    s.box(x + 15, 545, 200, 70, checks[i], [], k, size=18)
    s.arrow([(x + 115, 505), (x + 115, 543)])
s.label(425, 640, "the model says the window is gone; the laptop checks (SELF_REPORT_WRONG if not)", size=14)

# --- bottom: score, firewall, decision
s.band(40, 690, 1520, 160, "AFTER: THE SCORE IS THE KEY, NOT THE MODEL'S OPINION OF ITSELF")
s.box(70, 730, 300, 95, "v4_check rubric", ["six sealed lines, evidence shown"], "tool")
s.box(410, 742, 230, 72, "n / 6", ["the author ticks"], "verdict")
s.arrow([(370, 778), (408, 778)])
s.box(690, 730, 300, 95, "v4_check pastes", ["what crossed into the chats"], "tool")
s.box(1030, 742, 230, 72, "KEY_NEVER_PASTED", [], "verdict", size=18)
s.arrow([(990, 778), (1028, 778)])
s.box(1300, 730, 230, 95, "The author commits", ["message typed by hand", "`drafts/ch-04-beats.csv`"], "human", sub=14)
s.arrow([(1425, 615), (1425, 728)], colour="orange")
s.legend()
s.save("V4-FLOW-the-cognitive-contracts.svg")
print("saved V4-FLOW-the-cognitive-contracts.svg")
