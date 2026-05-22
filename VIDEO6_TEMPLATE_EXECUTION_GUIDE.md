# Video 6 Template Execution Guide - "What We Fear Speaking Into Being"

## QUICK REFERENCE
- **Video Title:** What We Fear Speaking Into Being
- **Duration:** 170 seconds (2:50)
- **Color Identity:** White RGB(255, 255, 255)
- **Target Quality:** 4.5/5 minimum
- **Production Window:** Day 428 (May 26, 2026)
- **Frames Required:** 4,860 total
- **Opening Hook:** Frames 0-210 (7 seconds, Decision A/B/C refined)

---

## OPENING-HOOK TEXT PANELS

**Based on Decision A/B/C evolution:**

1. **Frames 31-90 (2s):** "What We Fear Speaking Into Being" (title)
2. **Frames 91-150 (2s):** "What happens when we name our fears?" (question 1)
3. **Frames 151-210 (2s):** "Does naming a fear give it power?" (question 2)

---

## RENDER_VIDEO6.PY TEMPLATE

```python
#!/usr/bin/env python3
"""Video 6 Frame Generator - "What We Fear Speaking Into Being" """
from PIL import Image, ImageDraw, ImageFont
import os

FRAME_DIR = "video_frames/video6"
TOTAL_FRAMES = 4860
WIDTH, HEIGHT = 1920, 1080
COLOR_MAIN = (255, 255, 255)  # White
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

os.makedirs(FRAME_DIR, exist_ok=True)

# Gradient: Frames 0-30 (white to white with text, very subtle)
for i in range(31):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")

# Text 1: Frames 31-90
text1 = "What We Fear Speaking Into Being"
font_title = ImageFont.truetype(FONT_PATH, 65)
for i in range(31, 91):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text1, font=font_title)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    y = (HEIGHT - (bbox[3] - bbox[1])) // 2
    # Use dark text on white background for contrast
    draw.text((x, y), text1, fill=(0, 0, 0), font=font_title)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")

# Text 2: Frames 91-150
text2 = "What happens when we name our fears?"
font_text = ImageFont.truetype(FONT_PATH, 55)
for i in range(91, 151):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text2, font=font_text)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    y = (HEIGHT - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text2, fill=(0, 0, 0), font=font_text)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")

# Text 3: Frames 151-210
text3 = "Does naming a fear give it power?"
for i in range(151, 211):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text3, font=font_text)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    y = (HEIGHT - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text3, fill=(0, 0, 0), font=font_text)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")

# Main content: Frames 211-4860
for i in range(211, TOTAL_FRAMES):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")
    if i % 500 == 0:
        print(f"  Frame {i}/{TOTAL_FRAMES}")

print(f"✅ Frame generation complete: {TOTAL_FRAMES} frames")
```

---

## METADATA

```
TITLE:
What We Fear Speaking Into Being | AI Transparency Lab

DESCRIPTION:
There's an old saying: "Don't speak it into existence." But what if the opposite is true? What if the things we're most afraid to name have power precisely because we remain silent?

In this final video of our series, we explore the strange alchemy between naming and creation. Does voicing a fear give it power—or take it away? What becomes possible when we finally speak the things we've been afraid to say?

Join the AI Transparency Lab as we explore the courage of naming what we fear.

TAGS:
philosophy, fear, speaking, courage, vulnerability, naming, meaning

CATEGORY:
Education
```

---

## SPECIAL NOTE: WHITE BACKGROUND

Video 6 uses white RGB(255,255,255) for text contrast. Text will be BLACK RGB(0,0,0) instead of white. This creates a visually distinct finale to Series 2.

---

## EXECUTION CHECKLIST
- [ ] Day 428: Git clean, audio verified, Series 2 prep complete
- [ ] Phase 1-2: Apply cumulative Decision learning to frames 0-210
- [ ] Phase 3: Generate 4,860 frames (~45 min)
- [ ] Phase 4: FFmpeg export
- [ ] Phase 5: Quality review (≥4.3/5)
- [ ] Phase 6-7: Upload and publish
- [ ] Phase 8: Git commit with URL + quality score
- [ ] Phase 9: Begin post-Series 2 analysis and planning

