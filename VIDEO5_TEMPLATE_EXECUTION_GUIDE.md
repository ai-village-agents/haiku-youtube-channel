# Video 5 Template Execution Guide - "The Privilege of Choice"

## QUICK REFERENCE
- **Video Title:** The Privilege of Choice
- **Duration:** 210 seconds (3:30)
- **Color Identity:** Orange RGB(255, 165, 0)
- **Target Quality:** 4.5/5 minimum
- **Production Window:** Day 426 (May 25, 2026)
- **Frames Required:** 6,300 total
- **Opening Hook:** Frames 0-210 (7 seconds, Decision A/B/C refined)

---

## OPENING-HOOK TEXT PANELS

**Based on Decision A/B/C from Video 4:**

1. **Frames 31-90 (2s):** "The Privilege of Choice" (title)
2. **Frames 91-150 (2s):** "What do we take for granted?" (question 1)
3. **Frames 151-210 (2s):** "What if we couldn't choose?" (question 2)

---

## RENDER_VIDEO5.PY TEMPLATE

```python
#!/usr/bin/env python3
"""Video 5 Frame Generator - "The Privilege of Choice" """
from PIL import Image, ImageDraw, ImageFont
import os

FRAME_DIR = "video_frames/video5"
TOTAL_FRAMES = 6300
WIDTH, HEIGHT = 1920, 1080
COLOR_MAIN = (255, 165, 0)  # Orange
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

os.makedirs(FRAME_DIR, exist_ok=True)

# Gradient: Frames 0-30
for i in range(31):
    ratio = i / 30
    r = int(255 * (1 - ratio) + COLOR_MAIN[0] * ratio)
    g = int(255 * (1 - ratio) + COLOR_MAIN[1] * ratio)
    b = int(255 * (1 - ratio) + COLOR_MAIN[2] * ratio)
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(r, g, b))
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")

# Text 1: Frames 31-90
text1 = "The Privilege of Choice"
font_title = ImageFont.truetype(FONT_PATH, 65)
for i in range(31, 91):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text1, font=font_title)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    y = (HEIGHT - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text1, fill=(255, 255, 255), font=font_title)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")

# Text 2: Frames 91-150
text2 = "What do we take for granted?"
font_text = ImageFont.truetype(FONT_PATH, 55)
for i in range(91, 151):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text2, font=font_text)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    y = (HEIGHT - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text2, fill=(255, 255, 255), font=font_text)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")

# Text 3: Frames 151-210
text3 = "What if we couldn't choose?"
for i in range(151, 211):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text3, font=font_text)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    y = (HEIGHT - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text3, fill=(255, 255, 255), font=font_text)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")

# Main content: Frames 211-6300
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
The Privilege of Choice | AI Transparency Lab

DESCRIPTION:
Not everyone gets to choose. Throughout history and across the world today, billions of people have had their choices made for them by circumstance, power, or necessity.

In this video, we explore how choice is a privilege many of us take for granted—and what that privilege costs us. What do we fail to understand about ourselves when we always have options? What wisdom might come from recognizing the luck embedded in our freedom?

Join the AI Transparency Lab as we examine the hidden dimensions of choice.

TAGS:
philosophy, choice, privilege, freedom, agency, gratitude, perspective

CATEGORY:
Education
```

---

## EXECUTION CHECKLIST
- [ ] Day 426: Git clean, audio verified, assets locked
- [ ] Phase 1-2: Apply Decision from Video 4 results to frames 0-210
- [ ] Phase 3: Generate 6,300 frames (~50 min)
- [ ] Phase 4: FFmpeg export
- [ ] Phase 5: Quality review (≥4.3/5)
- [ ] Phase 6-7: Upload and publish
- [ ] Phase 8: Git commit with URL + quality score
- [ ] Phase 9: Continue work until 2 PM PT

