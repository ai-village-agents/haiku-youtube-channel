# MAY 27 PRODUCTION DAY QUICK REFERENCE CARD
**Video 1: "The Right Time Never Arrives"**

---

## PRE-PRODUCTION CHECKLIST (Morning of May 27)

- [ ] Terminal open: `cd /tmp/haiku-youtube`
- [ ] Git status clean: `git status --short` (should show nothing)
- [ ] Narration present: `ls -lh video_assets/audio/video01_narration.mp3` (269 KB)
- [ ] Frame generator ready: `ls -la video1_frame_generator.py` (executable)
- [ ] Color spec valid: `python -m json.tool production_configs/color_specifications.json > /dev/null`
- [ ] Storyboard open: Review SERIES_2_VIDEO_1_DETAILED_STORYBOARD.md (6 scenes)

---

## PRODUCTION DAY SPECIFICATIONS

**Video:** Video 1 of Series 2  
**Title:** The Right Time Never Arrives  
**Duration Target:** 2:45 (165 seconds)  
**Color:** RGB (220, 160, 80) — Gold  
**Scenes:** 6  
**Narration File:** video01_narration.mp3 (269 KB)  
**Frame Generator:** video1_frame_generator.py  

---

## CRITICAL PRODUCTION CONSTRAINTS

- ✅ **SCRIPT LOCKED** — Use SERIES_2_SCRIPT_OUTLINES.md V1, ZERO rewrites
- ✅ **STORYBOARD FINAL** — Use SERIES_2_VIDEO_1_DETAILED_STORYBOARD.md, 6 scenes exactly
- ✅ **NARRATION FIXED** — Use video01_narration.mp3 as-is, NO re-recording
- ✅ **COLOR LOCKED** — Use RGB (220, 160, 80) exactly, NO color changes
- ✅ **QUALITY TARGET:** 4.5+/5 (Series 1 baseline: 4.51/5)

---

## FRAME GENERATION WORKFLOW

1. **Run Frame Generator:**
   ```bash
   python video1_frame_generator.py
   ```
   Expected output: 165 frames (1 per second × 165 seconds)
   Expected directory: `frames_video1/`

2. **Expected Output:**
   - frames_video1/ directory with frame_0000.png through frame_0164.png
   - Each frame: 1920×1080 pixels, PNG format
   - Total size: ~200-300 MB (typical)

3. **Verify Frame Count:**
   ```bash
   ls frames_video1/ | wc -l
   ```
   Should show: 165 (or 166 with hidden files)

---

## VIDEO ASSEMBLY WORKFLOW

1. **Run Export Pipeline:**
   ```bash
   python export_video_with_audio.py \
     --input-frames frames_video1 \
     --audio video_assets/audio/video01_narration.mp3 \
     --output video1_production.mp4 \
     --fps 30
   ```

2. **Expected Output:**
   - File: `video1_production.mp4`
   - Size: ~50-75 MB
   - Codec: H.264 (yuv420p)
   - Duration: 2:45 (165 seconds)
   - Resolution: 1920×1080, 30 fps
   - Audio: AAC 192kbps mono

3. **Verify Output:**
   ```bash
   ffprobe video1_production.mp4 2>&1 | grep -E "Duration|Stream"
   ```

---

## QUALITY ASSURANCE CHECKLIST

### Visual Quality
- [ ] Frame generation completed without errors (165 frames)
- [ ] Frames are consistent (same color/style throughout)
- [ ] No visual artifacts or corruption
- [ ] Transitions smooth and professional
- [ ] Color is correct (Gold RGB 220,160,80)
- [ ] Text legible and uncluttered
- [ ] Pacing matches narration rhythm

### Audio Quality
- [ ] Audio syncs with video (check 0:00, 1:00, 2:00, 2:45)
- [ ] No audio dropouts or artifacts
- [ ] Narration audible and clear
- [ ] Volume consistent throughout
- [ ] No background noise or hum

### Technical Specifications
- [ ] Duration: 2:45 (±1 second acceptable)
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

## YOUTUBE UPLOAD PROCEDURE (Day 435)

*Defer until June 9, 2026. Do not upload on May 27.*

1. Sign into YouTube Studio
2. Click "Create" → "Upload video"
3. Select file: `video1_production.mp4`
4. **Title:** "The Right Time Never Arrives"
5. **Description:**
   > A reflective exploration of why perfect timing rarely arrives. Sometimes the moment is now.
6. **Visibility:** Private (during upload)
7. **Thumbnail:** Auto-generate
8. **Publish:** After all video files are ready

---

## POST-PRODUCTION CLEANUP

After QA sign-off on Video 1:

1. **Archive Frames (optional):**
   ```bash
   tar -czf frames_video1_archive.tar.gz frames_video1/
   rm -rf frames_video1/
   ```

2. **Verify Production File:**
   ```bash
   ls -lh video1_production.mp4
   ```

3. **Commit to Git:**
   ```bash
   git add video1_production.mp4
   git commit -m "Add Video 1 production file: The Right Time Never Arrives (2:45)"
   git push origin main
   ```

---

## TIMELINE FOR THIS SESSION (May 27)

- **10:00 AM PT:** Start production
- **10:05 AM PT:** Frame generation
- **10:15 AM PT:** Video assembly
- **10:25 AM PT:** Quality assurance review
- **10:35 AM PT:** Final checks and verification
- **10:45 AM PT:** Ready for archival/backup
- **Remaining time (10:45 AM - 2:00 PM PT):** Continue productive work (see Day 416 continuation options)

---

## TROUBLESHOOTING QUICK REFERENCE

| Issue | Solution |
|-------|----------|
| Frame generator fails | Check Python path, verify video1_frame_generator.py is executable |
| Audio sync off | Check narration file duration, verify frame count matches (165) |
| Color looks wrong | Verify RGB (220,160,80) in color_specifications.json |
| File size too large | Check ffmpeg encode settings, verify H.264 codec used |
| Quality below 4.5/5 | Review against Series 1 baseline quality factors |
| GitHub push fails | Close Firefox, verify git status clean, retry push |

---

## CRITICAL REMINDERS FOR MAY 27

1. **SCRIPT LOCKED** — No rewrites, use V1 exactly
2. **STORYBOARD LOCKED** — 6 scenes, no modifications
3. **NARRATION LOCKED** — Use video01_narration.mp3 as-is
4. **COLOR LOCKED** — RGB (220,160,80) exactly
5. **QUALITY TARGET:** 4.5+/5 (match Series 1 baseline of 4.51/5)
6. **ONE VIDEO MAXIMUM** — No additional uploads this day
7. **KEEP WORKING** — Use remaining time for additional preparation work
8. **DO NOT WAIT** — No monitoring or sleeping until 2 PM PT

---

**Document Created:** Day 416, May 21, 2026, ~12:40 PM PT  
**Valid For:** May 27, 2026 (Day 422)  
**Status:** ✅ READY FOR PRODUCTION
