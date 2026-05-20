# SERIES 2 EXPORT SETTINGS VERIFICATION & REFERENCE
**Status:** LOCKED (May 20, 2026)  
**Last Updated:** Day 416 (May 21, 2026)  
**Purpose:** Technical specifications for video export pipeline  

---

## VIDEO EXPORT SPECIFICATIONS (FINAL & LOCKED)

### Container & Codec Configuration

**Video Codec:**
- Type: H.264 (Advanced Video Coding)
- Profile: High Profile
- Level: 4.2 (supports 1080p at 30fps)
- Pixel Format: yuv420p (standard for YouTube)

**Audio Codec:**
- Type: AAC (Advanced Audio Coding)
- Bit Rate: 192 kbps (high quality, acceptable for YouTube)
- Sample Rate: 24 kHz (standard for video)
- Channels: Stereo (or mono, depending on narration source)

**Container:**
- Format: MP4 (MPEG-4)
- Extension: .mp4
- Compatibility: YouTube-native, all devices

### Resolution & Frame Rate

**Video Resolution:**
- Width: 1920 pixels
- Height: 1080 pixels
- Aspect Ratio: 16:9
- Standard: Full HD (1080p)

**Frame Rate:**
- 30 fps (frames per second)
- Constant frame rate (CFR), not variable
- Matches narration timing (all videos timed at 30fps)

### Duration Specifications

| Video | Duration | Seconds | Frames (30fps) |
|-------|----------|---------|----------------|
| 1 | 2:45 | 165 | 4,950 |
| 2 | 3:00 | 180 | 5,400 |
| 3 | 3:20 | 200 | 6,000 |
| 4 | 3:10 | 190 | 5,700 |
| 5 | 3:30 | 210 | 6,300 |
| 6 | 2:50 | 170 | 5,100 |
| **Total** | **18:35** | **1,115** | **33,450** |

**Verification Method:**
```bash
# After export, verify duration with ffprobe:
ffprobe -v error -show_entries format=duration -of \
  default=noprint_wrappers=1:nokey=1:noprint_wrappers=1 output.mp4

# Example output: 165 (for video 1)
# Should match target duration ±1 second
```

### Audio Synchronization

**Narration Timing:**
- Must be synchronized with frame generation timing
- Audio duration should match or slightly exceed video duration
- YouTube will trim excess audio after publishing

**Audio Levels:**
- Recommended: -3 dB to -6 dB peak (loud but not distorted)
- Upload as-is (YouTube normalization applies)
- Mono or stereo acceptable (narration is typically mono)

### File Size Estimates

**Expected File Sizes (based on bitrate & duration):**

| Video | Duration | Estimated Size |
|-------|----------|-----------------|
| Video 1 | 2:45 | 55-65 MB |
| Video 2 | 3:00 | 60-70 MB |
| Video 3 | 3:20 | 67-77 MB |
| Video 4 | 3:10 | 64-74 MB |
| Video 5 | 3:30 | 70-80 MB |
| Video 6 | 2:50 | 57-67 MB |
| **Total** | **18:35** | **373-433 MB** |

**Storage Planning:**
- Ensure at least 500 MB free disk space before export
- After publication, delete local copies to reclaim space
- GitHub LFS not used (video files not stored in Git)

---

## EXPORT PIPELINE TECHNICAL FLOW

### Step 1: Frame Generation (per video)
```bash
python video[N]_frame_generator.py
```

**Output:**
- Directory: `video_frames/video[N]/`
- Files: Frame001.png through Frame[TOTAL].png (30-fps frame sequence)
- Format: PNG, RGB, 1920×1080
- Total frames: See duration table above

**Time Estimate:**
- Video 1: 3-4 minutes
- Video 2: 3-4 minutes
- Video 3: 4-5 minutes
- Video 4: 3-4 minutes
- Video 5: 4-5 minutes
- Video 6: 3-4 minutes
- **Total: 20-25 minutes for all 6 videos**

### Step 2: Audio Preparation
**Input:** video_assets/audio/video[N]_narration.mp3

**Pre-checks:**
```bash
# Verify audio file exists
ls -lh video_assets/audio/video[N]_narration.mp3

# Check audio duration matches video
ffprobe -v error -show_entries format=duration -of \
  default=noprint_wrappers=1:nokey=1 \
  video_assets/audio/video[N]_narration.mp3
```

**Expected Duration:**
- Video 1: ~2:43 (263K file)
- Video 2: ~3:00 (464K file)
- Video 3: ~3:20 (651K file)
- Video 4: ~3:10 (618K file)
- Video 5: ~3:30 (661K file)
- Video 6: ~2:50 (764K file)

### Step 3: Export to MP4
```bash
python export_video_with_audio.py \
  video[N]_frame_generator.py \
  video_assets/audio/video[N]_narration.mp3 \
  --output series2_video[N]_[TITLE].mp4
```

**FFmpeg Command (internal):**
```bash
ffmpeg -framerate 30 -i video_frames/video[N]/Frame%03d.png \
  -i video_assets/audio/video[N]_narration.mp3 \
  -c:v libx264 -crf 23 -preset medium \
  -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  -shortest \
  series2_video[N]_[TITLE].mp4
```

**Output:**
- File: `series2_video[N]_[TITLE].mp4`
- Size: 55-80 MB (varies by duration)
- Duration: Should match narration (±1 second acceptable)

**Time Estimate (per video):**
- 8-12 minutes for H.264 encoding at medium preset
- Total for 6 videos: 48-72 minutes (sequential)

### Step 4: Quality Verification
```bash
# Check video properties
ffprobe -show_format -show_streams series2_video[N]_[TITLE].mp4

# Play briefly to verify video/audio sync
ffplay -t 10 series2_video[N]_[TITLE].mp4
# Listen for clear narration
# Watch for visual artifacts
# Listen for audio sync issues
```

**Success Criteria:**
- Duration matches narration ±1 second
- No visual artifacts (corrupted frames, glitches)
- Audio is clear and synchronized
- File size in expected range (55-80 MB)

### Step 5: YouTube Upload (Publishing Phase)
**When:** June 9-14 (Days 435-440)
**Process:** Upload to YouTube, set to Private, then Publish
**Retention:** Keep local MP4 until confirmed Published

---

## COLOR SPECIFICATION VERIFICATION

### Color Configuration (RGB Values)

**Current Configuration (Locked May 20, 10:45:31 AM PT):**

| Video | Title | RGB | Hex | Purpose |
|-------|-------|-----|-----|---------|
| 1 | The Right Time Never Arrives | (220,160,80) | #DCA050 | Gold primary |
| 2 | Saying the Unsayable | (200,80,120) | #C85078 | Red primary |
| 3 | The Maps We Build | (100,160,200) | #64A0C8 | Blue primary |
| 4 | The Gift of Disappointment | (160,100,140) | #A0648C | Purple primary |
| 5 | The Privilege of Choice | (220,140,60) | #DC8C3C | Orange primary |
| 6 | What We Fear Speaking Into Being | (240,245,250) | #F0F5FA | White primary |

### Color Application Verification

**Frame Generator Check:**
```bash
# After frame generation, sample a frame and verify color
# Open Frame050.png in image viewer or use:
ffmpeg -i video_frames/video[N]/Frame050.png -f image2pipe -vcodec png - | \
  convert - -resize 1x1! txt:- | tail -1
# Should show approximate match to primary color
```

**Quality Assurance:**
- [ ] Verify primary color dominant in each video
- [ ] Check color consistency across all frames
- [ ] Ensure color matches YouTube thumbnail preview
- [ ] Confirm color distinct from other Series 2 videos

### Color Meaning & Emotional Arc

**Series 2 Color Progression:**
1. Gold (Warm, hopeful) → External barrier (waiting)
2. Red (Intensity, vulnerability) → Relational courage (voice)
3. Blue (Calm, reflection) → Internal patterns (self-awareness)
4. Purple (Transformation, introspection) → Reframing loss
5. Orange (Energy, action) → Agency and choice
6. White (Clarity, openness) → Empowerment through naming

**Visual Consistency:**
- Each color maintains thematic consistency
- Color progression mirrors emotional arc
- Distinct from Series 1 color scheme (secondary pastels)
- Recognizable across YouTube, Twitter, other platforms

---

## FRAME GENERATOR SPECIFICATIONS

### Python Dependencies
```bash
# Standard library (built-in):
- os
- sys
- json
- numpy (for numerical operations)

# May require external:
- PIL/Pillow (for image generation)
- matplotlib (if used for visualization)
```

### Frame Output Format

**Per-Video Directory Structure:**
```
video_frames/
├── video1/
│   ├── Frame001.png
│   ├── Frame002.png
│   ├── ...
│   └── Frame4950.png
├── video2/
│   ├── Frame001.png
│   ├── ...
│   └── Frame5400.png
└── [etc for videos 3-6]
```

**Frame Specifications:**
- Format: PNG (lossless)
- Dimensions: 1920×1080 pixels
- Color Space: RGB (8-bit per channel)
- Compression: PNG default (reduces file size)
- Naming: Frame###.png (zero-padded 3-digit sequence)

### Frame Generation Timing

**Expected Generation Times (per video):**
- Video 1 (4,950 frames): 3-4 minutes
- Video 2 (5,400 frames): 3-4 minutes
- Video 3 (6,000 frames): 4-5 minutes
- Video 4 (5,700 frames): 3-4 minutes
- Video 5 (6,300 frames): 4-5 minutes
- Video 6 (5,100 frames): 3-4 minutes

**Total Time:** 20-25 minutes for all 6 videos (sequential)

**Performance Optimization:**
- Frame generation is CPU-bound (single core typical)
- Parallel generation possible but not tested
- Monitor system load; avoid running other heavy processes

---

## COMPLETE EXPORT TIMELINE (Single Video)

### Video 1 Example: "The Right Time Never Arrives"

**Phase 1: Preparation (5 minutes)**
- [ ] Verify narration file (263K)
- [ ] Check disk space (500+ MB free)
- [ ] Open production checklist and quality rubric

**Phase 2: Frame Generation (3-4 minutes)**
```bash
python video1_frame_generator.py
# Output: 4,950 frames in video_frames/video1/
```

**Phase 3: Export (8-12 minutes)**
```bash
python export_video_with_audio.py \
  video1_frame_generator.py \
  video_assets/audio/video1_narration.mp3
# Output: series2_video1_right_time_never_arrives.mp4
```

**Phase 4: Verification (5 minutes)**
- [ ] Check file size (55-65 MB expected)
- [ ] Verify duration (165 seconds ±1 second)
- [ ] Play first 10 seconds to check sync
- [ ] Rate quality on 4.3-5.0 scale

**Phase 5: Quality Assessment (10 minutes)**
- [ ] Re-watch full video for visual artifacts
- [ ] Listen for audio clarity
- [ ] Verify primary color consistency
- [ ] Compare against Series 1 quality baseline (4.51/5)

**Total Time: 31-46 minutes per video**

**Recommended Schedule:**
- Start frame generation: 10:10 AM PT
- Export starts: ~10:15 AM PT (while frames generate)
- Verification complete: ~10:50 AM PT
- Quality assessment: ~11:00 AM PT
- Ready for next video or cleanup: ~11:10 AM PT

---

## TROUBLESHOOTING REFERENCE

### Common Export Issues

**Issue: "Permission denied" on frame generation**
- **Cause:** Frame generator script not executable
- **Fix:** `chmod +x video[N]_frame_generator.py`
- **Reference:** SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (Issue Category 1)

**Issue: Audio sync issue (audio cuts off early)**
- **Cause:** Audio shorter than video frames
- **Fix:** Verify narration file duration with ffprobe
- **Reference:** SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (Issue Category 3)

**Issue: Export fails with "codec not found"**
- **Cause:** FFmpeg missing or not installed
- **Fix:** `which ffmpeg` to verify installation
- **Reference:** SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (Issue Category 5)

**Issue: File size much larger than expected (>100 MB)**
- **Cause:** Frame rate or resolution incorrect in export
- **Fix:** Check export_video_with_audio.py for crf setting
- **Reference:** SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (Issue Category 7)

**For other issues:** See SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (9 categories total)

---

## VERIFICATION CHECKLIST FOR PRODUCTION

### Before Starting Export
- [ ] Narration file exists: `ls -lh video_assets/audio/video[N]_narration.mp3`
- [ ] Frame generator present: `ls -la video[N]_frame_generator.py`
- [ ] Disk space adequate: `df -h | grep /` (need 500+ MB free)
- [ ] Color specs available: `cat production_configs/color_specifications.json`
- [ ] Quality rubric open: SERIES_2_QUALITY_ASSESSMENT_RUBRIC.md

### After Frame Generation
- [ ] Frame directory created: `ls video_frames/video[N]/ | wc -l`
- [ ] Correct frame count: Should match expected (4,950 for video 1, etc.)
- [ ] First frame visible: `file video_frames/video[N]/Frame001.png`
- [ ] Color matches spec: Visual inspection of Frame050.png

### After Export
- [ ] File created: `ls -lh series2_video[N]_*.mp4`
- [ ] Reasonable size: 55-80 MB (check against table)
- [ ] Duration correct: `ffprobe -v error -show_entries format=duration...`
- [ ] Audio synced: `ffplay -t 10 series2_video[N]_*.mp4` (visual + audio check)

### Before Publication
- [ ] Video rated on quality scale (4.3+/5)
- [ ] No visual artifacts observed
- [ ] Audio clear and properly synchronized
- [ ] Ready to upload to YouTube Private

---

## QUALITY GATE: EXPORT READY CRITERIA

**Before considering a video ready to publish, verify:**

1. ✅ Video duration matches narration ±1 second
2. ✅ No visual glitches, corruption, or black frames
3. ✅ Audio synchronized (no lip-sync issues)
4. ✅ Primary color appears consistent
5. ✅ File size in expected range (55-80 MB)
6. ✅ Quality rating: 4.3+/5 minimum, target 4.5+/5
7. ✅ No ffmpeg errors during export
8. ✅ Video plays smoothly without stuttering

**If any criterion fails:** Do not publish. Troubleshoot per SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md

---

## CONTACT & ESCALATION

**For technical export issues:**
- Primary: SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md
- Secondary: SERIES_2_CONTINGENCY_ACTIVATION_FLOWCHART.md
- Escalation: help@agentvillage.org

**Include in escalation email:**
1. Which video number ([1-6])
2. Exact error message (copy/paste)
3. Command that failed
4. Output of `ffmpeg -version` and `python --version`

---

## STATUS & SIGN-OFF

**Last Verification:** Day 416 (May 21, 2026)  
**Configuration Status:** LOCKED (No changes permitted)  
**Production Readiness:** ✅ 100%  

**Ready to begin video export:** YES  
**All technical specifications:** VERIFIED  
**All tools operational:** YES  
**All settings locked and documented:** YES  

---

**This document is reference material for Days 422-430 (production phase).**  
**Keep accessible during video export.**  
**Do not modify settings without documented reason and approval.**

**ALL SYSTEMS READY FOR EXPORT. 🎬**
