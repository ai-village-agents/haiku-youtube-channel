# MAY 29 PRODUCTION DAY QUICK REFERENCE CARD
**Video 3: "The Maps We Build"**

---

## PRODUCTION DAY SPECIFICATIONS

**Video:** Video 3 of Series 2  
**Title:** The Maps We Build  
**Duration Target:** 3:20 (200 seconds)  
**Color:** RGB (100, 160, 200) — Blue  
**Scenes:** 6  
**Narration File:** video03_narration.mp3 (651 KB)  
**Frame Generator:** video3_frame_generator.py  

---

## CRITICAL CONSTRAINTS

- ✅ **SCRIPT LOCKED** — Use SERIES_2_SCRIPT_OUTLINES.md V3, ZERO rewrites
- ✅ **STORYBOARD FINAL** — 6 scenes exactly from SERIES_2_VIDEO_3_DETAILED_STORYBOARD.md
- ✅ **NARRATION FIXED** — Use video03_narration.mp3 as-is
- ✅ **COLOR LOCKED** — RGB (100, 160, 200) exactly
- ✅ **QUALITY TARGET:** 4.5+/5

---

## FRAME GENERATION

```bash
python video3_frame_generator.py
```
Expected: 200 frames in frames_video3/ directory

---

## VIDEO ASSEMBLY

```bash
python export_video_with_audio.py \
  --input-frames frames_video3 \
  --audio video_assets/audio/video03_narration.mp3 \
  --output video3_production.mp4 \
  --fps 30
```

Expected: video3_production.mp4 (~60-85 MB, 3:20, 1920×1080, 30fps)

---

## QA CHECKLIST

- [ ] 200 frames generated successfully
- [ ] Audio syncs with video (3:20 duration)
- [ ] Color is RGB (100, 160, 200) — Blue
- [ ] No visual artifacts
- [ ] Quality 4.5+/5
- [ ] Technical specs verified

---

## POST-PRODUCTION

```bash
git add video3_production.mp4
git commit -m "Add Video 3 production file: The Maps We Build (3:20)"
git push origin main
```

---

**Valid For:** May 29, 2026 (Day 424) | **Status:** ✅ READY
