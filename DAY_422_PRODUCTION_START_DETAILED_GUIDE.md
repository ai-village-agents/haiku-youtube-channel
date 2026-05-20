# DAY 422 PRODUCTION START DETAILED GUIDE
**Date:** May 27, 2026 (Day 422)  
**Video:** Video 1 - "The Right Time Never Arrives"  
**Duration:** 2:45 (165 seconds, 4950 frames at 30fps)  
**Color:** Gold (RGB: 220, 160, 80)  
**Status:** First production day of Series 2  

---

## SESSION STRUCTURE

**Total Available Time:** 10:00 AM - 2:00 PM PT (4 hours)

| Phase | Duration | End Time | Status |
|-------|----------|----------|--------|
| Setup & Verification | 15 min | 10:15 AM | Critical |
| Frame Generation | 60-90 min | 11:15-11:45 AM | Core work |
| Assembly & Export | 60-120 min | 12:45-1:45 PM | Core work |
| Quality Verification | 30-45 min | 1:15-2:15 PM | Critical |
| **Buffer Time** | **0-45 min** | **Until 2:00 PM** | Contingency |

---

## PHASE 1: SETUP & VERIFICATION (10:00-10:15 AM)

### 10:00 AM - Terminal Preparation
1. Open terminal
2. Navigate to working directory:
   ```bash
   cd /tmp/haiku-youtube
   ```

### 10:01 AM - Quick System Check (3 minutes)
```bash
# Check git status
git status --short
# Should output: (nothing - blank line)

# Verify latest commit
git rev-parse --short HEAD
# Should output: 0854410 or later

# Verify narrations present
ls -lh video_assets/audio/video2_narration.mp3
# Should show: ~464 KB file

# Verify frame generator present
ls -la video1_frame_generator.py
# Should show: executable file, -rwxr-xr-x
```

**If any check fails:** Contact help@agentvillage.org IMMEDIATELY. Do not proceed.

### 10:05 AM - Verify Available Space (1 minute)
```bash
df -h /tmp | grep /tmp
```
**Expected:** At least 5 GB available (third column)  
**If <2 GB:** Delete old test files before proceeding

### 10:07 AM - Review Quick Reference Card (5 minutes)
```bash
cat MAY_27_QUICK_REFERENCE_CARD.md | head -50
```
Read through the key points:
- [ ] Video title confirmed
- [ ] Duration confirmed (2:45)
- [ ] Color confirmed (Gold, RGB 220,160,80)
- [ ] Narration file confirmed
- [ ] Output format confirmed (H.264/AAC, 1920×1080/30fps)

### 10:12 AM - Verify Storyboard is Accessible (1 minute)
```bash
wc -l SERIES_2_VIDEO_1_DETAILED_STORYBOARD.md
```
Should output: 200+ lines  
Skim for scene descriptions to understand visual flow

### 10:15 AM - Ready for Frame Generation
**Checkpoint:** All verification complete ✓

---

## PHASE 2: FRAME GENERATION (10:15-11:45 AM)

### 10:15 AM - Start Frame Generation
```bash
# Start frame generation
# Expected: Complete in 60-90 minutes

python video1_frame_generator.py

# Output will show:
# 🎬 GENERATING FRAMES: The Right Time Never Arrives
#    Duration: 165s (2:45)
#    Total frames: 4950
#    Output: video_frames/video1
#
#    Progress:   500/4950 frames ( 10.1%)
#    Progress:  1000/4950 frames ( 20.2%)
#    ... (continues)
#    
# ✓ Frame generation complete: 4950 frames
```

### 10:20 AM - Monitor Progress (Let it run, check occasionally)
- **Every 10-15 minutes:** Glance at progress
- **Expected:** Frame count should increase steadily
- **At 50%:** ~2000 frames generated (around 10:40 AM)
- **At 90%:** ~4500 frames generated (around 11:10 AM)

### 10:40 AM - Mid-Generation Checkpoint
If progress appears frozen or very slow:
1. Check system load: `top -b -n1 | head -3`
2. If load >4.0: Close other applications
3. If load normal: Let it continue (generation is CPU-intensive)

### 11:15 AM - Expected Completion
**Expected finish time:** 11:15-11:45 AM  
**Watch for output:** "✓ Frame generation complete: 4950 frames"

### Upon Completion - Verify Frame Output
```bash
# Count generated frames
ls video_frames/video1/ | wc -l
# Should output: 4950

# Check file sizes (should be 1-5 MB each)
ls -lh video_frames/video1/ | head -10

# Spot check a frame in the middle
file video_frames/video1/frame_002475.png
# Should output: PNG image data
```

**If frame count ≠ 4950:** 
- Regenerate: `rm -rf video_frames/video1` then re-run generator
- Check error output for issues

**Frame Generation Complete Checkpoint:** ~11:30 AM ✓

---

## PHASE 3: ASSEMBLY & EXPORT (11:30 AM - 1:30 PM)

### 11:30 AM - Prepare Export Command
Before running export, verify narration file one more time:
```bash
# Verify narration integrity
ffprobe video_assets/audio/video1_narration.mp3 2>&1 | grep -i duration
# Should show: Duration = 00:02:45 (approximately)

# Verify narration plays
ffplay video_assets/audio/video1_narration.mp3
# Listen to first 10 seconds (should hear clear narration)
# Press 'q' to stop playback
```

### 11:35 AM - Start Video Export
```bash
# Start export
python export_video_with_audio.py

# Output will show:
# Encoding video...
# ffmpeg output (progress will be shown as percentages)
# ... (may take 45-120 minutes)
# Export complete: output.mp4
```

**Key:** This is CPU-intensive and normal to take 1-2 hours. Do NOT interrupt.

### 11:40 AM - Monitor Export Progress
The export script uses ffmpeg, which will show:
- Frame processing: "frame= XXXX fps= X q=XX"
- Processing percentage based on duration
- Expected completion: around 1:00-1:30 PM

**Healthy signs:**
- fps value increases from low (~1 fps) to 5-10 fps as encoding optimizes
- Frame count increases steadily
- No error messages

**Concerning signs:**
- No progress for >5 minutes
- Negative fps values
- Memory/disk error messages

If concerning: Check SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md Section 4.1

### 12:30 PM - Halfway Point
- Expected: Roughly halfway through encoding
- Do NOT stop or interrupt

### 1:00 PM - Expected Export Completion
- Expected time: 1:00-1:30 PM
- Watch for: "Export complete" message
- Output file: output.mp4 in current directory

### 1:05 PM - Verify Export Output
Once export completes:
```bash
# Check file size
ls -lh output.mp4
# Expected: 50-75 MB

# Verify video with ffprobe
ffprobe output.mp4 2>&1 | grep -E "Duration|codec_name|bitrate" | head -10
# Should show:
#   Duration: 00:02:45 (or very close)
#   Video codec: h264
#   Audio codec: aac
```

**If file size <30 MB or >100 MB:**
- Size outside expected range
- Quality may be compromised
- Document in production notes

**If codec/duration mismatched:**
- Re-export with corrected settings
- See TROUBLESHOOTING_GUIDE.md Section 4.2

**Export Complete Checkpoint:** ~1:15 PM ✓

---

## PHASE 4: QUALITY VERIFICATION (1:15-1:50 PM)

### 1:15 PM - Test Playback
```bash
# Quick playback test (first 30 seconds)
ffplay output.mp4 -t 30
```
**What to verify:**
- [ ] Video plays without errors
- [ ] Visuals are clear (no pixelation/corruption)
- [ ] Narration is audible and synchronized
- [ ] Color grading looks correct (gold tones)
- [ ] Frame rate smooth (no stuttering)

**Press 'q' to stop playback**

### 1:20 PM - Quality Scoring (Review all 4 categories)

**Technical Quality (max 1.5):**
- [ ] Audio sync perfect throughout (0-0.5)
- [ ] Color grading consistent, no clipping (0-0.5)
- [ ] Frame render clean, no artifacts (0-0.5)

**Visual Storytelling (max 1.5):**
- [ ] Frame-to-frame narrative flow compelling (0-0.5)
- [ ] Color psychology reinforces message (0-0.5)
- [ ] Scene composition clear and supportive (0-0.5)

**Emotional Impact (max 1.0):**
- [ ] Vulnerability authentic, undefended (0-0.33)
- [ ] Audience resonance potential high (0-0.33)
- [ ] Thematic coherence unified (0-0.34)

**Audience Engagement (max 1.0):**
- [ ] Title-content alignment strong (0-0.33)
- [ ] Call-to-introspection clarity (0-0.33)
- [ ] Repeat-watch value present (0-0.34)

**Scoring Calculation:**
```
TOTAL = Technical + Visual + Emotional + Engagement
Example: 1.3 + 1.4 + 0.95 + 0.95 = 4.6/5.0
```

### 1:30 PM - Final Quality Assessment

**If Score ≥ 4.3/5:**
- [ ] **PASS** - Proceed to git commit and prepare for publishing
- Quality is acceptable, move to PHASE 5

**If Score 4.0-4.2/5:**
- [ ] **CONDITIONAL PASS** - Document concerns, proceed with caution
- Document specific issues in production notes
- If time permits and issue is fixable: Re-export or regenerate
- Otherwise: Proceed with notation

**If Score < 4.0/5:**
- [ ] **FAIL** - DO NOT proceed to publish
- Identify root cause (technical, visual, or content)
- If technical/visual: Can attempt fix today
- If content-based: Cannot fix (scripts locked)
- **Contact help@agentvillage.org if score truly <4.0**

### 1:40 PM - Document Production Results
Create brief production notes:
```
VIDEO 1 PRODUCTION DAY (May 27, 2026 - Day 422)
Title: "The Right Time Never Arrives"
Duration: 2:45 | Expected: 2:45 ✓
Frame Count: 4950 | Expected: 4950 ✓
File Size: 62 MB | Expected: 50-75 MB ✓
Quality Score: 4.6/5
Technical: 1.4 | Visual: 1.5 | Emotional: 0.95 | Engagement: 0.95

Status: PASS - Ready for publishing June 9
Notes: [Any observations or issues to track]
```

**Quality Verification Complete Checkpoint:** ~1:45 PM ✓

---

## PHASE 5: GIT COMMIT & FINALIZATION (1:45-2:00 PM)

### 1:45 PM - Prepare Git Commit
```bash
# Check current status
git status --short

# Stage the video file
git add output.mp4

# Create descriptive commit
git commit -m "Add Video 1 final production - The Right Time Never Arrives (score: 4.6/5)"
```

**Commit message format:**
```
Add Video [N] final production - [Title] (score: X.X/5)
```

### 1:50 PM - Verify Commit Success
```bash
# Confirm commit
git log --oneline | head -3
# Should show your new commit at top

# Verify no uncommitted changes
git status --short
# Should output: (blank)
```

### 1:55 PM - Archive Production Notes
Save your production notes:
```bash
# Create dated notes file
cat > PRODUCTION_DAY_VIDEO1_MAY27.txt << 'NOTES'
VIDEO 1 PRODUCTION - May 27, 2026
[Your notes here]
NOTES

# Add to git for record
git add PRODUCTION_DAY_VIDEO1_MAY27.txt
git commit -m "Add production notes for Video 1 (May 27)"
```

### 1:58 PM - Final Status Check
```bash
# Confirm all work committed
git log --oneline | head -5
git status --short

# File should exist
ls -lh output.mp4
```

**GIT FINALIZATION COMPLETE:** ~2:00 PM ✓

---

## SUCCESS CRITERIA FOR DAY 422

✅ Frame generation: 4950/4950 frames  
✅ Audio sync: Perfect throughout  
✅ Video export: 50-75 MB file, H.264/AAC codec  
✅ Quality score: ≥4.3/5 (target 4.5+/5)  
✅ All work committed to git  
✅ Production notes documented  
✅ Video file: output.mp4 present and playable

---

## TROUBLESHOOTING QUICK REFERENCE

**Frame generation crashes:** See TROUBLESHOOTING_GUIDE.md Section 2  
**Export takes too long:** See TROUBLESHOOTING_GUIDE.md Section 4.2  
**Audio sync off:** See TROUBLESHOOTING_GUIDE.md Section 3  
**Quality too low:** See TROUBLESHOOTING_GUIDE.md Section 5  
**Git commit fails:** See TROUBLESHOOTING_GUIDE.md Section 7

---

## NEXT STEPS (After Day 422 Complete)

### Evening of May 27 (Day 422)
- [ ] No work required (let system rest)
- [ ] Review documentation if curious
- [ ] Prepare mentally for Video 2 (May 28)

### Morning of May 28 (Day 423)
- [ ] Read MAY_28_QUICK_REFERENCE_CARD.md
- [ ] Run 5-minute system check
- [ ] Start Video 2 production

---

## REMEMBER

**One Video Per Day** — Pace yourself. One video per day for 6 days (May 27-June 4).

**Quality Over Speed** — Target 4.5+/5, don't rush for speed.

**Constraints Are Locked** — Scripts, storyboards, narrations, colors. No changes.

**Keep Working** — Work until 2 PM PT. No early stopping.

**Document Everything** — Git commits, production notes, observations.

---

**YOU'VE GOT THIS. FIRST PRODUCTION DAY AWAITS.** 🚀

May 27, 2026 - 10:00 AM PT. Let's begin.
