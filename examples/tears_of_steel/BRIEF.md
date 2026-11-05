# Brief: reframe a 2.39:1 film excerpt into a 9:16 Short

Source: "Tears of Steel" (CC BY 3.0, (CC) Blender Foundation | mango.blender.org), file 1920x800, 24 fps. Existing footage only. Target adapter: edit (crop, reframe, timing). The original audio may NOT be used (soundtrack licence is no-derivatives), so the Short is silent with on-screen captions written by us.

Goal: a 9:16 vertical version of this excerpt for a Short. The crop window is 450x800 px of the 1920x800 source. There is NO resolution headroom: any punch-in above 1.0 upscales and loses quality.

Shots (source seconds, in film order). Frame strips with a pixel ruler (yellow grid every 240 px, labels 0/480/960/1440) are in this folder: S1.jpg ... S7.jpg. Each strip shows frames at the times printed top-left.
| Shot | Source in-out | Content |
|---|---|---|
| S1 | 276.0-289.5 | a young man (Thom) walks along a bridge; the camera follows; around 284 s a giant robot appears behind him in the background |
| S2 | 299.0-300.85 | robot close view |
| S3 | 300.9-302.7 | wide: Thom on the bridge, robots behind |
| S4 | 310.6-312.35 | Thom facing a woman (Celia, back to camera, right) |
| S5 | 312.4-315.35 | Thom in profile left, holographic text over the houses on the right |
| S6 | 315.4-319.95 | Thom close-up |
| S7 | 320.0-322.2 | Celia close-up |

Task: use the cinematography-director skill. Read the frames. Decide, per shot:
1. where the 450 px crop window sits over time (crop centre x in source px, keyframes with times and easing) - follow the subject only with a motivation; otherwise hold;
2. trims (you may shorten shots; keep film order; total about 25-30 s);
3. any punch-in, respecting the zero headroom rule (say what quality it costs, or avoid it);
4. one short caption per shot (max 6 words) and where it sits (never on a face);
5. a one-line reason per decision.

Write two files in this folder:
- `edit_plan.json`: `{"shots":[{"id","src_in","src_out","keys":[{"t":<source s>,"cx":<px>,"scale":<1.0..>,"ease":"linear|inOut"}],"caption":"...","caption_y":<0..1 of frame height>,"why":"..."}]}`
- `report.md`: the skill's report (Director's summary first, short).
Also write `timeline.json` (the skill's schema, adapter edit_resolve, times in OUTPUT seconds) and run the skill's cdcheck on it.
For comparison, the naive version will be: centre crop (cx = 960) everywhere, no trims, no captions logic.
