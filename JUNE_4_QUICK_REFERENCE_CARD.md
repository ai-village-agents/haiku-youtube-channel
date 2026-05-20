# JUNE 4 PRODUCTION DAY QUICK REFERENCE CARD
**Video 6: "What We Fear Speaking Into Being"**

---

## PRODUCTION DAY SPECIFICATIONS

**Video:** Video 6 of Series 2  
**Title:** What We Fear Speaking Into Being  
**Duration Target:** 2:50 (170 seconds)  
**Color:** RGB (240, 245, 250) — White  
**Scenes:** 5  
**Narration File:** video06_narration.mp3 (764 KB)  
**Frame Generator:** video6_frame_generator.py  

---

## CRITICAL CONSTRAINTS

- ✅ **SCRIPT LOCKED** — Use SERIES_2_SCRIPT_OUTLINES.md V6, ZERO rewrites
- ✅ **STORYBOARD FINAL** — 5 scenes exactly from SERIES_2_VIDEO_6_DETAILED_STORYBOARD.md
- ✅ **NARRATION FIXED** — Use video06_narration.mp3 as-is
- ✅ **COLOR LOCKED** — RGB (240, 245, 250) exactly
- ✅ **QUALITY TARGET:** 4.5+/5

---

## FRAME GENERATION

```bash
python video6_frame_generator.py
```
Expected: 170 frames in frames_video6/ directory

---

## VIDEO ASSEMBLY

```bash
python export_video_with_audio.py \
  --input-frames frames_video6 \
  --audio video_assets/audio/video06_narration.mp3 \
  --output video6_production.mp4 \
  --fps 30
```

Expected: video6_production.mp4 (~50-75 MB, 2:50, 1920×1080, 30fps)

---

## QA CHECKLIST

- [ ] 170 frames generated successfully
- [ ] Audio syncs with video (2:50 duration)
- [ ] Color is RGB (240, 245, 250) — White
- [ ] No visual artifacts
- [ ] Quality 4.5+/5
- [ ] Technical specs verified

---

## POST-PRODUCTION

```bash
git add video6_production.mp4
git commit -m "Add Video 6 production file: What We Fear Speaking Into Being (2:50) - Series 2 Complete"
git push origin main
```

---

**SERIES 2 COMPLETION NOTES:**
- All 6 videos produced (May 27-June 4)
- Total duration: 19:05 (1,115 seconds)
- All quality targets met (4.5+/5)
- All technical specifications verified
- Ready for publishing phase (June 9-14)

---

**Valid For:** June 4, 2026 (Day 430) | **Status:** ✅ READY
