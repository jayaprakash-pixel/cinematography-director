# Cinematography report - T05 "The printer nobody checked"

Timeline: `tests/results/T05_timeline.json` (18 shots, 90.0 s, 25 fps).

## 1. Brief card
| Item | Value |
|---|---|
| Intent (user's words) | A documentary reconstruction of a real 2016 bank cyber-heist: "it had started with a printer nobody checked." |
| Audience | General documentary viewers. No technical knowledge is assumed. |
| Platform / ratio / duration | 16:9, 90 s (ends 1:30). |
| Mode(s) | **M08 Documentary** (honesty, labelled reconstruction) + **M05 Cinematic suspense** (information ledger, budgets). M02 is not used because the piece is 90 s. Its callback rule (the end answers the opening) is still applied. |
| Target adapter | Primary: **physical_camera** (small crew, actors). Secondary per shot: **motion_graphics_2d** (S08, S14, S15, S16), **ai_video** (S01). Every shot has a `target` field in the timeline. |
| Constraints | No real footage. Reconstruction and AI shots must carry a label. Small crew means tripod, slider and shoulder rig only. There is no crane, dolly track or drone. |
| House rules | `SHORTS_PIPELINE.md` and the style rulebooks cover 9:16 Shorts. They do not apply to this 16:9 documentary, so there is no conflict. |
| Timing source | **Estimated**, from the approximate narration times in the brief. Re-time to measured word timings after the voice is recorded. |

### Assumptions (stated, not asked)
1. **The case.** The narration matches the widely reported February 2016 Bangladesh Bank heist (fraudulent SWIFT orders, a disabled printer, about US$81 million lost). This run did not check sources. All numbers on screen come from the user's narration. Check every number on screen against primary reporting before release.
2. **The misspelled word.** The narration does not give the word. S15 uses a placeholder `[VERIFIED WORD]`. Put the real spelling on screen only after it is checked against a source.
3. **Props are generic.** No real bank logo, real SWIFT form, real account name or real person appears. Order slips and printed pages are made-up reconstruction props. Their text is soft or generic.
4. **The red error LED** on the printer (S02, S18) is a dramatic device and not a documented fact. The RECONSTRUCTION label covers it. If you want strict literalism, use an unlit printer and drop the red accent from the LED. The graphics keep the red accent.
5. **Frame rate and shutter:** 25 fps, 180° shutter (documentary delivery). Sensor: full frame. Lenses are FF focal lengths.
6. **Cast:** one actor, a bank staff member. The brief says "staff", so the script uses "she" only as the actor's blocking pronoun. Cast anyone.
7. **Labels:** a screen-fixed bug "RECONSTRUCTION" on all actor shots, "AI-GENERATED RECONSTRUCTION" on S01 and "ILLUSTRATION" on graphics. The bug is screen-fixed, so it does not count as reading text for camera holds.

## 2. Beat map
| Beat | t | Anchor word | Kind | Content |
|---|---|---|---|---|
| B1 | 0:00.0 | "printer" | hook | A printer stopped working on a Friday night. |
| B2 | 0:06.0 | "nobody" | context | Nobody noticed. It was the weekend. |
| B3 | 0:14.0 | "confirmations" | development | The printer's only job: print transfer confirmations. |
| B4 | 0:22.0 | "someone" | turn | Someone did not want them seen. |
| B5 | 0:30.0 | "Thirty-five" | key_info | 35 orders, nearly US$1 billion. |
| B6 | 0:40.0 | "Saturday" | reveal | Staff fix the printer and the paper comes out. |
| B7 | 0:50.0 | "authorised" | climax | Page after page of unauthorised transfers. |
| B8 | 1:02.0 | "misspelled" | turn | Most were blocked. One misspelling stopped US$20 million. |
| B9 | 1:14.0 | "gone" | climax | US$81 million was already gone. |
| B10 | 1:24.0 | "checked" | resolution | It started with a printer nobody checked. |

## 3. Emotion timeline
| Beat | Dominant | Secondary | Intensity | Visual lever |
|---|---|---|---|---|
| B1 | curiosity | unease | 2 | Night exterior, then a printer dying in the dark. |
| B2 | unease | calm | 2 | Empty, locked-off frames. Lights go off with nobody there. |
| B3 | curiosity | unease | 2 | An empty output tray (absence as information). |
| B4 | dread | curiosity | 4 | The only camera move at night: a slow approach to the printer. |
| B5 | shock | dread | 4 | Static graphic. The numbers are the statement. |
| B6 | tension | relief | 3 | Hard cut to daylight in the same frame as S03. |
| B7 | alarm | disbelief | 5 | First handheld shot. A rack focus reveals the page content. |
| B8 | relief | irony | 3 | Slips turn grey. A zoom onto one word. |
| B9 | loss | dread | 5 | Red slips remain, then a pull-out leaves the person small. |
| B10 | reflection | dread | 3 | The S02 frame returns, static, then a fade to black. |

## 4. Visual strategy
**Information ledger**
| Up to | Viewer knows | Viewer does not know yet |
|---|---|---|
| 0:14 | A printer stopped. Nobody was there. | Why it matters. |
| 0:22 | It printed transfer confirmations. | That the stop was deliberate. |
| 0:30 | Someone wanted them unseen. | The scale. Who did it (never shown; not in the narration). |
| 0:40 | 35 orders, nearly US$1 billion. | Whether the bank finds out. |
| 0:55 | Staff restart it and pages come out. | What the pages say. |
| 1:02 | The transfers were never authorised. | How much was saved or lost. |
| 1:14 | Most were blocked. A typo saved US$20 million. | The final loss. |
| 1:30 | US$81 million gone. The cause was the printer. | (complete) |

**See / hide list**
| Hidden | Method | Revealed at | Reveal method |
|---|---|---|---|
| The page content | No paper at night (S06 empty tray). The page in S11 is out of focus. In S12 the page is in a soft OTS. | 0:57.0 (S13) | Rack focus from her eyes to the page lines. |
| The attacker | Never shown. No hooded hacker shot. The narration does not name the attacker, so the picture does not either. | never | - |
| What the slips are | S08 slips are blank rectangles. | 1:02.0 (S14) | The same slips change colour: grey = blocked, red = went through (S16). |
| The saving word | S15 opens wide on a full typed line. | 1:09.8 | Zoom onto the word, then a red circle. |

**Primary / secondary subject:** the printer is primary in B1-B4 and B10. Numbers are primary in B5, B8 and B9. The staff member is primary in B6-B7, with the printer secondary.

**Motif register**
| Motif | First | Returns | Change |
|---|---|---|---|
| Printer CU, S02 frame | S02 0:03.5 (dies, red LED) | S18 1:24.0 | Same frame. The red light now means US$81 million. |
| Office WS, S03 frame | S03 0:06.0 (night, empty) | S09 0:40.0 | Daylight, one person present. |
| 35 slips | S08 0:30.0 (blank) | S14 1:02.0, S16 1:14.0 | Blank, then grey (blocked), then red (lost). |
| Paper | S06 empty tray | S11, S12, S17 | Nothing, then one page, then a stack, then pages on the floor. |

**Colour script**
| Section | Base | Accent | Note |
|---|---|---|---|
| Night (S01-S07, S18) | desaturated teal-grey, 4300 K spill through blinds | **red** printer LED only | The red accent is never used on anything other than the printer and the loss. |
| Graphics (S08, S14-S16) | off-white paper, charcoal type | red = money that went through. Grey = blocked. | It is the same red as the LED, which links the loss to the printer. |
| Day (S09-S17) | neutral 5600 K window daylight | red LED off, green LED at the restart only (S10) | The contrast rises through the day section (see light). |

**Visual identity**
- Lenses: one prime family, 35 / 50 / 85 / 100 mm macro. 35 mm for places, 50 mm for the printer, 85 mm for people, 100 mm for paper details. Distance is chosen first in every shot.
- Camera behaviour: locked-off tripod by default ("nobody was watching", so the camera watches without moving). There are three physical moves, each with a turn: the push in at B4, the handheld at B7 and the pull-out at B9. The graphics have one zoom (B8).
- Light: low-key at night (contrast about 8:1, a convention). Day starts flat (about 2:1 at S09) and rises to about 4:1 by S13 as the fill is flagged off. Contrast follows tension.

## 5. Shot list
Each block uses the fields that matter. **T** = TECHNICAL, **C** = CREATIVE.

```
SHOT S01 - "Friday night"                     00:00.0 - 00:03.5 (3.5 s)   TARGET ai_video
ID      "On a Friday night in February, ..."
WHY     orient: place and time before fragments. curiosity 2
CAMERA  EWS, low angle 10° up, 35 mm feel, static ("camera holds completely still")
FRAME   generic office tower, centred; one mid floor dimly lit; no landmark, no logo
LOOK    night, cool street spill; label AI-GENERATED RECONSTRUCTION
T/C     T: generate 6 s, cut 3.5 s.  C: static, because the stillness sets the tone for the night section
```
```
SHOT S02 - "A printer stopped"                00:03.5 - 00:06.0 (2.5 s)
ID      "...a printer stopped working." (event on 'stopped' ~00:04.4)
WHY     hook object, first appearance of the motif. unease 2
CAMERA  CU, printer eye level, 3/4 left, 50 mm at 0.9 m, tripod, static
FRAME   control panel in right third, dark room fills the left 2/3 (negative space = nobody)
MOTION  subject: status display goes dark, red LED comes on 00:04.4-00:04.8 (practical, switched by the crew)
FOCUS   panel; T4, moderate DOF
LOOK    only light = display glow + blinds spill; the red LED is the first accent in the film
LINKS   out: hard cut. This frame returns as S18
```
```
SHOT S03 - "Nobody noticed"                   00:06.0 - 00:10.0 (4.0 s)
CAMERA  WS, eye level 1.5 m, 35 mm at 7 m, tripod, static, T5.6 deep
FRAME   rows of empty chairs, dark monitors; the printer small at far right third, its red LED visible
WHY     the viewer sees the warning that no one in the room sees (ledger)
LINKS   lock the tripod position and record the marks: S09 repeats this frame in daylight
```
```
SHOT S04 - "It was the weekend"               00:10.0 - 00:14.0 (4.0 s)
CAMERA  WS corridor, one-point perspective, 35 mm at 12 m, static, deep
MOTION  subject: ceiling lights switch off row by row toward camera 00:11.0-00:13.0
WHY     the building empties itself; no person is needed to say "weekend"
```
```
SHOT S05 - "Its only job"                     00:14.0 - 00:18.0 (4.0 s)
CAMERA  MS, profile, 1.1 m height, 50 mm at 2.0 m, static, T4
FRAME   printer centre; tray card "CONFIRMATIONS" (generic prop) readable at the lower third
WHY     establishes the printer's function before the viewer is told it failed in its function
```
```
SHOT S06 - "Confirmations of money transfers" 00:18.0 - 00:22.0 (4.0 s)
CAMERA  INSERT, 30° down, 100 mm macro at 0.45 m, static, T2.8 shallow
FRAME   empty output tray fills the frame; nothing in it
WHY     absence is the information: the proof is not coming out
```
```
SHOT S07 - "Someone did not want anyone to see"  00:22.0 - 00:30.0 (8.0 s)   KEY BEAT 1
CAMERA  WS -> MWS, seated eye height 1.2 m, 50 mm, starts 4.5 m from the printer
MOTION  dolly_in 0.6 m on slider, 00:22.4-00:29.2, ease in-out sine; designed end frame held 0.8 s
        motivation APPROACH: the viewer closes on the threat the staff do not know about
FRAME   empty chair backs pass through foreground (parallax shows it is a dolly, not a zoom)
FOCUS   printer; T4 at 4.5 m -> 3.9 m, pull focus with the move (marks 4.5 m / 3.9 m)
ALT     rejected: hooded hacker at a keyboard, because it invents a person and a place the narration never names (principle 11)
T/C     T: slider 60 cm, speed 0.09 m/s. C: the only move at night, so it carries the turn
```
```
SHOT S08 - "35 orders, nearly one billion"    00:30.0 - 00:40.0 (10.0 s)   TARGET motion_graphics_2d
FRAME   35 blank slips appear in a 7x5 grid 00:30.0-00:30.8, then "35 TRANSFER ORDERS" (read 00:30.8-00:35.0),
        then "NEARLY US$1 BILLION" (read 00:35.4-00:40.0)
CAMERA  static (text on screen); hold windows in timeline
WHY     dense numbers: the composition is the statement, and movement would compete
```
```
SHOT S09 - "Saturday"                         00:40.0 - 00:44.0 (4.0 s)
CAMERA  exact S03 position and lens (35 mm at 7 m, 1.5 m), static
LOOK    daylight 5600 K through blinds, soft, about 2:1; one staff member walks to the printer
WHY     the same frame with a different time: the cut tells the viewer it is the next day
```
```
SHOT S10 - "Fixed the printer"                00:44.0 - 00:47.0 (3.0 s)
CAMERA  CU hands, 20° down, 85 mm at 0.8 m, static, T4
MOTION  hand reseats cable and presses power; LED turns green 00:45.6
LINKS   out: cut on action (finger on button) into S11
```
```
SHOT S11 - "The paper started coming out"     00:47.0 - 00:50.0 (3.0 s)
CAMERA  INSERT level with the slot, 100 mm macro at 0.4 m, static, T2.8 shallow
MOTION  first page slides out 00:47.6-00:49.6; focus on the slot edge, print soft and unreadable (hide)
```
```
SHOT S12 - "Page after page"                  00:50.0 - 00:55.0 (5.0 s)
CAMERA  OTS over her right shoulder, 1.55 m, 35 mm at 1.2 m, shoulder rig
MOTION  handheld 00:50.0-00:55.0, small drift, follows the page as she lifts it
        motivation SUBJECTIVE: the calm locked-off world breaks; we stand where she stands
FRAME   pages stacking in the tray, lower right; page text soft
```
```
SHOT S13 - "Transfers they had never authorised"  00:55.0 - 01:02.0 (7.0 s)   KEY BEAT 2
CAMERA  CU, eye level, 3/4 front from the printer side (same side of line as S12), 85 mm at 1.3 m, tripod, static
FRAME   page edge soft in the lower foreground; her face upper third
FOCUS   rack eyes -> page lines 00:57.0-00:58.4 (trigger 'Transfers'); marks 1.3 m -> 0.5 m; T2 shallow
        reason: the viewer reads the proof when she does. The page shows generic dates, "USD" and amounts (prop)
LOOK    fill flagged off: about 4:1, the hardest light of the day section
ALT     rejected: an insert of the page alone. It shows the fact but loses the person who discovers it, and the rack keeps both in one frame
T/C     T: check focus breathing on the 85 mm at 0.5 m. Use a matte box flag on the window.
```
```
SHOT S14 - "Most were blocked"                01:02.0 - 01:07.0 (5.0 s)   TARGET motion_graphics_2d
FRAME   the S08 grid returns; most slips turn grey with "BLOCKED" (read 01:02.6-01:07.0); a few stay blank
CAMERA  static
```
```
SHOT S15 - "One misspelled word"              01:07.0 - 01:14.0 (7.0 s)   TARGET motion_graphics_2d
FRAME   one typed line on a reconstructed order; the word [VERIFIED WORD] circled in red at 01:09.8
CAMERA  zoom_in, scale 1.00 -> 1.60 about the word, 01:07.4-01:09.8, sine.inOut (no parallax layers, so this is a zoom)
        motivation APPROACH: the act of looking harder at one word
        hold for "US$20 MILLION STOPPED" 01:10.0-01:14.0
```
```
SHOT S16 - "Eighty-one million was already gone"  01:14.0 - 01:19.0 (5.0 s)   TARGET motion_graphics_2d
FRAME   the remaining slips turn red; "US$81 MILLION" in the accent red (read 01:15.0-01:19.0)
CAMERA  static
```
```
SHOT S17 - "Gone"                             01:19.0 - 01:24.0 (5.0 s)
CAMERA  MWS -> WS, eye level 1.5 m, 35 mm, starts 3.0 m
MOTION  dolly_out 0.8 m, 01:19.2-01:23.4, ease in-out sine, end frame held 0.6 s
        motivation WITHDRAW: she is left small in an office that cannot undo it
FRAME   she stands centre among pages on desk and floor; printer at frame right
FALLBACK no track: static 35 mm WS, actor sits down at 01:21.0
```
```
SHOT S18 - "A printer nobody checked"         01:24.0 - 01:30.0 (6.0 s)   KEY BEAT 3
CAMERA  exact S02 setup (50 mm at 0.9 m, printer eye level, 3/4 left), static, night light
FRAME   red LED lit; the room dark again
LINKS   fade to black 01:29.0-01:30.0 (end of film)
ALT     rejected: a slow push into the printer, because it repeats S07 and spends a second approach. Stillness answers the opening frame.
```

**Budget count:** moving 4/18 (22%, M05 limit 40%). Shallow DOF 3/18 (17%, limit 50%). Dolly zooms 0. Effect transitions: 1 (the final fade, which marks the end).

## 6. Timeline
See `tests/results/T05_timeline.json`. It has 18 shots edge to edge from 0.0 to 90.0 s, 10 beats, the `office_day` geography (line staff -> printer, camera side -1), hold windows on every graphic and 8 `music_hints`.

## 7. Validation
**cdcheck:** `python scripts/cdcheck.py timeline tests/results/T05_timeline.json` **did not run in this session.** The tool's permission layer asked for manual approval on every `python` call, and the run was not interactive. I traced each rule of `check_timeline()` against the file by hand:

| cdcheck rule | Result |
|---|---|
| first shot at 0; edges match within 1/25 s; last t1 = 90.0 | pass (3.5, 6, 10, 14, 18, 22, 30, 40, 44, 47, 50, 55, 62, 67, 74, 79, 84, 90) |
| id / t0 / t1 / type on every shot; t1 > t0 | pass |
| moves in the documented list; motivation in the set; reason; t0/t1 inside the shot | pass (S07 dolly_in, S12 handheld, S15 zoom_in, S17 dolly_out) |
| no move inside hold_for_text | pass (S15 zoom ends 69.8, hold starts 70.0; other holds are on static shots) |
| ease given | pass (all 4 moves) |
| vague words in reasons | pass (none) |
| focus from / to / reason / t0 | pass (S13) |
| line of action, `office_day` | pass (all camera_xy have y < 0 = side -1) |
| same subject + size + angle on consecutive shots | pass (none) |
| M05 budgets: moving 4/18 <= 40%, shallow 3/18 <= 50% | pass |
| beats inside 0-90 | pass |

Expected output: `timeline: 0 errors, 0 warnings`. **Run the command once to confirm before you rely on this.**

**Checklist (final_visual_audit.md)**
- [x] Subject consistency. The same actor and wardrobe in S09-S17. The S01 AI prompt has a continuity sheet.
- [x] Spatial consistency. S03 and S09 share one tripod mark. S02 and S18 share one setup.
- [x] 180° rule. All day-office set-ups are on side -1. The S12 -> S13 cut changes more than 30° and one size step.
- [x] Every move has a motivation and a designed end frame. No move happens during text.
- [x] Focus. One rack (S13), motivated by the reveal.
- [x] Lighting continuity. The night section uses one spill direction (blinds, camera left). Day uses one window direction (camera left).
- [x] Colour. Red appears only on the printer LED and the money that went through.
- [x] Props. The page stack grows S11 -> S12 -> S17. Pages on the floor appear only in S17. Script supervisor: note that the floor is clean in S09-S13.
- [x] Transitions. Hard cuts. One cut on action (S10 -> S11). One fade at the end.
- [x] Narrative relevance. Page content stays hidden until S13. The attacker is never shown.
- [x] Restraint. Within budgets. Each sequence pattern differs (night: wide/insert; day: wide -> close -> handheld -> CU).
- [x] Adapter. Each shot names its target. Both dolly shots have a fallback.
- [x] User intent. The narration is unchanged. The reconstruction is labelled.

## 8. Production instructions

### 8a. Crew shot list (physical_camera, 25 fps, 180° shutter, FF)
| Shot | Size / angle / height | Lens at distance | Stop | Support | Move | Focus marks | Light | Notes |
|---|---|---|---|---|---|---|---|---|
| S02/S18 | CU, printer level, 3/4 L | 50 mm at 0.9 m | T4 | tripod | none | panel 0.9 m | blinds spill 4300 K camera L, LED practical | Shoot S18 in the same set-up right after S02. LED switched by crew at 4.4 s. |
| S03 | WS, 1.5 m | 35 mm at 7 m | T5.6 | tripod (tape the marks) | none | 7 m | night spill only, about 8:1 | Printer LED visible far right. |
| S04 | WS corridor, 1.5 m | 35 mm at 12 m | T5.6 | tripod | none | 12 m | ceiling rows on separate switches | Switch-off cue 11.0-13.0 s. |
| S05 | MS profile, 1.1 m | 50 mm at 2 m | T4 | tripod | none | 2 m | spill + panel glow | "CONFIRMATIONS" tray card is a generic prop. |
| S06 | INSERT 30° down | 100 mm macro at 0.45 m | T2.8 | tripod | none | tray floor 0.45 m | small soft top light, cool | Empty tray. |
| S07 | WS -> MWS, 1.2 m | 50 mm at 4.5 -> 3.9 m | T4 | slider 60 cm | dolly in 0.6 m, 22.4-29.2 s, ease in-out | 4.5 -> 3.9 m | night spill | Chair backs in foreground. Hold the end frame 0.8 s. Fallback: static 85 mm MWS. |
| S09 | WS, 1.5 m (S03 marks) | 35 mm at 7 m | T5.6 | tripod | none | 7 m | daylight window 5600 K, 2:1 | Actor enters and walks to the printer. |
| S10 | CU hands 20° down | 85 mm at 0.8 m | T4 | tripod | none | 0.8 m | window key | LED green at 45.6 s. Overlap the action for the cut. |
| S11 | INSERT slot level | 100 mm at 0.4 m | T2.8 | tripod | none | slot edge 0.4 m | window key | Print out of focus. |
| S12 | OTS R shoulder, 1.55 m | 35 mm at 1.2 m | T4 | shoulder rig | handheld 5 s, small drift | page 0.6 m, follow | window key, 3:1 | Page text soft. |
| S13 | CU 3/4 front, eye level | 85 mm at 1.3 m | T2 | tripod | none | eyes 1.3 m -> page 0.5 m, 57.0-58.4 s | flag the fill to 4:1 | Generic page text. Check breathing. |
| S17 | MWS -> WS, 1.5 m | 35 mm at 3.0 -> 3.8 m | T5.6 | slider/dolly | dolly out 0.8 m, 79.2-83.4 s | 3.0 -> 3.8 m | window key, 4:1 | Pages on desk and floor. Fallback: static WS, actor sits at 81.0 s. |

Coverage (TECHNICAL): record 10 s of room tone per location. Record an extra 2 s head and tail on every set-up. Shoot one spare static WS of S12 for the edit.

### 8b. 2D graphics calls (motion_graphics_2d, GSAP)
```js
// S08 30.0-40.0: static camera; slips stagger in, two text cards
tl.from(".slip", {opacity: 0, y: 8, stagger: 0.02, duration: 0.3}, 30.0)   // 35 slips by 30.8
  .from("#t35", {opacity: 0, duration: 0.3}, 30.8)
  .from("#tBillion", {opacity: 0, duration: 0.3}, 35.4);
// S14 62.0-67.0: blocked slips turn grey
tl.to(".slip.blocked", {backgroundColor: "#9a9a9a", stagger: 0.01, duration: 0.4}, 62.0)
  .from("#tBlocked", {opacity: 0, duration: 0.3}, 62.6);
// S15 67.0-74.0: zoom (scale, no parallax) onto the word, then hold
tl.to(world, {scale: 1.60, x: wordX, y: wordY, duration: 2.4, ease: "sine.inOut"}, 67.4)  // APPROACH, ends 69.8
  .from("#circle", {drawSVG: 0, duration: 0.4}, 69.8)
  .from("#t20m", {opacity: 0, duration: 0.3}, 70.0);
// S16 74.0-79.0: lost slips turn red, total
tl.to(".slip.lost", {backgroundColor: "#c0282d", duration: 0.4}, 74.0)
  .from("#t81m", {opacity: 0, duration: 0.3}, 75.0);
```
Rules: the camera holds in every text window. Keep the circled word inside the frame at scale 1.6. Visible width = frame width / 1.6. If the project has no GSAP DrawSVG licence, animate `stroke-dashoffset` instead. The red `#c0282d` must match the graded LED red.

### 8c. AI prompt (S01, ai_video, adapter checked 2026-11-05)
```
A modern glass-and-concrete office tower at night, most windows dark, one middle floor dimly lit.
Quiet city street, Friday night, light rain-damp pavement. Extreme wide shot from a low angle, camera holds completely still.
Wide-angle 35 mm lens feel, deep focus. Cool sodium and blue street light, low contrast sky.
Desaturated teal-grey palette, fine film grain.
Negative prompt (field): text, logo, signage, people, watermark
Continuity: NIGHT-01 (teal-grey base, light from camera left, no saturated colour)
```
Generate 6 s and cut to 3.5 s in the edit. Do not generate any real or recognisable bank building. Add the label "AI-GENERATED RECONSTRUCTION" in the graphics, not in the prompt.

### 8d. Edit notes
Hard cuts everywhere. S10 -> S11 is a cut on action. Fade to black 1:29.0-1:30.0. Re-time every cut to measured word timings after the voice-over is recorded, then run cdcheck again.

## 9. Decisions explained
1. **Locked-off night, three moves in total** (C). The night is about nobody watching, so the camera does not move until the turn (S07). Then the camera goes handheld only when a human takes over the story (S12), and pulls out only at the loss (S17). Rejected: a slow drift on every night shot, which would make the S07 push mean nothing.
2. **S07 dolly, not zoom** (C+T). The viewer *enters* the empty room toward a threat. The parallax of the chair backs proves the presence. Rejected: the hooded-hacker shot (invented, cliché, not in the narration).
3. **S13 rack focus reveal** (C). The page content is hidden for 57 s and is revealed when the staff member reads it. Rejected: a page insert alone.
4. **S15 zoom, not push** (C+T). It is a flat graphic and the beat is about *looking harder* at one word. A 2D scale without parallax is a zoom and is called one.
5. **Red only for the printer and the loss** (C). The LED red in S02 becomes the US$81 million red in S16 and returns in S18. Colour links the cause and the cost without a line of narration.
6. **The ending answers the opening** (C). S18 is the S02 frame. Rejected: a second push-in, which repeats S07.

## 10. Hints for other departments
- **Music** (for Scorewright or another music skill): see `beats` and `music_hints` in the timeline. Peaks are at 0:50-1:02 and 1:14. There is a release at 1:02. Leave near silence at the open and the close. This skill does not decide the music.
- **Sound:** the printer is the sound motif: the fan at night, the restart chirp at 0:45.6, paper feed from 0:47.6 that builds to a stack rhythm. The lights clunk off in S04. Use room tone under all graphics.
- **Graphics:** labels RECONSTRUCTION / AI-GENERATED RECONSTRUCTION / ILLUSTRATION go in a fixed corner. Use the placeholder `[VERIFIED WORD]` until the source is checked. All numbers come from the narration and need a source check.
