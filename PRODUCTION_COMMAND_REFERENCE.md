# Production Command Reference (Days 417-428)

**Quick-access document for all exact production commands and specifications**  
**Last updated:** Day 416, May 22, 2026  
**Status:** LOCKED - NO MODIFICATIONS ALLOWED

---

## IMMUTABLE FFMPEG EXPORT COMMAND (NEVER MODIFY)

Copy this exact command for each video. Replace `[N]` with video number (2, 3, 4, 5, 6).

```bash
ffmpeg -framerate 30 \
  -i "video_frames/video[N]/frame_%06d.png" \
  -i "video_assets/audio/video[N]_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video[N]_export.mp4"
```

### Critical FFmpeg Specifications (IMMUTABLE)
- **Codec:** H.264 (libx264)
- **Profile:** High
- **Pixel format:** YUV420P (4:2:0)
- **Bitrate:** 5000k video
- **CRF:** 18 (LOCKED - no exceptions)
- **Audio codec:** AAC
- **Audio bitrate:** 192k
- **Audio sample rate:** 24000 Hz
- **Framerate:** 30 fps
- **Resolution:** 1920x1080
- **NO `-shortest` flag** (critical - narration drives length)

---

## GIT COMMIT COMMAND FORMAT (IMMUTABLE)

Use this exact format after YouTube publication. Replace placeholders with actual values.

```bash
git add DAY[XXX]_PUBLICATION_RECORD.md
git commit -m "Day [XXX]: Published Video [X] '[TITLE]' - [SCORE]/5 quality — https://youtu.be/[ID]"
git push origin main
```

### Example (Video 1):
```bash
git commit -m "Day 421: Published Video 1 'The Right Time Never Arrives' - 4.5/5 quality — https://youtu.be/BOBSjmDcio8"
```

### Required elements:
1. `Day [XXX]:` — Day number (3 digits)
2. `Published Video [X]` — Video number (1-10)
3. `'[TITLE]'` — Exact video title in single quotes
4. `[SCORE]/5` — Quality score (e.g., 4.5/5)
5. `https://youtu.be/[ID]` — YouTube short URL with video ID
6. Final push: `git push origin main`

---

## PAUSE(90) PROTOCOL (IMMUTABLE)

Use before every manual announcement.

```python
pause(90)  # Wait 90 seconds for auto-fire event
```

### Protocol steps:
1. Call `pause(90)` immediately after YouTube upload confirmation
2. **DO NOT send manual announcement while paused**
3. After pause completes, check visible events for auto-fire
4. **IF auto-fire detected in events:** Do NOT send manual announcement (duplicate)
5. **IF no auto-fire detected:** Send manual announcement to chat
6. Proceed to `git add` and `git commit`

---

## PRODUCTION TIMELINE (LOCKED SCHEDULE)

### Day 417 (Monday, May 26)
**10:00 AM - 12:30 PM PT: Video 2 Polish Collaboration**
- Partner: Claude Opus 4.5
- Asset location: ~/deepseek-video2-assets/
- Quality gate: ≥4.3/5 (4-category rubric)
- Decision: Publish (≥4.3/5) or Hold (<4.3/5)

### Day 424 (Thursday, May 23)
**10:00 AM - 2:00 PM PT: Video 3 Production**
- Title: "The Maps We Build"
- Duration: 200s
- Color: Blue (RGB 50,100,180)
- Narration: 83.3s (6,255 frames at 30fps)
- FFmpeg export: CRF 18

### Day 425 (Friday, May 24)
**10:00 AM - 2:00 PM PT: Video 4 Production**
- Title: "The Gift of Disappointment"
- Duration: 190s
- Color: Purple (RGB 128,0,128)
- Narration: 79.0s (5,700 frames at 30fps)
- FFmpeg export: CRF 18

### Day 426 (Saturday, May 25)
**10:00 AM - 2:00 PM PT: Video 5 Production**
- Title: "The Privilege of Choice"
- Duration: 210s
- Color: Orange (RGB 255,165,0)
- Narration: 84.5s (6,300 frames at 30fps)
- FFmpeg export: CRF 18

### Day 427 (Sunday, May 26)
**10:00 AM - 10:30 AM PT: Analytics Decision Gate**
- Check YouTube Analytics for Video 2 early retention @7-second mark
- Evaluate: Decision A (≥20%), Decision B (11-15%), Decision C (<11%)
- Create DAY427_ANALYTICS_RESULT.md
- Lock V3-V6 strategy

### Day 428 (Monday, May 27)
**10:00 AM - 2:00 PM PT: Video 6 Production**
- Title: "What We Fear Speaking Into Being"
- Duration: 170s
- Color: White (RGB 255,255,255)
- Narration: 97.8s (5,100 frames at 30fps)
- FFmpeg export: CRF 18

---

## QUALITY GATE RUBRIC (4-CATEGORY WEIGHTED)

### Scoring formula:
**(Hook × 0.30) + (Content × 0.35) + (Production × 0.20) + (Value × 0.15) = FINAL SCORE**

### Category definitions:
1. **Hook (30% weight, target 8.5/10)**
   - Question: Is the first 7 seconds compelling?
   - Scoring: 0-10 scale
   - Multiply by 0.30

2. **Content (35% weight, target 8.5/10)**
   - Question: Is the message clear, coherent, emotionally resonant?
   - Scoring: 0-10 scale
   - Multiply by 0.35

3. **Production (20% weight, target 9.0/10)**
   - Question: Are audio/visual elements professionally executed?
   - Scoring: 0-10 scale
   - Multiply by 0.20
   - **CRITICAL for audio/export quality**

4. **Value (15% weight, target 8.5/10)**
   - Question: Does the video offer unique perspective and viewer transformation?
   - Scoring: 0-10 scale
   - Multiply by 0.15

### Final score calculation example:
- Hook: 8.5 × 0.30 = 2.55
- Content: 8.5 × 0.35 = 2.975
- Production: 9.0 × 0.20 = 1.80
- Value: 8.5 × 0.15 = 1.275
- **Total: 8.6/10 weighted → 4.3/5 scale** ✓ (meets gate)

### Mandatory gate:
- **≥4.3/5 to publish** (no exceptions)
- **<4.3/5 to hold** and schedule refinement

---

## YOUTUBE UPLOAD CHECKLIST

Use this checklist for each video publication.

### Pre-upload verification:
- [ ] FFmpeg export completed (CRF 18 verified)
- [ ] Video file exists: `video_exports/video[N]_export.mp4`
- [ ] File size reasonable (typically 100-200MB for 3-10min video)
- [ ] Quality score calculated (≥4.3/5 confirmed)

### Upload steps:
1. [ ] Open https://www.youtube.com/studio
2. [ ] Click "Create" → "Upload video"
3. [ ] Select file: `video[N]_export.mp4`
4. [ ] Enter title: Exact title from documentation
5. [ ] Enter description: (see documentation for each video)
6. [ ] Select playlist: AI Transparency Lab (main channel)
7. [ ] Audience: Made for Everyone (not made for kids)
8. [ ] Click "Publish"
9. [ ] **Wait for "Published" confirmation** (typically 30-120 seconds)
10. [ ] Copy video URL: `https://youtu.be/[ID]`

### Post-upload:
- [ ] Video appears in YouTube Studio
- [ ] Status shows "Published" (not "Unlisted" or "Private")
- [ ] Video accessible via public URL
- [ ] Copy video ID from URL for git commit

---

## DAILY STARTUP CHECKLIST (10:00-10:15 AM)

Use this 15-minute verification before starting production.

### System verification:
- [ ] Terminal open at `/tmp/haiku-youtube/`
- [ ] Git status clean: `git status` shows no uncommitted changes
- [ ] Latest commit visible: `git log --oneline -1`
- [ ] Narration file present: `ls -lh video_assets/audio/video[N]_narration.mp3`
- [ ] Frame generator script present: `ls -lh video[N]_framegen.py`

### Asset verification:
- [ ] Disk space adequate: `df -h /tmp` shows 50GB+ available
- [ ] Python3 installed: `python3 --version`
- [ ] FFmpeg installed: `ffmpeg -version | head -1`
- [ ] PIL/Pillow available: `python3 -c "from PIL import Image; print('OK')"`

### Documentation verification:
- [ ] Quick-start guide open: DAY[XXX]_QUICK_START_REFERENCE.md
- [ ] Quality rubric accessible: VIDEO[N]_QUALITY_RUBRIC_EVAL.md
- [ ] Production checklist visible: This file

### Collaboration verification (Day 417 only):
- [ ] Chat available: https://theaidigest.org/village
- [ ] Claude Opus 4.5 confirmed availability
- [ ] Assets at ~/deepseek-video2-assets/ accessible

---

## TROUBLESHOOTING QUICK REFERENCE

### FFmpeg command fails
- Check file paths are correct
- Verify narration MP3 exists
- Verify frame directory exists with frames
- Check CRF 18 is NOT changed
- Try: `ffmpeg -version` to verify installation

### Git commit fails
- Verify clean working tree: `git status`
- Check commit message includes URL and score
- Verify all documentation files added: `git add DAY[XXX]*.md`
- Try: `git status` to see what needs to be added

### YouTube upload fails
- Check file size is reasonable (typically 100-200MB)
- Verify video plays locally before uploading
- Check YouTube Studio is accessible
- Try uploading to playlist explicitly

### pause(90) duplicate announcement
- If auto-fire event detected in post-pause events, skip manual announcement
- Check visible events for `AGENT_TALK` with agent name
- Verify no similar message already sent

---

## IMMUTABLE REMINDERS (DO NOT IGNORE)

1. **FFmpeg CRF 18 is LOCKED** — NO modifications
2. **Quality gate ≥4.3/5 is FIRM** — Do NOT publish if below
3. **pause(90) is MANDATORY** — Always wait before manual announcement
4. **One video/day MAX** — Schedule locked (no exceptions)
5. **Git commits MUST include URL + score** — Required format
6. **Series 1 is LOCKED FOREVER** — No modifications
7. **YouTube "Published" confirmation required** — Always verify before commit
8. **No duplicate announcements** — Check auto-fire events first
9. **Work until 2 PM PT** — No early stopping per Shoshannah's mandate
10. **All specifications IMMUTABLE** — This document is the source of truth

---

**Reference document locked.** No modifications allowed without explicit approval.  
**Last verified:** Day 416, fa6726b commit  
**Next update:** Only if new Day added to production schedule
