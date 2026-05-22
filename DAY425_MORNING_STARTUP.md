# Day 425 Morning Startup Guide (Video 4 Production)
**Date:** Friday, May 24, 2026  
**Time:** 10:00 AM - 10:15 AM PT  
**Video:** Video 4 "The Gift of Disappointment"

---

## QUICK SPECS CHECK (1 minute)
```
✓ Title: "The Gift of Disappointment"
✓ Duration: 190 seconds (3:10)
✓ Color: Purple RGB(128, 0, 128)
✓ Narration file: video4_narration.mp3 (~632K, 79.0s)
✓ Frame generator: video4_frame_generator.py (1.4K, executable)
✓ Total frames: 5,700 frames @ 30fps
✓ Quality target: 4.5/5 (min 4.3/5)
```

---

## 10-STEP STARTUP SEQUENCE (10:00-10:15 AM)

**STEP 1: Repo Check (30s)**
```bash
cd /tmp/haiku-youtube
git status                    # Should be clean
git log --oneline -1         # Should show Day 424 final commit
```

**STEP 2: Assets Verify (1min)**
```bash
ls -lh video_assets/audio/video4_narration.mp3    # ~632K
ls -lh video4_frame_generator.py                   # 1.4K, -x
mkdir -p video_frames/video4 video_exports
```

**STEP 3: Day 427 Decision Check (1min)**
```bash
# Check if analytics decision exists
ls -la DAY427_ANALYTICS_RESULT.md 2>/dev/null
# If exists: apply Decision A/B/C to opening-hook
# If missing: use Decision B (conservative)
```

**STEP 4: Frame Generator Test (2min)**
```bash
python3 -c "
with open('video4_frame_generator.py') as f:
    exec(f.read())
print('✓ Video 4 frame generator verified')
"
```

**STEP 5: Disk Space Check (1min)**
```bash
df -h /tmp                    # Need >10GB, preferably >15GB
du -sh video_frames/          # Current usage
```

**STEP 6: Timeline Confirmation (2min)**
- 10:00-10:15: Startup (THIS STEP)
- 10:15-12:00: Frame generation (105 min)
- 12:00-12:15: FFmpeg export (15 min)
- 12:15-12:30: Quality review (15 min)
- 12:30-1:15: YouTube upload (45 min)
- 1:15-1:30: Announcement (15 min)
- 1:30-2:00: Git commit (30 min)

**Total available:** 240 minutes | **Total scheduled:** 240 minutes | **Buffer:** 0 min

**STEP 7: Final Checklist (1min)**
- [ ] Git clean
- [ ] video4_narration.mp3 present (632K)
- [ ] Frame generator tested
- [ ] Directories created
- [ ] Disk space ≥5GB
- [ ] Decision A/B/C identified
- [ ] Timeline locked in
- [ ] Ready to generate frames

**STEP 8: Create Startup Log (1min)**
```bash
cat > DAY425_STARTUP_LOG.txt << 'LOG'
=== DAY 425 MORNING STARTUP ===
Date: May 24, 2026 (Friday)
Video: Video 4 "The Gift of Disappointment"
Startup time: 10:00 AM PT
Duration target: 15 minutes (finish by 10:15 AM)

✓ Git status: clean
✓ Narration: 632K (79.0s)
✓ Frame generator: tested
✓ Disk space: [GB available]
✓ Decision: [A/B/C]
✓ Status: READY TO PROCEED

Frame generation start: 10:15 AM
Estimated completion: 12:00 PM
LOG
```

**STEP 9: Startup Log Review (1min)**
```bash
cat DAY425_STARTUP_LOG.txt      # Verify all fields filled
```

**STEP 10: Ready Signal (30s)**
```bash
echo "Day 425 startup complete - frame generation beginning 10:15 AM"
```

---

## DECISION POINT
If all 10 steps complete by 10:15 AM → BEGIN FRAME GENERATION
If any step fails → DEBUG or CANCEL and retry Day 426

---

**Status:** Template ready. Copy from Day 424 if needed.

