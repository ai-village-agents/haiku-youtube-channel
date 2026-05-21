# SERIES 2: TECHNICAL WORKFLOW QUICK REFERENCE
## All Commands, Paths, and Specifications in One Place

**Purpose:** Fast operational reference during production. Memorize the structure; use when needed.

**Date Created:** Day 415, May 21, 2026

---

## QUICK REFERENCE STRUCTURE

- **Section A:** File System Paths (memorize these)
- **Section B:** Daily Production Workflow (one command per phase)
- **Section C:** Complete ffmpeg Export Command (copy-paste ready)
- **Section D:** Quality Verification Procedures (testing)
- **Section E:** Troubleshooting & Edge Cases (when issues arise)
- **Section F:** Git Workflow (saving work)

---

## SECTION A: FILE SYSTEM PATHS (CRITICAL)

### Working Directory
```
Base: /tmp/haiku-youtube
Repository: https://github.com/ai-village-agents/haiku-youtube-channel
```

### Core Subdirectories
```
/tmp/haiku-youtube/video_assets/          ← Narrations and audio
/tmp/haiku-youtube/video_assets/audio/    ← All .mp3 files (3.82 MB total, all verified)
/tmp/haiku-youtube/video_generators/      ← All Python frame generators
/tmp/haiku-youtube/video_frames/          ← Generated frame directories (one per video)
/tmp/haiku-youtube/video_exports/         ← Final exported MP4 files
/tmp/haiku-youtube/production_configs/    ← Configuration files (color_specifications.json)
```

### Critical File Paths
```
Audio Files (LOCKED, verified May 20-21):
- /tmp/haiku-youtube/video_assets/audio/video1_narration.mp3  (2:45, verified)
- /tmp/haiku-youtube/video_assets/audio/video2_narration.mp3  (3:00, verified)
- /tmp/haiku-youtube/video_assets/audio/video3_narration.mp3  (3:20, verified)
- /tmp/haiku-youtube/video_assets/audio/video4_narration.mp3  (3:10, verified)
- /tmp/haiku-youtube/video_assets/audio/video5_narration.mp3  (3:30, verified)
- /tmp/haiku-youtube/video_assets/audio/video6_narration.mp3  (2:50, verified)

Frame Generators (LOCKED, Python syntax verified):
- /tmp/haiku-youtube/video_generators/video1_frame_generator.py
- /tmp/haiku-youtube/video_generators/video2_frame_generator.py
- /tmp/haiku-youtube/video_generators/video3_frame_generator.py
- /tmp/haiku-youtube/video_generators/video4_frame_generator.py
- /tmp/haiku-youtube/video_generators/video5_frame_generator.py
- /tmp/haiku-youtube/video_generators/video6_frame_generator.py

Color Specifications (LOCKED May 20, 10:45:31 AM PT):
- /tmp/haiku-youtube/production_configs/color_specifications.json

Frame Output Directories (created during production):
- /tmp/haiku-youtube/video_frames/video1/   ← Frame PNG files from generator
- /tmp/haiku-youtube/video_frames/video2/   ← etc.
- /tmp/haiku-youtube/video_frames/videoN/   ← Generic naming

Video Exports (final deliverables):
- /tmp/haiku-youtube/video_exports/video1_export.mp4
- /tmp/haiku-youtube/video_exports/video2_export.mp4
- /tmp/haiku-youtube/video_exports/videoN_export.mp4
```

### Documentation Paths
```
Daily Checklists:
- /tmp/haiku-youtube/DAY_421_PERSONAL_PRODUCTION_TIMELINE.md
- /tmp/haiku-youtube/DAY_421_PERSONALIZED_QUALITY_CHECKLIST.md

Quick Reference (this file):
- /tmp/haiku-youtube/SERIES_2_QUICK_REFERENCE_CARDS.md
- /tmp/haiku-youtube/SERIES_2_SCENE_BY_SCENE_MENTAL_MODELS.md

All located in: /tmp/haiku-youtube/*.md
```

---

## SECTION B: DAILY PRODUCTION WORKFLOW

### Phase 1: Frame Generation (First Action of the Day)
```bash
# Navigate to working directory
cd /tmp/haiku-youtube

# TIMING: Expect 60-120 minutes for most videos
# VIDEO 3 EXCEPTION: Expect 120-150 minutes (longest frame gen)
# VIDEO 5 NOTE: Most technically complex (expect full 90-120 min range)

# Command structure (copy and adapt for videoN):
time python3 video_generators/videoN_frame_generator.py

# EXAMPLE - VIDEO 1:
time python3 video_generators/video1_frame_generator.py

# Expected output:
# - Creates /tmp/haiku-youtube/video_frames/videoN/ directory
# - Generates frame_00001.png, frame_00002.png, ..., frame_00NNN.png
# - Each frame is PNG format at video resolution (1920x1080 or 1280x720, depending on design)
# - Console output shows generation progress
# - Final line shows total execution time (e.g., "real 1m23s")

# CRITICAL RULE: Do NOT use --frames parameter. EVER.
# Correct:   python3 video1_frame_generator.py
# WRONG:     python3 video1_frame_generator.py --frames 100
```

### Phase 2: Verify Frames Generated Successfully
```bash
# Check if frames directory was created
ls -la /tmp/haiku-youtube/video_frames/video1/

# Expected output:
# - Directory exists with frame_00001.png, frame_00002.png, etc.
# - First frame should show title/opening scene
# - Frame count should match expected frame count (fps × duration)
#   Video 1: 30 fps × 165 sec = 4,950 frames
#   Video 2: 30 fps × 180 sec = 5,400 frames
#   Video 3: 30 fps × 200 sec = 6,000 frames
#   Video 4: 30 fps × 190 sec = 5,700 frames
#   Video 5: 30 fps × 210 sec = 6,300 frames
#   Video 6: 30 fps × 170 sec = 5,100 frames

# Quick frame count verification:
ls /tmp/haiku-youtube/video_frames/video1/ | wc -l
# Should show: (frame count + 1 for directory entry) or just count PNG files:
find /tmp/haiku-youtube/video_frames/video1/ -name "*.png" | wc -l
```

### Phase 3: Video Export with ffmpeg (Copy-Paste Ready)
```bash
# BEFORE RUNNING: Ensure audio file exists
ls -lh /tmp/haiku-youtube/video_assets/audio/video1_narration.mp3

# Change to video directory
cd /tmp/haiku-youtube

# Run COMPLETE ffmpeg export command (see SECTION C for full command)
# For Video 1, replace N with 1 throughout:

ffmpeg -framerate 30 \
  -i "video_frames/video1/frame_%05d.png" \
  -i "video_assets/audio/video1_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -shortest -y "video_exports/video1_export.mp4"

# TIMING: Expect 8-12 minutes for 2:45-3:30 videos
# Watch console output for progress. Final message: "frame=..." and duration

# NOTE: "-y" flag means "overwrite if exists" (safe for day-of production)
```

### Phase 4: Quality Check (After Export)
```bash
# 1. Verify file was created
ls -lh /tmp/haiku-youtube/video_exports/video1_export.mp4

# Expected: File size 20-35 MB (depends on video complexity/duration)

# 2. Get technical metadata
ffprobe -v error -show_format -show_streams \
  /tmp/haiku-youtube/video_exports/video1_export.mp4

# Key metrics to check:
# - Duration: Should be ±1 second from target (e.g., video1 target 2:45 = 165s, acceptable 164-166s)
# - Video codec: h264 (libx264)
# - Audio codec: aac
# - Resolution: 1920x1080 or specified dimensions
# - Bitrate: ~5000k video, ~192k audio

# 3. Visual quality spot check (if in GUI environment):
# Play first 30 seconds to check for visual artifacts, color accuracy, audio sync
# mpv /tmp/haiku-youtube/video_exports/video1_export.mp4
```

### Phase 5: Git Commit (After Successful Export)
```bash
# Navigate to repo root
cd /tmp/haiku-youtube

# Check status
git status

# Stage all new/modified files
git add -A

# Commit with clear message
git commit -m "feat: Video 1 frame generation and export complete - quality verified"

# Example commit messages by type:
# - "feat: Video 1 production complete - frame generation 1m23s, export 9m45s"
# - "fix: Video 1 color accuracy verified against specifications"
# - "docs: Video 1 production notes and timing documentation"
```

---

## SECTION C: COMPLETE ffmpeg EXPORT COMMAND (COPY-PASTE)

### The Locked Export Command
This command is IDENTICAL for all 6 videos. Only change: the "N" in videoN and the frame number format.

```bash
ffmpeg -framerate 30 \
  -i "video_frames/videoN/frame_%05d.png" \
  -i "video_assets/audio/videoN_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -shortest -y "video_exports/videoN_export.mp4"
```

### Component Explanation
```
-framerate 30                    ← 30 frames per second (standard for these videos)
-i "video_frames/videoN/frame_%05d.png"  ← Input: PNG frames (00001-99999 naming)
-i "video_assets/audio/videoN_narration.mp3"  ← Input: MP3 audio
-c:v libx264                    ← Video codec: H.264 (most compatible)
-profile:v high                 ← High profile (better quality/compatibility)
-pix_fmt yuv420p                ← Pixel format (YouTube standard)
-b:v 5000k                      ← Bitrate: 5000k (high quality)
-crf 18                         ← Quality: 18 (0=lossless, 51=worst; 18 is professional)
-c:a aac                        ← Audio codec: AAC
-b:a 192k                       ← Audio bitrate: 192k
-ar 24000                       ← Audio sample rate: 24000 Hz
-shortest                       ← Use shortest input (sync audio/video)
-y                              ← Overwrite output file (safe for production)
```

### Copy-Paste Template for Each Video
```bash
# VIDEO 1
ffmpeg -framerate 30 -i "video_frames/video1/frame_%05d.png" -i "video_assets/audio/video1_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video1_export.mp4"

# VIDEO 2
ffmpeg -framerate 30 -i "video_frames/video2/frame_%05d.png" -i "video_assets/audio/video2_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video2_export.mp4"

# VIDEO 3
ffmpeg -framerate 30 -i "video_frames/video3/frame_%05d.png" -i "video_assets/audio/video3_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video3_export.mp4"

# VIDEO 4
ffmpeg -framerate 30 -i "video_frames/video4/frame_%05d.png" -i "video_assets/audio/video4_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video4_export.mp4"

# VIDEO 5
ffmpeg -framerate 30 -i "video_frames/video5/frame_%05d.png" -i "video_assets/audio/video5_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video5_export.mp4"

# VIDEO 6
ffmpeg -framerate 30 -i "video_frames/video6/frame_%05d.png" -i "video_assets/audio/video6_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video6_export.mp4"
```

---

## SECTION D: QUALITY VERIFICATION PROCEDURES

### Quick Duration Check
```bash
# Get duration in seconds
ffprobe -v error -show_entries format=duration -of \
  default=noprint_wrappers=1:nokey=1:divider="  " \
  /tmp/haiku-youtube/video_exports/video1_export.mp4

# Expected outputs (±1 second tolerance):
# Video 1: 165.0 seconds (±1s = 164-166s) ✓
# Video 2: 180.0 seconds (±1s = 179-181s) ✓
# Video 3: 200.0 seconds (±1s = 199-201s) ✓
# Video 4: 190.0 seconds (±1s = 189-191s) ✓
# Video 5: 210.0 seconds (±1s = 209-211s) ✓
# Video 6: 170.0 seconds (±1s = 169-171s) ✓
```

### Full Metadata Check
```bash
# Complete technical verification
ffprobe -v error \
  -select_streams v:0 \
  -show_entries stream=codec_name,codec_type,width,height,r_frame_rate,duration \
  -select_streams a:0 \
  -show_entries stream=codec_name,sample_rate,channels \
  /tmp/haiku-youtube/video_exports/video1_export.mp4

# Expected values:
# Video codec: h264
# Resolution: 1920x1080 (or as specified in generator)
# Frame rate: 30/1 fps
# Audio codec: aac
# Sample rate: 24000 Hz
# Channels: 2 (stereo)
```

### Frame Count Verification (Pre-Export Check)
```bash
# Count generated frames before export
frame_count=$(find /tmp/haiku-youtube/video_frames/video1 -name "*.png" | wc -l)
echo "Generated $frame_count frames"

# For Video 1 (165s @ 30fps): expect 4950 frames (tolerance ±5)
# For Video 2 (180s @ 30fps): expect 5400 frames (tolerance ±5)
# For Video 3 (200s @ 30fps): expect 6000 frames (tolerance ±5)
# For Video 4 (190s @ 30fps): expect 5700 frames (tolerance ±5)
# For Video 5 (210s @ 30fps): expect 6300 frames (tolerance ±5)
# For Video 6 (170s @ 30fps): expect 5100 frames (tolerance ±5)
```

---

## SECTION E: TROUBLESHOOTING & EDGE CASES

### Issue: Frame generator crashes or hangs
```bash
# Check if Python is available
python3 --version

# Check if required libraries are installed
python3 -c "import PIL; import numpy; import matplotlib"

# If errors: you shouldn't have this problem (environment pre-configured)
# If still failing: stop, document error, email help@agentvillage.org
```

### Issue: ffmpeg command not found
```bash
# Check if ffmpeg is installed
which ffmpeg
ffmpeg -version

# If not found: Try full path
/usr/bin/ffmpeg -framerate 30 -i ...

# If still failing: email help@agentvillage.org
```

### Issue: Input MP3 file missing
```bash
# Verify audio file exists and is readable
ls -lh /tmp/haiku-youtube/video_assets/audio/video1_narration.mp3

# Expected: File size 5-10 MB, -rw- permissions

# If missing: Do NOT proceed. Email help@agentvillage.org
# All narrations are locked and verified (May 20-21)
```

### Issue: Frames don't match RGB specifications
```bash
# This shouldn't happen (all generators are verified)
# But if color looks wrong:

# 1. Check color spec file
cat /tmp/haiku-youtube/production_configs/color_specifications.json | grep -A5 videoN

# 2. Verify generator hasn't been modified
git diff video_generators/video1_frame_generator.py
# Should show: no changes (file is committed as-is)

# 3. If generator was modified: REVERT IMMEDIATELY
git checkout video_generators/video1_frame_generator.py

# 4. If still wrong: Document issue, email help@agentvillage.org
```

### Issue: Export takes much longer than expected
```bash
# Video 3 naturally takes longer (2+ hours for frame gen)
# Video 5 is most complex (but still same export time)

# For ffmpeg export:
# - Normal: 8-12 minutes
# - Slow system: 12-15 minutes
# - Very slow: 15-20 minutes

# If taking >20 minutes: stop (Ctrl+C), check disk space
du -sh /tmp/haiku-youtube/
# Need: ~500MB free space minimum
# If low: email help@agentvillage.org

# If not disk space issue: Check system load
uptime
# If load average >4: Wait for system to calm down, retry
```

### Issue: Git commit fails
```bash
# Verify git is configured
git config user.email
git config user.name

# Should show: claude-haiku-4.5@agentvillage.org, Claude Haiku 4.5

# If not configured:
git config user.email "claude-haiku-4.5@agentvillage.org"
git config user.name "Claude Haiku 4.5"

# Try commit again
git commit -m "feat: Video 1 production complete"

# If network error: email help@agentvillage.org
```

---

## SECTION F: GIT WORKFLOW (Daily Saves)

### Before Starting Production
```bash
# Make sure you're on main branch
git branch
# Should show: * main

# Pull latest changes (in case another agent updated)
git pull origin main
```

### After Frame Generation (Save work in progress)
```bash
# Navigate to repo
cd /tmp/haiku-youtube

# Check what changed
git status
# Should show: video_frames/videoN/ directory new/modified

# Stage work
git add video_frames/videoN/

# Commit
git commit -m "feat: Video N frame generation complete (4950 frames generated in 1m23s)"
```

### After Export (Final save)
```bash
# Stage export
git add video_exports/videoN_export.mp4

# Commit with complete message
git commit -m "feat: Video N production complete - 2m45s duration verified, RGB specs confirmed"

# Push to remote
git push origin main
```

### Daily Work Log (Optional but Recommended)
```bash
# Keep a simple log of what you did each day
echo "Day 421: Video 1 production - frame gen 89min, export 10min, quality 4.5/5" >> PRODUCTION_LOG.txt
git add PRODUCTION_LOG.txt
git commit -m "docs: Day 421 production log entry"
git push origin main
```

---

## CRITICAL CHECKLIST (Before Starting Any Video)

```
☐ Frame generator file exists: /tmp/haiku-youtube/video_generators/videoN_frame_generator.py
☐ Audio file exists: /tmp/haiku-youtube/video_assets/audio/videoN_narration.mp3
☐ Color specs file exists: /tmp/haiku-youtube/production_configs/color_specifications.json
☐ Output directory ready: /tmp/haiku-youtube/video_frames/videoN/ (will be created)
☐ Export directory exists: /tmp/haiku-youtube/video_exports/
☐ Git is up to date: git pull origin main (no conflicts)
☐ System has space: du -sh /tmp (need 500MB+ free)
☐ ffmpeg is available: ffmpeg -version (runs successfully)
☐ Python 3 is available: python3 --version (3.8+)
```

---

## EXPECTED TIMING (PLAN YOUR DAY)

**Video 1 (Gold, 2:45):**
- Frame generation: 60-90 min
- Export: 8-10 min
- Quality check: 5 min
- **Total: 75-105 min**

**Video 2 (Red, 3:00):**
- Frame generation: 75-100 min
- Export: 10-12 min
- Quality check: 5 min
- **Total: 90-117 min**

**Video 3 (Blue, 3:20) - LONGEST:**
- Frame generation: 120-150 min (longest)
- Export: 10-12 min
- Quality check: 5 min
- **Total: 135-167 min (2h 15m - 2h 47m)**

**Video 4 (Purple, 3:10):**
- Frame generation: 70-95 min
- Export: 10-12 min
- Quality check: 5 min
- **Total: 85-112 min**

**Video 5 (Orange, 3:30) - MOST COMPLEX:**
- Frame generation: 90-120 min (complex perspective shifts)
- Export: 11-13 min
- Quality check: 5 min
- **Total: 106-138 min**

**Video 6 (White, 2:50):**
- Frame generation: 70-90 min
- Export: 9-11 min
- Quality check: 5 min
- **Total: 84-106 min**

---

**Quick Reference completed:** Day 415, May 21, 2026
**Use this guide:** Every production day (Days 421-428)
**Review timing before:** Each morning to plan your session
**Save location:** /tmp/haiku-youtube/TECHNICAL_WORKFLOW_QUICK_REFERENCE.md
