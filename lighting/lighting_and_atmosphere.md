# Lighting and atmosphere (D08)

Light shows the subject, separates it from the background, creates depth and sets mood. Every source should be motivated (a window, lamp, screen, fire, the sun) unless the style is openly theatrical.

## Contrast ratio (stop arithmetic)
One stop = double the light. Key:fill 1 stop apart = 2:1, 2 stops = 4:1, 3 stops = 8:1 (S32). Craft convention for the look: about 2:1 open/high-key; about 4:1 natural drama; 8:1 and above hard drama, noir, horror. Write the ratio when the look depends on it; treat the look labels as conventions.

## Techniques

### Three-point lighting
What: key (main), fill (softens shadows), back light (separates from background) (S27). Effect: a clear, modelled subject.
Use when: interviews, presenters, products; a base to break from. Avoid when: it makes a natural or dramatic scene look like a studio. Source: S27.

### Key light
What: the brightest light; sets direction and shadow shape (S27). Effect: side key = drama and texture; frontal key = openness and flatness; top key = isolation, interrogation.
Use when: always decide its direction first. Avoid when: -. Source: S27.

### Fill light
What: lifts shadows. Effect: lower contrast, friendlier.
Use when: open looks, explainers. Avoid when: the scene needs darkness; use negative fill instead. Source: S27.

### Back light / rim light
What: light from behind the subject; rim = a thin edge. Effect: separation, depth, a halo/hero edge.
Use when: dark backgrounds, silhouettes, product edges. Avoid when: unmotivated in naturalistic scenes (a rim with no source). Source: S27.

### Practical lighting
What: lights visible in frame (lamps, screens, candles). Effect: realism, motivation, warmth or loneliness.
Use when: night interiors; tech scenes lit by screens. Show "just enough, not too much" (S09). Avoid when: practicals overexpose and pull attention. Source: S09.

### Natural and available light
What: sun, sky, windows, fire. Effect: truth and texture; timing by weather and hour.
Use when: personal, documentary, epic realism (S10: Revenant used only natural light and firelight; S09: overcast skies for 360° moves). Avoid when: the schedule cannot follow the sun. Source: S09, S10.

### Motivated lighting
What: light that seems to come from a source in the story world. Effect: belief in the space.
Use when: default for fiction and animation. Avoid when: a stylised world openly breaks it. Source: S09, S10.

### High-key lighting
What: bright, low contrast, few shadows. Effect: openness, safety, comedy, commercial clarity.
Use when: explainers, products, upbeat content. Avoid when: mystery and tension. Source: craft convention; S32.

### Low-key lighting
What: dark tones dominate, high contrast. Effect: mystery, danger, intimacy, drama.
Use when: suspense, night, secrets. Avoid when: the viewer must read details or text. Source: craft convention; S32.

### Chiaroscuro
What: strong light-dark modelling, often one hard side key. Effect: moral conflict, painterly drama.
Use when: a character torn; portraits with gravity. Avoid when: light, friendly tones. Source: craft convention.

### Silhouette
What: the subject dark against a bright background. Effect: anonymity, mystery, iconic shape, an ending.
Use when: hiding identity (see/hide list); a graphic moment. Avoid when: the face matters. Source: craft convention.

### Volumetric light / haze
What: light shafts visible in haze, smoke or dust. Effect: atmosphere, depth, the sacred or the dangerous.
Use when: the shafts mean something (a holy place, a dusty archive, a smoky server room under stress). Avoid when: added "for cinema" to every scene. Execution: physical - haze machine; Blender - volume scatter in the world or a cube; AI - "volumetric light, haze". Source: craft convention.

### Hard and soft light
What: hard = small/far source, crisp shadows; soft = large/near source, soft shadows. Effect: hard = drama, heat, truth; soft = gentleness, beauty, calm.
Use when: choose by mood and by the source the story shows. Avoid when: mixing both on one face without a reason. Source: craft convention.

### Light falloff
What: light gets weaker with distance from the source (inverse-square law for a point source). Effect: a near source gives fast falloff (pools of light, dark backgrounds); a far source lights evenly.
Use when: control the background brightness by source distance. Avoid when: -. Source: physics.

### Colour temperature
What: warm (tungsten, fire, low sun) vs cool (shade, sky, many screens). Effect: warm = home, nostalgia, safety, danger of fire; cool = night, technology, distance, clinical. Meaning is set inside the video (`colour/colour_direction.md`).
Use when: a warm-cool contrast separates two worlds or two times. Avoid when: mixed temperatures on a face with no motivation. Source: craft convention.

### Negative fill and shadow control
What: black surfaces or flags that remove light to deepen shadows. Effect: shape and drama in soft light.
Use when: overcast or bright rooms that make faces flat. Avoid when: the look must be open. Source: craft convention.

## Lighting as an arc
Plan contrast like the emotion timeline: low contrast at calm, rising with tension, release at resolution. Keep light direction continuous within a scene (`direction/blocking_and_continuity.md`).

## Adapter notes
- Blender: Area lights (soft), Spot/Sun (hard), world HDRI for natural light, volume scatter for haze, light linking for rims.
- 2D: gradients, glows, vignettes, light wipes; keep one light direction per scene.
- AI: describe source, direction, quality and time of day ("soft window light from the left, late afternoon, warm"); one light idea per clip.
