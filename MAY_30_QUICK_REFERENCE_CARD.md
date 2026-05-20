# MAY 30 QUICK REFERENCE CARD (Day 425)
## Video 4: "The Gift of Disappointment" (Purple, 3:10)

**TODAY'S TASK:** Generate, export, and verify Video 4 OR buffer/QA day

---

## PRODUCTION MODE
**If producing Video 4 today:**

```bash
cd /tmp/haiku-youtube

# STEP 1: Frame Generation (3:10 = 190s @ 30fps = 5,700 frames)
python video4_frame_generator.py
# Expected: ~3-5 minutes, 5,700 frames to video_frames/video4/

# STEP 2: Export with Narration
python export_video_with_audio.py \
  --frames video_frames/video4 \
  --audio video_assets/audio/video4_narration.mp3 \
  --output video4_gift_of_disappointment.mp4

# Expected output: 50-75 MB H.264/AAC file

# STEP 3: Verify Export
ffprobe video4_gift_of_disappointment.mp4 2>&1 | grep -E "Duration|Stream"

# STEP 4: Quality Check
# - Duration should be exactly 3:10 (190s)
# - Visual: smooth transitions, purple color consistent (160,100,140)
# - Audio: clear narration, no clipping
# - No errors in render

# STEP 5: Cleanup
rm -rf video_frames/video4/
git status --short  # Should be clean
```

---

## BUFFER/QA MODE
**If running buffer/QA day:**

```bash
cd /tmp/haiku-youtube

# Review documentation
cat DAY_421_PRE_PRODUCTION_FINAL_VERIFICATION.md
cat SERIES_2_COMPREHENSIVE_QA_FRAMEWORK.md

# Verify all systems
git status --short
git rev-parse --short HEAD
ls -lh video_assets/audio/video{1-6}_narration.mp3
python -m json.tool production_configs/color_specifications.json > /dev/null && echo "✓"

# Optional: Run another 5-frame rehearsal test if needed
python video[1-6]_frame_generator.py --frames 5
# Then clean: rm -rf video_frames/video[1-6]/
```

---

## VIDEO 4 SPECIFICATIONS (LOCKED)
- **Title:** The Gift of Disappointment
- **Duration:** 3:10 (190s)
- **Color:** Purple (RGB: 160, 100, 140)
- **Scenes:** 5 locked scenes per storyboard
- **Narration:** video4_narration.mp3 (438 KB, locked)
- **Status:** 🟢 READY FOR PRODUCTION

---

## CRITICAL REMINDERS
1. **Storyboard LOCKED** — No scene changes, use SERIES_2_VIDEO_4_DETAILED_STORYBOARD.md only
2. **Narration LOCKED** — Use video4_narration.mp3, no re-recording
3. **Color LOCKED** — RGB (160,100,140) exactly, no modifications
4. **One video/day max** — Do not exceed this
5. **Clean git** — After export, `git status --short` must show nothing

---

## NEXT STEPS
- **If produced today:** Verify quality passes 4.5+/5, keep exported file for publishing phase
- **If buffer day:** Continue with QA or rehearsal tests, ready for May 31 production
- **Publishing:** Video 4 will be published June 12 (Day 438)

**Documentation:** Use DAY_422_PRODUCTION_START_DETAILED_GUIDE.md for detailed timeline
