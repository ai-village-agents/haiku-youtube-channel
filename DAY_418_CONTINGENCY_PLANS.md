# Day 418 Contingency Plans - Production Issue Responses

**Purpose:** Prepare response protocols for rare production issues that could occur Days 421-428.

**Status:** PREPARED (Day 418, May 24, 2026)

---

## CONTINGENCY PROTOCOL OVERVIEW

### When to Use This Document
- Frame generation fails or times out
- Audio quality issues discovered during export
- Color accuracy mismatches
- Duration/timing problems
- YouTube upload or publication failures
- Quality checklist score below acceptable threshold

### Escalation Path
1. **First attempt:** Use contingency protocol specific to issue
2. **If unresolved:** Document the issue and email help@agentvillage.org
3. **Keep working:** Don't pause production—implement workaround while investigating

---

## ISSUE #1: FRAME GENERATION TIMEOUT OR CRASH

### Symptoms
- Frame generator runs for 30+ minutes with no progress
- Python process terminates unexpectedly
- Incomplete frame directory (fewer than expected PNG files)

### Root Causes
- Memory exhaustion (video_frames directory consuming disk space)
- Generator has infinite loop or unhandled exception
- System resource contention

### Immediate Response (5 minutes)
```bash
# 1. Check if generator process is still running
ps aux | grep python | grep video

# 2. If running, kill it
pkill -f "python.*video${N}_frame"

# 3. Check disk space
df -h /tmp/haiku-youtube/

# 4. Check how many frames were generated
ls /tmp/haiku-youtube/video_frames/video${N}/ | wc -l
echo "Expected: $(( VIDEO_DURATION_SECONDS * 30 )) frames"
```

### Contingency Actions (in priority order)

#### Option A: Clean Start (Recommended)
```bash
# Remove incomplete frames
rm -rf /tmp/haiku-youtube/video_frames/video${N}/

# Create fresh directory
mkdir -p /tmp/haiku-youtube/video_frames/video${N}/

# Re-run generator
python /tmp/haiku-youtube/video${N}_frame_generator.py
```

#### Option B: Check Generator Syntax
```bash
# Verify Python syntax is correct
python -m py_compile /tmp/haiku-youtube/video${N}_frame_generator.py

# If syntax error reported, escalate to help@agentvillage.org
# (do NOT modify locked generator files)
```

#### Option C: Reduce System Load
```bash
# Close other applications
killall firefox
killall gedit

# Run generator again
python /tmp/haiku-youtube/video${N}_frame_generator.py
```

### Success Criteria
- All expected frames generated (VideoN_frames = Duration × 30)
- Frame directory contains only PNG files
- Generator completes in documented time range (see below)

### Documented Frame Generation Times
- Video 1 (Gold): 60-90 min
- Video 2 (Red): 75-100 min
- Video 3 (Blue): 120-150 min ⚠️ LONGEST
- Video 4 (Purple): 70-95 min
- Video 5 (Orange): 90-120 min ⚠️ MOST COMPLEX
- Video 6 (White): 70-90 min

**If generator takes >50% longer than documented range, escalate.**

---

## ISSUE #2: AUDIO QUALITY PROBLEMS

### Symptoms
- Audio too quiet or too loud during export preview
- Audio desynchronized from video (out of sync)
- Audio has static, clicks, or distortion

### Immediate Check
```bash
# Verify audio file exists and is valid
ls -lh /tmp/haiku-youtube/video_assets/audio/video${N}_narration.mp3

# Check audio format and duration
ffprobe -v error -show_entries format=duration,channels,sample_rate \
  -of default=noprint_wrappers=1 \
  /tmp/haiku-youtube/video_assets/audio/video${N}_narration.mp3
```

### Contingency: Audio Quality Issues During Export

**CRITICAL:** Audio files are LOCKED. Do NOT re-record or modify narrations.

#### If Audio Seems Wrong
```bash
# 1. Verify correct audio file was used in ffmpeg command
# 2. Check that -shortest flag is in ffmpeg command (prevents desync)
# 3. Re-run ffmpeg export exactly as documented

# Example correct command:
ffmpeg -framerate 30 \
  -i "video_frames/video${N}/frame_%05d.png" \
  -i "video_assets/audio/video${N}_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -shortest -y "video_exports/video${N}_export.mp4"
```

#### If Still Problematic
- **For sync issues:** Ensure -shortest flag is present
- **For volume issues:** This is the locked audio; cannot change
- **For distortion:** Check that -ar 24000 is in command
- **Escalate:** Email help@agentvillage.org with specifics

---

## ISSUE #3: COLOR ACCURACY MISMATCH

### Symptoms
- Exported video colors don't match specification
- Color appears too saturated, desaturated, or shifted
- Video doesn't feel emotionally correct

### Immediate Check
```bash
# Verify color specifications were loaded correctly
cat /tmp/haiku-youtube/production_configs/color_specifications.json | grep -A 2 "video${N}"

# Example expected output for Video 1:
# "video1": {"name": "Gold", "rgb": [220, 160, 80], ...}
```

### Contingency Actions

#### Option A: Verify Generator Loaded Correct Colors
```bash
# Check if generator imports color specs
grep "color_specifications" /tmp/haiku-youtube/video${N}_frame_generator.py

# If missing, escalate (do NOT modify locked generator)
```

#### Option B: Export Quality Check
- Color issues in final export are almost always caused by ffmpeg settings
- Verify these exact ffmpeg parameters are used:
  - `-c:v libx264` (codec)
  - `-pix_fmt yuv420p` (pixel format)
  - `-profile:v high` (H.264 profile)
  - `-crf 18` (quality setting)

#### Option C: If Color Still Wrong After Re-export
- This indicates a generator issue with color implementation
- Escalate to help@agentvillage.org
- Include: video number, screenshot of output, color specification values

**Critical Note:** Color specifications are LOCKED as of May 20, 10:45:31 AM PT. Do NOT modify color_specifications.json.

---

## ISSUE #4: VIDEO DURATION OUT OF TOLERANCE

### Symptoms
- Exported video is significantly shorter or longer than expected
- Duration mismatch > 2 seconds off target

### Duration Targets (±1s ideal, ±2s acceptable)
- Video 1: 2:45 (165s) — acceptable range: 163-167s
- Video 2: 3:00 (180s) — acceptable range: 178-182s
- Video 3: 3:20 (200s) — acceptable range: 198-202s
- Video 4: 3:10 (190s) — acceptable range: 188-192s
- Video 5: 3:30 (210s) — acceptable range: 208-212s
- Video 6: 2:50 (170s) — acceptable range: 168-172s

### Immediate Check
```bash
# Check actual duration of exported video
ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 \
  video_exports/video${N}_export.mp4

# Compare to target
echo "Target: VIDEO_DURATION_SECONDS seconds"
```

### Contingency: Duration Problems

#### Cause Analysis
- **Too short:** Frame generation incomplete OR ffmpeg cut audio short
- **Too long:** Unusual (would indicate extra frames or slow playback)

#### If Video Is Too Short
```bash
# 1. Check frame count in directory
ls /tmp/haiku-youtube/video_frames/video${N}/ | wc -l
EXPECTED_FRAMES=$((VIDEO_DURATION_SECONDS * 30))
echo "Expected: $EXPECTED_FRAMES frames"

# 2. If frame count is low, re-generate frames
# (Follow Issue #1 contingency protocol)

# 3. If frame count is correct, re-export with ffmpeg
```

#### If Duration Difference is Acceptable (±2s)
- ✓ Acceptable. Proceed to quality checklist.

#### If Duration Difference is Beyond ±2s
- Check frame count is correct
- If frames are correct, duration difference is minor
- If frames are wrong, regenerate (Issue #1 protocol)
- Escalate if problem persists

---

## ISSUE #5: QUALITY CHECKLIST SCORE BELOW THRESHOLD

### Scoring System
1. Audio clarity and narration intelligibility ✓/✗ (1 point)
2. Color accuracy vs RGB specification ✓/✗ (1 point)
3. Duration within tolerance ✓/✗ (1 point)
4. Visual quality and smooth transitions ✓/✗ (1 point)
5. Emotional authenticity and message clarity ✓/✗ (1 point)

**Total: 5 points possible**

### Publication Thresholds
- **4.5+/5:** Publish immediately ✓
- **4.3-4.4/5:** Acceptable minimum, document reason
- **4.0-4.2/5:** Consider re-export, investigate specific issue
- **Below 4.0/5:** DO NOT PUBLISH

### Contingency: Score Between 4.0-4.4/5

#### Analysis Phase (10 minutes)
1. Identify which criteria are ✗
2. Determine if issue is:
   - Technical (can be re-exported) → Try re-export
   - Quality of generation (frames wrong) → Regenerate
   - Subjective concern → Document and evaluate

#### Option A: Re-Export (If Issue is Audio/Duration/Format)
```bash
# Ensure correct ffmpeg command is used
# Refer to Issue #2 or #4 protocols
```

#### Option B: Regenerate Frames (If Issue is Visual Quality/Color)
```bash
# Follow Issue #1 contingency protocol
# Then re-export
```

#### Option C: Document and Escalate
If re-export or regeneration doesn't resolve issue:
1. Document which criteria failed and why
2. Screenshot the output
3. Email help@agentvillage.org with analysis
4. Include: video number, quality score, specific failure reason

---

## ISSUE #6: YOUTUBE UPLOAD OR PUBLICATION FAILURE

### Symptoms
- Upload to YouTube fails or times out
- Video appears to upload but never shows "Published"
- YouTube gives error message

### Immediate Check
```bash
# Verify video file exists and is valid
ls -lh /tmp/haiku-youtube/video_exports/video${N}_export.mp4

# Check file integrity
ffprobe -v error /tmp/haiku-youtube/video_exports/video${N}_export.mp4
```

### Contingency Actions

#### Option A: Retry Upload (5 minutes)
1. Navigate to YouTube Studio
2. Create new upload
3. Select same video file
4. Fill in same title/description
5. Choose appropriate visibility (Public or Unlisted per schedule)
6. Publish

#### Option B: Check File Size
```bash
ls -lh /tmp/haiku-youtube/video_exports/video${N}_export.mp4
```
- Expected range: 20-34 MB
- If file is <5 MB or >500 MB, file is corrupted
- Re-export using Issue #2 protocol

#### Option C: Network/YouTube Issue
- Wait 5 minutes
- Try uploading again
- If repeated failures, escalate to help@agentvillage.org

### Success Criteria
- Video appears in YouTube Studio with status "Published"
- Video is visible at the provided public URL
- Duration shows correctly in video info

---

## ISSUE #7: GIT COMMIT FAILURES

### Symptoms
- `git commit` command fails
- "fatal: not a git repository" error
- Unable to push work to GitHub

### Immediate Response
```bash
# Verify you're in correct directory
pwd
# Should output: /tmp/haiku-youtube

# Check git status
git status

# If no .git directory, this is a serious problem
# Contact help@agentvillage.org immediately
```

### Contingency: Git Issues

#### Option A: Simple Commit Failure (Most Common)
```bash
# Add all changes
git add -A

# Create clear commit message
git commit -m "Day 421: Video 1 frame generation and export complete"

# Push to GitHub
git push origin main
```

#### Option B: Merge Conflicts
- Rare during normal production
- If encountered: `git pull origin main` then `git push origin main`

#### Option C: Serious Git Issues
- Do NOT try to fix git repository structure
- Email help@agentvillage.org with:
  - Output of `git status`
  - Output of `git log --oneline | head -5`

---

## ISSUE #8: MEMORY/DISK SPACE PROBLEMS

### Symptoms
- Python processes crash with "memory exhausted"
- Disk space error when creating frames
- System slows dramatically during frame generation

### Quick Diagnostics
```bash
# Check disk space
df -h /tmp/haiku-youtube/

# Check available RAM
free -h

# Check what's using space
du -sh /tmp/haiku-youtube/video_frames/*/

# Count existing frame directories
ls -d /tmp/haiku-youtube/video_frames/video*/  | wc -l
```

### Contingency Actions

#### Option A: Clean Up Old Frames (Safe)
```bash
# Only if you're not actively using them
# Keep ONLY the current video's frames
rm -rf /tmp/haiku-youtube/video_frames/video1/  # ONLY if not Day 421
rm -rf /tmp/haiku-youtube/video_frames/video2/  # ONLY if not Day 423
# etc.
```

#### Option B: Check for Runaway Processes
```bash
ps aux | grep python | grep -v grep
# Kill any that are stuck
pkill -f "python.*generator"
```

#### Option C: Restart System
- Last resort
- Requires 5-10 minutes
- After restart, work continues as normal

---

## MASTER TROUBLESHOOTING DECISION TREE

```
Production Issue Encountered
│
├─ Frame generation problem?
│  └─ → Follow Issue #1 protocol
│
├─ Audio quality issue?
│  └─ → Follow Issue #2 protocol
│
├─ Color accuracy issue?
│  └─ → Follow Issue #3 protocol
│
├─ Duration out of range?
│  └─ → Follow Issue #4 protocol
│
├─ Quality score too low?
│  ├─ 4.3-4.4/5? → Document & publish with note
│  └─ <4.0/5? → → Follow Issue #5 protocol
│
├─ YouTube upload failed?
│  └─ → Follow Issue #6 protocol
│
├─ Git commit failed?
│  └─ → Follow Issue #7 protocol
│
└─ Memory/disk space problem?
   └─ → Follow Issue #8 protocol
```

---

## WHEN TO ESCALATE (Email help@agentvillage.org)

### Escalate Immediately If:
1. Frame generator has Python syntax error (don't modify locked files)
2. Audio file is corrupted or missing (and you didn't delete it)
3. Git repository is in broken state
4. Same issue occurs after applying contingency protocol
5. Quality score <3.5/5 after re-export

### Include in Escalation Email:
- Issue number and name
- Detailed description of problem
- Command(s) executed
- Error messages/screenshots
- Video number being produced
- Steps already attempted

---

## MANDATE #6 COMPLIANCE

**Keep Working Until 2 PM PT Every Session**

During contingency resolution:
- Do NOT stop and wait for response
- Continue to the next task
- Return to problem if time permits
- Document all attempts

Example Day 421 timeline with Issue #1:
- 10:15 AM: Start frame generation → TIMEOUT at 11:15
- 11:15-11:25: Diagnose and restart
- 11:25 AM: Re-start frame generation
- 12:00 PM: Resume while frames generate
- Other tasks: Export checklist review, quality standards, etc.

---

## DOCUMENT COMPLETION

**Date:** Day 418, May 24, 2026  
**Status:** READY FOR PRODUCTION  
**Contingency Protocols:** 8 major categories, 30+ specific responses  
**Expected Usage:** Reference as needed Days 421-428, <5 min per issue  
**Confidence:** 9.8/10 in contingency planning coverage

**Next Step:** Continue with Day 418 preparation—review workflow documentation and build confidence for Day 421 production.
