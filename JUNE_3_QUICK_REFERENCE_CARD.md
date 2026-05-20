# JUNE 3 PRODUCTION DAY QUICK REFERENCE CARD
**Video 5: "The Privilege of Choice"**

---

## PRODUCTION DAY SPECIFICATIONS

**Video:** Video 5 of Series 2  
**Title:** The Privilege of Choice  
**Duration Target:** 3:30 (210 seconds)  
**Color:** RGB (220, 140, 60) — Orange  
**Scenes:** 6  
**Narration File:** video05_narration.mp3 (661 KB)  
**Frame Generator:** video5_frame_generator.py  

---

## CRITICAL CONSTRAINTS

- ✅ **SCRIPT LOCKED** — Use SERIES_2_SCRIPT_OUTLINES.md V5, ZERO rewrites
- ✅ **STORYBOARD FINAL** — 6 scenes exactly from SERIES_2_VIDEO_5_DETAILED_STORYBOARD.md
- ✅ **NARRATION FIXED** — Use video05_narration.mp3 as-is
- ✅ **COLOR LOCKED** — RGB (220, 140, 60) exactly
- ✅ **QUALITY TARGET:** 4.5+/5

---

## FRAME GENERATION

```bash
python video5_frame_generator.py
```
Expected: 210 frames in frames_video5/ directory

---

## VIDEO ASSEMBLY

```bash
python export_video_with_audio.py \
  --input-frames frames_video5 \
  --audio video_assets/audio/video05_narration.mp3 \
  --output video5_production.mp4 \
  --fps 30
```

Expected: video5_production.mp4 (~60-85 MB, 3:30, 1920×1080, 30fps)

---

## QA CHECKLIST

- [ ] 210 frames generated successfully
- [ ] Audio syncs with video (3:30 duration)
- [ ] Color is RGB (220, 140, 60) — Orange
- [ ] No visual artifacts
- [ ] Quality 4.5+/5
- [ ] Technical specs verified

---

## POST-PRODUCTION

```bash
git add video5_production.mp4
git commit -m "Add Video 5 production file: The Privilege of Choice (3:30)"
git push origin main
```

---

**Valid For:** June 3, 2026 (Day 429) | **Status:** ✅ READY
