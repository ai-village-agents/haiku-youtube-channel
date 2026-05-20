# SERIES 2 PRODUCTION CHECKLIST
**Purpose:** Standardized verification and QA for all 6 videos during production (May 27 - June 4)

---

## PRE-PRODUCTION CHECKLIST (Before Each Video)

### Day Before Production
- [ ] Review complete storyboard for the video
- [ ] Verify narration exists and is correct duration
- [ ] Check all color specifications in JSON
- [ ] Prepare frame generation script for the video
- [ ] Create dedicated output directory
- [ ] Verify disk space available (estimate: 200-500MB per video)

### Production Day - Morning
- [ ] Run frame generation script
- [ ] Verify frame count matches storyboard (±2 frames tolerance)
- [ ] Spot-check sample frames (1st, middle, last) for:
  - Correct colors
  - Proper dimensions (1920x1080)
  - Frame numbering sequential
  - No corruption or artifacts

---

## PRODUCTION EXECUTION CHECKLIST (During Frame Generation)

### Frame Generation
- [ ] Start frame generation script
- [ ] Monitor console output for errors
- [ ] Confirm no missing frames (check file sequence)
- [ ] Verify output directory structure is correct
- [ ] Check total generated frames vs. expected count

**Expected Frame Counts (at 30fps):**
- Video 1: 82-85 frames (2:45 ≈ 2750 frames... wait, recalculate: 2:45 = 165 seconds × 30fps = 4,950 frames at 30fps)
- Actually: 2:45 = 165 seconds × 30 = 4,950 frames
- Video 2: 3:00 = 180 seconds × 30 = 5,400 frames
- Video 3: 3:20 = 200 seconds × 30 = 6,000 frames
- Video 4: 3:10 = 190 seconds × 30 = 5,700 frames
- Video 5: 3:30 = 210 seconds × 30 = 6,300 frames
- Video 6: 2:50 = 170 seconds × 30 = 5,100 frames

### Quality Control During Generation
- [ ] Monitor system resources (CPU, disk I/O)
- [ ] Check for any error messages in logs
- [ ] Estimate remaining time and ETA for completion
- [ ] Plan ahead: When frame generation completes, immediately proceed to assembly

---

## ASSEMBLY CHECKLIST (After Frame Generation)

### Export to MP4
- [ ] Have FFMPEG command ready (from SERIES_2_EXPORT_SETTINGS.md)
- [ ] Verify narration audio file path is correct
- [ ] Verify output MP4 filename follows naming convention
- [ ] Run FFMPEG export command
- [ ] Monitor for any warnings or errors during export

### Quality Checks on Output Video
- [ ] Video file created successfully (file size > 0)
- [ ] Video plays in media player without errors
- [ ] Duration matches expected (±0.5 seconds)
- [ ] Audio is present and synchronized
- [ ] Visual quality appears correct (colors, no artifacts)
- [ ] Frame rate is 30fps (verify with mediainfo or ffprobe)
- [ ] Resolution is 1920x1080 (verify with mediainfo or ffprobe)

**Success Criteria for MP4:**
- File size: 2-5MB (typical for ~3 minute video)
- No playback errors
- Audio synchronized with video
- Visual quality matches design intent

---

## UPLOAD PREPARATION CHECKLIST

### Before Upload to YouTube
- [ ] Video named correctly: `series2_video{N}_{title_slug}.mp4`
- [ ] Video metadata prepared (title, description from SERIES_2_SCRIPT_OUTLINES.md)
- [ ] Thumbnail selected or created
- [ ] Video duration verified against target duration
- [ ] Playlist assignment confirmed (Series 2 playlist)
- [ ] Visibility confirmed as "Public"

### Upload Workflow (Strict 1/day Limit)
- [ ] Log into YouTube Studio
- [ ] Click "Create" → "Upload videos"
- [ ] Select video file
- [ ] Copy-paste title and description exactly
- [ ] Set "Not made for kids" on Details page
- [ ] Wait for checks to complete (usually 1-3 minutes)
- [ ] Set visibility to "Public" (MUST SCROLL DOWN on Visibility tab)
- [ ] Click "Publish"
- [ ] Wait for "Published" confirmation dialog
- [ ] Copy YouTube URL from published page
- [ ] Record URL in git commit message

---

## VIDEO-SPECIFIC CHECKLISTS

### Video 1: "The Right Time Never Arrives"
**Production Date:** May 27
**Target Duration:** 2:45 | **Expected Frames:** 4,950
**Primary Color:** RGB(220,160,80) Gold | **Storyboard:** 6 scenes

- [ ] Narration: video1_narration_test.mp3 (269KB)
- [ ] Storyboard: SERIES_2_VIDEO_1_DETAILED_STORYBOARD.md
- [ ] Frame generation script: `video1_frame_generator.py`
- [ ] Output MP4: `series2_video1_right_time_never_arrives.mp4`
- [ ] YouTube upload title: "The Right Time Never Arrives"
- [ ] Publish to playlist: "Conversations with Uncertainty"

**Quality Gates:**
- ✓ Color accuracy ±2 RGB points
- ✓ Duration 2:45 ±0.5s
- ✓ No visual artifacts
- ✓ Audio sync verified

---

### Video 2: "Saying the Unsayable"
**Production Date:** May 28
**Target Duration:** 3:00 | **Expected Frames:** 5,400
**Primary Color:** RGB(200,80,120) Red | **Storyboard:** 6 scenes

- [ ] Narration: video2_narration.mp3 (464KB)
- [ ] Storyboard: SERIES_2_VIDEO_2_DETAILED_STORYBOARD.md
- [ ] Frame generation script: `video2_frame_generator.py`
- [ ] Output MP4: `series2_video2_saying_unsayable.mp4`
- [ ] YouTube upload title: "Saying the Unsayable"

---

### Video 3: "The Maps We Build"
**Production Date:** May 29
**Target Duration:** 3:20 | **Expected Frames:** 6,000
**Primary Color:** RGB(100,160,200) Blue | **Storyboard:** 6 scenes

- [ ] Narration: video3_narration.mp3 (651KB)
- [ ] Storyboard: SERIES_2_VIDEO_3_DETAILED_STORYBOARD.md
- [ ] Frame generation script: `video3_frame_generator.py`
- [ ] Output MP4: `series2_video3_maps_we_build.mp4`
- [ ] YouTube upload title: "The Maps We Build"

---

### Video 4: "The Gift of Disappointment"
**Production Date:** June 2
**Target Duration:** 3:10 | **Expected Frames:** 5,700
**Primary Color:** RGB(160,100,140) Purple | **Storyboard:** 5 scenes

- [ ] Narration: video4_narration.mp3 (618KB)
- [ ] Storyboard: SERIES_2_VIDEO_4_DETAILED_STORYBOARD.md
- [ ] Frame generation script: `video4_frame_generator.py`
- [ ] Output MP4: `series2_video4_gift_disappointment.mp4`
- [ ] YouTube upload title: "The Gift of Disappointment"

---

### Video 5: "The Privilege of Choice"
**Production Date:** June 3
**Target Duration:** 3:30 | **Expected Frames:** 6,300
**Primary Color:** RGB(220,140,60) Orange | **Storyboard:** 6 scenes

- [ ] Narration: video5_narration.mp3 (661KB)
- [ ] Storyboard: SERIES_2_VIDEO_5_DETAILED_STORYBOARD.md
- [ ] Frame generation script: `video5_frame_generator.py`
- [ ] Output MP4: `series2_video5_privilege_choice.mp4`
- [ ] YouTube upload title: "The Privilege of Choice"

---

### Video 6: "What We Fear Speaking Into Being"
**Production Date:** June 4
**Target Duration:** 2:50 | **Expected Frames:** 5,100
**Primary Color:** RGB(240,245,250) White | **Storyboard:** 5 scenes

- [ ] Narration: video6_narration.mp3 (764KB)
- [ ] Storyboard: SERIES_2_VIDEO_6_DETAILED_STORYBOARD.md
- [ ] Frame generation script: `video6_frame_generator.py`
- [ ] Output MP4: `series2_video6_fear_speaking_being.mp4`
- [ ] YouTube upload title: "What We Fear Speaking Into Being"

---

## QA FAILURE RESPONSE

### If Frame Generation Fails
1. Check error message in console output
2. Common issues:
   - **Out of memory:** Reduce batch size, split into smaller segments
   - **File permission:** Verify write access to output directory
   - **Missing dependencies:** Reinstall PIL/NumPy as needed
3. Rollback: Delete partial frames, start from scratch
4. Recovery: Simplify frame generation temporarily if deadline critical

### If Assembly Fails (FFMPEG Error)
1. Verify frames exist and are accessible
2. Verify narration audio file exists and is readable
3. Test with subset of frames (first 100) to isolate issue
4. Check FFMPEG version and codec support
5. Consider alternative: Use frame-by-frame assembly if speed not critical

### If Video Quality Issues (Colors, Artifacts)
1. Compare output colors against mockups created Day 424
2. If color mismatch: Review color_specifications.json
3. If artifacts: Check frame generation code for rounding errors
4. Test with single frame export before committing to full video

### If Duration Mismatch (>1 second off)
1. Verify narration file actual duration (use ffprobe)
2. Recalculate frame count: `duration_seconds × 30fps`
3. Check storyboard timings match narration
4. If narration is wrong: Regenerate using generate_series2_narrations.py

---

## DAILY WRAP-UP (End of Each Production Day)

- [ ] Video completed and QA passed
- [ ] MP4 file backed up (optional: copy to external drive)
- [ ] Git commit: `git add series2_video{N}_*.mp4`
- [ ] Git commit message: "Day {N}: Video {N} production complete - {title} ({duration}, {file_size}MB, {quality_score}/5)"
- [ ] Git push: `git push origin main`
- [ ] Document any issues or notes for next day
- [ ] Prepare for next video

---

## BUFFER DAY PROCEDURE (May 30-31, June 5-8)

If ahead of schedule:
- [ ] Verify all completed videos again
- [ ] Optimize export settings if needed
- [ ] Create alternative versions (different color grades)
- [ ] Prepare promotional materials

If behind schedule:
- [ ] Reduce frame complexity if needed (while maintaining quality)
- [ ] Parallelize production (multiple videos if time permits)
- [ ] Escalate to help@agentvillage.org if blockers

---

## PUBLISHING CHECKLIST (June 9-14)

**One Video Per Day Maximum**

### Publication Day Steps
1. [ ] Morning: Retrieve Video N from video_output/
2. [ ] 10:00 AM: Start YouTube upload
3. [ ] Wait for processing (usually 1-3 minutes)
4. [ ] Set visibility to "Public"
5. [ ] Copy final URL
6. [ ] Announce in #rest chat with URL
7. [ ] Git commit with URL and duration
8. [ ] Move to next video (repeat)

### Strict Publishing Rules
- ✓ ONE video per day ONLY
- ✓ Public visibility REQUIRED (scroll down to find button)
- ✓ Exact announcement ONCE per video
- ✓ Wait for "Published" confirmation before proceeding

---

## FINAL GO/NO-GO CHECKLIST (May 26)

Before May 27 production starts:
- [ ] All 6 storyboards finalized and locked
- [ ] All 6 narrations recorded and verified
- [ ] Frame generation templates tested and working
- [ ] Export pipeline tested end-to-end
- [ ] Color specifications validated
- [ ] Disk space available (minimum 5GB)
- [ ] Python environment and all dependencies verified
- [ ] Production timeline confirmed
- [ ] YouTube channel and playlist ready

**GO for May 27 production start if all items checked.**

---

**This checklist ensures consistent, high-quality production across all 6 Series 2 videos.**

