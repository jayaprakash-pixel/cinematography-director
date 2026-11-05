# Cinematography report - T04 "The Keeper's Lamp" (Blender, 16:9, 24 fps, 40 s)

## 1. Brief card
- **Intent (user's words):** "the keeper alone ... the girl enters, wet, holding a broken lantern ... REVEAL: ... the same engraved initials as on the lamp he was repairing - it was his lamp, given away long ago ... he smiles for the first time; the lighthouse beam passes over both faces." No dialogue.
- **Audience / platform / ratio / duration:** short animated film, 16:9 (1920x1080), 24 fps, 40.0 s = 960 frames (frame_start 1).
- **Mode(s):** M03 Animation (format/tool) + M05 Cinematic storytelling (genre: quiet drama with one reveal).
- **Target adapter:** `blender` only. No physical-camera instructions.
- **House rules:** none for this test (the JpAbhiNews Shorts rulebooks are for 9:16 explainer Shorts; they do not apply to a 16:9 drama scene).
- **Timing source:** ESTIMATED. The brief gives action windows only; I placed every event inside the brief's window. All times below are estimated; retime to the animation when the blocking is keyed.

### Assumptions (stated, not asked)
| # | Assumption | Why it matters |
|---|---|---|
| A1 | Scene scale is real metres (brief says so). Room is round, radius 3 m. Table top at z = 0.75, table diameter 0.9 m. | DOF values are computed at this scale. |
| A2 | Keeper sits at (0.80, 0) facing west (-X); seated eye height 1.15 m. | Line of action and eyelines. |
| A3 | Girl is about 11 years old, 1.45 m tall, standing eye height 1.35 m. Her stop mark is (-0.80, -0.20), west side of the table, facing east. | Line of action; camera heights express power (she stands, he sits). |
| A4 | Door is centred at (0, -3), 0.9 m wide. Window is centred at (0, +3), x from -0.6 to +0.6, sill z = 1.0, top z = 2.2. | Beam path into the room in S13. |
| A5 | The lamp he repairs sits at (0.35, 0, 0.75). Its initials face camera S03 (rotate the lamp so the engraving faces about 50 deg east of north). | Plant shot. |
| A6 | The lantern's initials are under soot. The engraving faces away from the keeper and the camera until 26.3 s. | Hide method for the reveal. |
| A7 | "The beam passes over both faces": physically the lighthouse lamp is above this room. I keep the user's intent and execute it with a spot light outside the window (motivated as the beam reflected off the storm cloud). Physical accuracy is not required for this story beat. | User intent wins over realism. |
| A8 | The room has no practical light of its own. I add a hidden warm light as a ceiling lantern. If the set has a practical, use it in place of LIGHT_PRAC. | Light continuity. |
| A9 | Character animation (door, walk, hands, smile) is keyed by the animator. This report gives the times; it does not key the characters. | Scope. |

## 2. Beat map (estimated)
| Beat | t | Anchor event | Kind | Content |
|---|---|---|---|---|
| B1 | 00:00.0 | beam pass 1.0-2.2 | hook | Storm on the window glass; the beam passes outside. |
| B2 | 00:03.0 | cut | context | The keeper alone at the table; the empty door behind him. |
| B3 | 00:06.0 | thumb on lamp | key_info | PLANT: engraved initials on the lamp. |
| B4 | 00:08.0 | door opens | turn | Door opens; he turns. |
| B5 | 00:11.0 | girl in doorway | development | Girl enters, wet, broken lantern. |
| B6 | 00:14.0 | she stops | development | They look at each other. |
| B7 | 00:17.0 | lantern lowered | development | She puts the lantern on the table. |
| B8 | 00:21.0 | stillness | turn | He hesitates, then takes it (23.0 reach, 24.0 lift). |
| B9 | 00:28.4 | soot cleared | reveal | The same initials on the lantern. |
| B10 | 00:29.4 | rack to lamp | climax | Link made: it was his lamp. |
| B11 | 00:34.8 | smile starts | resolution | His first smile. |
| B12 | 00:37.9 | beam on keeper (38.5 on girl) | resolution | The beam passes over both faces. |

## 3. Emotion timeline
| Beat | Dominant | Secondary | Intensity | Visual lever |
|---|---|---|---|---|
| B1 | mystery | sadness | 1 | Glass between us and the beam; cold palette. |
| B2 | sadness | anticipation | 1 | Small figure in a wide, deep frame; empty door in BG. |
| B3 | curiosity | sadness | 2 | Insert; shallow DOF isolates the engraving. |
| B4 | surprise | tension | 3 | Rack focus pulled by his look; cold light floods in. |
| B5 | mystery | tension | 3 | She walks from FS into MS toward the lens. |
| B6 | tension | curiosity | 3 | Static 2S; the table is the gap between them. |
| B7 | anticipation | tension | 3 | Low OTS on her (she has power); insert of the two objects side by side. |
| B8 | tension | anticipation | 4 | Static 5 s hold on his face from her height; stillness = hesitation. |
| B9-B10 | realisation | surprise / sadness | 5 (peak) | Match frame of the plant; rack between the two engravings. |
| B10->B11 | realisation | sadness | 5 | Push-in to BCU, the closest size of the film, then hold. |
| B11 | warmth | relief | 4 | Same frame as the hesitation; only the face changes. |
| B12 | warmth | resolution | 3 | Callback of the 2S; warm beam light joins both faces. |

The peak (5) sits on the reveal (B9-B10), as required.

## 4. Visual strategy

### Information ledger
| Beat | Viewer knows | Viewer must NOT know yet |
|---|---|---|
| B1-B2 | A storm; a lone keeper. | Anything about a past. |
| B3 | The lamp has initials; they matter to him (thumb). | Why. |
| B4-B7 | A girl brings a broken lantern. | That the lantern carries the same initials. |
| B8 | He is afraid of something in this object. | What. |
| B9-B10 | Same initials -> it was his lamp, given away. | - |
| B11-B12 | He accepts it; a link to the girl. | (Who she is stays open - not told by the brief; I do not invent it.) |

### See / hide list
| Hidden | Method | Reveal at | Reveal method |
|---|---|---|---|
| Lantern initials | Soot on the engraving + engraving faces away from keeper and camera (S05, S07, S08, S09) | 28.4 s | He turns it (26.3-27.0), thumb wipes soot (27.0-28.4) in CU |
| Link between the two objects | Never framed together with readable engravings before 28.4 | 29.4-30.2 s | Rack focus lantern -> lamp in one frame (S10) |
| The girl | Door shown empty in S02 | 10.0 s | Rack from keeper to doorway, silhouette first (S04) |
| His smile | No smile in any earlier shot | 34.8 s | Same frame as the hesitation (S09 = S12) |

### Primary / secondary subject per beat
B1 window / beam · B2 keeper / door · B3 initials / thumb · B4 keeper -> doorway · B5 girl / lantern · B6 both / table gap · B7 girl / lantern · B8 keeper / lantern · B9-B10 lantern initials -> lamp initials · B11 keeper eyes · B12 both faces / beam.

### Motif register
| Motif | First | Returns | Change |
|---|---|---|---|
| The beam | S01: outside, behind glass, cold | S13 | Comes inside and touches both faces (isolation -> connection). |
| Thumb across the engraving | S03 (lamp) | S10 (lantern) | Same gesture, same framing; the second time it reveals. |
| Framing S03 = S10 | S03 | S10 | Same camera position and lens: the audience compares the two frames. |
| Framing S09 = S12 | S09 hesitation | S12 smile | Only the face changes. |
| 2S from the window S06 = S13 | S06 cold, distance | S13 | Same frame, warm beam closes the gap. |

### Colour script
- **Base:** cold storm blue-grey (window and door light 7000-7500 K, low saturation).
- **Accent:** small warm practical (2700 K) over the table only - the keeper's shrinking world.
- **Motif colour:** brass amber of the engravings. Do not put amber on anything else.
- **Progression:** Act 1 (0-14 s) cold, warm pinpoint only; Act 2 (14-26 s) the open door adds more cold, contrast about 6:1 (convention); Reveal (26-34 s) amber engraving is the brightest warm value in frame; Resolution (34-40 s) the beam (warm white 5200 K-like, RGB 1.0/0.93/0.82) adds warmth to both faces; grade ends warmer than it starts, contrast about 4:1.

### Visual identity
- Lens family: 35 mm for relations (2S, walk), 85 mm for faces, 65 mm for the two engraving inserts, 28 mm once for the lone wide, 50 mm for the window and table inserts. Sensor 36 mm, horizontal fit.
- Camera behaviour: static by default (stillness = tension, M05). Two moves only: one FOLLOW pan, one APPROACH push on the realisation.
- Camera height carries power: keeper singles from the girl's standing eye (1.4 m, slight high); girl singles from his seated eye (1.2 m, slight low); the final 2S at a neutral 1.25 m.
- All cameras on the north (window) side of the keeper-girl line, so the beam in S13 front-lights the faces instead of backlighting them.

### Intended response
- Act 1: "He is alone and waiting for nothing."
- Act 2: "Something in that lantern frightens him."
- Act 3: "It was his - and now it has come back to him."

## 5. Shot list (blueprints, estimated times)

```
SHOT S01 - "Storm"                                   00:00.0 - 00:03.0 (3.0 s)  f1-72
WHY       hook: the storm and the beam, seen through glass (isolation) - mystery 1
CAMERA    INSERT, eye level, frontal to the window; CAM_S01 at (0.30, 2.35, 1.70) -> target (0.30, 3.00, 1.85); 50 mm
FRAME     rain streaks fill the glass; window mullion on the left third; storm dark outside
MOTION    static. Subject: BEAM_EXT sweeps left -> right behind the glass 1.0-2.2 s
FOCUS     0.65 m (glass), f/2.8, moderate: beam soft = far away
LOOK      cold 7500 K; the beam is the only bright value
LINKS     out: hard cut to S02
TECHNICAL vs CREATIVE: T = beam must be in frame at f37-53 (verify still; tilt BEAM_EXT down if not). C = open on the beam, not on the keeper (alt rejected: open on the WS - loses the motif plant).
```
```
SHOT S02 - "Alone"                                   00:03.0 - 00:06.0 (3.0 s)  f73-144
WHY       context: a lone man in a round room; the door is planted - sadness 1
CAMERA    WS, slight high, three-quarter front from north-west; CAM_S02 (-1.90, 1.90, 1.75) -> target (0.40, -0.60, 0.95); 28 mm at 3.36 m
FRAME     keeper left third, small; door right third in BG, empty; negative space between
MOTION    static (no reason to move; the emptiness is the information)
FOCUS     3.36 m, f/8, deep: keeper and door both sharp
LOOK      warm pool over the table, cold window fill; contrast ~6:1 (convention)
LINKS     in: hard cut. out: hard cut to S03
```
```
SHOT S03 - "The initials" (PLANT)                    00:06.0 - 00:08.0 (2.0 s)  f145-192
WHY       key_info: the audience sees initials on the lamp, meaning unknown - curiosity 2
CAMERA    INSERT, high, beside his right hand; CAM_S03 (0.85, 0.50, 1.05) -> target (0.35, 0.06, 0.82); 65 mm at 0.71 m
FRAME     engraving centred in the lower third; his thumb enters from frame right
MOTION    static. Subject: thumb rubs the engraving 6.3-7.6
FOCUS     0.71 m on the engraving, f/2.0, shallow
LOOK      the brass catches the warm practical: first amber accent
GUARD     the engraving must be readable for >= 1 s (2-3 letters)
```
```
SHOT S04 - "The door" (KEY BEAT 1)                   00:08.0 - 00:11.0 (3.0 s)  f193-264
WHY       turn: the door opens; we learn it when he does - surprise 3
CAMERA    MCU, seated eye level, three-quarter from north-west; CAM_S04 (0.45, 1.50, 1.18) -> target (0.25, -0.40, 1.10); 85 mm
FRAME     keeper left third (about 8 deg left of centre), doorway right of centre (about 9 deg)
MOTION    static. Subject: door opens 8.0-8.8; head turn 8.3-9.0; silhouette in doorway 10.0-11.0
FOCUS     rack 1.53 m (keeper eyes) -> 4.53 m (doorway), 9.0-10.0, inOutSine, f/2.8 - pulled by his look
LOOK      cold exterior light floods the doorway (area light 7500 K ramps 0 -> full, 8.0-8.8)
TECHNICAL vs CREATIVE: C = rack in one frame (alt rejected: cut to a door shot from inside the storm, tracking her in - shows the girl before his reaction and breaks the "learn with him" rule).
```
```
SHOT S05 - "The girl"                                00:11.0 - 00:14.0 (3.0 s)  f265-336
WHY       development: she crosses the room, wet, lantern in hand - mystery 3
CAMERA    FS -> MS by her walk; near the keeper's eyeline; CAM_S05 (0.30, 1.20, 1.15); 35 mm
FRAME     she stays centred; the lantern low, engraving turned against her leg
MOTION    pan right 34 deg, 11.6-13.4, inOutSine, FOLLOW (target empty moves from the door to her stop mark)
FOCUS     follow focus 4.15 m -> 1.78 m, 11.6-13.4, f/4
LOOK      wet highlights on her hair and coat from the cold doorway light behind her
```
```
SHOT S06 - "Two"                                     00:14.0 - 00:17.0 (3.0 s)  f337-408
WHY       development: they look at each other - tension 3; establishes the line of action
CAMERA    2S, eye level 1.30 m, from the window side; CAM_S06 (0.00, 2.30, 1.30) -> target (0.00, -0.10, 1.10); 35 mm at 2.4 m
FRAME     keeper screen left, girl screen right, table between them, open door BG centre
MOTION    static
FOCUS     2.4 m, f/5.6
```
```
SHOT S07 - "She knows"                               00:17.0 - 00:19.0 (2.0 s)  f409-456
WHY       development: she offers the lantern - anticipation 3
CAMERA    OTS keeper, slight low (1.20 m); CAM_S07 (1.40, 0.60, 1.20) -> target girl eyes (-0.80, -0.20, 1.35); 85 mm at 2.34 m
FRAME     keeper's right shoulder soft FG left; girl right of centre, looking screen left
MOTION    static. Subject: she lowers the lantern out of frame bottom 18.2-19.0
FOCUS     2.34 m, f/2.8, shallow
LINKS     out: cut on action (lantern going down) to S08
```
```
SHOT S08 - "Two objects"                             00:19.0 - 00:21.0 (2.0 s)  f457-504
WHY       development: the lamp and the lantern side by side; the pair is shown, the link is not
CAMERA    INSERT, high (about 50 deg down); CAM_S08 (0.00, 0.70, 1.55) -> target (0.05, -0.10, 0.78); 50 mm at 1.13 m
FRAME     lamp frame left, lantern frame right (camera looks south: east = left)
MOTION    static. Subject: lantern lands 19.0-19.4; hand withdraws 19.6-20.2
FOCUS     1.13 m, f/5.6, both sharp
GUARD     lantern engraving faces south-west: not visible
```
```
SHOT S09 - "Hesitation"                              00:21.0 - 00:26.0 (5.0 s)  f505-624
WHY       turn: he does not move, then he takes it - tension 4
CAMERA    OTS girl, slight high (1.40 m, her eye); CAM_S09 (-1.30, 0.45, 1.40) -> target keeper eyes (0.75, 0.00, 1.15); 85 mm at 2.11 m
FRAME     her left shoulder soft FG right; keeper left of centre, looking screen right
MOTION    static (stillness carries the hesitation). Subject: 21.0-23.0 no move; 23.0-24.0 reach; 24.0-25.5 lifts lantern to chest
FOCUS     2.11 m, f/4, moderate
```
```
SHOT S10 - "Same initials" (KEY BEAT 2, REVEAL)      00:26.0 - 00:31.0 (5.0 s)  f625-744
WHY       reveal + climax: same initials - realisation 5 (peak)
CAMERA    INSERT, match of S03: CAM_S10 at S03's position (0.85, 0.50, 1.05) -> target (0.45, 0.00, 0.90); 65 mm
FRAME     lantern base upper half of frame; lamp engraving lower third, behind and below
MOTION    static. Subject: turn 26.3-27.0; thumb wipes soot 27.0-28.4; initials readable hold 28.4-29.4
FOCUS     0.63 m on lantern engraving; rack to 0.71 m (lamp engraving) 29.4-30.2, inOutSine; hold 30.2-31.0; f/2.0 (DOF about 1.2 cm at 0.65 m: the two planes 8 cm apart separate clearly)
LOOK      amber on both engravings, the brightest warm values of the film so far
TECHNICAL vs CREATIVE: T = verify stills f683 (28.4 s), f721 (30.0 s), f739 (30.8 s): both engravings in frame. C = match frame + rack (alt rejected: dolly zoom on his face - too strong for a quiet recognition, and it hides the proof; alt rejected: cut between two inserts - splits the proof across a cut).
```
```
SHOT S11 - "It was mine"                             00:31.0 - 00:34.0 (3.0 s)  f745-816
WHY       realisation 5 -> held
CAMERA    CU -> BCU by push; seated eye level 1.18 m; CAM_S11 (-0.25, 0.75, 1.20) -> (0.05, 0.53, 1.18); target keeper eyes (0.75, 0.00, 1.15); 85 mm
FRAME     eyes on the upper third; lantern edge soft at frame bottom
MOTION    push_in 0.37 m, 31.2-33.6, inOutSine, APPROACH; hold 33.6-34.0
FOCUS     1.25 m -> 0.88 m with the push, f/2.8
```
```
SHOT S12 - "First smile"                             00:34.0 - 00:37.0 (3.0 s)  f817-888
WHY       resolution: the smile, in the hesitation frame - warmth 4
CAMERA    = S09 set-up (CAM_S12 duplicates CAM_S09), 85 mm, 2.11 m, f/4
MOTION    static. Subject: eyes up to her 34.2-34.6; smile 34.8-36.5
```
```
SHOT S13 - "The beam" (KEY BEAT 3)                   00:37.0 - 00:40.0 (3.0 s)  f889-960
WHY       resolution: the beam passes over both faces - warmth 3
CAMERA    = S06 set-up at 1.25 m (CAM_S13 (0.00, 2.30, 1.25)), 35 mm at 2.4 m, f/5.6
FRAME     same 2S as S06; the lantern now in his hands
MOTION    static; the light moves, not the camera. Beam on keeper 37.9, on girl 38.5, exits 38.9; warm afterglow hold to 40.0; cut to black
TECHNICAL vs CREATIVE: C = static callback (alt rejected: crane up to the ceiling as the beam passes - a large move on a small, private moment; it also takes us away from the faces at the moment the beam reaches them).
```
**Budget count:** moving 2/13 (15%, M05 max 40%) · shallow DOF 5/13 (38%, M05 max 50%) · effect transitions 0 (hard cuts, one cut on action, one cut to black).

## 6. Timeline
`tests/results/T04_timeline.json` (schema `templates/timeline.schema.json`, version 1, 13 shots, 12 beats, geography for scene `room`).

## 7. Validation
**cdcheck run: NOT executed.** The sandbox permission layer blocked `python ... cdcheck.py timeline ...` two times (the command needs your approval). Run it yourself:
```
python "~/.claude/skills/cinematography-director/scripts/cdcheck.py" timeline tests\results\T04_timeline.json
```
I checked the file against each rule in `cdcheck.py` by hand. The JSON parses (PowerShell `ConvertFrom-Json`: duration 40.0, fps 24, adapter blender).
| cdcheck rule | Result |
|---|---|
| first shot starts at 0; shots edge to edge; last t1 = duration | 0-3-6-8-11-14-17-19-21-26-31-34-37-40: pass |
| move names in the documented list | `static`, `pan`, `push_in`: pass |
| non-static moves have motivation, reason, t0/t1 inside the shot, ease | S05 pan FOLLOW 11.6-13.4 in 11-14; S11 push_in APPROACH 31.2-33.6 in 31-34: pass |
| no vague words in reasons | none of cinematic/epic/dynamic/cool/stunning/beautiful shot: pass |
| focus events have from/to/reason and t0 | all 13: pass |
| line of action (line (0.8,0)->(-0.8,0), camera_side -1) | all camera_xy have y > 0 -> side -1: pass |
| same subject + size + angle on consecutive shots | none (S09->S10, S11->S12 differ): no warning expected |
| M05 budgets | moving 15%, shallow 38%: pass |
| beats inside 0-40 | pass |
Expected result: **0 errors, 0 warnings** - to confirm by a real run.

### Final visual audit
- [x] Subject consistency: one keeper, one girl, one lamp, one lantern; positions fixed (A2-A6).
- [x] Spatial consistency: all 13 cameras on the north side; S06 establishes both before any single.
- [x] Screen direction: keeper always screen left / looks right; girl screen right / looks left (S04-S13). S01-S03 have one character only; keeper also screen-left in S02 and S04.
- [x] Movement: 2 moves, both motivated, both with designed end frames and a hold after.
- [x] Focus: racks pulled by his look (S04) and by the story link (S10).
- [x] Lighting continuity: practical over the table, cold window fill from north, door light from south after 8.0 s, beam only in S01 (outside) and S13 (inside).
- [x] Colour: amber only on the engravings and the final beam warmth.
- [x] Objects: lantern engraving hidden until 26.3 s in every shot.
- [x] Transitions: hard cuts; one cut on action (S07->S08); end cut to black.
- [x] Narrative relevance: every shot maps to a beat; nothing reveals early.
- [x] Restraint: budgets kept; no repeated sequence pattern (the two repeats S03=S10, S06=S13, S09=S12 are intended motifs).
- [x] Adapter: every instruction is in the Blender matrix (static, pan, push-in, rack focus, DOF).
- [x] User intent unchanged: all five action windows kept in order; no dialogue added; the girl's identity is not invented.

## 8. Production instructions (Blender)
**Scene settings (TECHNICAL):** 1920x1080, 24 fps, frame 1-960, frame(t) = round(t*24) + 1. Cycles or EEVEE; enable Motion Blur (shutter 0.5). One camera per shot, bound to timeline markers. Every camera aims with a Track To constraint at its own empty (`TGT_<shot>`); a pan = the empty moves while the camera stays; a push = the camera moves. Bezier keys with the default AUTO easing give the ease in-out; static shots carry no keys. Read `bpy.app.version` first; the script uses no fcurve access, so the 4.4+ layered-action change does not affect it.

**Before render:** render stills at the start, key moment and end frame of each shot (list below) and compare with the blueprint.

```python
import bpy
scn = bpy.context.scene
scn.render.fps = 24; scn.frame_start = 1; scn.frame_end = 960
scn.render.resolution_x, scn.render.resolution_y = 1920, 1080
scn.render.use_motion_blur = True
def f(t): return round(t * 24) + 1
def obj(name, data=None):
    o = bpy.data.objects.get(name) or bpy.data.objects.new(name, data)
    if o.name not in scn.collection.objects: scn.collection.objects.link(o)
    return o
def aim(o, target):
    c = o.constraints.get("Track To") or o.constraints.new('TRACK_TO')
    c.target = target; c.track_axis = 'TRACK_NEGATIVE_Z'; c.up_axis = 'UP_Y'

# id, t0, cam xyz, target xyz, lens mm, f-stop, focus keys [(t, m)], cam keys [(t, xyz)], target keys [(t, xyz)]
SHOTS = [
 ("S01", 0.0, (0.30, 2.35, 1.70), (0.30, 3.00, 1.85), 50, 2.8, [(0.0, 0.65)], [], []),
 ("S02", 3.0, (-1.90, 1.90, 1.75), (0.40, -0.60, 0.95), 28, 8.0, [(3.0, 3.36)], [], []),
 ("S03", 6.0, (0.85, 0.50, 1.05), (0.35, 0.06, 0.82), 65, 2.0, [(6.0, 0.71)], [], []),
 ("S04", 8.0, (0.45, 1.50, 1.18), (0.25, -0.40, 1.10), 85, 2.8, [(9.0, 1.53), (10.0, 4.53)], [], []),
 ("S05", 11.0, (0.30, 1.20, 1.15), (-0.03, -2.80, 1.20), 35, 4.0, [(11.6, 4.15), (13.4, 1.78)], [],
        [(11.6, (-0.03, -2.80, 1.20)), (13.4, (-0.80, -0.20, 1.10))]),
 ("S06", 14.0, (0.00, 2.30, 1.30), (0.00, -0.10, 1.10), 35, 5.6, [(14.0, 2.40)], [], []),
 ("S07", 17.0, (1.40, 0.60, 1.20), (-0.80, -0.20, 1.35), 85, 2.8, [(17.0, 2.34)], [], []),
 ("S08", 19.0, (0.00, 0.70, 1.55), (0.05, -0.10, 0.78), 50, 5.6, [(19.0, 1.13)], [], []),
 ("S09", 21.0, (-1.30, 0.45, 1.40), (0.75, 0.00, 1.15), 85, 4.0, [(21.0, 2.11)], [], []),
 ("S10", 26.0, (0.85, 0.50, 1.05), (0.45, 0.00, 0.90), 65, 2.0, [(29.4, 0.63), (30.2, 0.71)], [], []),
 ("S11", 31.0, (-0.25, 0.75, 1.20), (0.75, 0.00, 1.15), 85, 2.8, [(31.2, 1.25), (33.6, 0.88)],
        [(31.2, (-0.25, 0.75, 1.20)), (33.6, (0.05, 0.53, 1.18))], []),
 ("S12", 34.0, (-1.30, 0.45, 1.40), (0.75, 0.00, 1.15), 85, 4.0, [(34.0, 2.11)], [], []),
 ("S13", 37.0, (0.00, 2.30, 1.25), (0.00, -0.10, 1.10), 35, 5.6, [(37.0, 2.40)], [], []),
]
for sid, t0, loc, tgt, lens, fs, focus, ckeys, tkeys in SHOTS:
    cam = obj("CAM_" + sid, bpy.data.cameras.get("CAM_" + sid) or bpy.data.cameras.new("CAM_" + sid))
    tg = obj("TGT_" + sid)
    cam.location, tg.location = loc, tgt
    aim(cam, tg)
    c = cam.data
    c.lens = lens; c.sensor_fit = 'HORIZONTAL'; c.sensor_width = 36.0
    c.dof.use_dof = True; c.dof.aperture_fstop = fs; c.dof.aperture_blades = 7
    c.dof.focus_distance = focus[0][1]
    if len(focus) > 1:
        for t, d in focus:
            c.dof.focus_distance = d; c.dof.keyframe_insert("focus_distance", frame=f(t))
    for t, xyz in ckeys:
        cam.location = xyz; cam.keyframe_insert("location", frame=f(t))
    for t, xyz in tkeys:
        tg.location = xyz; tg.keyframe_insert("location", frame=f(t))
    m = scn.timeline_markers.get(sid) or scn.timeline_markers.new(sid, frame=f(t0))
    m.frame = f(t0); m.camera = cam

# BEAM inside the room (S13 only): spot outside the window, aimed by an empty that sweeps east -> west.
# Window x -0.6..0.6 at y=3 lets the beam in while the target x is within -2.1..2.1:
# keeper (x 0.8) lit at ~37.9 s, girl (x -0.8) at ~38.5 s, beam leaves at ~38.9 s.
beam = obj("BEAM", bpy.data.lights.get("BEAM") or bpy.data.lights.new("BEAM", 'SPOT'))
beam.location = (0.0, 4.2, 1.6)
beam.data.spot_size = 0.105; beam.data.spot_blend = 0.3          # 6 deg cone
beam.data.color = (1.0, 0.93, 0.82); beam.data.energy = 2000
bt = obj("BEAM_TGT"); aim(beam, bt)
for t, x in ((37.4, 2.5), (39.0, -2.5)):
    bt.location = (x, 0.0, 1.25); bt.keyframe_insert("location", frame=f(t))
for t, e in ((0.0, 0), (36.9, 0), (37.0, 2000)):                 # off before S13
    beam.data.energy = e; beam.data.keyframe_insert("energy", frame=f(t))
```
Set the BEAM_TGT keys to LINEAR (a lighthouse turns at constant speed): Graph Editor > select BEAM_TGT keys > T > Linear. Same for BEAM_EXT.

**Lights (TECHNICAL; values are starting points, check stills):**
| Light | Type / place | Value | Shots |
|---|---|---|---|
| LIGHT_PRAC | point, (0.20, 0.30, 1.90), hidden ceiling lantern (A8) | 2700 K-like (1.0, 0.72, 0.42), 60 W, radius 0.05 | all interior |
| LIGHT_WIN | area 1.2 x 1.2 at the window (0, 2.95, 1.6), aimed south | 7500 K-like (0.75, 0.85, 1.0), 40 W | all interior |
| LIGHT_DOOR | area 0.9 x 2.0 in the doorway (0, -3.05, 1.0), aimed north | (0.72, 0.82, 1.0), key energy 0 at 8.0 s -> 150 W at 8.8 s | S04-S13 |
| BEAM_EXT | spot at (0, 0, 9), rotation X = 80 deg, rotate Z -40 -> +40 deg linear 1.0-2.2 s; World Volume Scatter density about 0.02 outside | (1.0, 0.93, 0.82), 50000 W | S01 |
| BEAM | see script | | S13 |
No lightning: a flash would compete with the beam motif.

**Rain and the glass (S01):** rain-streak normal map on the window glass; a rain particle system outside. The wet girl: wet shader (higher specular, lower roughness) on hair and coat from S05 on.

**Stills to check before rendering (frames):**
S01 1/37/72 · S02 73/108/144 · S03 145/160/192 · S04 193/217/241/264 · S05 265/280/323/336 · S06 337/408 · S07 409/437/456 · S08 457/467/504 · S09 505/553/601/624 · S10 625/683/721/739 · S11 745/752/809/816 · S12 817/835/876 · S13 889/911/925/960.
Check per still: composition matches the blueprint, the focus subject is sharp, camera is on the north side, no engraving on the lantern visible before f632 (26.3 s).

**Fallback (stated for completeness):** if the S10 rack does not separate the two engravings (planes too close after animation), increase the keeper's lift so the lantern base is 15 cm above the lamp, or open to f/1.4. Do not cut to a second insert unless both fail.

## 9. Decisions explained
1. **All cameras on the window side (north).** Why: the brief's last beat is light on the faces. Looking north would backlight the faces with the beam and the window. Looking south puts the door - where the past walks in - in the background of the reaction shots. Rejected: south-side coverage with the storm window behind them - it gives a nicer storm background but turns the final beam into a silhouette.
2. **Plant before the reveal (S03) and a match frame (S10).** Why: "the same initials" only works if the viewer has seen the first set. Same camera, same lens, same thumb gesture: the audience compares two frames, not two descriptions. Rejected: no plant, reveal both engravings at 26 s - the audience would read a second object, not a recognition.
3. **The reveal is a rack focus inside one frame, not a camera move.** Why: proof and link in one image; the camera stays still because the discovery is in his hands, not in space. Rejected: dolly zoom - too strong for a quiet recognition (and M05 allows one per film; this film needs none).
4. **The door: rack pulled by his look (S04).** Why: we learn about the visitor at the same time he does; the silhouette keeps her a mystery for one more second. Rejected: exterior tracking shot through the door with the girl - gives away information before his reaction.
5. **Stillness as hesitation (S09, 5 s static) and the same frame for the smile (S12).** Why: the only change in the frame is his face, so the smile carries the whole turn. Rejected: slow push-in through the hesitation - it would spend the push that the realisation needs.
6. **The beam moves, the camera does not (S13).** Why: the light that went past the window in S01 now comes in and touches both of them. Rejected: crane up to the ceiling - a large move on a small, private moment.

## 10. Hints for other departments
- **Music (for a music skill such as Scorewright; this skill does not decide music):** beats and `music_hints` in the timeline. Peak at 28.4-30.2 s; near silence 21.0-23.0 s; warmth from 34.8 s; resolve by 40.0 s.
- **Sound:** storm bed through glass 0-8 s; door opening at 8.0 s lets the storm in (wind, rain, louder); door stays open, so keep the storm louder after 8.0 s, or key the door closing - the brief does not say; I assume it stays open. Soot wipe 27.0-28.4 s is a close, quiet sound (it marks the reveal). No whoosh on cuts.
- **Graphics:** none. No titles over S10 (the engraving must read clean).
