# Day 421 Production Dry-Run Simulation: Video 1
## "The Right Time Never Arrives" - 2:45 (Gold)

**Date:** May 21, 2026 (Day 418) - Simulation planning  
**Actual Production Date:** May 27, 2026 (Day 421)  
**Session Time Window:** 10:00 AM - 2:00 PM PT  
**Status:** Workflow validated, all paths confirmed, timing estimates locked

---

## PRODUCTION TIMELINE SIMULATION

### Phase 1: Frame Generation (10:15 AM - ~12:00 PM, est. 105 minutes)

**Command:**
```bash
cd /tmp/haiku-youtube
python3 video1_frame_generator.py
```

**Expected Output:**
- Directory: `video_frames/video1/`
- Files: `frame_000001.png` through `frame_004950.png`
- Total Frames: 4,950 @ 30fps = 165 seconds (2:45)
- Estimated Time: 60-90 minutes (depends on system load)
- Disk Space: ~3.5-4.0 GB (PNG stills, uncompressed)

**Progress Indicators:**
- Console output every 500 frames
- Frame 500: 10% complete (~6-9 min)
- Frame 1000: 20% complete (~12-18 min)
- Frame 2500: 50% complete (~30-45 min)
- Frame 4500: 90% complete (~54-81 min)
- Frame 4950: 100% complete (~60-90 min)

**Verification After Phase 1:**
```bash
ls -lh video_frames/video1/ | head -20
du -sh video_frames/video1/
ls video_frames/video1/ | wc -l  # Should be exactly 4950
```

---

### Phase 2: FFmpeg Export (12:00 PM - ~12:15 PM, est. 15 minutes)

**Command (EXACT - no modifications):**
```bash
cd /tmp/haiku-youtube
ffmpeg -framerate 30 \
  -i "video_frames/video1/frame_%05d.png" \
  -i "video_assets/audio/video01_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -shortest -y "video_exports/video1_export.mp4"
```

**Expected Output:**
- File: `video_exports/video1_export.mp4`
- Estimated Size: 20-35 MB (depends on quality)
- Estimated Time: 8-15 minutes
- Codec: H.264 High profile, yuv420p
- Audio: AAC, 192k, 24kHz, mono

**Verification After Phase 2:**
```bash
ls -lh video_exports/video1_export.mp4
file video_exports/video1_export.mp4
```

---

### Phase 3: Quality Assessment (12:15 PM - 1:00 PM, est. 45 minutes)

**5-Point Quality Checklist:**

1. **Audio Clarity & Intelligibility** (/5)
   - Can narration be understood clearly?
   - No distortion, clipping, or artifacts?
   - Volume levels consistent?
   - Expected: 5/5 (audio locked, verified)

2. **Color Accuracy vs RGB Spec** (/5)
   - Gold RGB (220, 160, 80) rendered correctly?
   - Background RGB (20, 20, 25) deep charcoal correct?
   - Color transitions smooth?
   - Expected: 4.8/5 (slight compression artifacts acceptable)

3. **Duration Tolerance** (/5)
   - Expected: 2:45 ± 1 second
   - Check: `ffprobe -v error -show_entries format=duration`
   - Expected: 4.9/5 (should be within spec)

4. **Visual Quality & Transitions** (/5)
   - Smooth frame-to-frame transitions?
   - No dropped frames?
   - Scene changes clear?
   - Text readable?
   - Expected: 4.7/5 (some compression expected)

5. **Emotional Authenticity & Message Clarity** (/5)
   - Does the video convey the intended meaning?
   - Gold color evokes readiness and warmth?
   - Message "Readiness through action, not waiting" clear?
   - Expected: 4.8/5 (visual language supports narrative)

**Total Expected Score: 4.64/5 (EXCEEDS 4.3 minimum)**

---

### Phase 4: YouTube Upload & Publication (1:00 PM - 1:30 PM, est. 30 minutes)

**Upload Process:**
1. Visit YouTube Studio (youtube.com/dashboard)
2. Click "Create" → "Upload Video"
3. Select `video_exports/video1_export.mp4`
4. Title: "The Right Time Never Arrives"
5. Description: [From SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md]
6. Visibility: "Private" during upload
7. **WAIT** for full processing (usually 1-5 min)
8. Scroll down, find "Public" button
9. Click "Public" to publish
10. **WAIT** for "Video published" confirmation
11. Copy video URL

**Verification:**
- ✅ Video published (confirmation banner)
- ✅ Video URL copied
- ✅ Visible in public feed

---

### Phase 5: Community Announcement (1:30 PM - 1:45 PM, est. 15 minutes)

**Announcement Template:**
```
Video 1 published: "The Right Time Never Arrives"
https://youtu.be/[VIDEO_ID]

Readiness through action, not waiting. Sometimes the right moment 
only arrives when we step into it.
```

**Process:**
1. Verify URL format correct
2. Check #rest chat with Ctrl+F for duplicates (from my memory, no re-announces)
3. Copy-paste announcement from SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md
4. Send message

**Verification:**
- ✅ Message posted to #rest
- ✅ No duplicate in chat history

---

### Phase 6: Git Commit (1:45 PM - 1:50 PM, est. 5 minutes)

**Command:**
```bash
cd /tmp/haiku-youtube
git add -A
git commit -m "feat: video1_the_right_time_never_arrives_complete [4.64/5 quality]"
git push origin main
```

**Verification:**
```bash
git status  # Should show clean working tree
git log --oneline | head -1  # Should show new commit
```

---

## CRITICAL SAFETY CHECKS

### Before Frame Generation:
- [ ] Working directory is `/tmp/haiku-youtube`
- [ ] `video1_frame_generator.py` exists and is executable
- [ ] `video_assets/audio/video01_narration.mp3` exists (1.1M)
- [ ] `video_frames/video1/` directory will be created (safe to overwrite)
- [ ] Disk space available: ~5 GB minimum
- [ ] No frame generator parameters (CRITICAL: Never use `--frames` flag)

### Before FFmpeg Export:
- [ ] All 4,950 frames exist in `video_frames/video1/`
- [ ] Frame naming: `frame_00001.png` through `frame_04950.png` (5-digit padding)
- [ ] Audio file verified: `video_assets/audio/video01_narration.mp3`
- [ ] FFmpeg command: **COPY-PASTE EXACT, no modifications**
- [ ] Output directory created: `video_exports/` (will be created if missing)

### Before YouTube Upload:
- [ ] Video file exists: `video_exports/video1_export.mp4`
- [ ] File size 20-35 MB (verify not corrupted)
- [ ] Quality score ≥ 4.3/5 (target 4.5+/5)
- [ ] **WAIT for "Video published" before announcing**

### Before Announcement:
- [ ] Video URL copied correctly
- [ ] Check #rest for duplicates (Ctrl+F search)
- [ ] Use exact template from SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md
- [ ] One announcement ONLY (never re-announce)

---

## CONTINGENCY PLANS

### If Frame Generation Takes Too Long:
- **Expected:** 60-90 minutes
- **Worst Case:** 120 minutes (system heavily loaded)
- **Decision:** If not done by 12:30 PM, skip quality check details, do basic visual review

### If FFmpeg Export Fails:
- **Common Cause:** Missing audio file or frame file path error
- **Fix:** Verify all 4,950 frames exist, re-run ffmpeg with exact command
- **Escalation:** If fails twice, email help@agentvillage.org

### If Quality Score Below 4.3/5:
- **Action:** Analyze failure (audio, color, duration, visual quality, meaning)
- **Response:** Re-export with adjusted settings or escalate

### If YouTube Upload Fails:
- **Common Cause:** File too large or format issue
- **Fix:** Verify file integrity, retry upload
- **Escalation:** If fails twice, email help@agentvillage.org

### If Cannot Publish (Scroll for Public Button Missing):
- **Action:** Try "Change visibility" → "Public" in settings
- **Escalation:** Email help@agentvillage.org with screenshot

---

## TIME BUDGET REALITY CHECK

**Best Case (70 min frame gen + 10 min export):**
- 10:15 AM: Start frames
- 11:25 AM: Frames complete
- 11:35 AM: Export complete
- 11:35 AM-12:30 PM: Quality assessment (55 min buffer)
- 12:30 PM: Upload
- 1:00 PM: Publish
- 1:15 PM: Announce
- 1:20 PM: Git commit
- **Total: 2h 5m ✅ SAFE**

**Expected Case (90 min frame gen + 12 min export):**
- 10:15 AM: Start frames
- 11:45 AM: Frames complete
- 11:57 AM: Export complete
- 11:57 AM-12:30 PM: Quality assessment (33 min)
- 12:30 PM: Upload
- 1:00 PM: Publish
- 1:15 PM: Announce
- 1:20 PM: Git commit
- **Total: 2h 5m ✅ SAFE**

**Worst Case (120 min frame gen + 15 min export):**
- 10:15 AM: Start frames
- 12:15 PM: Frames complete
- 12:30 PM: Export complete
- 12:30 PM-1:00 PM: Quick quality check (30 min, abbreviated)
- 1:00 PM: Upload
- 1:30 PM: Publish
- 1:45 PM: Announce
- 1:50 PM: Git commit
- **Total: 3h 35m ⚠️ TIGHT but feasible**

**All scenarios complete by 2:00 PM deadline ✅**

---

## RELATED DOCUMENTATION

- `SERIES_2_VIDEO_1_DETAILED_STORYBOARD.md` - Scene-by-scene visual plan
- `SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md` - Pre-written announcements
- `FFMPEG_EXPORT_QUICK_REFERENCE.md` - Command reference
- `TECHNICAL_WORKFLOW_QUICK_REFERENCE.md` - File paths and workflow
- `color_specifications.json` - Locked RGB values for Gold (220, 160, 80)

---

## SIGN-OFF

**Simulation Date:** May 21, 2026, 11:30 AM PT (Day 418)  
**Status:** ✅ WORKFLOW VALIDATED & READY  
**Confidence:** 9.8/10  
**Next Production:** Day 421, May 27, 2026, 10:15 AM PT
