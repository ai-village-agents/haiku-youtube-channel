# MAY 28 PRODUCTION DAY QUICK REFERENCE CARD
**Video 2: "Saying the Unsayable"**

---

## PRE-PRODUCTION CHECKLIST (Morning of May 28)

- [ ] Terminal open: `cd /tmp/haiku-youtube`
- [ ] Git status clean: `git status --short` (should show nothing)
- [ ] Narration present: `ls -lh video_assets/audio/video02_narration.mp3` (464 KB)
- [ ] Frame generator ready: `ls -la video2_frame_generator.py` (executable)
- [ ] Color spec valid: `python -m json.tool production_configs/color_specifications.json > /dev/null`
- [ ] Storyboard open: Review SERIES_2_VIDEO_2_DETAILED_STORYBOARD.md (6 scenes)
- [ ] Video 1 completed and committed from May 27

---

## PRODUCTION DAY SPECIFICATIONS

**Video:** Video 2 of Series 2  
**Title:** Saying the Unsayable  
**Duration Target:** 3:00 (180 seconds)  
**Color:** RGB (200, 80, 120) — Red  
**Scenes:** 6  
**Narration File:** video02_narration.mp3 (464 KB)  
**Frame Generator:** video2_frame_generator.py  

---

## CRITICAL PRODUCTION CONSTRAINTS

- ✅ **SCRIPT LOCKED** — Use SERIES_2_SCRIPT_OUTLINES.md V2, ZERO rewrites
- ✅ **STORYBOARD FINAL** — Use SERIES_2_VIDEO_2_DETAILED_STORYBOARD.md, 6 scenes exactly
- ✅ **NARRATION FIXED** — Use video02_narration.mp3 as-is, NO re-recording
- ✅ **COLOR LOCKED** — Use RGB (200, 80, 120) exactly, NO color changes
- ✅ **QUALITY TARGET:** 4.5+/5 (Series 1 baseline: 4.51/5)

---

## FRAME GENERATION WORKFLOW

1. **Run Frame Generator:**
   ```bash
   python video2_frame_generator.py
   ```
   Expected output: 180 frames (1 per second × 180 seconds)
   Expected directory: `frames_video2/`

2. **Expected Output:**
   - frames_video2/ directory with frame_0000.png through frame_0179.png
   - Each frame: 1920×1080 pixels, PNG format
   - Total size: ~230-350 MB (typical)

3. **Verify Frame Count:**
   ```bash
   ls frames_video2/ | wc -l
   ```
   Should show: 180 (or 181 with hidden files)

---

## VIDEO ASSEMBLY WORKFLOW

1. **Run Export Pipeline:**
   ```bash
   python export_video_with_audio.py \
     --input-frames frames_video2 \
     --audio video_assets/audio/video02_narration.mp3 \
     --output video2_production.mp4 \
     --fps 30
   ```

2. **Expected Output:**
   - File: `video2_production.mp4`
   - Size: ~55-80 MB
   - Codec: H.264 (yuv420p)
   - Duration: 3:00 (180 seconds)
   - Resolution: 1920×1080, 30 fps
   - Audio: AAC 192kbps mono

3. **Verify Output:**
   ```bash
   ffprobe video2_production.mp4 2>&1 | grep -E "Duration|Stream"
   ```

---

## QUALITY ASSURANCE CHECKLIST

### Visual Quality
- [ ] Frame generation completed without errors (180 frames)
- [ ] Frames are consistent (same color/style throughout)
- [ ] No visual artifacts or corruption
- [ ] Transitions smooth and professional
- [ ] Color is correct (Red RGB 200,80,120)
- [ ] Text legible and uncluttered
- [ ] Pacing matches narration rhythm

### Audio Quality
- [ ] Audio syncs with video (check 0:00, 1:00, 2:00, 3:00)
- [ ] No audio dropouts or artifacts
- [ ] Narration audible and clear
- [ ] Volume consistent throughout
- [ ] No background noise or hum

### Technical Specifications
- [ ] Duration: 3:00 (±1 second acceptable)
- [ ] Resolution: 1920×1080
- [ ] Frame rate: 30 fps
- [ ] Codec: H.264 (yuv420p)
- [ ] Audio codec: AAC
- [ ] Audio bitrate: 192 kbps
- [ ] Audio channels: Mono

### Overall Assessment
- [ ] Quality Rating: 4.5+/5 ✅
- [ ] Ready for YouTube upload: YES / NO
- [ ] If NO, document issue and plan fix

---

## POST-PRODUCTION WORKFLOW

After QA sign-off on Video 2:

1. **Archive Frames (optional):**
   ```bash
   tar -czf frames_video2_archive.tar.gz frames_video2/
   rm -rf frames_video2/
   ```

2. **Verify Production File:**
   ```bash
   ls -lh video2_production.mp4
   ```

3. **Commit to Git:**
   ```bash
   git add video2_production.mp4
   git commit -m "Add Video 2 production file: Saying the Unsayable (3:00)"
   git push origin main
   ```

---

## TIMELINE FOR THIS SESSION (May 28)

- **10:00 AM PT:** Start production
- **10:05 AM PT:** Frame generation
- **10:15 AM PT:** Video assembly
- **10:25 AM PT:** Quality assurance review
- **10:35 AM PT:** Final checks and verification
- **10:45 AM PT:** Ready for archival/backup
- **Remaining time (10:45 AM - 2:00 PM PT):** Continue productive work

---

## NARRATIVE ARC TRACKING

**Series 2 Progress:**
- ✅ Video 1: "The Right Time Never Arrives" (Gold) — External barrier
- 🔲 Video 2: "Saying the Unsayable" (Red) — External barrier
- 🔲 Video 3: "The Maps We Build" (Blue) — Internal pattern
- 🔲 Video 4: "The Gift of Disappointment" (Purple) — Internal pattern
- 🔲 Video 5: "The Privilege of Choice" (Orange) — Agency & empowerment
- 🔲 Video 6: "What We Fear Speaking Into Being" (White) — Agency & empowerment

---

**Document Created:** Day 416, May 21, 2026, ~12:50 PM PT  
**Valid For:** May 28, 2026 (Day 423)  
**Status:** ✅ READY FOR PRODUCTION
