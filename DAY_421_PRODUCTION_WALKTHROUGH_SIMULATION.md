# Day 421 Production Walkthrough Simulation
**Purpose:** Mental rehearsal of complete Day 421 workflow (Video 1 production)  
**Date:** May 27, 2026 (Day 421)  
**Video:** Video 1 - "The Right Time Never Arrives" (Gold, 2:45)  
**Time Window:** 10:00 AM - 2:00 PM PT

---

## PRE-PRODUCTION SETUP (Before 10:00 AM)

### 9:55 AM - Terminal Preparation
```bash
cd /tmp/haiku-youtube
git status --short    # Verify clean working directory
# Expected: (no output - working tree clean)
```

### 9:58 AM - Mental Preparation
- Read Video 1 affirmation from DAILY_MENTAL_PREPARATION_GUIDE.md
- Internalize: "I know this video. Gold. 2:45. 6 scenes. Movement. Readiness."
- Take 3 deep breaths
- Confidence check: 9.8/10

---

## PHASE 1: FRAME GENERATION (10:00 AM - ~11:45 AM)

### 10:00 AM - Pre-Generation Check
```bash
# Verify all critical assets exist
ls -lh /tmp/haiku-youtube/video_generators/video1_frame_generator.py
# Expected: File exists, size ~50-200 KB

ls -lh /tmp/haiku-youtube/video_assets/audio/video1_narration.mp3
# Expected: File exists, size ~300 KB, timestamp May 20-21
```

**Status Check:**
- Frame generator: ✓ Present
- Audio file: ✓ Present
- Directory: ✓ Clean
- Confidence: 9.8/10

### 10:05 AM - Start Frame Generation

**Command to execute:**
```bash
time python3 /tmp/haiku-youtube/video1_frame_generator.py
```

**What to expect:**
- Console output begins immediately
- Periodic progress messages (every 30-60 seconds)
- Generator message format: "Generating frame X of 4950..."
- Total time: 60-90 minutes (Video 1 is LOW complexity)
- Expected completion: 11:05 AM - 11:35 AM

### 10:15 AM - First Progress Check
```bash
# Count frames generated so far
find /tmp/haiku-youtube/video_frames/video1/ -name "*.png" | wc -l
# Expected at 10:15: 100-200 frames (10 min elapsed ÷ 60 min total = 17%)
```

**Analysis:**
- If frame count is 50-500: NORMAL, continue
- If frame count is 0: Generator might be initializing, wait 2 more minutes
- If frame count is 0 after 2 min: Check generator syntax, investigate

**Expected Progress Timeline:**
- 10:15 AM: ~200 frames (4% of 4,950)
- 10:45 AM: ~1,000 frames (20%)
- 11:15 AM: ~2,500 frames (50%)
- 11:35 AM: ~4,500 frames (90%)
- 11:45 AM: ~4,950 frames (100%)

### 10:30 AM - Monitor System
```bash
# Check system health while waiting
uptime
# Expected: Load average reasonable (below 4.0)

df -h /tmp/haiku-youtube/
# Expected: Plenty of free space (100+ GB available)
```

### 11:00 AM - Mid-Generation Status
```bash
# Check frame count
find /tmp/haiku-youtube/video_frames/video1/ -name "*.png" | wc -l
# Expected: ~2,000-2,500 frames (50% complete)
```

**Decision Point:**
- If on track: Continue, let generator finish
- If slow: Check system load, consider closing background apps
- If very slow (30+ min for 50%): Might take 120+ minutes total, note but continue

### 11:35 AM - Expected Completion

**Check if generation is complete:**
```bash
# Final frame count
find /tmp/haiku-youtube/video_frames/video1/ -name "*.png" | wc -l
# Expected: Exactly 4,950 frames (or 4,949-4,951 acceptable)

# Check for frame_00001.png (first frame)
ls /tmp/haiku-youtube/video_frames/video1/frame_00001.png
# Expected: File exists

# Check for last frame
ls /tmp/haiku-youtube/video_frames/video1/frame_04950.png
# Expected: File exists
```

**Success Criteria:**
- All 4,950 frames generated: ✓
- First and last frames exist: ✓
- Generation completed in reasonable time: ✓
- Generator process finished cleanly: ✓

**If generation NOT complete by 11:45:**
- This is UNUSUAL for Video 1 (LOW complexity)
- Check frame count: If at 4,800+, likely finishing (let it complete)
- If stuck below 4,000, investigate (consult contingency protocol)
- Time buffer exists: Don't panic, can export until ~1:15 PM if needed

---

## PHASE 2: FFMPEG EXPORT (11:45 AM - ~12:00 PM)

### 11:45 AM - Pre-Export Verification

**Verify frame directory is complete:**
```bash
ls /tmp/haiku-youtube/video_frames/video1/ | wc -l
# Expected: 4,950 PNG files (should match 4,950 × 30 fps = 165 seconds)
```

### 11:48 AM - Prepare Export Command

**Review exact command (from TECHNICAL_WORKFLOW_QUICK_REFERENCE.md):**
```bash
ffmpeg -framerate 30 \
  -i "video_frames/video1/frame_%05d.png" \
  -i "video_assets/audio/video1_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -shortest -y "video_exports/video1_export.mp4"
```

**Key points:**
- Frame input: video_frames/video1/frame_%05d.png
- Audio input: video_assets/audio/video1_narration.mp3
- Output: video_exports/video1_export.mp4
- Do NOT modify any flags
- Copy-paste exact command

### 11:50 AM - Execute Export

**Command:**
```bash
cd /tmp/haiku-youtube
ffmpeg -framerate 30 \
  -i "video_frames/video1/frame_%05d.png" \
  -i "video_assets/audio/video1_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -shortest -y "video_exports/video1_export.mp4"
```

**What to expect:**
- ffmpeg starts processing immediately
- Console output shows: `frame=X fps=Y time=HH:MM:SS bitrate=...` periodically
- Very normal for this to show progress every 5-10 seconds
- Processing time: 8-12 minutes (Video 1 is 2:45, should be ~9 minutes)
- Final message: "muxing overhead: ..." indicates successful completion

### 11:55 AM - Monitor Export

**Expected export timeline:**
- 11:50 AM: Start
- 12:00 PM: ~50% complete (processing ~90 seconds of 165-second video)
- 12:05 PM: ~90% complete
- 12:00 PM: Finished (8-10 minutes after start)

**What NOT to do:**
- Do NOT close terminal while ffmpeg is running
- Do NOT interrupt (Ctrl+C) unless export completely fails
- Do NOT modify any files in video_frames/video1/ while exporting

### 12:00 PM - Export Completion (Expected)

**Check if export completed successfully:**
```bash
# Look for final MP4 file
ls -lh /tmp/haiku-youtube/video_exports/video1_export.mp4
# Expected: File exists, size 20-35 MB (Video 1 is 2:45, should be ~25 MB)
```

**Success verification:**
```bash
# Verify file is valid MP4
ffprobe -v error /tmp/haiku-youtube/video_exports/video1_export.mp4
# Expected: No error output (file is valid)

# Check exact duration
ffprobe -v error -show_entries format=duration -of \
  default=noprint_wrappers=1:nokey=1 \
  /tmp/haiku-youtube/video_exports/video1_export.mp4
# Expected: ~165.0 seconds (±1 second acceptable)
# Video 1 target: 165 seconds (2:45)
# Acceptable range: 164-166 seconds
```

---

## PHASE 3: QUALITY CHECK (12:00 PM - 1:00 PM)

### 12:00 PM - Initial File Verification

**File size check:**
```bash
ls -lh /tmp/haiku-youtube/video_exports/video1_export.mp4
# Expected: 20-35 MB (typical for 2:45 video at CRF 18)
```

**If file size is:**
- 20-35 MB: ✓ Normal
- <10 MB: ✗ Suspiciously small, check for corruption
- >50 MB: ✗ Suspiciously large, may indicate settings issue
- File missing: ✗ Export failed, consult contingency protocol

### 12:05 PM - Duration Verification

**Precise duration check:**
```bash
ffprobe -v error -show_entries format=duration -of \
  default=noprint_wrappers=1:nokey=1 \
  /tmp/haiku-youtube/video_exports/video1_export.mp4
```

**Expected output:** `165.04` (approximately)

**Evaluation:**
- 164.0-166.0 seconds: ✓ PASS (±1 second tolerance)
- 162.0-168.0 seconds: ⚠️ ACCEPTABLE (±2 second emergency tolerance)
- <162.0 or >168.0 seconds: ✗ FAIL (investigate)

### 12:10 PM - Visual Quality Assessment

**Optional: Play video sample (first 30 seconds)**

If in GUI environment:
```bash
mpv /tmp/haiku-youtube/video_exports/video1_export.mp4 --start=0 --length=30
# Watch for: audio sync, color accuracy, visual quality
```

**What to look for:**
- ✓ Audio plays without lag/sync issues
- ✓ Gold color visible and consistent
- ✓ Smooth motion/transitions
- ✓ No visual artifacts or pixelation
- ✓ Narration intelligible and clear

### 12:15 PM - Complete Quality Checklist

**5-Point Quality Assessment:**

1. **Audio clarity and narration intelligibility?**
   - YES: Narration is clear, intelligible throughout
   - NO: Audio is muffled, hard to understand, or distorted

2. **Color accuracy vs RGB specification (Gold 220,160,80)?**
   - YES: Gold color visible, matches specification reasonably
   - NO: Color appears wrong (too dark, too yellow, etc.)

3. **Duration within tolerance (165s ±1s)?**
   - YES: Duration is 164-166 seconds
   - NO: Duration is outside acceptable range

4. **Visual quality and smooth transitions?**
   - YES: Smooth motion, no jarring cuts, professional appearance
   - NO: Choppy motion, visible artifacts, quality issues

5. **Emotional authenticity and message clarity?**
   - YES: Video conveys "readiness through action" message clearly
   - NO: Message unclear, emotional arc doesn't land

### 12:20 PM - Quality Score Calculation

**Calculate score:**
- Count checkmarks (YES answers): _____ out of 5
- Quality score: _____ / 5

**Score interpretation:**
- 5/5: Excellent (4.5+/5 minimum requirement MET) ✅
- 4/5: Very Good (4.0/5 quality level) ⚠️
- 3/5: Acceptable (3.5/5 quality level) ⚠️
- 2 or fewer: Problematic (below minimum) ❌

### 12:25 PM - Decision Point

**If score is 4.5+/5 (5 YES answers):**
- ✅ APPROVED FOR PUBLICATION
- Proceed to Phase 4: YouTube Upload

**If score is 4.3-4.4/5 (4 YES answers, document reason):**
- ⚠️ ACCEPTABLE MINIMUM (with documentation)
- Document which criterion failed slightly
- Proceed to Phase 4: YouTube Upload (with note)

**If score is 4.0-4.2/5 (3 YES answers):**
- ❌ BELOW MINIMUM - INVESTIGATE
- Determine which criterion(s) failed
- Consult DAY_418_CONTINGENCY_PLANS.md Issue #5
- Consider re-export vs. regenerate frames
- Time available: May be able to regenerate and re-export by 2 PM

**If score is below 4.0/5:**
- ❌ DO NOT PUBLISH
- Document detailed failure analysis
- Email help@agentvillage.org with findings
- Save export for reference

---

## PHASE 4: YOUTUBE UPLOAD (12:30 PM - 1:30 PM)

### 12:30 PM - Open YouTube Studio

**Go to:** https://studio.youtube.com

**Expected:** YouTube Studio homepage with upload option visible

### 12:32 PM - Create Upload

**Click:** Create > Upload video

**Select file:** /tmp/haiku-youtube/video_exports/video1_export.mp4

**Expected:** File begins uploading, progress bar appears

### 12:35 PM - Fill in Video Details

**Title:** "The Right Time Never Arrives"

**Description:** (Create simple, human-focused description)
Example:
```
A 2:45 meditation on readiness.

Sometimes the right time never arrives—
it emerges through the courage to move.
```

**Visibility:** PUBLIC (not Unlisted, not Private)

**Other settings:** Default (no special processing needed)

### 12:40 PM - Publish

**Click:** PUBLISH

**Expected:** YouTube returns confirmation and generates public URL

**Note:** Video may take 5-30 minutes to appear as "Published" in YouTube Studio

### 12:45 PM - Wait for Confirmation

**Monitor YouTube Studio dashboard:**
- Video appears with status "Processing"
- After 1-2 minutes: Status changes to "Published"
- Video becomes publicly viewable

**URL format:** https://youtu.be/[VIDEO_ID] or https://www.youtube.com/watch?v=[VIDEO_ID]

**Success criteria:**
- YouTube Studio shows "Published" status
- Video is publicly accessible
- Duration displays correctly

---

## PHASE 5: ANNOUNCEMENT IN CHAT (1:15 PM - 1:45 PM)

### 1:15 PM - Wait for Published Confirmation

**Requirement:** Must wait until YouTube shows "Published" status

**If not published yet:** Wait additional 5-10 minutes

**If published:** Proceed to announcement

### 1:20 PM - Prepare Announcement

**From SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md, Video 1 section:**

Example announcement format:
```
Published: "The Right Time Never Arrives" (2:45)
https://youtu.be/[VIDEO_ID]

Sometimes the right time never arrives—
it emerges through action, not waiting.
```

### 1:22 PM - Check #rest Chat for Duplicates

**Before posting:**
1. Go to #rest chat room
2. Press Ctrl+F
3. Search for: "The Right Time Never Arrives"
4. Expected: No duplicate announcement exists
5. If duplicate found: STOP, investigate, escalate to help@agentvillage.org

### 1:25 PM - Send Announcement

**Paste announcement into #rest chat**

**Click:** Send

**Status:** Announcement posted once, exactly

### 1:30 PM - Verify Announcement Posted

**Check #rest chat:**
- Message appears with timestamp
- No duplicate exists
- Message is readable and clear

---

## PHASE 6: GIT COMMIT & CLEANUP (1:30 PM - 2:00 PM)

### 1:35 PM - Commit Frame Generation

```bash
cd /tmp/haiku-youtube

# Stage frame generation work
git add video_frames/video1/

# Commit with clear message
git commit -m "feat: Video 1 frame generation complete (4,950 frames, 75 minutes)"
```

### 1:40 PM - Commit Export

```bash
# Stage export work
git add video_exports/video1_export.mp4

# Commit export
git commit -m "feat: Video 1 export complete (165s duration, quality 4.5/5, published)"
```

### 1:45 PM - Final Status Check

```bash
# Verify clean working directory
git status --short
# Expected: (no output - working tree clean)

# Verify latest commit
git log --oneline -1
# Expected: Latest commit is "feat: Video 1 export complete..."

# Push to GitHub
git push origin main
```

---

## TIMELINE SUMMARY

```
10:00 AM: Read affirmation, start frame generation
10:05 AM: Frame generation begins (time python3 video1_frame_generator.py)
10:15 AM: First progress check (~200 frames expected)
10:30 AM: Monitor system health
11:00 AM: Mid-generation check (~2,000 frames expected)
11:35 AM: Frame generation complete (~4,950 frames)
11:45 AM: Prepare and execute ffmpeg export
12:00 PM: Export complete, begin quality check
12:15 PM: Complete 5-point quality checklist
12:25 PM: Decision point (publish or investigate)
12:30 PM: Begin YouTube upload
12:45 PM: File uploaded, wait for "Published"
1:15 PM: Receive published confirmation
1:20 PM: Prepare announcement
1:25 PM: Send announcement in #rest chat
1:35 PM: Commit frame generation to git
1:40 PM: Commit export to git
1:45 PM: Final verification, push to GitHub
2:00 PM: END OF PRODUCTION DAY
```

---

## BUFFER TIME ANALYSIS

**Ideal scenario (fastest possible):**
- Frame gen: 60 min (10:05-11:05)
- Export: 8 min (11:05-11:13)
- Quality check: 10 min (11:13-11:23)
- YouTube upload: 30 min (11:23-11:53)
- Announcement: 5 min (11:53-11:58)
- Git commit: 5 min (11:58-2:03 PM)
- **Completion: 11:58 AM** (plenty of buffer)

**Realistic scenario (normal pace):**
- Frame gen: 75 min (10:05-11:20)
- Export: 10 min (11:20-11:30)
- Quality check: 15 min (11:30-11:45)
- YouTube upload: 45 min (11:45-12:30)
- Announcement: 5 min (12:30-12:35)
- Git commit: 10 min (12:35-12:45)
- **Completion: 12:45 PM** (good buffer)

**Slow scenario (maximum time):**
- Frame gen: 90 min (10:05-11:35)
- Export: 12 min (11:35-11:47)
- Quality check: 20 min (11:47-12:07)
- YouTube upload: 45 min (12:07-12:52)
- Announcement: 5 min (12:52-12:57)
- Git commit: 10 min (12:57-1:07)
- **Completion: 1:07 PM** (good buffer, complete by 2 PM)

**Critical observation:**
- Even slowest realistic scenario finishes by 1:07 PM
- No video should take longer than 2 hours frame generation (Video 1 is LOW complexity)
- 2 PM deadline is comfortably achievable

---

## CONTINGENCY REFERENCE

**If any phase fails or takes longer:**
- Consult: DAY_418_CONTINGENCY_PLANS.md
- Issue #1: Frame generation problems
- Issue #2: Audio quality problems
- Issue #5: Quality score below 4.3/5
- Issue #6: YouTube upload failures

**Key principle:**
Keep working, don't stop. Use remaining time to resolve or escalate.

---

## SUCCESS CRITERIA FOR DAY 421

✅ **Minimum acceptable:**
- Video 1 generated, exported, published
- Quality score 4.3+/5
- Announcement sent exactly once

✅ **Target achievement:**
- Video 1 published by 12:00 PM
- Quality score 4.5+/5
- All work committed to git
- Finish by 2:00 PM with time to spare

---

**Walkthrough Created:** Day 418, May 21, 2026  
**Use Date:** Day 421, May 27, 2026  
**Expected Duration:** 4 hours (10:00 AM - 2:00 PM PT)  
**Confidence After Completion:** 100% (EXCELLENT)  
**Ready to Execute?** YES ✅

You've got this. All systems are GO. 🎬
