# Cinematography report - "How a vaccine teaches your immune system"

Timeline: `T02_timeline.json` (51 shots, 420.0 s, 25 fps). All times are `mm:ss.s` and **estimated** (see assumption A2).

## 0. Assumptions (stated, not asked)
| # | Assumption | Effect if wrong |
|---|---|---|
| A1 | The hook text has 48 words. At a calm 2.4 words/s with pauses, it ends at about 00:21.0. The brief gives the hook 40 s. I fill 00:21.0-00:34.0 with a **picture-only preview** (frames from the animations and the poster back), then a title card from 00:34.0 to 00:40.0. I did not change or add narration. | If the presenter speaks more lines, the preview gets shorter. If the editor wants a 30 s hook, delete P01-P03 and move everything 13 s earlier. |
| A2 | Only the hook has text. Chapter shots use the chapter times from the brief, with placeholder presenter lines. | Re-time every event from `words.json` after the voice is recorded, then run cdcheck again. |
| A3 | 25 fps, 180° shutter (1/50 s), UHD 3840x2160 capture and delivery. 25 fps matches 50 Hz mains (India), so no light flicker. No digital punch-ins are planned, so headroom is not a constraint. | At 24 fps, multiply frame numbers by 24/25. |
| A4 | The lens values are full-frame equivalent. On APS-C, divide by 1.5 (50 mm FF = 33 mm APS-C). | - |
| A5 | The studio has a white 1x1 m foam board (fill), C-stands, and a boom arm for overhead inserts. These are cheap and not in the brief. | No boom arm: shoot the overhead inserts with the card on a 60° easel at table height. Use the same lens and distance. |
| A6 | The 3D animator uses Blender. Scale: 1 Blender unit (BU) = 1 µm. | In another 3D tool, the focal lengths and key times transfer as they are. |
| A7 | 3 animations: **A** = Ch1 invader, **B** = Ch2 defenders, **C** = Ch3 rehearsal. The previews P01/P02 are frames from A and B. C4-03 is a **re-render of the set of animation B** (about 12 s) with changed actors. It is not a fourth animation. | If the budget does not allow C4-03, use the end frame of C3-08 plus the graph. You lose the callback (see Decision 4). |
| A8 | The vaccine type is not given. Animation C shows a generic "harmless piece (antigen)" with the same shape as the virus spike and no genetic core. The script owner decides if the script names mRNA, protein or inactivated vaccines. | - |
| A9 | The editor builds the antibody graph in Resolve (Fusion page). | - |
| A10 | House rules: none for this brief. The Shorts rulebooks of this workspace apply to 9:16 Shorts, not to a 16:9 long-form client piece. The no-whoosh transition rule is kept anyway: no transition SFX. | - |

## 1. Brief card
```
BRIEF CARD
Intent (user's words): "Your body has a memory - and a vaccine writes the first entry."
Audience / platform / ratio / duration: high-school students / YouTube / 16:9 / 7:00
Mode(s): M02 long-form + M06 educational
Target: physical_camera (studio, primary) + blender (3 animations) + motion_graphics_2d (graph, Resolve Fusion) + edit_resolve (stock B-roll, titles). Each shot names one target.
Constraints (TECHNICAL): 1 camera, 1 operator, 2 LED panels, 1 slider (assumed 60 cm travel), small studio (assumed 4 x 5 m), 3 short animations, stock allowed, Resolve edit.
House rules: none (A10)
Timing source: script estimate (hook) + chapter times from the brief - ESTIMATED
```

## 2. Beat map
| Beat | t | Anchor | Kind | Content |
|---|---|---|---|---|
| B1 | 00:00.0 | "card" | hook | "This card is 30 years old." It looks like paperwork. |
| B2 | 00:05.9 | "stamp" | reveal | Each stamp is a memory - in your blood, not your head. |
| B3 | 00:19.4 | "met" | hook | The promise: a harmless sample teaches cells to know an unseen enemy. |
| B4 | 00:40.0 | chapter card | section | Ch1 The invader. |
| B5 | 01:00.0 | spike docks | development | The virus binds to a cell. |
| B6 | 01:26.0 | pull-out | key_info | One cell becomes a factory; copies spread. |
| B7 | 02:00.0 | chapter card | section | Ch2 The defenders. |
| B8 | 02:26.0 | receptor fit | key_info | One B cell's receptor fits the spike exactly. |
| B9 | 02:54.0 | presenter | turn | The first time, this takes days (meanwhile you are ill). |
| B10 | 03:30.0 | chapter card | section | Ch3 The rehearsal. |
| B11 | 03:49.0 | "wanted" | reveal | The wanted poster: a harmless description of the enemy. |
| B12 | 04:16.0 | first amber cell | reveal | The B cell learns; memory cells are born. |
| B13 | 05:00.0 | chapter card | section | Ch4 The real attack. |
| B14 | 05:12.0 | memory cells meet virus | climax | Memory cells answer at once. |
| B15 | 05:32.0 | zoom on graph | key_info | Second response: faster and higher. |
| B16 | 06:20.0 | card again | resolution | Back to the vaccination card. |
| B17 | 06:41.0 | "remembers" | resolution | "Every entry in this card is a lesson your body remembers." |
| B18 | 06:52.0 | end screen | cta | End screen. |

## 3. Emotion timeline
| Beat | Dominant | Secondary | Int. | Visual lever |
|---|---|---|---|---|
| B1 | curiosity | warmth | 2 | object first (insert), presenter face not yet shown |
| B2 | surprise | curiosity | 3 | shallow focus hides the stamp, the rack reveals it |
| B3 | anticipation | curiosity | 3 | push-in MS -> MCU, the first move of the video |
| B4-B5 | tension | curiosity | 3 | new world (crane to orient), magenta enters |
| B6 | fear | awe | 4 | pull-out reveals scale; Ch1 studio light rises to 4:1 |
| B8 | discovery | relief | 3 | arc brings the fit into profile |
| B9 | tension | curiosity | 3 | static MCU; graph planted with only one curve |
| B11 | curiosity | warmth | 3 | subject-motion reveal (poster turns), amber paper |
| B12 | realisation | awe | 4 | push-in, shallow DOF, first amber cells |
| B14-B15 | confidence | relief | **5 (peak)** | callback frame of C2-02 with a change; amber curve, zoom to look harder |
| B16-B17 | warmth | resolution | 2-3 | callback of H02 and H01, warmer key, truck along the stamps, pull-out |
| B18 | resolution | - | 1 | wide, static |

The peak (B14-B15) sits on the climax. Intensity drops at each chapter card on purpose (M02: dense and breathing sections alternate).

## 4. Visual strategy
**Information ledger**
| Section | Viewer knows | Must NOT know yet |
|---|---|---|
| Hook | the card is old; stamps = memories in the blood | what the virus looks like; what the "sample" is |
| Ch1 | how the virus enters and multiplies | how the body fights back |
| Ch2 | innate + adaptive defence; the first answer is slow | that it can be rehearsed; the second curve of the graph |
| Ch3 | a vaccine is a harmless piece; cells learn; memory cells remain | how fast the memory answer is |
| Ch4 | memory cells answer fast; the second curve | - |

**See / hide list**
| Hidden | Hide method | Reveal at | Reveal method |
|---|---|---|---|
| The stamp | shallow focus (eyes sharp, card soft) | 00:05.4-00:06.2 | rack focus to the card |
| The virus shape | darkness / back-light silhouette (P01) | 01:00.0 (C1-04) | lit, magenta, held still at docking |
| The poster drawing | angle: back of the paper (P03), then face-down | 03:49.0 (C3-03) | the presenter turns it |
| The receptor fit | angle: the receptor is on the far side | 02:27.0-02:33.0 | 90° arc |
| Second graph curve | time: the right half stays empty in C2-08 | 05:24.5 (C4-04) | the amber curve draws in |
| Amber (memory colour) | not used anywhere before Ch3 | 03:49.0 poster paper, 04:17.0 cells | the colour itself |

**Primary / secondary subject:** presenter shots = face / prop in hand. Animation = the one actor named in the shot subject / its target. Graph = the curve that draws / the axis labels.

**Motif register**
| Motif | First | Returns | Change |
|---|---|---|---|
| Vaccination card | H01 (folded, paperwork) | C2-10, C3-09, C4-06, CL-01, CL-02 | from paper to "lessons": warm raking light in CL-02 |
| Opening frame H02 (MS front) | 00:03.0 | CL-01 06:20.0 | same frame; card open; key 500 K warmer |
| Battlefield frame C2-02 | 02:06.0 | C4-03 05:12.0 | same camera; now amber memory cells answer at once |
| Graph | C2-08 (one grey curve) | C4-04 | the amber second curve completes it |
| Spike shape | C1-04 (virus) | C3-04 poster drawing, C3-05 harmless piece | drawn -> 3D (graphic match), pale = harmless |
| Amber | C3-03 poster paper | C3-06, C4-03, C4-04, CL-02 | grows from paper to cells to curve to card light |

**Colour script**
| Item | Value | Meaning in this video |
|---|---|---|
| Studio base | neutral skin, slate-blue wall `#3A4656` | the classroom |
| Micro-world base | plasma teal `#1F4E5F`, cells off-white `#E8E4DA` | inside the body |
| Defender cells | pale blue `#8FB8DE` | the immune system |
| Threat | magenta `#D6336C` | the real virus only |
| Harmless piece | pale magenta `#E9A3BD` (same shape, low saturation, no core) | the same shape, without danger |
| **Accent** | amber `#F2B33D` | learned memory - the core idea |
| Graph first curve | grey `#9AA3AD` | the slow first answer |

Progression: hook neutral-warm -> Ch1 cooler, higher contrast, magenta rises -> Ch2 neutral -> Ch3 amber enters -> Ch4 amber dominates the micro world -> close warmest (grade +500 K, key 3800 K). Saturation and contrast peak at C4-03/C4-04.

**Visual identity:** studio = "teacher across a desk": 50 mm at 2.2 m (MS) or 1.3 m (MCU), eye level, tripod or slider, high-key 2:1. Micro world = "a probe at cell scale": 35-50 mm virtual, deep focus, slow eased moves, always a stop and a held end frame before labels. One push-in in the hook, one in the key reveal (C3-06), one pull-out at each ending (C1-07, C3-08, CL-03).

**Intended response:** Hook: "I want to know how paper can be a memory." Ch1: "This is how I get ill." Ch2: "My body fights, but slowly the first time." Ch3: "A vaccine is a safe rehearsal." Ch4: "So the second time it wins fast." Close: "Each stamp is a lesson."

## 5. Shot list
Full blueprints for the 6 key shots follow. The other shots are in the compact table. The timeline holds every value.

```
SHOT H03 - "Each stamp is a memory"                     00:05.2 - 00:11.0 (5.8 s)
ID        "But each stamp on it is a memory - not in your head, in your blood." ('stamp' ~00:05.9 est.)
WHY       narrative: the turn of the hook - paper becomes biology. emotional: surprise 3
CAMERA    MCU, eye level 1.55 m, setup B: 1.3 m from the face, 30° camera-left of the A axis. 50 mm (distance first: near = personal)
FRAME     card held in FG frame-left, lower third, 0.6 m from lens; face in the right third, eyes on the upper third line
FOCUS     start on eyes 1.3 m (card soft = stamp hidden). Rack eyes -> stamp 00:05.4-00:06.2 (0.8 s);
          rack stamp -> eyes 00:08.3-00:09.0 as the presenter touches the inner forearm. f/2.0, shallow (budgeted)
LOOK      key LED1 4300 K camera-left; card catches the key
GUARD     no camera move: two racks already move attention
TECHNICAL vs CREATIVE: T = focus marks 1.3 m / 0.6 m, test for focus breathing on the 50 mm. C = racks; alt rejected: push-in to the card (moves during dense lines, loses the person-card relation)
```
```
SHOT H06 - "An enemy they have never met"               00:16.8 - 00:21.0 (4.2 s)
CAMERA    MS -> MCU, eye level, setup A front, 50 mm, slider push 2.2 m -> 1.8 m
MOTION    push_in 0.4 m, 00:16.8-00:19.6 (2.8 s), ease in-out. APPROACH: the promise of the video, said to the viewer
          end frame MCU, eyes on the upper third, held 1.4 s after 'met'
FOCUS     eyes, pull 2.2 m -> 1.8 m with the move (operator marks on the slider). f/4
TECHNICAL vs CREATIVE: T = 60 cm slider, marks at 0 and 40 cm. C = first move of the video, so it has weight.
```
```
SHOT C2-04 - "The fit"                                  02:26.0 - 02:36.0 (10 s)   target: blender
CAMERA    MS of one B cell, 50 mm virtual, eye level to the cell equator, radius 12 BU
MOTION    arc 90° around the B cell 02:27.0-02:33.0 (6 s), ease in-out. REVEAL: the matching receptor is on the far side
          end frame: receptor + spike in exact profile, frame centre-right, held 3 s
FOCUS     deep (DOF off): the mechanism must be readable
GUARD     no labels during the arc; label "receptor fits the spike" may appear after 02:33.0
```
```
SHOT C3-06 - "The cell learns"                          04:16.0 - 04:28.0 (12 s)   target: blender
WHY       the thesis of the video; first amber memory cells. realisation 4
CAMERA    MS -> CU, 85 mm virtual, dolly from 14 BU to 9.8 BU from the B cell (30% closer)
MOTION    push_in 04:17.0-04:22.5 (5.5 s), ease in-out. APPROACH: we enter the moment of learning
          zoom: none - a zoom would only "look harder"; here the camera enters the space (parallax of plasma particles)
FOCUS     B cell sharp, background plasma soft: Blender f/1.4 at focus 9.8 BU (test frames; scene scale is not real)
LOOK      daughter cells shift off-white -> amber #F2B33D from 04:22.5; hold 5.5 s
TECHNICAL vs CREATIVE: C = alt rejected: zoom-in (reads as scrutiny, not arrival); slow motion (no reason)
```
```
SHOT C4-04 - "Faster and higher"                        05:24.0 - 05:40.0 (16 s)   target: motion_graphics_2d
CAMERA    flat graph, full frame. Same layout as C2-08 (grey curve already present)
TEXT      hold 05:24.5-05:31.5: amber second curve draws 05:24.5-05:28.5, labels "1st time" (grey) / "2nd time" (amber)
MOTION    zoom_in scale 100% -> 140% 05:32.0-05:34.5 (2.5 s), ease in-out, centred on days 0-7. APPROACH (act of looking).
          This is a 2D scale, so it is a zoom, not a dolly.
          hold 05:35.0-05:40.0 on the end frame
GUARD     no numbers on the y axis unless a sourced value is supplied (accuracy)
```
```
SHOT CL-03 - "A lesson your body remembers"             06:38.0 - 06:52.0 (14 s)
CAMERA    MCU -> MS, setup B, 50 mm, slider 1.3 m -> 1.7 m, f/2.0 shallow (card and face both inside DOF at 1.3 m: card held next to the face)
MOTION    line said 06:40.0-06:44.0 (est.) on a still camera; pull_out 0.4 m 06:45.0-06:51.0, ease in-out. WITHDRAW: the ending
          end frame MS, held 1 s
LOOK      key 3800 K (500 K warmer than the rest), grade warm; amber skim on the card from LED2
TECHNICAL vs CREATIVE: C = alt rejected: crane up (no jib; too grand for a quiet line)
```

**All shots (compact)** - setups: A = front, 50 mm at 2.2 m (MS), 1.8 m (MCU), 24 mm at 2.6 m (WS); B = 30° left, 50 mm at 1.3 m (MCU) or 35 mm at 1.6 m (MS); C = overhead / table inserts.
| ID | t0-t1 | Target | Size / angle | Lens / DOF | Camera | Job |
|---|---|---|---|---|---|---|
| H01 | 00:00.0-00:03.0 | phys C | INSERT overhead | 90 mm 0.55 m f/8 deep | static | card unfolds; object first |
| H02 | 00:03.0-00:05.2 | phys A | MS front | 50 mm 2.2 m f/4 | static | establish room + presenter |
| H03 | 00:05.2-00:11.0 | phys B | MCU 30°L | 50 mm 1.3 m f/2 shallow | static + 2 racks | stamp reveal |
| H04 | 00:11.0-00:14.8 | phys A | MS front | 50 mm f/4 | static | "Today I'll show you" |
| H05 | 00:14.8-00:16.8 | stock | INSERT microscope | - | static | "billions of cells" |
| H06 | 00:16.8-00:21.0 | phys A | MS->MCU | 50 mm, slider | push_in 0.4 m | the promise |
| P01 | 00:21.0-00:25.4 | blender A | MS | 50 mm | static | virus silhouette (hidden) |
| P02 | 00:25.4-00:29.8 | blender B | CU | 50 mm | static | receptors, no labels |
| P03 | 00:29.8-00:34.0 | phys C | INSERT | 50 mm 0.8 m | static | poster back, back-lit |
| T01 | 00:34.0-00:40.0 | edit | title over H01 plate | - | static, text hold | title; fade 0.5 s |
| C1-01 | 00:40.0-00:46.0 | phys A | WS | 24 mm 2.6 m f/5.6 | static, text hold | chapter card |
| C1-02 | 00:46.0-00:52.0 | stock | MS side | - | static | sneeze, back-lit droplets |
| C1-03 | 00:52.0-01:00.0 | blender A | EWS high | 35 mm | crane ORIENT | airway geography |
| C1-04 | 01:00.0-01:08.0 | blender A | MS | 50 mm | track FOLLOW, stop | virus docks; labels |
| C1-05 | 01:08.0-01:16.0 | phys B | MCU | 50 mm f/2.8 | static | presenter: hijack |
| C1-06 | 01:16.0-01:26.0 | blender A | CU cutaway | 50 mm | static, text hold | copying inside the cell |
| C1-07 | 01:26.0-01:36.0 | blender A | WS | 35 mm | pull_out REVEAL | scale of multiplication |
| C1-08 | 01:36.0-01:44.0 | phys A | MS | 50 mm | static | presenter |
| C1-09 | 01:44.0-01:50.0 | stock | MS high | - | static | consequence: ill in bed |
| C1-10 | 01:50.0-02:00.0 | phys B | MCU | 50 mm | static | "who fights back?"; fade |
| C2-01 | 02:00.0-02:06.0 | phys A | WS | 24 mm | static, text hold | chapter card |
| C2-02 | 02:06.0-02:16.0 | blender B | WS | 35 mm **locked** | static, text hold | innate: fast, general |
| C2-03 | 02:16.0-02:26.0 | phys A | MS | 50 mm | static | hands: innate vs adaptive |
| C2-04 | 02:26.0-02:36.0 | blender B | MS | 50 mm | arc 90° REVEAL | receptor fit |
| C2-05 | 02:36.0-02:44.0 | blender B | CU | 85 mm | static, text hold | antibodies bind |
| C2-06 | 02:44.0-02:54.0 | blender B | MS | 50 mm | track FOLLOW, stop | killer T cell |
| C2-07 | 02:54.0-03:04.0 | phys B | MCU | 50 mm | static | turn: it takes days |
| C2-08 | 03:04.0-03:14.0 | 2D | graph | - | static, text hold | plant graph, grey curve only |
| C2-09 | 03:14.0-03:24.0 | phys A | MS | 50 mm | static | picks up card |
| C2-10 | 03:24.0-03:30.0 | phys C | INSERT overhead | 90 mm f/8 | static | finger on first stamp; fade |
| C3-01 | 03:30.0-03:36.0 | phys A | WS | 24 mm | static, text hold | chapter card |
| C3-02 | 03:36.0-03:46.0 | stock | CU | - | static | vial + syringe |
| C3-03 | 03:46.0-03:58.0 | phys B | MS | 35 mm 1.6 m f/4 | static; poster turns 03:48.6 | poster reveal |
| C3-04 | 03:58.0-04:06.0 | phys C | INSERT | 50 mm 0.8 m f/8 | static, text hold | poster drawing; graphic match out |
| C3-05 | 04:06.0-04:16.0 | blender C | MS | 50 mm | static, text hold | harmless piece |
| C3-06 | 04:16.0-04:28.0 | blender C | MS->CU | 85 mm shallow | push_in APPROACH | the cell learns |
| C3-07 | 04:28.0-04:40.0 | phys B | MCU | 50 mm | static | presenter: no illness, a lesson |
| C3-08 | 04:40.0-04:50.0 | blender C | WS | 35 mm | pull_out WITHDRAW | memory cells rest |
| C3-09 | 04:50.0-05:00.0 | phys C | CU table level | 50 mm 0.6 m f/2 shallow | static + rack | poster -> stamp; fade |
| C4-01 | 05:00.0-05:06.0 | phys A | WS | 24 mm | static, text hold | chapter card |
| C4-02 | 05:06.0-05:12.0 | stock | WS | - | static | crowd, years later |
| C4-03 | 05:12.0-05:24.0 | blender B (re-render) | WS **= C2-02 frame** | 35 mm | static, text hold | memory cells answer at once |
| C4-04 | 05:24.0-05:40.0 | 2D | graph | - | zoom_in 140% between holds | faster and higher |
| C4-05 | 05:40.0-05:52.0 | phys B | MCU | 50 mm | static | presenter |
| C4-06 | 05:52.0-06:02.0 | phys A | MS | 50 mm | static | poster + card together |
| C4-07 | 06:02.0-06:12.0 | stock | WS | - | static | healthy teens playing |
| C4-08 | 06:12.0-06:20.0 | phys A | MCU | 50 mm 1.8 m | static | chapter end; fade |
| CL-01 | 06:20.0-06:28.0 | phys A | MS **= H02 frame** | 50 mm | static | callback, card open |
| CL-02 | 06:28.0-06:38.0 | phys C | INSERT table | 90 mm 0.5 m f/8 | truck 0.3 m REVEAL | each stamp in turn |
| CL-03 | 06:38.0-06:52.0 | phys B | MCU->MS | 50 mm f/2 shallow | pull_out WITHDRAW | final line |
| CL-04 | 06:52.0-07:00.0 | phys A | WS | 24 mm | static, text hold | end screen; fade |

**Budget count:** moving 11/51 = 22% (limit M02/M06 50%). Shallow DOF 4/51 = 8% (limit M06 20%). Effect transitions: 5 chapter fades to black (M02 allows these between chapters) + 1 graphic match. Dolly zooms: 0.
**Sequence patterns (no repeat in a row):** Hook = insert -> person -> close (object first). Ch1 = wide -> stock -> orient -> follow -> person (wide-to-close). Ch2 = wide -> process -> person -> reveal (alternating). Ch3 = wide -> stock -> subject-motion reveal -> insert -> graphic match -> push (static-moving-static). Ch4 = callback -> graph -> people (repeat-with-change). Close = callback of the opening (close-to-wide).

## 6. Timeline
`tests/results/T02_timeline.json` - schema v1, `adapter: physical_camera`, and each shot names its `target`. It also holds the 18 beats and 8 `music_hints`.

## 7. Validation
**cdcheck.py: NOT RUN.** I tried 3 times to run `python ../scripts/cdcheck.py timeline results/T02_timeline.json`. Each time the permission system asked for approval, and this run was not interactive. `node` and scripted PowerShell were blocked the same way. So I traced every rule of `check_timeline()` by hand:

| cdcheck rule | Result |
|---|---|
| first shot starts at 0 | H01 t0 = 0.0 - pass |
| edge to edge (tol 1/25 s) | all 50 joins checked: each t1 = the next t0 - pass |
| last t1 = duration | CL-04 t1 = 420.0 = duration - pass |
| id/t0/t1/type, t1 > t0 | all 51 - pass |
| move names | static, push_in, crane, track, pull_out, arc, zoom_in, truck - all in MOVES - pass |
| motivation + reason + times + ease on 11 moves | all present; no vague words - pass |
| move inside its shot | all 11 - pass |
| move vs hold_for_text | C1-04 track ends 64.5 < hold 65.0; C4-04 zoom 332.0-334.5 sits between holds [324.5,331.5] and [335.0,340.0] - pass |
| focus events (from/to/reason/t0) | H03 (2), C3-09 (1) - pass |
| line of action (studio, line y=0, side -1) | every studio camera_xy has y < 0 - pass |
| same subject + size + angle in a row | none (checked every pair) - no warning |
| budgets M02/M06 | moving 11/51, shallow 4/51 - no warning |
| beats inside 0-420 | 18/18 - pass |

Expected output: `timeline: 0 errors, 0 warnings`. **This is a hand trace, not a real run.** To confirm it, run this command from the skill folder:
```
python scripts/cdcheck.py timeline tests/results/T02_timeline.json
```

**Audit checklist**
- [x] Subject consistency: one presenter, one wardrobe; virus design shared by animation A, the poster drawing and animation C (continuity sheet in section 8).
- [x] Spatial: one studio line; all setups on the front side; each chapter opens on the WS to re-establish.
- [x] Screen direction / 30°: A <-> B is 31° and a size step; inserts sit between same-angle shots.
- [x] Movement: 11 moves, each motivated, each with a designed and held end frame; no move during text.
- [x] Focus: 3 racks, each tied to a word or an action; deep focus on every mechanism shot.
- [x] Light: one key direction (camera-left) all video; changes only at Ch1 (contrast) and Close (temperature), both on purpose.
- [x] Colour: amber is not used before 03:46.0; magenta only on the virus.
- [x] Props: card (folded in H01, open from C2-09), poster (face-down until 03:48.6).
- [x] Transitions: fades only at chapter ends; 1 graphic match; no whoosh SFX.
- [x] Relevance: every shot maps to a beat; no reveal before its time.
- [x] Adapter: each shot is written for its own target (section 8).
- [x] Intent unchanged: no narration added or rewritten.

**Accuracy flags (M06 rule 7) for the science reviewer:**
1. Not to scale: a real virus (~0.1 µm) is far smaller than a cell (~10 µm). Make the virus 5x larger and show "not to scale" once, in C1-03.
2. The graph has no numbers on the y axis unless a sourced value is supplied. The shape must show a shorter delay and a higher peak for the second response.
3. The harmless piece must not have a genetic core inside it, so the picture does not teach that a vaccine is a weak virus. If the script names inactivated or mRNA vaccines, adapt animation C.

## 8. Production instructions

### 8a. Real camera - crew shot list, in shooting order (by setup)
Camera: UHD 25p, shutter 1/50, base ISO, log or flat profile, fixed white balance 4300 K (3800 K for the Close block). Presenter mark: tape "P" 1.8 m in front of the wall. Presenter looks into the lens on every setup.

| Setup | Shots | Size / angle / height | Lens at distance | Stop / ND | Support | Move | Focus marks | Light | Notes |
|---|---|---|---|---|---|---|---|---|---|
| A-WS | C1-01, C2-01, C3-01, C4-01, CL-04 | WS, eye 1.55 m, front | 24 mm at 2.6 m | f/5.6 | tripod | none | 2.6 m | base | leave the lower-left third empty for the chapter card |
| A-MS | H02, H04, C1-08, C2-03, C2-09, C4-06, CL-01 | MS, eye 1.55 m, front | 50 mm at 2.2 m | f/4 | slider at 0 cm, on tripods | none | 2.2 m | base (C1-08: no fill) | H02 and CL-01 same frame: mark the tripod feet |
| A-push | H06 | MS -> MCU | 50 mm, 2.2 -> 1.8 m | f/4 | slider 0 -> 40 cm | push 40 cm in 2.8 s from "to recognise", ease in-out | 2.2 -> 1.8 m | base | hold 1.4 s at the end |
| A-MCU | C4-08 | MCU front | 50 mm at 1.8 m | f/4 | slider at 40 cm | none | 1.8 m | base | |
| B-MCU | C1-05, C1-10, C2-07, C3-07, C4-05 | MCU, eye 1.55 m, 31° camera-left | 50 mm at 1.3 m | f/2.8 | tripod | none | 1.3 m | base (C1-05, C1-10: no fill) | |
| B-card | H03 | MCU, card FG | 50 mm at 1.3 m | f/2.0 (ND 0.6 if needed) | tripod | none | eyes 1.3 m <-> card 0.6 m | base | racks at 00:05.4 and 00:08.3 (from VO); presenter touches the inner forearm on "in your blood" |
| B-MS | C3-03 | MS, 31° left | 35 mm at 1.6 m | f/4 | tripod | none | 1.6 m | base | poster face-down; turn it on "wanted" in 0.8 s |
| B-pull | CL-03 | MCU -> MS | 50 mm, 1.3 -> 1.7 m | f/2.0 | slider 0 -> 40 cm | pull 40 cm in 6 s after the last word | 1.3 -> 1.7 m | Close (3800 K) | card held next to the face |
| C-over | H01, C2-10 | INSERT overhead | 90 mm (macro) at 0.55 m | f/8 | boom arm (fallback: 60° easel) | none | card | soft top from LED1 | card fills 70% of the frame height |
| C-poster | P03, C3-04 | INSERT | 50 mm at 0.8 m | f/8 | tripod | none | poster | P03: LED2 behind the poster | C3-04: drawn spike at frame centre-right (graphic match) |
| C-table | C3-09 | CU table level | 50 mm at 0.6 m | f/2.0 | tripod low | none | poster 1.0 m -> stamp 0.6 m | base | rack 1.5 s |
| C-truck | CL-02 | INSERT table level | 90 mm at 0.5 m | f/8 | slider parallel to the card | truck 30 cm in 7 s, ease in-out | 0.5 m (constant) | LED2 raking, 3200 K, 10° across the card | end on the latest stamp |

**Lighting (2 LED panels + 1 foam board)**
- LED1 key: soft (softbox or diffusion), 4300 K, camera-left 45°, 0.4 m above eye height, 1.5 m from the face, tilted down 20°.
- Fill: white foam board, camera-right, 1 m from the face. Key:fill about 2:1 = high-key (convention). For Ch1 (C1-05, C1-08, C1-10), remove the board. This gives about 4:1, a threat beat (convention).
- LED2 back light: camera-right, behind the presenter, 2.2 m high, 4300 K, 1 stop under the key. It separates the presenter from the slate wall.
- Wall: slate blue, 1.8 m behind the presenter, 1 stop under the face.
- Close block (CL-01, CL-03): set the key to 3800 K. The grade adds warmth too.
- LED2 moves for P03 (behind the poster) and CL-02 (raking at table level). Shoot these at the end of the day.
- TECHNICAL: shoot each chapter's presenter lines in order inside each setup. Change the fill only between the Ch1 takes and the other takes.

### 8b. Blender - animator brief
Scene scale: 1 BU = 1 µm (the virus is enlarged 5x; see the accuracy flags). Render 25 fps, 3840x2160, camera sensor 36 mm. Bezier keys with ease in/out. Hold every end frame for the time in the table. Deep shots: `dof.use_dof = False`. Labels are added in the edit, so leave clean space for them during the text holds.

| Shot (anim) | Frames (shot-local, start 1) | Lens | Camera keys |
|---|---|---|---|
| P01 (A) | 1-110 | 50 | static; virus back-lit, rim only |
| P02 (B) | 1-110 | 50 | static; receptor CU, rim light |
| C1-03 (A) | 1-200 | 35 | crane: f1 z=+40 BU, tilt -60° -> f151 z=0, tilt -20°; hold to f200 |
| C1-04 (A) | 1-200 | 50 | track 8 BU parallel to the virus path f1 -> f113 (ease-out), stop; dock at f113; hold |
| C1-06 (A) | 1-250 | 50 | static cutaway; free space on the left for labels f51-f226 |
| C1-07 (A) | 1-250 | 35 | pull_out: distance d -> 6d, f1 -> f188; hold f188-f250 |
| C2-02 (B) | 1-250 | 35 | **static, save this camera as `CAM_BATTLEFIELD`** (reused in C4-03) |
| C2-04 (B) | 1-250 | 50 | camera parented to an empty at the B-cell centre, Track To the cell; empty Z-rotation 0° f26 -> 90° f176; hold |
| C2-05 (B) | 1-200 | 85 | static |
| C2-06 (B) | 1-250 | 50 | track beside the T cell, 10 BU, f1 -> f151; stop; hold |
| C3-05 (C) | 1-250 | 50 | static; spike at frame centre-right (graphic match from C3-04) |
| C3-06 (C) | 1-300 | 85 | push_in 14 -> 9.8 BU, f26 -> f163; DOF f/1.4 at 9.8 BU; amber from f163 |
| C3-08 (C) | 1-250 | 35 | pull_out d -> 4d, f14 -> f189; hold |
| C4-03 (B re-render) | 1-300 | 35 | `CAM_BATTLEFIELD` unchanged; amber memory cells already present and answer within the first 2 s |

Snippet for C3-06 (check `bpy.app.version`. In Blender 4.4+, fcurves can sit in action layers/slots):
```python
import bpy
scn = bpy.context.scene; scn.render.fps = 25; scn.frame_start = 1
cam = bpy.data.objects.get("CAM_C3_06") or bpy.data.objects.new("CAM_C3_06", bpy.data.cameras.new("CAM_C3_06"))
if cam.name not in scn.collection.objects: scn.collection.objects.link(cam)
c = cam.data; c.lens = 85.0; c.sensor_width = 36.0
c.dof.use_dof = True; c.dof.aperture_fstop = 1.4; c.dof.focus_distance = 9.8   # BU; test frames, scene scale not real
def f(t): return round(t * 25) + scn.frame_start          # t = seconds from shot start (04:16.0)
# push_in 04:17.0 -> 04:22.5 (APPROACH): 14 BU -> 9.8 BU on -Y towards the B cell at the origin
cam.location = (0.0, -14.0, 0.0); cam.rotation_euler = (1.5708, 0, 0); cam.keyframe_insert("location", frame=f(1.0))
cam.location = (0.0, -9.8, 0.0);  cam.keyframe_insert("location", frame=f(6.5))
for fc in (cam.animation_data.action.fcurves if cam.animation_data and cam.animation_data.action else []):
    for k in fc.keyframe_points: k.interpolation = 'BEZIER'; k.easing = 'AUTO'
scn.frame_end = f(12.0) - 1   # 300 frames
```

**Continuity sheet (animation + studio prop):** the virus is a sphere with 24 spikes, magenta `#D6336C`. The harmless piece is one spike shape, `#E9A3BD`, with no sphere and no core. B cells are pale blue `#8FB8DE` with Y-shaped receptors. Memory cells are amber `#F2B33D`. The poster drawing copies the virus design (line art, magenta ink, on amber-tinted paper) at the same spike count.

### 8c. 2D graph - Resolve Fusion
- One comp, 3840x2160. X axis "days after exposure". Y axis "antibody level", with no numbers (accuracy flag 2). Font and colours from the colour script.
- C2-08: the axes draw in 03:04.0-03:05.0. The grey curve draws 03:05.0-03:09.0. Hold to 03:14.0. The right side stays empty.
- C4-04: the same comp, with the grey curve already on screen. The amber curve draws 05:24.5-05:28.5 (shorter delay, higher peak). The labels appear at 05:28.5. Zoom (Transform Size 1.0 -> 1.4, centre on days 0-7) 05:32.0-05:34.5, ease in-out. This is a zoom, not a dolly. Hold to 05:40.0.

### 8d. Edit list (Resolve)
- Hard cuts are the default. Fade to black 0.5 s (12 frames) at the end of each section: 00:40.0, 02:00.0, 03:30.0, 05:00.0, 06:20.0 and 07:00.0. The fade at 06:20.0 separates Ch4 from the Close, so the callback frame CL-01 comes up out of black. Use no transition SFX.
- Graphic match C3-04 -> C3-05 at 04:06.0: the spike is at the same screen position.
- Narration over animation and stock: the presenter's studio voice continues as an L-cut. Example: C1-05 audio runs 0.5 s into C1-06.
- Text holds are in the timeline (`hold_for_text`). Chapter cards go in the lower-left third of the A-WS frame.
- Stock (licence check before use; search terms): "blood cells microscope" (H05), "sneeze backlit slow motion" (C1-02), "sick teenager bed" (C1-09), "vaccine vial syringe" (C3-02), "crowded school corridor" (C4-02), "teenagers football" (C4-07). Use static shots only. If a clip moves, trim to a still part.
- Grade: one node tree per group (studio, animation, stock). Match stock skin and white balance to the studio. Close group: +500 K warm.

## 9. Decisions explained
1. **Rack focus, not a push-in, for the stamp reveal (H03).** The hook moves meaning from paper to blood. A rack shows both the object and the person in one frame, and moves attention on the words. Rejected: push-in to the card. It moves the camera during dense lines, and the presenter leaves the frame.
2. **The one studio push-in sits on the promise (H06).** Every other presenter shot is static (M06: static while explaining). So the one push gives "an enemy they have never met" its weight. Rejected: a push on every chapter's key line. The push would mean nothing by Ch2.
3. **The thesis shot (C3-06) is a virtual dolly, not a zoom.** The camera enters the moment of learning, and the plasma parallax shows it. A zoom would only mean "look harder". This is also the only shallow-DOF animation shot, so the first amber cell is the sharpest thing on screen. Rejected: zoom-in. Also rejected: slow motion (no reason).
4. **Climax = the same frame with one change (C2-02 -> C4-03), not new energy.** The viewer saw the slow first fight in this exact frame. Now the amber cells meet the virus at once, so the difference is the lesson. Rejected: faster cutting or handheld energy. These break the identity, and they show "excitement", not "faster because of memory".
5. **The graph is planted early and completed later (C2-08 -> C4-04).** The empty half of the graph is a hide. The amber curve is the reveal. The zoom comes after both curves are read, never during them.
6. **The ending answers the opening (H02 -> CL-01, H01 -> CL-02).** It uses the same frames with the card open, warmer light and amber raking light. The stamps now read as lessons, not paperwork.

## 10. Hints for other departments
- **Music** (for Scorewright or another music skill; this report does not decide music): see `music_hints` in the timeline. Speech-free windows: 00:21.0-00:34.0 (preview) and 06:52.0-07:00.0 (end screen). Use beds only under explanation.
- **Sound:** add a soft stamp "thud" at H01 (the card) only if the presenter touches it. Use no whooshes.
- **Graphics:** chapter cards in the lower-left third of A-WS. Animation labels in the free space each animation shot leaves during its text hold. A "not to scale" tag once in C1-03.
