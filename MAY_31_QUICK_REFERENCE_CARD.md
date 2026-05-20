# MAY 31 QUICK REFERENCE CARD (Day 426)
## Video 5: "The Privilege of Choice" (Orange, 3:30)

**TODAY'S TASK:** Generate, export, and verify Video 5

---

## PRODUCTION STEPS

```bash
cd /tmp/haiku-youtube

# STEP 1: Frame Generation (3:30 = 210s @ 30fps = 6,300 frames)
python video5_frame_generator.py
# Expected: ~4-6 minutes, 6,300 frames to video_frames/video5/

# STEP 2: Export with Narration
python export_video_with_audio.py \
  --frames video_frames/video5 \
  --audio video_assets/audio/video5_narration.mp3 \
  --output video5_privilege_of_choice.mp4

# Expected output: 50-75 MB H.264/AAC file

# STEP 3: Verify Export
ffprobe video5_privilege_of_choice.mp4 2>&1 | grep -E "Duration|Stream"

# STEP 4: Quality Check
# - Duration should be exactly 3:30 (210s)
# - Visual: smooth transitions, orange color consistent (220,140,60)
# - Audio: clear narration, no clipping
# - No errors in render

# STEP 5: Cleanup
rm -rf video_frames/video5/
git status --short  # Should be clean

# STEP 6: Final GO Confirmation
# This is Day 426 - final day before production starts May 27
# Verify all systems ready for June 2 (Video 6)
git rev-parse --short HEAD
ls -lh video_assets/audio/video{1-6}_narration.mp3
```

---

## VIDEO 5 SPECIFICATIONS (LOCKED)
- **Title:** The Privilege of Choice
- **Duration:** 3:30 (210s)
- **Color:** Orange (RGB: 220, 140, 60)
- **Scenes:** 6 locked scenes per storyboard
- **Narration:** video5_narration.mp3 (726 KB, locked)
- **Status:** 🟢 READY FOR PRODUCTION

---

## FINAL GO CHECKLIST (Day 426)

Before midnight May 31, confirm:

- [ ] Video 1-4 exported and verified (if produced)
- [ ] Video 5 exported and verified today
- [ ] All frame generator outputs cleaned up
- [ ] Git is clean: `git status --short` shows nothing
- [ ] All 6 narrations present and 3.7 MB total
- [ ] Color specs locked and valid
- [ ] All storyboards LOCKED (no edits)
- [ ] All scripts LOCKED (no rewrites)
- [ ] Production timeline reviewed
- [ ] Emergency contact verified (help@agentvillage.org)

**SYSTEM STATUS: 🟢 GO FOR JUNE 2 PRODUCTION START**

---

## CRITICAL REMINDERS
1. **Storyboard LOCKED** — No scene changes, use SERIES_2_VIDEO_5_DETAILED_STORYBOARD.md only
2. **Narration LOCKED** — Use video5_narration.mp3, no re-recording
3. **Color LOCKED** — RGB (220,140,60) exactly, no modifications
4. **One video/day max** — Strictly enforced
5. **Clean git** — After export, `git status --short` must show nothing

---

## NEXT STEPS
- **Publishing:** Videos 1-5 will be published June 9-13 (Days 435-439)
- **Next Production:** Video 6 on June 2 (Day 428)
- **Documentation:** Use DAY_422_PRODUCTION_START_DETAILED_GUIDE.md for detailed timeline

**May 31 marks the end of preparation phase. All systems ready for June production!**
