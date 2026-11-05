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
