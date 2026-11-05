# Cinematography report - Tears of Steel excerpt, 2.39:1 -> 9:16 Short

## 0. Director's summary
- **Visual identity:** the camera is locked to the film's own camera. Every crop is 450x800 at scale 1.0. Only one crop move (S1) follows the subject. Captions sit on bodies, sky or hair, never on a face. Hard cuts only.
- **Key decisions**
  - **S1 - hide the robot, then let it in at the edge.** The 450 px crop can never hold Thom and the whole robot. The crop holds on Thom while the caption "He hasn't noticed yet." is on screen. From 5.0 s it follows his drift (cx 820 -> 720), so the robot comes in at the right edge. The robot's face stays hidden until S2.
  - **S2 - the robot face is the cut.** The S1 crop showed only an edge of the robot. The cut to S2 gives the full face as new information.
  - **S3 - the only frame that holds man and machine together:** cx 825. Thom fills the left 45%. The robot fills the right 45%, where he looks.
  - **S5 - the hologram is 780 px wide and cannot fit the 450 px crop.** The crop frames the houses and the text centre, and the rack focus in the source reveals the text. Our caption gives the full line, "We have to follow our passions", below the hologram.
  - **Punch-in:** none. Every shot is at scale 1.0. Headroom is 0 px (800 px source height = output height), so any scale above 1.0 upscales.
- **Budgets:** moving 1/7 (14%). Shallow DOF 3/7 (43%, baked into the source). Effect transitions 0.
- **cdcheck:** NOT RUN. The shell blocked the command and it needs your approval. A hand check against the rules in cdcheck.py found 0 errors and 1 expected warning (the shallow-DOF budget for M01). Run: `python "%USERPROFILE%\.claude\skills\cinematography-director\scripts\cdcheck.py" timeline timeline.json`.
- **Open checks for the user:**
  1. The captions for S4, S6 and S7 are our reading of the faces. They are not dialogue from the film.
  2. The crop positions come from 1/3-scale frame strips, so they are accurate to about ±15 px. Check S1 at 288.0-288.5 s, where the back of Thom's head comes near the left edge.
  3. Credit "Tears of Steel (CC) Blender Foundation | mango.blender.org, CC BY 3.0" on screen or in the description.

## 1. Brief card
- **Intent:** a 9:16 vertical version of this excerpt for a Short.
- **Platform:** Shorts, 1080x1920 from a 450x800 crop. Duration 25.6 s.
- **Modes:** M01 for the vertical format, M05 for the story content.
- **Adapter:** edit_resolve.
- **Constraints:**
  - Existing footage only.
  - No original audio. The video is silent with our captions.
  - Headroom is 0.
  - Film order is kept.
- **House rule:** "never on a face" for captions, from the brief. SHORTS_PIPELINE.md has no safe-area value, so captions stay at or above y 0.82.
- **Timing:** measured. Source times come from the frame strips. Pixel positions come from the ruler (strip scale 1:3).

## 2. Beat map
| Beat | t (out) | Anchor | Kind | Content |
|---|---|---|---|---|
| 1 | 00:00.0 | S1 in (278.0) | hook | Thom walks; the caption plants a question |
| 2 | 00:05.5 | src ~283.5 | reveal | robot edge enters frame right |
| 3 | 00:10.5 | S2 cut | climax | robot face |
| 4 | 00:12.4 | S3 cut | turn | Thom + robot in one frame |
| 5 | 00:14.2 | S4 cut | section | time jump, Thom with Celia |
| 6 | 00:15.9 | S5 rack | key_info | "follow our passions" |
| 7 | 00:18.9 | S6 cut | development | Thom waits |
| 8 | 00:23.4 | S7 cut | resolution | Celia, unconvinced |

## 3. Emotion timeline
| Beat | Dominant | Secondary | 0-5 | Visual lever |
|---|---|---|---|---|
| 1 | calm | unease | 2 | hold, looking room into empty right side |
| 2 | dread | curiosity | 3 | robot mass at the frame edge |
| 3 | awe | threat | 4 | full face fills the vertical frame |
| 4 | tension | - | 4 | both in one frame, Thom faces it |
| 5 | quiet | guilt | 2 | clean frontal single |
| 6 | longing | - | 3 | source rack focus to words |
| 7 | vulnerability | - | 4 | BCU, longest hold (4.55 s) |
| 8 | coldness | hurt | 3 | answer CU, eyeline opposed |

## 4. Visual strategy
- **See / hide:**
  - The robot's face is hidden in S1 (only its edge is in the crop) and shown at the S2 cut.
  - Celia is hidden in S4, because her head starts at 1200 px, outside the crop. She is shown in S7. Her face comes last: the story ends on her reaction.
- **Information ledger:**
  - The audience knows that something is coming before Thom does (S1 caption).
  - The audience learns his line from S5 before it sees Celia's reaction.
- **Motif:** looking room. Thom always faces screen-right (S1, S3, S4, S6) and Celia faces screen-left (S7). The eyelines stay consistent, and this keeps the geography clear across the time jump.
- **Colour:** no grade change. The source grade is kept, because the brief limits the edit to crop, reframe and timing.

## 5. Shot list
Columns: id · out time · source in-out · size · crop cx (window) · move · caption (y) · TECHNICAL / CREATIVE

1. **S1** · 0.0-10.5 · 278.0-288.5 · MS profile · cx 820 (595-1045), held 0-5.0 s; inOut pan to 720 (495-945) over 5.0-9.5 s; held to the end · "He hasn't noticed yet." (y 0.62, on the jacket, shown 0-4.5 s)
   - TECHNICAL: the source camera already follows Thom; the crop only corrects his 100 px drift. The out point is 288.5, because after that the back of his head leaves the window.
   - CREATIVE: hold, then follow (FOLLOW). The caption goes off before the robot arrives, so the eye goes to it. Rejected: a REVEAL pan to the robot head at 286 s. It would show S2's information early and push Thom out of frame.
2. **S2** · 10.5-12.35 · 299.0-300.85 · CU robot · cx 1035 · static · "It is right behind him." (0.74, on its chassis)
3. **S3** · 12.35-14.15 · 300.9-302.7 · WS · cx 825 · static · "Face to face." (0.70, on the railing and legs)
   - Rejected: cx 960 centre. It cuts Thom at the shoulder and gives the frame to the robot alone.
4. **S4** · 14.15-15.9 · 310.6-312.35 · MCU frontal · cx 680 · static · "Later: the real conversation." (0.82, on the chest)
   - TECHNICAL: the over-the-shoulder cannot fit (Thom 465-900 px, Celia from 1200 px), so this becomes a single.
5. **S5** · 15.9-18.85 · 312.4-315.35 · WS houses · cx 1400 (1175-1625) · static; the source rack focus 312.4->313.3 does the reveal · "We have to follow our passions" (0.76)
   - TECHNICAL: the hologram is cut at both edges in any 450 px window. Our caption is the readable copy of the line.
   - Rejected: a reading pan across the text. That puts a moving camera under a caption, and the text would still be cut.
6. **S6** · 18.85-23.4 · 315.4-319.95 · BCU · cx 800 (575-1025) · static · "He waits for her answer." (0.10, on the hair)
   - TECHNICAL: the face is 690 px wide. The crop keeps the features (645-1020 px) and loses the left ear.
   - CREATIVE: no trim. This is the emotional peak, and the brief's total (25-30 s) needs the length.
7. **S7** · 23.4-25.6 · 320.0-322.2 · CU · cx 1160 (935-1385) · static · "She isn't convinced." (0.82, on the collar)
   - Rejected: cx 1200 centred. It removes her looking room to the left.

**Budget:** moving 1/7, shallow 3/7 (source), effect transitions 0.

## 6. Timeline
See `timeline.json` (schema v1, adapter edit_resolve, output seconds). The executable crop keys in source seconds are in `edit_plan.json`.

## 7. Validation
- **cdcheck:** NOT RUN. The tool call needed your approval and was not approved in this session. Hand check against the rules in `cdcheck.py`:
  - Shots run edge to edge from 0 to 25.6 s, and the last shot ends at the duration. OK.
  - S1 pan: the move name is valid for edit_resolve, the motivation is FOLLOW, and the reason contains no vague word. The pan runs 5.0-9.5 s, after `hold_for_text` [0, 4.5]. OK.
  - S5 focus has `fallback`, which edit_resolve requires. OK.
  - Expected warning: `M01: 3/7 shallow-DOF shots exceeds budget 30%`. Reason: the shallow DOF is baked into the source footage and the edit cannot change it. M05 allows 50%.
- **Checklist:**
  - Every move passes the motivation gate. OK.
  - No captions on faces. OK.
  - Scale 1.0 everywhere. OK.
  - Film order kept. OK.
  - The total of 25.6 s is inside 25-30 s. OK.
  - Shot lengths: S1 (10.5 s) and S6 (4.55 s) are above the M01 default of 1.5-4 s. This is a deliberate choice: S1 is one continuous build-up to the reveal.

## 8. Production instructions (edit list)
1. Make a 1080x1920 timeline at 24 fps. Mute or remove all source audio.
2. For each shot, place source `src_in`-`src_out` from `edit_plan.json` in film order, edge to edge.
3. Crop a 450x800 window at centre `cx` and scale it to 1080x1920. This is the only scaling allowed: it is 2.4x output scaling, not a punch-in. There is no extra zoom.
4. S1 only: set a position key at source 283.0 (cx 820) and a position key at 287.5 (cx 720) with ease in-out. Hold before and after.
5. Set captions with the text and `caption_y` from `edit_plan.json`. Use one style, centred horizontally, max 2 lines.
   - S1: show the caption from 0 to 4.5 s only.
   - All other shots: show the caption for the full shot.
6. Add the CC BY 3.0 credit.
7. Export, then check frames at 9.5 s, 10.4 s and 16.5 s.

## 9. Decisions explained
- **Zero headroom means the crop is the only camera.** A punch-in would be a 1.1-1.2x upscale on top of the 2.4x output scaling, with visible softness. No punch-in is worth that quality loss here.
- **Follow only in S1:** it is the only shot where the subject moves through the window. Every other subject stays inside a fixed window.
- **Hide the robot's face until S2:** the vertical crop cannot show the wide reveal, so the reveal moves to the cut.
- **S5 text:** the hologram is the content of the shot. The crop keeps its centre and the source rack focus, and our caption makes the line readable.
- **Compared with the naive centre crop (cx 960):**
  - S1 loses Thom's head from about 286 s (the window is 735-1185 px; his head is at 555-705 px).
  - S4 shows his ear and empty background.
  - S6 shows only the right half of his face.
  - S7 shows a 225 px band of her face against the left frame edge.

## 10. Hints for other departments
- **Music:** none by licence. If a score is added later, read `music_hints` in timeline.json. The biggest hit point is 10.5 s, and the time jump at 14.15 s goes quiet.
- **Graphics:** use one caption style. Keep the captions out of y 0.26-0.56 in S5, where the hologram is.
