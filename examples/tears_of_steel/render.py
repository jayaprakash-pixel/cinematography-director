"""Render the README/page demo from the skill's edit_plan.json.

before = same cuts, centre crop (cx 960), no captions   (what an auto-reframe does)
after  = the skill's crop keyframes + captions            (what the skill decided)
Outputs (in OUT): before.mp4, after.mp4 (450x800), compare.mp4 (side by side with labels).
Usage: python render.py <source.mov> <edit_plan.json> <out_dir>
"""
import json, os, subprocess, sys

SRC, PLAN, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
W, H, CW = 1920, 800, 450
FONT_CAP = "C\\:/Windows/Fonts/georgiai.ttf"
FONT_UI = "C\\:/Windows/Fonts/consola.ttf"
WORK = os.path.join(OUT, "_work"); os.makedirs(WORK, exist_ok=True)
plan = json.load(open(PLAN, encoding="utf-8"))

# one-line summaries of the skill's own "why" (shortened for the screen; full text in edit_plan.json)
WHY = {
    "S1": "Hold while the caption reads, then follow his drift: the robot enters right",
    "S2": "Cut to the robot's full face - new information",
    "S3": "The only frame that holds man and machine",
    "S4": "Over-the-shoulder cannot fit 450 px: a clean single",
    "S5": "Hologram too wide: frame its centre, caption restores the line",
    "S6": "Face wider than the crop: keep eyes, nose and mouth",
    "S7": "Eyeline matches S6: she looks left, toward him",
}


def x_expr(shot):
    """crop x as a piecewise function of source time T (eased segments)."""
    keys = shot["keys"]; t0 = shot["src_in"]
    T = f"(t+{t0})"
    def seg(a, b):
        u = f"(({T}-{a['t']})/{b['t'] - a['t']})"
        f = f"({u}*{u}*(3-2*{u}))" if a.get("ease") == "inOut" else u
        return f"({a['cx']}+({b['cx']}-{a['cx']})*{f})"
    expr = f"{keys[-1]['cx']}"
    for a, b in reversed(list(zip(keys, keys[1:]))):
        expr = f"if(lt({T},{b['t']}),{seg(a, b)},{expr})"
    return f"max(0,min({W - CW},{expr}-{CW // 2}))"


def run(args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


clips = {"before": [], "after": []}
t_out, windows = 0.0, []
for s in plan["shots"]:
    dur = round(s["src_out"] - s["src_in"], 3)
    windows.append((s["id"], t_out, t_out + dur)); t_out += dur
    for variant in ("before", "after"):
        xe = "960-225" if variant == "before" else x_expr(s)
        vf = f"crop={CW}:{H}:x='{xe}':y=0"
        if variant == "after" and s.get("caption"):
            cap = os.path.join(WORK, f"{s['id']}_cap.txt")
            open(cap, "w", encoding="utf-8").write(s["caption"])
            win = s.get("caption_window_src")
            en = f":enable='between(t,{win[0] - s['src_in']},{win[1] - s['src_in']})'" if win else ""
            capf = cap.replace("\\", "/").replace(":", "\\:")
            vf += (f",drawtext=fontfile='{FONT_CAP}':textfile='{capf}':fontsize=27:fontcolor=white:"
                   f"box=1:boxcolor=black@0.55:boxborderw=12:x=(w-text_w)/2:y={s['caption_y']}*h-text_h/2{en}")
        out = os.path.join(WORK, f"{variant}_{s['id']}.mp4")
        script = os.path.join(WORK, f"{variant}_{s['id']}.txt")
        open(script, "w", encoding="utf-8").write(f"[0:v]{vf},format=yuv420p[v]")
        run(["-ss", str(s["src_in"]), "-t", str(dur), "-i", SRC, "-an", "-/filter_complex", script, "-map", "[v]",
             "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-r", "24", out])
        clips[variant].append(out)

for variant, files in clips.items():
    lst = os.path.join(WORK, f"{variant}.txt")
    open(lst, "w").write("".join(f"file '{os.path.abspath(f)}'\n" for f in files))
    run(["-f", "concat", "-safe", "0", "-i", lst, "-c:v", "libx264", "-crf", "21", "-preset", "slow",
         "-movflags", "+faststart", os.path.join(OUT, f"{variant}.mp4")])

# side-by-side comparison with labels and the skill's reason per shot
lines = []
for sid, a, b in windows:
    f = os.path.join(WORK, f"{sid}_why.txt"); open(f, "w", encoding="utf-8").write(f"{sid}  {WHY[sid]}")
    ff = f.replace("\\", "/").replace(":", "\\:")
    lines.append(f"drawtext=fontfile='{FONT_UI}':textfile='{ff}':fontsize=17:fontcolor=0xffb347:x=(w-text_w)/2:y=h-62:enable='between(t,{a},{b})'")
credit = os.path.join(WORK, "credit.txt"); open(credit, "w").write("Tears of Steel (CC) Blender Foundation | mango.blender.org - CC BY 3.0 - silent")
cf = credit.replace("\\", "/").replace(":", "\\:")
graph = (
    "[0:v]pad=iw+24:ih:0:0:color=0x050507[l];[l][1:v]hstack=2,pad=iw+48:ih+150:24:76:color=0x050507,"
    f"drawtext=fontfile='{FONT_UI}':text='AUTO CENTRE CROP':fontsize=20:fontcolor=0x9b97a6:x=24+225-text_w/2:y=34,"
    f"drawtext=fontfile='{FONT_UI}':text='CINEMATOGRAPHY DIRECTOR':fontsize=20:fontcolor=0xffb347:x=24+474+225-text_w/2:y=34,"
    + ",".join(lines) +
    f",drawtext=fontfile='{FONT_UI}':textfile='{cf}':fontsize=12:fontcolor=0x6f6b79:x=(w-text_w)/2:y=h-30,format=yuv420p[v]"
)
script = os.path.join(WORK, "compare.txt"); open(script, "w", encoding="utf-8").write(graph)
run(["-i", os.path.join(OUT, "before.mp4"), "-i", os.path.join(OUT, "after.mp4"), "-/filter_complex", script,
     "-map", "[v]", "-c:v", "libx264", "-crf", "22", "-preset", "slow", "-movflags", "+faststart", os.path.join(OUT, "compare.mp4")])
print("done", round(t_out, 2), "s;", [w[0] for w in windows])
