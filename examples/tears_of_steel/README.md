# Example: 2.39:1 film scene to a 9:16 Short

- `BRIEF.md`: the task given to a fresh Claude session with only this skill installed. It came with frame strips (with a pixel ruler) of each shot.
- `edit_plan.json`, `timeline.json`, `report.md`: what the skill decided (crop keyframes, trims, captions, reasons). `cdcheck.py timeline timeline.json` returns 0 errors and 1 expected warning: the shallow focus is baked into the source.
- `render.py`: a ffmpeg script that executes the plan exactly, plus the naive centre-crop version for comparison. Usage: `python render.py <tears_of_steel_1080p.mov> edit_plan.json <out_dir>`. The font paths are for Windows; edit `FONT_CAP` and `FONT_UI` for other systems.

Source: *Tears of Steel* (CC) Blender Foundation | mango.blender.org, CC BY 3.0 (`tears_of_steel_1080p.mov` from download.blender.org). The demo is silent: the soundtrack is CC BY-ND.
