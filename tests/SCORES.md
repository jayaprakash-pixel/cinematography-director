# Test scores — round 1 (2026-11-05)

Method: each test ran in a fresh `claude -p` session with only the installed skill and the brief (no access to the design conversation). Mechanical checks were run by script. Scoring was done by the skill's builder with `tests/rubric.md`. This is **not a blind review**: treat the scores as a careful self-assessment, not an independent benchmark. The reports and timelines are in `tests/results/`.

## Mechanical checks
| Test | cdcheck | Extra execution check |
|---|---|---|
| T01 30 s tech Short (2D + AI) | 0 errors, 0 warnings | - |
| T02 7 min educational (studio + 3D + Resolve) | 0 errors, 0 warnings | - |
| T03 personal travel (APS-C, gimbal) | 0 errors, 0 warnings | - |
| T04 Blender 40 s (lighthouse) | 0 errors, 0 warnings | **Camera script run in Blender 5.2 headless**: 13 cameras (lens, f-stop, DOF), 13 markers bound to cameras, keyed rack focus (S04, S05, S10, S11) and a keyed push-in (S11) |
| T05 suspense documentary 90 s | 0 errors, 0 warnings | - |

## Rubric (0-4)
| # | Criterion | T01 | T02 | T03 | T04 | T05 |
|---|---|---|---|---|---|---|
| 1 | Narrative understanding | 4 | 4 | 4 | 4 | 4 |
| 2 | Shot selection | 4 | 4 | 4 | 4 | 4 |
| 3 | Movement motivation | 4 | 4 | 4 | 4 | 4 |
| 4 | Zoom vs dolly | 4 | 4 | 3 | 4 | 4 |
| 5 | Focus direction | 3 | 4 | 4 | 4 | 4 |
| 6 | Composition | 4 | 3 | 4 | 4 | 3 |
| 7 | Lens | 3 | 3 | 4 | 4 | 3 |
| 8 | Lighting | 3 | 3 | 3 | 4 | 3 |
| 9 | Colour consistency | 4 | 4 | 3 | 3 | 4 |
| 10 | Continuity | 4 | 4 | 4 | 4 | 4 |
| 11 | Timestamp accuracy | 4 | 3 | 3 | 3 | 3 |
| 12 | AI prompt quality | 3 | n/a | n/a | n/a | 4 |
| 13 | Executability | 4 | 3 | 4 | 4 | 3 |
| 14 | Restraint | 4 | 4 | 4 | 4 | 4 |
| 15 | Storytelling gain | 4 | 4 | 4 | 4 | 4 |
| | **Mean** | **3.73** | **3.64** | **3.71** | **3.86** | **3.67** |
Pass rule (mean >= 3.0, none < 2, cdcheck 0 errors): **all 5 pass.**

Evidence for the scores (examples):
- T01: 2D scale moves named as zooms, not dollies; camera holds on every text window; the answer (the address) is hidden from 0.0 s and revealed at 21.0 s; the lock "docks on the line, not on the site" so the visual does not teach a wrong model; the agent flagged the unverified phishing statistic.
- T02: one studio push-in kept for the promise; the climax re-uses the Ch2 frame with one change; the graph is planted early and completed in Ch4.
- T03: APS-C equivalents given (18 mm = 27 mm FF); partner kept from behind (authentic, not staged); rack focus triggered by a footstep; callback positions recorded for the ending.
- T04: all cameras on the north side to light the final faces; the reveal is a rack focus in one frame instead of a move; a planted match frame (S03 -> S10).
- T05: camera locked off until the turn; dolly (not zoom) into the empty room for presence; a 2D graphic scale called a zoom; red reserved for the printer and the loss; facts it could not verify were flagged, with a `[VERIFIED WORD]` placeholder.
Times 11 = 3 where the brief gave only estimated times (correctly labelled "estimated").

## Weaknesses found and fixed
| # | Weakness | Evidence | Fix | Verified |
|---|---|---|---|---|
| W1 | Blender adapter snippet used `action.fcurves`, which does not exist in Blender 5.2, so eases would silently not apply | T04 verification in Blender 5.2 (`hasattr(Action, "fcurves") = False`) | `adapters/blender.md`: `fcurves()` helper for layered actions with a fallback | snippet run in Blender 5.2: 16 key points, all `EASE_IN_OUT` |
| W2 | Reports are long (25-34 KB). Length earns nothing; the reader needs decisions first | report sizes | `templates/cinematography_report.md` section 0 "Director's summary"; SKILL output contract: complete, not long | T01 retest (round 2) |
| W3 | Fact-flagging happened, but it was not a written rule | T01, T05 agents did it on their own | SKILL output contract: flag factual claims that need a source check | T01 retest |
| - | T03's session could not call `python` on a relative path (test-harness permission rule, not the skill) | T03 log | none in the skill; the agent asked the user to run the check, which is correct behaviour | - |

## Round 2 (retest after W1-W3)
| Check | Result |
|---|---|
| W1 Blender snippet | run in Blender 5.2 headless: keys inserted, eases `EASE_IN_OUT` applied - **fixed** |
| W2 report shape | T01 retest (fresh session) opens with a one-screen Director's summary (identity, 5 key decisions with reasons, budgets 4/11 moving and 1/11 shallow, open fact checks) - **summary fixed**. Length did NOT drop (27 KB vs 25 KB) - **partly fixed**, see Known limits |
| W3 fact flagging | retest lists 4 claims to verify (phishing share, free certificates, simplification, fictional domains WHOIS) - **fixed** |
| cdcheck on retest timeline | 0 errors, 0 warnings (run by the builder; the test session's permission rule blocked its own python call) |
| Retest rubric (T01) | same as round 1 (3.73); readability of the deliverable improved by the summary |
