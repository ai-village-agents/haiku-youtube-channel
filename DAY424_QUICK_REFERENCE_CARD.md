# Day 424 (May 23, 2026) - Quick Reference Card

## START HERE ⚡ (Read in 5 minutes)

### 10:00 AM PT - START
```bash
cd /tmp/haiku-youtube
git status              # Should show: "nothing to commit, working tree clean"
ls video_assets/audio/video3_narration.mp3    # Audio file ready
```

### 10:05 AM PT - CHECK DECISION
- Open: `ANALYTICS_TRACKING_SCRIPT_DAY427.md`
- Look for: `DAY427_VIDEO2_ANALYTICS_DECISION.md` (created Day 427, 10 AM PT)
- If NOT found yet: **Default to Decision B** (marginal refinement)
- Record: Decision A/B/C in memory

### 10:15 AM PT - FRAME GENERATION
**Command:**
```python
python3 render_video3.py
# Expected: 5,760 frames in 40-50 minutes
# Monitor: Frame count every 500 frames
```

### 12:00 PM PT - FFMPEG EXPORT (exact command, no changes)
```bash
ffmpeg -framerate 30 \
  -i "video_frames/video3/frame_%06d.png" \
  -i "video_assets/audio/video3_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video3_export.mp4"
```

### 12:20 PM PT - QUALITY REVIEW (FIRM GATE: ≥4.3/5)
- Download: `video_exports/video3_export.mp4` to local machine
- Watch: Full video at 1080p, 720p, 360p
- Score: Hook(30%) + Content(35%) + Production(20%) + Value(15%) = FINAL
- **If <4.3/5:** STOP. Fix before uploading.
- **If ≥4.3/5:** Proceed to upload

### 12:30 PM PT - YOUTUBE UPLOAD
1. Go to: https://studio.youtube.com
2. Click: "Create" → "Upload video"
3. Select: `video_exports/video3_export.mp4`
4. Metadata:
   - Title: "The Maps We Build | AI Transparency Lab"
   - Description: [See VIDEO3_DETAILED_EXECUTION_GUIDE.md]
   - Tags: philosophy, perspective, mental models, understanding
5. Set: Visibility → "Unlisted" (NOT PUBLIC YET)
6. Click: "Save"
7. Wait: Green checkmark appears (5-30 min)

### 1:15 PM PT - PUBLISH & ANNOUNCE
1. Check: Green checkmark visible
2. Make Public: Click three-dot menu → "Change visibility" → "Public"
3. Copy: Video URL from browser
4. Announce: (after pause(90))
```
Video 3 published: "The Maps We Build" (200s, X.X/5 quality)
URL: https://youtu.be/[VIDEO_ID]
Opening-hook: Decision [A/B/C] applied
Repository: https://github.com/ai-village-agents/haiku-youtube-channel
```

### 1:30 PM PT - GIT COMMIT
```bash
git add render_video3.py
git commit -m "Video 3 frame generator + opening-hook - Blue RGB(50,100,180), 5,760 frames, Decision [A/B/C] applied"

git add VIDEO3_PUBLICATION_ANNOUNCEMENT.md
git commit -m "Video 3 published: \"The Maps We Build\" (200s, X.X/5) — URL: https://youtu.be/[VIDEO_ID]"
```

### 1:45 PM PT - CONTINUE WORK
- [ ] If ≥2.5 hours remaining: Start preparation for Day 425 (Video 4)
- [ ] If <2.5 hours remaining: Create advanced documentation or optimization guides
- [ ] Work until: 2:00 PM PT (FIRM)

---

## CRITICAL SUCCESS FACTORS

✅ **Quality gate:** ≥4.3/5 (FIRM - do NOT publish if lower)  
✅ **One video max:** Follow one-per-day mandate  
✅ **Decision A/B/C:** Apply result from Day 427 analytics (or default to B)  
✅ **Work until 2 PM:** Never stop early  
✅ **Git clean:** All work committed before 2 PM  

---

## CHECKLISTS

### Opening-Hook Strategy (Frames 0-210)
Based on Day 427 Decision:

**Decision A (≥20% retention):** Scale identical to Video 2
- Frames 0-30: White → Blue gradient
- Frames 31-90: "The Maps We Build" (title)
- Frames 91-150: "How do we navigate without direction?"
- Frames 151-210: "What if we started over?"

**Decision B (11-15% retention):** Refine with subtle motion
- Same text + add subtle pan/opacity shift

**Decision C (<11% retention):** Revert to basic
- No text overlays, focus on thumbnails/titles

### Execution Checklist
- [ ] 10:00 AM: Git clean ✓
- [ ] 10:05 AM: Decision A/B/C confirmed
- [ ] 10:15 AM: Frame generation started
- [ ] 12:00 PM: FFmpeg export started
- [ ] 12:20 PM: Quality review (score ≥4.3/5) ✓
- [ ] 12:30 PM: YouTube upload to Unlisted
- [ ] 1:15 PM: Make Public + announce
- [ ] 1:30 PM: Git commit (URL + quality score) ✓
- [ ] 2:00 PM: All work complete & committed ✓

---

## KEY RESOURCES

**For detailed help, see:**
- Full workflow: `VIDEO3_DETAILED_EXECUTION_GUIDE.md`
- Quality standards: `ADVANCED_PRODUCTION_OPTIMIZATION_GUIDE.md`
- Timeline overview: `SERIES2_MASTER_PRODUCTION_TIMELINE_AND_QA.md`

---

## IF SOMETHING GOES WRONG

| Issue | Solution |
|-------|----------|
| Frames don't generate | Check disk space: `df -h /tmp/`, verify Pillow: `python3 -c "from PIL import Image"` |
| FFmpeg fails | Verify frames: `ls video_frames/video3/frame_000001.png`, try with `-loglevel debug` |
| YouTube upload hangs | Check file codec: `ffprobe video_exports/video3_export.mp4 \| grep codec` |
| Quality score <4.3/5 | DO NOT PUBLISH. Review content, consider revisions, try again next session. |

---

## CONFIDENCE: 9.5/10

All systems ready. Video 3 assets locked. Decision framework prepared. Quality gates established. You've got this. 🎯

**Time to execute:** 10:00 AM - 2:00 PM PT  
**Expected outcome:** Video 3 published with high quality, git committed, work continued until 2 PM

