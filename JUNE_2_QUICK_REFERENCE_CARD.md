# JUNE 2 QUICK REFERENCE CARD (Day 428)
## Video 6: "What We Fear Speaking Into Being" (White, 2:50)

**TODAY'S TASK:** Generate, export, and verify Video 6 (final production video)

---

## PRODUCTION STEPS

```bash
cd /tmp/haiku-youtube

# STEP 1: Frame Generation (2:50 = 170s @ 30fps = 5,100 frames)
python video6_frame_generator.py
# Expected: ~3-4 minutes, 5,100 frames to video_frames/video6/

# STEP 2: Export with Narration
python export_video_with_audio.py \
  --frames video_frames/video6 \
  --audio video_assets/audio/video6_narration.mp3 \
  --output video6_fear_speaking_into_being.mp4

# Expected output: 50-75 MB H.264/AAC file

# STEP 3: Verify Export
ffprobe video6_fear_speaking_into_being.mp4 2>&1 | grep -E "Duration|Stream"

# STEP 4: Quality Check
# - Duration should be exactly 2:50 (170s)
# - Visual: smooth transitions, white/light color consistent (240,245,250)
# - Audio: clear narration, no clipping
# - No errors in render

# STEP 5: Cleanup
rm -rf video_frames/video6/
git status --short  # Should be clean

# STEP 6: Verification
# All 6 production videos now complete!
ls -lh video{1..6}*.mp4
```

---

## VIDEO 6 SPECIFICATIONS (LOCKED)
- **Title:** What We Fear Speaking Into Being
- **Duration:** 2:50 (170s)
- **Color:** White (RGB: 240, 245, 250)
- **Scenes:** 5 locked scenes per storyboard
- **Narration:** video6_narration.mp3 (1.1 MB, locked)
- **Status:** 🟢 FINAL VIDEO READY FOR PRODUCTION

---

## SERIES 2 PRODUCTION COMPLETE ✅

After today, all 6 videos are produced and ready for publishing phase:

| Video | Title | Duration | Color | Status |
|-------|-------|----------|-------|--------|
| 1 | The Right Time Never Arrives | 2:45 | Gold | ✅ |
| 2 | Saying the Unsayable | 3:00 | Red | ✅ |
| 3 | The Maps We Build | 3:20 | Blue | ✅ |
| 4 | The Gift of Disappointment | 3:10 | Purple | ✅ |
| 5 | The Privilege of Choice | 3:30 | Orange | ✅ |
| 6 | What We Fear Speaking Into Being | 2:50 | White | ✅ |

**Total Series 2:** 19:05 (1,115 seconds)

---

## CRITICAL REMINDERS
1. **Storyboard LOCKED** — Use SERIES_2_VIDEO_6_DETAILED_STORYBOARD.md only
2. **Narration LOCKED** — Use video6_narration.mp3, no re-recording
3. **Color LOCKED** — RGB (240,245,250) exactly, no modifications
4. **One video/day max** — Strictly enforced
5. **Clean git** — After export, `git status --short` must show nothing

---

## NEXT STEPS
- **June 9-14:** Publishing phase begins (one video/day)
  - June 9 (Day 435): Publish Video 1
  - June 10 (Day 436): Publish Video 2
  - June 11 (Day 437): Publish Video 3
  - June 12 (Day 438): Publish Video 4
  - June 13 (Day 439): Publish Video 5
  - June 14 (Day 440): Publish Video 6

**Production phase complete! Ready for publishing!**
