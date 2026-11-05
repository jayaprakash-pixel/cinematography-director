# Cinematography report - T01 retest: "The padlock is not the safety sign"

Timeline: `tests/results/T01_retest_timeline.json` (11 shots, 30.0 s, 30 fps, 1080x1920).

## 0. Director's summary
- **Visual identity:** flat 2D, front-on, no perspective. Camera = world-layer scale (a **zoom**, never called a dolly). Static by default, with 4 eased zooms, each one between reading windows. Palette: navy base. The padlock is always neutral white. **Yellow = the address** (the core idea). Red = the scam.
- **Key decisions:**
  - S01/S11 - the video opens on a padlock ECU with the address blurred. It ends on the same frame, but now we know that the lock belongs to the **fake** bar. Reason: the loop turns the hook into the lesson.
  - S03 - a zoom-out from the padlock to the line between YOU and the SITE. Reason: it defines the padlock as a property of the connection, before any word says it.
  - S05 - a zoom-in to the site while the password dots pass through the blue line untouched, and then a red hook takes them. Reason: this shows the correct model. Transit is safe, but the endpoint is the thief.
  - S09 - a zoom-out from the lock to the name, plus a simulated focus pull. Reason: the lesson ("look at the address, not the lock") becomes the camera move. The address is hidden from 0.0 s until this moment.
  - S06 - the padlock appears on all 12 phishing cards at once on "have the padlock too". Reason: one image proves "most" better than a number.
- **Budgets:** moving 4/11 = 36% (M01 max 40%). Shallow DOF 1/11 = 9% (M06 max 20%). Effect transitions 0 (hard cuts, 1 graphic match, 1 loop).
- **cdcheck:** I could not execute it in this session, because the shell permission layer blocked every `python` call. I traced each rule in `scripts/cdcheck.py` by hand: expected **0 errors, 0 warnings** (see section 7). Run it once to confirm: `python scripts/cdcheck.py timeline tests/results/T01_retest_timeline.json`.
- **Open checks for the user:** (1) the phishing-HTTPS share ("most") needs a current source; (2) "free and automatic" certificates; (3) the simplification "nobody in the middle can read it"; (4) the fictional domains `northbank.com` / `northbamk.com` must not belong to a real bank (do a WHOIS check). Section 1 lists the assumptions.

## 1. Brief card
- **Intent (user's words):** "why 'HTTPS' padlock does not mean a site is safe."
- **Audience / platform / ratio / duration:** general viewers 18-35 / YouTube Short / 9:16 1080x1920 / 30.0 s.
- **Modes:** M01 (Short) + M06 (tech explainer). **Target:** `motion_graphics_2d` (HTML/GSAP). `ai_video` is used for 1 of the 2 allowed inserts.
- **Constraints (TECHNICAL):** voice-over only, with no presenter. Inserts in AI video must not contain generated UI or text.
- **House rules:** `SHORTS_PIPELINE.md` (no swish/whoosh on transitions): kept, with no conflict. I did not apply the Hybrid rulebook, because the brief is a standalone test and names generic HTML/GSAP. The `cam()` helper in section 8 uses the same call signature, so it can be ported.
- **Timing source:** measured phrase-start times from the brief. I did not get word-level times inside a phrase. Times inside a phrase (for example "scam" at 13.0, "one letter off" at about 26.5) use the given phrase start, or they are estimated and marked "about".

**Assumptions (stated, not asked):**
1. Captions come from the edit stage. They are screen-fixed (outside the camera layer) in the band y 1440-1580. The camera-hold rule applies to text inside the world (labels, URLs). It does not apply to the caption HUD.
2. Safe area (convention, not a platform spec): key content inside the central 4:5 area, y 285-1635. There is no content at y > 1600 (platform UI) and no content in the right rail x > 960.
3. I use only 1 AI insert. The brief allows 2. The second insert has no beat that needs a human (see Decisions explained).
4. The domains are fictional: `northbank.com` (real) and `northbamk.com` (fake, with one letter changed: n -> m).
5. Fps is 30 (Shorts standard). Output is 1080x1920.

## 2. Beat map
| Beat | t | Anchor | Kind | Content |
|---|---|---|---|---|
| B1 | 00:00.0 | "That little padlock" | hook | the padlock everyone trusts |
| B2 | 00:02.6 | "It does NOT mean" | turn | padlock is not equal to a safe site |
| B3 | 00:05.2 | "It means one thing:" | key info | the padlock = the encrypted line |
| B4 | 00:09.6 | "Nobody in the middle" | development | the middle sees only noise |
| B5 | 00:11.8 | "But the site itself" | reveal | the destination is the scam |
| B6 | 00:14.6 | "In fact, most phishing sites" | key info | phishing sites have padlocks too |
| B7 | 00:18.6 | "because certificates" | development | certificates are free and automatic |
| B8 | 00:21.0 | "So check the address," | resolution | the instruction |
| B9 | 00:23.8 | "Real bank:" | development | the exact name |
| B10 | 00:26.0 | "Fake:" | climax | one letter off |
| B11 | 00:27.6 | "Lock and all." | resolution | identical locks; loop to 0.0 |

## 3. Emotion timeline
| Beat | Dominant | Secondary | Int. | Visual lever |
|---|---|---|---|---|
| B1 | curiosity | recognition | 2 | the closest framing (ECU), address hidden by blur |
| B2 | surprise | doubt | 4 | hard cut, "≠ SAFE SITE" stated as a graphic |
| B3 | discovery | calm | 2 | zoom-out reveal, then a static diagram that builds |
| B4 | confidence | relief | 2 | static CU, cool steel blue |
| B5 | realisation | tension | 4 | zoom-in (look harder), red enters, vignette 25% |
| B6 | tension | surprise | 3 | quantity: 12 cards, padlocks appear together |
| B7 | realisation | unease | 3 | static CU, "$0" |
| B8 | confidence | anticipation | 3 | human insert, steadier, yellow appears |
| B9 | anticipation | discovery | 4 | reveal move + focus pull, the background brightens |
| B10 | **surprise (peak)** | realisation | 5 | cut to a CU on the wrong letter, red circle |
| B11 | realisation | resolution | 4 | wide on both, then a fast zoom to the opening frame |

The peak (B10) is on the climax reveal. B5 is the secondary peak, on the first reveal.

## 4. Visual strategy
**Information ledger**
| Beat | Viewer knows | Must not know yet |
|---|---|---|
| B1-B2 | padlock exists; it does not mean safe | what it does mean; the address |
| B3-B4 | padlock = encrypted line; the middle sees noise | that the endpoint can be bad |
| B5-B7 | the endpoint can be the thief; scam sites have locks | what to check instead |
| B8 | check the address | what a fake address looks like |
| B9-B10 | real vs fake differ by one letter | that the opening lock was the fake's |
| B11 | the opening lock was the fake's (loop) | - |

**See / hide list**
| Hidden | Method | Reveal at | Reveal method |
|---|---|---|---|
| The address text | simulated focus (18 px blur) in S01 and S08; absent in S02-S07 | 00:23.8-00:24.5 | zoom-out + focus pull (S09) |
| The site is a scam | distance (the site is a small grey card in the S03 wide) | 00:13.0 | zoom-in + red hook (S05) |
| Padlocks on phishing cards | time (cards appear without locks) | 00:17.0 | all 12 appear at once (S06) |
| The fake bar | time (opacity 0 in S09) | 00:26.0 | hard cut (S10) |
| The owner of the S01 padlock | framing (ECU, URL soft) | 00:29.7 (and on loop) | zoom-in lands on the S01 frame (S11) |

**Primary / secondary subject:** S01 padlock / blurred bar · S02 "≠ SAFE SITE" / padlock · S03 line+padlock / YOU, SITE · S04 scrambled readout / middle node · S05 site + hook / password dots · S06 the 12 padlocks / cards · S07 "$0 · automatic" / token · S08 thumb on bar / dimmed lock · S09 "northbank.com" / REAL tag · S10 the red-circled "m" / FAKE tag · S11 the two identical locks -> the fake lock.

**Motif register**
| Motif | First | Returns | Change |
|---|---|---|---|
| Padlock (same SVG, white, never the accent colour) | S01 | S02, S03, S06, S08, S09, S10, S11 | from "the thing you trust" to "on everything" to "on the fake" |
| Yellow underline = the address | S08 21.6 | S09 24.5 | from blurred to readable |
| Red hook = the scam | S05 13.0 | S06 (card icons), S10 (red circle, FAKE tag) | from mechanism to the one letter |
| S01 frame | S01 | S09 start (the real lock looks the same), S11 end (loop) | the same pixels, now the owner is known |

**Colour script** (meaning is defined inside this video)
- Base: navy `#0E1320`, off-white `#F2F4F8`, steel blue `#5B7FA6` (= encryption, the line).
- Accent: yellow `#FFD23F` = the address (the core idea). It appears first at 21.6.
- Danger: red `#E5484D` = the scam / attacker. It appears first at 13.0.
- The padlock is always `#F2F4F8`. It never gets a colour, because in this video it is not the signal.
- Progression: B1-B4 neutral cool -> B5-B7 base with a 25% black radial vignette (threat) -> B8 warm practical footage -> B9-B11 base lifted to `#1A2335`, with no vignette (clarity).

**Lens / format identity:** a 2D orthographic view with no lens. Distance = world scale (1.0 = the full diagram; 4.0 = the closest framing, used only for the padlock). Eye level and front-on everywhere except the single insert (S08).

**Intended response:** Act 1 (0-11.8): "OK, the lock protects the line." Act 2 (11.8-21.0): "The line is safe, but the end of it can be the thief." Act 3 (21.0-30.0): "I look at the name now, and the lock at the start was the fake's."

## 5. Shot list
Coordinates: world px in a 1080x1920 world per scene. A camera frame is `(fx, fy, s)` = the world point at the screen centre, at scale s. Visible width = 1080/s.
Scenes: **card** (S02), **diagram** (site card 360x300 at (540,500); phone icon at (540,1300); line (540,1230)->(540,590); padlock 120 px at (540,910); middle node at (800,910)), **grid**, **cert**, **bar** (real bar x 120-960 at y 760; fake bar at y 1160; padlocks at x 190; URL text from x 240, 44 px font).

```
SHOT S01 - "That little padlock"                      00:00.0 - 00:02.6 (2.6 s)
WHY       hook: the most familiar trust symbol, isolated; curiosity 2
CAMERA    ECU, front-on; frame (190,1160, 4.0) = the FAKE bar's padlock (the viewer does not know)
FRAME     padlock centred, ~190 px on screen; URL to the right at 18 px blur; bar edges as a frame
MOTION    static. Padlock fades in 0.0-0.3 (power2.out); glow 0->40%->0 1.4-2.0 on "in your browser?"
FOCUS     simulated shallow: padlock sharp, URL blurred - the hide of the whole video
LINKS     out: hard cut on "It" 2.6.   This frame = the S11 end frame (loop)
GUARD     the URL must not be readable at phone size (test on a phone at 100%)
```
```
SHOT S02 - "It does NOT mean the website is safe"     00:02.6 - 00:05.2 (2.6 s)
WHY       turn: the false belief stated and crossed out; surprise 4
CAMERA    CU, static, identity frame
FRAME     padlock 240 px at (540,960); "≠" at (540,1150) on "NOT" (2.6-2.9); "SAFE SITE" at (540,1260) on 3.9
MOTION    static - text window 3.9-5.2
LINKS     out: graphic match cut on 5.2 - the padlock keeps its screen position and size into S03
TECH/CREA C: alt rejected - a red X stamp over the lock: it says "the lock is bad", which is a wrong model
```
```
SHOT S03 - "the line between you and the site is encrypted"  00:05.2 - 00:09.6 (4.4 s)
WHY       key info: defines what the padlock means; discovery 2
CAMERA    CU -> WS. ZOOM OUT (2D scale, no parallax) (540,910,2.0) -> (540,960,1.0), 5.2-6.6, power2.inOut
          motivation REVEAL: the padlock floats between YOU and the SITE
FRAME     end: site (540,500) top, phone (540,1300) bottom - vertical stack inside the 4:5 safe area
MOTION    line draws through the padlock 6.6-7.2 on "the line"; turns steel blue + "ENCRYPTED" at (680,910) 8.4-8.8
GUARD     camera holds 6.6-9.6 (text 8.4-9.6). The site card stays small, grey and generic (distance hide)
```
```
SHOT S04 - "Nobody in the middle can read it."        00:09.6 - 00:11.8 (2.2 s)
WHY       development: the protection, shown from the outsider's seat; confidence 2
CAMERA    CU, hard cut (one size step from the S03 wide), frame (760,960,2.2), static
FRAME     grey middle node (labelled "Wi-Fi / network", not a hooded figure) upper half; readout panel below
MOTION    readout fills with scrambled glyphs 9.8-10.2; hold 10.2-11.8
GUARD     the readout shows the scrambled message body only - no claim that everything about the visit is hidden
```
```
SHOT S05 - "But the site itself can still be a scam." 00:11.8 - 00:14.6 (2.8 s)   KEY BEAT
WHY       reveal: the threat is the destination; realisation 4
CAMERA    WS -> MCU. Hard cut to the S03 end frame, ZOOM IN (540,960,1.0) -> (540,540,1.7), 11.8-12.9, power2.inOut
          motivation APPROACH (the act of looking at the destination) - a zoom, because nothing enters the space
FRAME     end: the site card 612x510 on screen, the blue line entering from the bottom edge
MOTION    password dots travel up the line untouched 12.6-13.0; on "scam" 13.0 the red hook lifts them,
          site outline goes red, vignette 25% (13.0-13.4); hold 13.4-14.6
TECH/CREA C: alt rejected - cut to a "SCAM" stamp card: it tells the conclusion and hides the mechanism.
          Here the safe blue line stays in frame while the end goes red - both facts in one picture
```
```
SHOT S06 - "most phishing sites today have the padlock too"  00:14.6 - 00:18.6 (4.0 s)
WHY       key info: scale of the problem; tension 3
CAMERA    WS, hard cut, identity, static (the previous shot moved; stillness lets 12 cards read)
FRAME     3x4 cards 260x180, x 150-930, y 420-1500; centre card = the S05 site (red hook icon, continuity)
MOTION    cards pop in 14.6-15.8 (stagger 0.1 s from centre); on "have the padlock too" 17.0 the white
          padlock appears on all 12 at once (17.0-17.3)
GUARD     no on-screen percentage (the figure is not verified - section 0)
```
```
SHOT S07 - "because certificates are free and automatic."  00:18.6 - 00:21.0 (2.4 s)
WHY       development: why the padlock is everywhere; unease 3
CAMERA    CU, hard cut, identity, static
FRAME     dispenser (540,700) issues tokens 18.6-19.4; one token at (540,860); "$0 · automatic" at (540,1180) 19.4
GUARD     text hold 19.4-21.0
```
```
SHOT S08 - "So check the address, not the lock."      00:21.0 - 00:23.8 (2.8 s)   AI VIDEO INSERT
WHY       resolution: ground the instruction in a real hand on a real phone; confidence 3
CAMERA    INSERT CU over the right shoulder, 20° down onto the phone, ~0.6 m, 50 mm FF-equivalent feel; static
FRAME     phone portrait in the upper-centre third; thumb enters from the bottom right
MOTION    generated: thumb rises to the top bar 21.0-21.6. Comp: bar UI corner-pinned onto the screen;
          yellow underline under the (still blurred) address 21.6-22.0; padlock dims 100->40% on "not the lock" 22.6-22.9
FOCUS     moderate DOF (phone sharp, room readable as a room) - not budgeted as shallow
LOOK      warm lamp from the left, cool screen light on the thumb - the only warm, human light in the video
LINKS     in: hard cut on "So" 21.0; out: hard cut on "Real" 23.8
```
```
SHOT S09 - "Real bank: one exact name."               00:23.8 - 00:26.0 (2.2 s)   KEY BEAT
WHY       reveal of the address hidden since 0.0; anticipation 4
CAMERA    ECU -> MS. ZOOM OUT (190,760,4.0) -> (540,760,1.25), 23.8-24.5, power2.inOut, motivation REVEAL
          start frame looks the same as S01 (the real lock is identical to the fake lock - on purpose)
FOCUS     simulated pull padlock -> address 23.8-24.5 (blur 18 -> 0 px), power2.inOut
FRAME     end: the real bar fills x 108-972; "northbank.com" underlined in yellow + tag "REAL" 24.5-24.8.
          The fake bar exists in the world at y 1160 but is at opacity 0 (time hide)
GUARD     hold 24.5-26.0
TECH/CREA C: alt rejected - both bars on screen at 23.8: it gives the answer before "Fake" and spends the climax
```
```
SHOT S10 - "Fake: one letter off."                    00:26.0 - 00:27.6 (1.6 s)   PEAK
WHY       climax: the difference is one letter; surprise 5
CAMERA    CU, hard cut, frame (420,1160,1.8), static (text read, the camera must not compete)
FRAME     fake bar "northbamk.com", padlock at screen x≈126 (inside the margin); red tag "FAKE";
          red circle around the "m" at about 26.5-26.8 (on "one letter off" - estimated inside the phrase)
GUARD     hold 26.0-27.6; the circle is the only red element
```
```
SHOT S11 - "Lock and all." -> loop                    00:27.6 - 00:30.0 (2.4 s)   KEY BEAT
WHY       resolution and the loop reveal: the opening padlock was the fake's
CAMERA    MS (identity: both bars, REAL / FAKE tags), hold 27.6-28.9;
          ZOOM IN (540,960,1.0) -> (190,1160,4.0), 28.9-29.7, power3.inOut, motivation APPROACH; end frame = S01, held 29.7-30.0
FOCUS     simulated: URL of both bars blurs back to 18 px 28.9-29.7 (padlock stays sharp) - the S01 look
MOTION    both padlocks pulse together 27.6-28.0 (scale 1.0->1.15->1.0)
TECH/CREA T: a 0.8 s 4x zoom is fast (the "sudden noticing" speed band); the 0.3 s hold + the 2.6 s static S01
          on loop give the designed end frame its read time.
          C: alt rejected - fade to black + "Check the address" card: no loop, it repeats the narration as text
```
**Budget count:** moving 4/11 (S03, S05, S09, S11) = 36%. Shallow 1/11 (S01) = 9%. Effect transitions 0. Sequence patterns: Act 1 close -> wide -> close; Act 2 wide -> close -> wide -> close; Act 3 insert -> close -> wide. No size-angle-length pattern repeats 3 times.

## 6. Timeline
See `tests/results/T01_retest_timeline.json`. Extra fields used: `frame_cam` (the static frame) and `subject_motion` (graphic events). `secondary_adapter` marks S08 as AI video. The timeline holds 11 beats and 6 `music_hints`.

## 7. Validation
**cdcheck:** not executed. In this session the shell permission layer refused every `python ...` call (it asked for an approval that I could not get). I traced each rule of `check_timeline()` by hand:
| Rule | Result |
|---|---|
| first shot at 0; edge to edge; last t1 = 30.0 | pass (2.6, 5.2, 9.6, 11.8, 14.6, 18.6, 21.0, 23.8, 26.0, 27.6, 30.0) |
| moves in MOVES; motivation in the set; reason; t0/t1 inside the shot; ease | pass (static, zoom_out, zoom_in only) |
| no move inside `hold_for_text` (tolerance 1/30 s) | pass - S03 5.2-6.6 vs [8.4,9.6]; S09 ends 24.5 = hold start; S11 starts 28.9 = hold end |
| 2D: push/dolly without parallax | not used - all scale moves are named zoom |
| vague words in reasons | none |
| focus events have from/to/reason/t0 | pass (S09, S11) |
| same subject+size+angle on consecutive shots | none |
| budgets M01 40%/30%, M06 50%/20% | 36% moving, 9% shallow - pass |
| beats inside 0-30 | pass |
Expected output: `timeline: 0 errors, 0 warnings`. **Status: unconfirmed until it is run.**

**Final visual audit**
- [x] Subject consistency: one padlock SVG everywhere. The S08 continuity sheet is below.
- [x] Spatial consistency: each scene has fixed coordinates. S05 starts on the S03 end frame. S11 ends on the S01 frame.
- [x] Screen direction: the data flows bottom -> top (YOU -> SITE) in S03 and S05. Real bar is above, fake bar is below, in S09-S11. There are no dialogue lines, so 180° does not apply. Each cut changes size by at least one step, or it changes the subject.
- [x] Movement: 4 moves, each with a motivation and a designed end frame. No moves during in-world text windows.
- [x] Focus: blur is used only to hide or reveal the address. It does not decorate.
- [x] Lighting: flat design light. The vignette appears only in the threat act. The S08 practical light is defined.
- [x] Colour: yellow only on the address. Red only on the scam elements. The padlock is never coloured.
- [x] Transitions: hard cuts, 1 graphic match (S02->S03), 1 loop. No swish (house rule).
- [x] Relevance: every shot maps to a beat. The address is not readable before 23.8. The fake bar is not visible before 26.0.
- [x] Restraint: budgets kept. 1 of 2 allowed AI inserts is used.
- [x] Adapter: zoom, translate and blur are all "full" or "simulated" in the 2D matrix. The AI insert has a static camera, no generated text, and a fallback.
- [x] Intent: narration unchanged. Nothing in the narration is rewritten.
- [ ] **Accuracy (M06):** 4 claims need a source check (section 0). The S04 readout is designed so that it does not claim that metadata is hidden.

## 8. Production instructions
### 2D (HTML/GSAP) - camera calls
Each scene is one `world` div (1080x1920, `transform-origin: 0 0`). Captions and tags that must not scale sit in a screen-fixed HUD layer.
```js
// put world point (fx,fy) at the screen centre at scale s
const frame = (fx, fy, s) => ({ x: 540 - fx * s, y: 960 - fy * s, scale: s });
const cam = (tl, world, t, d, fx, fy, s, ease) => tl.to(world, { ...frame(fx, fy, s), duration: d, ease }, t);
const tl = gsap.timeline();
// static frames are set at shot start
tl.set(bar,     frame(190, 1160, 4.0), 0.0);                    // S01 ECU fake padlock (URL blur 18px)
tl.set(diagram, frame(540, 910, 2.0), 5.2);                      // S03 start = S02 padlock size/position
cam(tl, diagram, 5.2, 1.4, 540, 960, 1.0, "power2.inOut");      // S03 REVEAL zoom out
tl.set(diagram, frame(760, 960, 2.2), 9.6);                      // S04 CU middle node (cut)
tl.set(diagram, frame(540, 960, 1.0), 11.8);                     // S05 cut back to the wide
cam(tl, diagram, 11.8, 1.1, 540, 540, 1.7, "power2.inOut");     // S05 APPROACH zoom in to the site
tl.set(bar,     frame(190, 760, 4.0), 23.8);                     // S09 start: real padlock ECU
cam(tl, bar, 23.8, 0.7, 540, 760, 1.25, "power2.inOut");        // S09 REVEAL zoom out to the name
tl.fromTo(realUrl, { filter: "blur(4.5px)" }, { filter: "blur(0px)", duration: 0.7, ease: "power2.inOut" }, 23.8); // focus pull: 4.5px world x4 = 18px screen
tl.set(bar,     frame(420, 1160, 1.8), 26.0);                    // S10 CU wrong letter (cut)
tl.set(bar,     frame(540, 960, 1.0), 27.6);                     // S11 both bars (cut)
cam(tl, bar, 28.9, 0.8, 190, 1160, 4.0, "power3.inOut");        // S11 APPROACH zoom to the S01 frame
tl.to([realUrl, fakeUrl], { filter: "blur(4.5px)", duration: 0.8, ease: "power3.inOut" }, 28.9); // 4.5px world x4 = 18px screen
```
- TECHNICAL: the world blur is scaled by the camera. For 18 px of screen blur at s = 4.0, set 4.5 px on the world element. Render at 30 fps and check that the S11 end frame matches the S01 first frame pixel for pixel (diff the two PNGs).
- TECHNICAL: the fake bar has `opacity: 0` until 26.0. The grid padlocks have `opacity: 0` until 17.0.
- Scenes card / grid / cert are static at identity. Their events are in the `subject_motion` of the timeline.

### AI video - S08 (one generation)
Tool: Veo (static camera and depth-of-field terms are listed in its guide, per the adapter matrix checked 2026-11-05). Check its current guide and 9:16 support before the run. Generate 6-8 s at 9:16 and use the 2.8 s where the thumb reaches the top bar.
```
A right hand holds a black smartphone upright; the thumb rises slowly and rests on the top edge of the screen.
The phone screen shows a plain, flat, light-grey page with a white bar across the top.
A living room at night, a sofa cushion in the background. Close-up over the right shoulder, looking down onto
the phone, camera holds completely still. Natural lens feel, moderate depth of field: the phone sharp, the room
softly visible. Warm lamp light from the left, cool even light from the phone screen on the thumb.
Muted navy palette with soft warm lamp tones, clean image, fine grain.
Negative prompt (field): text, letters, logos, icons, app interface, watermark, screen glare, rings
```
- **Continuity sheet C1** (paste into any re-generation): adult right hand, medium-brown skin, short clean nails, no rings, grey knit sleeve at the wrist. Black phone, thin bezels, no case. Night living room, one warm lamp on the left. Muted navy + soft warm tones.
- **Comp:** corner-pin track the 4 screen corners, then place the same bar UI as the bar scene (fake bar style, URL at 18 px blur). Yellow underline at 21.6. Padlock dims to 40% at 22.6.
- **Fallbacks:** if the thumb motion is wrong or the hand deforms, use a still frame from the best take (thumb already on the bar) for 2.8 s, with the comp events unchanged. If the screen will not track, build S08 in 2D: a flat phone illustration with the same events.

## 9. Decisions explained
1. **Hide the address until 23.8, end on the S01 frame.** The whole video argues "look at the address", so the address is the one thing the viewer never sees until the instruction. The loop answers "whose lock was that?" with "the fake's". Rejected: a readable URL in S01. It gives the lesson away and turns the loop into a repeat.
2. **Show the correct mechanism in S05.** The dots pass through the blue line untouched, and the hook waits at the end. This teaches the right model (TLS protects transit and does not judge the endpoint). Rejected: a hooded attacker on the line. That is a cliché, and it teaches the wrong model (that the danger is in the middle).
3. **The padlock never gets the accent colour.** Yellow goes to the address. Colour alone tells the viewer which element is the signal. Rejected: a green padlock that turns red. That says "the lock broke", which is false.
4. **Every scale move is a zoom.** These are flat layers with no parallax, so the moves are the act of looking (S05, S11), or reveals by framing (S03, S09). Rejected: calling S05 a push-in. No layer depth exists, so it would be a mislabel.
5. **One AI insert, not two.** Only B8 ("check the address") gains from a real hand. It is the viewer's own action. A second insert at the hook would need generated UI, which AI video must not render, and it would be weaker at phone size than the ECU graphic. Rejected: an insert at 9.6 of a café with Wi-Fi. It is accurate, but it would replace the ciphertext readout, which carries the information.
6. **Static under information.** S04, S06, S07 and S10 are static. S10 is the peak and it is static, because the viewer must find one letter, and a moving frame would compete with the search.

## 10. Hints for other departments
- **Music** (decide nothing here; see `music_hints`): quiet pulse bed under the speech. A drop on "NOT" at 2.6. Tension toward 13.0. Release at 21.0. One accent on "Fake" at 26.0 or the red circle at about 26.5. The tail must loop into 0.0.
- **Sound:** no transition swish (house rule). A soft click is possible when the 12 padlocks appear at 17.0, at a level below the voice.
- **Graphics:** keep caption band y 1440-1580 free of world content (the phone icon ends at about y 1360). The bar UI must look generic, not like a real browser brand.
- **Fact check (before publish):** (1) "most phishing sites today have the padlock": I recall that APWG Phishing Activity Trends reports gave a share above 80% around 2020-2021, but I did **not** verify it in this session. Cite the latest report or soften the line. (2) "certificates are free and automatic": true for Let's Encrypt (ACME) and many hosts, but not for every certificate. (3) "Nobody in the middle can read it": true for the content. The site name and IP stay visible to the network, so the visuals do not claim more. (4) "Real bank: one exact name": some banks use several official domains. This is a simplification and acceptable for a 30 s Short.
