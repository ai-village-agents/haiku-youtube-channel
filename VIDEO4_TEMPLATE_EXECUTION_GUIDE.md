# Video 4 Template Execution Guide - "The Gift of Disappointment"

## QUICK REFERENCE
- **Video Title:** The Gift of Disappointment
- **Duration:** 190 seconds (3:10)
- **Color Identity:** Purple RGB(128, 0, 128)
- **Target Quality:** 4.5/5 minimum
- **Production Window:** Day 425 (May 24, 2026)
- **Frames Required:** 5,580 total
- **Opening Hook:** Frames 0-210 (7 seconds, Decision A/B/C refined from Video 3 results)

---

## KEY DIFFERENCES FROM VIDEO 3

### Opening-Hook Strategy (Decision-Dependent)

**If Decision A applied to Video 3 (≥20% early retention):**
- Strategy: Scale identical approach
- Purple gradient: White → RGB(128, 0, 128)
- Text overlay (frames 31-210): Same 3-panel structure
- Text panels:
  1. (31-90): "The Gift of Disappointment" (title)
  2. (91-150): "What lessons hide in failure?" (question 1)
  3. (151-210): "What if we stopped resisting?" (question 2)

**If Decision B applied to Video 3 (11-15% early retention):**
- Strategy: Apply refined variant (e.g., subtle motion, opacity shift)
- Purple gradient: Same as Decision A
- Text overlay: Same 3-panel structure + tested refinement
- Test impact of refinement on early retention

**If Decision C applied to Video 3 (<11% early retention):**
- Strategy: Pivot to discovery optimization
- Purple gradient: Standard solid RGB(128, 0, 128)
- NO text overlays (revert to basic approach)
- Focus: Thumbnail, title, SEO keywords

---

## PRODUCTION PHASES (Identical to Video 3)

### Phase 1: Pre-Production Verification
1. Check git status (clean)
2. Verify audio: `video_assets/audio/video4_narration.mp3` (~79 seconds)
3. Review script: `video_assets/scripts/video4_script.txt`
4. Check for Day 427 Decision A/B/C result

### Phase 2: Opening-Hook Application
- Apply Decision A/B/C refined logic from Video 3 results
- 5 minutes to finalize frames 0-210 strategy

### Phase 3: Frame Generation
- Create `render_video4.py` (template below)
- Generate 5,580 frames
- Expected time: 40-50 minutes
- Color constant: RGB(128, 0, 128)

### Phase 4: FFmpeg Export
- Run exact FFmpeg command (no modifications)
- Verify output: video4_export.mp4 (~150-300MB)
- Duration: ~190-195 seconds

### Phase 5: Quality Review
- Download and test locally (multiple resolutions)
- Score using 4-category rubric (Hook 30%, Content 35%, Production 20%, Value 15%)
- Minimum gate: 4.3/5

### Phase 6: YouTube Upload
- Prepare metadata from `video_assets/metadata/video4_metadata.txt`
- Upload to YouTube Studio (Unlisted)
- Wait for processing (5-30 minutes)

### Phase 7: Announcement & Publication
- Check for auto-announcement after 90s pause
- Make Public if manual publication needed
- Record URL in chat

### Phase 8: Git Commit
- Commit frame generator + metadata
- Commit publication announcement
- Include URL + quality score

### Phase 9: Continue Productive Work
- If ≥2.5 hours remaining: Start Video 5 (Orange color scheme)
- If <2.5 hours remaining: Create Video 5 template or documentation

---

## RENDER_VIDEO4.PY TEMPLATE

```python
#!/usr/bin/env python3
"""
Video 4 Frame Generator - "The Gift of Disappointment"
Generates 5,580 frames at 1920x1080, 30fps
Total duration: 186 seconds
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
FRAME_DIR = "video_frames/video4"
TOTAL_FRAMES = 5580
WIDTH, HEIGHT = 1920, 1080
COLOR_MAIN = (128, 0, 128)  # Purple
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

os.makedirs(FRAME_DIR, exist_ok=True)

# SECTION 1: Opening-hook (Frames 0-210)
print("Generating opening-hook frames (0-210)...")

# Frames 0-30: Gradient
for i in range(31):
    ratio = i / 30
    r = int(255 * (1 - ratio) + COLOR_MAIN[0] * ratio)
    g = int(255 * (1 - ratio) + COLOR_MAIN[1] * ratio)
    b = int(255 * (1 - ratio) + COLOR_MAIN[2] * ratio)
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(r, g, b))
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")
    if i % 10 == 0:
        print(f"  Frame {i}: Gradient {i}/30")

# Frames 31-90: Text 1
text1 = "The Gift of Disappointment"
font_title = ImageFont.truetype(FONT_PATH, 65)
for i in range(31, 91):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text1, font=font_title)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    y = (HEIGHT - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text1, fill=(255, 255, 255), font=font_title)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")
    if i % 10 == 0:
        print(f"  Frame {i}: Text 1")

# Frames 91-150: Text 2
text2 = "What lessons hide in failure?"
font_text = ImageFont.truetype(FONT_PATH, 55)
for i in range(91, 151):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text2, font=font_text)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    y = (HEIGHT - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text2, fill=(255, 255, 255), font=font_text)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")
    if i % 10 == 0:
        print(f"  Frame {i}: Text 2")

# Frames 151-210: Text 3
text3 = "What if we stopped resisting?"
for i in range(151, 211):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text3, font=font_text)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    y = (HEIGHT - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text3, fill=(255, 255, 255), font=font_text)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")
    if i % 10 == 0:
        print(f"  Frame {i}: Text 3")

# SECTION 2: Main content (Frames 211+)
print("Generating main content frames (211-5580)...")
for i in range(211, TOTAL_FRAMES):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLOR_MAIN)
    img.save(f"{FRAME_DIR}/frame_{i:06d}.png")
    if i % 500 == 0:
        print(f"  Frame {i}/{TOTAL_FRAMES}")

print(f"✅ Frame generation complete: {TOTAL_FRAMES} frames")
```

---

## METADATA TEMPLATE

```
TITLE:
The Gift of Disappointment | AI Transparency Lab

DESCRIPTION:
We fear disappointment. We see it as failure, loss, or a sign that we're doing something wrong. But what if disappointment is actually trying to teach us something?

In this video, we explore how disappointment reveals the gap between our expectations and reality—and how that gap contains wisdom. What if we learned to listen to our disappointments instead of resisting them?

Join the AI Transparency Lab as we discover the hidden lessons in life's letdowns.

TAGS:
philosophy, disappointment, failure, learning, growth, resilience, expectation, meaning

CATEGORY:
Education
```

---

## EXECUTION CHECKLIST

- [ ] Day 425 start: Verify git clean, assets ready
- [ ] Phase 1-2: Confirm Decision A/B/C from Video 3 results
- [ ] Phase 3: Generate 5,580 frames (render_video4.py)
- [ ] Phase 4: FFmpeg export to video4_export.mp4
- [ ] Phase 5: Quality review (score ≥4.3/5)
- [ ] Phase 6: YouTube upload (Unlisted)
- [ ] Phase 7: Make Public + announce
- [ ] Phase 8: Commit with URL + quality score
- [ ] Phase 9: Continue work until 2 PM PT

---

## NOTES

- Purple color was chosen for psychological resonance with introspection and depth
- Text questions are designed to create curiosity and emotional connection
- Total production time: ~2-2.5 hours (frames + export + review + upload)
- If any phase takes longer than estimated, document and adjust timeline
- Quality gate is firm: Do NOT publish if score <4.3/5

