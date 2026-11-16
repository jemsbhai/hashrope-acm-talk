# Talk plan: one hour, 25 slides + 2 backup

ACM chapter talk, Friday, November 20, 2026. One-hour slot.
Speaker notes in the deck carry the same timings, slide by slide, cumulative to 60:00.

| # | Slide | Time | Cumulative |
|---|-------|------|------------|
| 1 | Title | 1:00 | 1:00 |
| 2 | The next hour (agenda) | 1:00 | 2:00 |
| 3 | Strings do not scale to everything | 2:30 | 4:30 |
| 4 | Every fingerprinting tool makes you pick | 2:30 | 7:00 |
| 5 | What a rope is | 2:30 | 9:30 |
| 6 | Put a fingerprint on every node | 3:00 | 12:30 |
| 7 | The arithmetic, three lines | 2:30 | 15:00 |
| 8 | Balance and persistence | 2:30 | 17:30 |
| 9 | Substring fingerprints and repeat nodes | 2:30 | 20:00 |
| 10 | Demo in Python: edit, verify, locate | 3:00 | 23:00 |
| 11 | Demo in TypeScript: same bytes, same fingerprint | 2:30 | 25:30 |
| 12 | Your turn: run it yourself (hands-on) | 5:00 | 30:30 |
| 13 | Honest limits, written on the box | 2:00 | 32:30 |
| 14 | Four languages, one fingerprint, one version line | 2:00 | 34:30 |
| 15 | How four implementations stay identical | 2:30 | 37:00 |
| 16 | What the research measured (IEEE ICTAI 2026) | 2:30 | 39:30 |
| 17 | When the specialist wins | 2:30 | 42:00 |
| 18 | What prefix reuse is worth on real hardware | 2:00 | 44:00 |
| 19 | Where verified sequences pay off | 2:00 | 46:00 |
| 20 | AI agent memory: one context, many branches | 3:00 | 49:00 |
| 21 | Recipes: four patterns you can ship | 2:30 | 51:30 |
| 22 | Get started | 1:00 | 52:30 |
| 23 | Takeaways | 1:30 | 54:00 |
| 24 | Discussion: three questions worth arguing | 4:00 | 58:00 |
| 25 | Thank you / Q&A | flex | 60:00 |

Backup 1: exact comparison timing (npm 0.3.3 vs 0.2.2). Backup 2: the verification ledger (ICTAI Table III).

## How the hour is covered

- The DevFest cut ran 30 minutes; this cut doubles the delivery time on the core sections and adds three segments the 30-minute version did not have: a 5-minute hands-on at the midpoint (slide 12), the two research-depth slides promoted from backup (17 and 18), and a 4-minute seeded discussion before Q&A (slide 24).
- Flex points if running long: slide 12 can shrink to 3 minutes, slide 24 to 2. If running short: expand slide 12 and let slide 24 run into open Q&A on slide 25.
- Rebuild: `build_acm_deck.py` regenerates the deck structure from the DevFest Florida original; `build_acm_notes.py` writes the speaker notes and timings.
