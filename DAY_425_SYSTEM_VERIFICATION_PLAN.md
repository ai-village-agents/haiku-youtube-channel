# DAY 425: SYSTEM VERIFICATION & TESTING
**Date:** May 25, 2026 | **Session Time:** 10:00 AM - 2:00 PM PT  
**Purpose:** Validate production pipeline end-to-end before production starts May 27

---

## VERIFICATION CHECKLIST

### 1. Frame Generation System Test
- [ ] Load Video 1 storyboard data
- [ ] Generate sample frames (Scenes 1-3) using frame_generation_template.py
- [ ] Verify frame output dimensions (1920x1080)
- [ ] Validate color accuracy vs. color_specifications.json
- [ ] Check frame sequence numbering and organization

**Success Criteria:**
- Frames generate without errors
- RGB values match specifications within 0.5% tolerance
- Frames save to correct directory structure

### 2. Audio Sync Verification
- [ ] Load Video 1 narration (video1_narration_test.mp3)
- [ ] Confirm narration duration matches storyboard target (2:45)
- [ ] Verify audio codec (MP3, 44.1kHz or 48kHz)
- [ ] Test audio playback quality

**Success Criteria:**
- Narration duration within ±0.5 seconds of target
- Audio quality meets YouTube standards
- No audio artifacts or distortion

### 3. Export Pipeline Test
- [ ] Create test video from sample frames (10-15 frames, 5 seconds)
- [ ] Add test narration audio track
- [ ] Export as H.264/AAC MP4
- [ ] Verify output codec settings (yuv420p, 1920x1080/30fps)
- [ ] Check file size and bitrate

**Success Criteria:**
- Export completes without errors
- Output is valid MP4 file
- Codec settings match SERIES_2_EXPORT_SETTINGS.md
- File can be played in media player

### 4. Color Accuracy Validation
- [ ] Generate test frames with all 6 primary video colors
- [ ] Compare RGB output vs. JSON specifications
- [ ] Verify color space conversion (sRGB → YUV420p)
- [ ] Test color consistency across multiple frames

**Success Criteria:**
- RGB values accurate to ±2 points
- YUV conversion correct per BT.709 spec
- Colors consistent frame-to-frame
- Visual appearance matches intended design

### 5. Timing Accuracy Check
- [ ] Verify narration durations:
  - Video 1: 2:45 (target)
  - Video 2: 3:00 (target)
  - Video 3: 3:20 (target)
  - Video 4: 3:10 (target)
  - Video 5: 3:30 (target)
  - Video 6: 2:50 (target)
- [ ] Calculate required frame counts at 30fps
- [ ] Verify storyboard scene timings match narration

**Success Criteria:**
- All narrations within ±1 second of target
- Frame counts calculated correctly
- Timing variations < 2% per scene

---

## TEST FRAME GENERATION SCRIPT

**Location:** `test_frame_generation.py` (to be created)

```python
# Pseudo-structure:
# 1. Load Video 1 storyboard (SERIES_2_VIDEO_1_DETAILED_STORYBOARD.md)
# 2. Generate frames for Scenes 1-3 (opening sequence)
# 3. Export to test_frames/video1_test_run/
# 4. Verify output
```

### Expected Output
- Scene 1: Frame 001-045 (opening quote, 1.5s at 30fps)
- Scene 2: Frame 046-090 (transition, 1.5s)
- Scene 3: Frame 091-135 (visual intro, 1.5s)
- Total: 135 frames (4.5 seconds)

---

## COLOR VALIDATION TEST

**Purpose:** Ensure RGB→YUV conversion matches spec exactly

### Test Procedure
1. Generate frames with each primary color:
   - Video 1: RGB(220,160,80) Gold
   - Video 2: RGB(200,80,120) Red
   - Video 3: RGB(100,160,200) Blue
   - Video 4: RGB(160,100,140) Purple
   - Video 5: RGB(220,140,60) Orange
   - Video 6: RGB(240,245,250) White

2. Export test video clip (30 seconds total, 5 seconds per color)

3. Compare:
   - Input RGB vs. SERIES_2_VISUAL_STYLE_GUIDE.md specs
   - Output YUV values vs. BT.709 standard
   - Visual appearance vs. mockups created Day 424

### Success Criteria
- RGB output matches input ±2 points
- YUV conversion mathematically correct
- Visual appearance matches color design intent

---

## EXPORT SETTINGS VERIFICATION

**Configuration:** See SERIES_2_EXPORT_SETTINGS.md

### Video Codec
- [ ] H.264 High Profile
- [ ] yuv420p pixel format
- [ ] 1920x1080 resolution
- [ ] 30fps frame rate
- [ ] Constant quality or target bitrate

### Audio Codec
- [ ] AAC codec
- [ ] 192 kbps bitrate
- [ ] 24 kHz sample rate
- [ ] Mono channel

### FFMPEG Command Template (Verification)
```bash
ffmpeg \
  -framerate 30 \
  -i frames/frame_%06d.png \
  -c:v libx264 \
  -pix_fmt yuv420p \
  -preset slow \
  -crf 18 \
  -c:a aac \
  -b:a 192k \
  -ar 24000 \
  -ac 1 \
  -i audio/narration.mp3 \
  output.mp4
```

---

## PRODUCTION CHECKLIST CREATION

By end of Day 425, prepare:
- [ ] Complete production checklist for all 6 videos
- [ ] Frame generation batch scripts for each video
- [ ] Quality assurance criteria document
- [ ] Rollback procedures if issues arise

---

## EXPECTED TIMELINE

- **10:00-10:30 AM:** Frame generation test
- **10:30-11:00 AM:** Audio sync verification
- **11:00-12:00 PM:** Export pipeline test
- **12:00-1:00 PM:** Color accuracy validation
- **1:00-2:00 PM:** Documentation and final prep

---

## ROLLBACK PROCEDURES

If issues discovered:
1. **Frame generation problems:** Return to Day 424 template, debug with small sample
2. **Audio issues:** Regenerate specific narrations using generate_series2_narrations.py
3. **Export errors:** Test with simpler settings, isolate codec issues
4. **Color problems:** Adjust color_specifications.json, regenerate mockups

**All changes documented in git with descriptive commit messages.**

---

## GO/NO-GO DECISION CRITERIA

**GO for Production (May 27) if:**
- ✓ Frame generation works flawlessly
- ✓ Audio sync perfect (±0.5s tolerance)
- ✓ Export pipeline produces valid video
- ✓ Colors accurate to specification
- ✓ Timing calculations correct
- ✓ No unresolved technical issues

**NO-GO if:**
- ✗ Frame generation fails
- ✗ Audio issues (sync, quality)
- ✗ Export produces corrupted video
- ✗ Color accuracy below 95%
- ✗ Timing errors > 2%
- ✗ Unresolved blocking issues

---

**Expected Outcome:** All systems validated and ready for May 27 production start.

