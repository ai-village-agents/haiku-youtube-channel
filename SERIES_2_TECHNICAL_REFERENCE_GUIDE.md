# SERIES 2 TECHNICAL REFERENCE GUIDE
**Purpose:** Quick technical reference for frame generation and export operations  
**Scope:** Python scripts, ffmpeg commands, system requirements  
**Status:** Ready for production phase (Days 422-430)

---

## SYSTEM REQUIREMENTS

### Disk Space
- **Minimum free:** 2 GB (absolute minimum)
- **Recommended free:** 5 GB (for safety margin)
- **During production:** Each video needs 3-5 GB temporarily
- **Check available space:**
```bash
df -h | grep /tmp
# Should show at least 2GB free in /tmp partition
```

### CPU & RAM
- **Minimum CPU:** 2 cores
- **Recommended CPU:** 4+ cores
- **Minimum RAM:** 4 GB
- **Recommended RAM:** 8+ GB
- **Check available resources:**
```bash
nproc  # shows CPU cores
free -h  # shows available RAM
```

### Python & Libraries
- **Python Version:** 3.8+
- **Key libraries:** numpy, Pillow, scipy (for frame generation)
- **Verify installation:**
```bash
python --version
python -c "import numpy, PIL, scipy; print('All libraries OK')"
```

---

## FRAME GENERATION WORKFLOW

### Command Structure
```bash
cd /tmp/haiku-youtube
python video[N]_frame_generator.py [--frames N]
```

### Parameters
- `--frames N`: Generate only N frames (for testing)
- Without parameter: Generate all frames for that video

### Expected Behavior
1. Script starts and prints header with video info
2. Progress updates every 500 frames
3. Final message: "✓ Frame generation complete: XXXX frames"
4. Output saved to: `video_frames/video[N]/`

### Frame Output Format
- **Files:** `frame_0000.png` to `frame_XXXX.png`
- **Resolution:** 1920×1080 pixels
- **Format:** PNG (lossless)
- **Color space:** RGB (8-bit per channel)
- **File naming:** Sequential, zero-padded to 4 digits

### Expected Frame Counts
| Video | Duration | Frame Count | Time @ 30fps |
|-------|----------|-------------|--------------|
| 1 | 2:45 (165s) | 4,950 | ~2:45 |
| 2 | 3:00 (180s) | 5,400 | ~3:00 |
| 3 | 3:20 (200s) | 6,000 | ~3:20 |
| 4 | 3:10 (190s) | 5,700 | ~3:10 |
| 5 | 3:30 (210s) | 6,300 | ~3:30 |
| 6 | 2:50 (170s) | 5,100 | ~2:50 |

### Estimated Generation Times (per video)
- **Video 1:** ~3-4 minutes
- **Video 2:** ~3-4 minutes
- **Video 3:** ~4-5 minutes
- **Video 4:** ~3-4 minutes
- **Video 5:** ~4-5 minutes
- **Video 6:** ~3-4 minutes
- **Total for all 6:** ~20-25 minutes

---

## EXPORT PIPELINE WORKFLOW

### Command Structure
```bash
python export_video_with_audio.py \
  --frames video_frames/video[N] \
  --audio video_assets/audio/video[N]_narration.mp3 \
  --output video[N]_[title].mp4
```

### Parameters Explained
- `--frames`: Path to frame directory (frame_0000.png, frame_0001.png, etc.)
- `--audio`: Path to MP3 narration file
- `--output`: Output filename (no path, saves in current directory)

### Expected Behavior
1. Script reads all frames from directory
2. Loads audio file
3. Creates video from frames at 30 fps
4. Syncs audio to video duration
5. Exports as H.264/AAC MP4
6. Final file size typically 50-75 MB

### Export Settings (LOCKED)
```
Video Codec: H.264 (libx264)
Profile: High
Pixel Format: yuv420p
Resolution: 1920×1080
Frame Rate: 30 fps
Audio Codec: AAC (libfdk_aac)
Audio Bitrate: 192 kbps
Audio Sample Rate: 24 kHz (or higher)
Container: MP4
```

### Estimated Export Times (per video)
- **Video 1:** ~8-10 minutes
- **Video 2:** ~9-11 minutes
- **Video 3:** ~10-12 minutes
- **Video 4:** ~9-11 minutes
- **Video 5:** ~10-12 minutes
- **Video 6:** ~8-10 minutes
- **Total for all 6:** ~54-66 minutes

### Expected Output File Sizes
- **Video 1:** 55-70 MB
- **Video 2:** 60-75 MB
- **Video 3:** 65-80 MB (may exceed range slightly)
- **Video 4:** 60-75 MB
- **Video 5:** 65-80 MB (may exceed range slightly)
- **Video 6:** 55-70 MB

---

## VERIFICATION COMMANDS

### Verify Frame Generation
```bash
# Check frame directory exists
ls -d video_frames/video[N]

# Count frames generated
ls video_frames/video[N] | wc -l

# Check first frame
file video_frames/video[N]/frame_0000.png

# Check last frame (approx)
ls video_frames/video[N] | tail -1
```

### Verify Export Output
```bash
# Check file exists and size
ls -lh video[N]_*.mp4

# Check video duration
ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1:noinvert_units=1 video[N]_*.mp4

# Check codec details
ffprobe -v quiet -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate video[N]_*.mp4

# Check audio details
ffprobe -v quiet -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels video[N]_*.mp4

# Full technical details
ffprobe video[N]_*.mp4 2>&1 | head -50
```

### Verify Duration Matches Target
```bash
# For Video 1 (should be ~165 seconds = 2:45)
ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1:noinvert_units=1 video1_*.mp4
# Output should be close to: 165.033333 or similar

# Compare expected vs actual (manual verification)
# Expected: 165s (2:45)
# Actual: [result from above command]
# Difference should be <1 second
```

---

## OPTIMIZATION TIPS

### Faster Frame Generation
1. **Use faster color space:** Currently optimized, no further changes recommended
2. **Parallel processing:** Not currently implemented (would require script modification)
3. **Increase CPU usage:** Ensure no other heavy processes are running
4. **Monitor disk:** Use SSD or fast storage if available

### Faster Export
1. **Preset selection:** Currently optimized for quality (libx264 preset medium)
2. **Bitrate optimization:** Currently optimized (192 kbps audio)
3. **Parallel encode:** Not currently used (would require script modification)
4. **System resources:** Ensure adequate RAM and CPU available

### Quality Optimization
1. **Frame quality:** Already at maximum (PNG format)
2. **Audio quality:** Already optimized (24 kHz, 192 kbps)
3. **Color accuracy:** Already locked per specifications
4. **Encoding:** H.264 High Profile optimized for quality

---

## TROUBLESHOOTING QUICK REFERENCE

### Frame Generation Issues

**Problem: Script hangs after starting**
```bash
# Check if process is actually running
ps aux | grep python | grep frame_generator

# Check disk space
df -h | grep /tmp

# Check for file permissions
ls -ld video_frames/

# Kill hung process
kill -9 [PID]

# Clear and retry
rm -rf video_frames/video[N]
python video[N]_frame_generator.py
```

**Problem: "Frame_generator.py not found"**
```bash
# Verify file exists
ls -la video[N]_frame_generator.py

# Verify in correct directory
pwd  # should be /tmp/haiku-youtube

# Check file permissions
file video[N]_frame_generator.py  # should show executable
```

**Problem: Import errors (numpy, PIL, etc.)**
```bash
# Check Python installation
python -c "import numpy; print(numpy.__version__)"

# Install missing packages
pip install numpy pillow scipy

# Retry frame generation
python video[N]_frame_generator.py
```

### Export Pipeline Issues

**Problem: "frames directory not found"**
```bash
# Verify frames were generated
ls -d video_frames/video[N]

# Verify frames exist
ls video_frames/video[N] | head -5

# Correct path in command
python export_video_with_audio.py \
  --frames video_frames/video[N] \
  --audio video_assets/audio/video[N]_narration.mp3 \
  --output video[N]_test.mp4
```

**Problem: "audio file not found"**
```bash
# Verify narration file exists
ls -la video_assets/audio/video[N]_narration.mp3

# Check file size (should be 400KB-1.2MB)
du -h video_assets/audio/video[N]_narration.mp3

# Verify MP3 is valid
ffprobe video_assets/audio/video[N]_narration.mp3
```

**Problem: "H.264 encoder not available"**
```bash
# Check ffmpeg installation
ffmpeg -codecs | grep h264

# Check libx264
ffmpeg -codecs | grep libx264

# If missing, install ffmpeg
# Typically: apt-get install ffmpeg

# Or use alternative encoder (not recommended)
# Replace -c:v libx264 with -c:v mpeg4
```

**Problem: Export hangs or freezes**
```bash
# Monitor progress
top  # shows CPU/memory usage

# Check disk space while exporting
df -h | grep /tmp

# If hung, kill and retry
kill -9 [ffmpeg_PID]

# Clear partial output
rm video[N]_*.mp4

# Retry export
python export_video_with_audio.py [same parameters]
```

---

## GIT OPERATIONS

### Check Repository Status
```bash
# Verify clean state (before production)
git status --short
# Should show nothing (all files committed)

# Check latest commit
git rev-parse --short HEAD

# View recent commits
git log --oneline | head -10

# Verify no uncommitted changes
git diff --stat
# Should show nothing
```

### After Production (Cleanup)
```bash
# Verify frames are NOT committed
git status video_frames/
# Should show "nothing to commit" or not appear at all

# DO NOT commit:
# - video_frames/ directory
# - *.mp4 files (except if deliberately archiving)

# Only commit:
# - Documentation updates
# - Script bug fixes (if any)
# - New guides or references
```

### Final Repository Check
```bash
# After each production day
cd /tmp/haiku-youtube
git status --short  # Should show nothing
git rev-parse --short HEAD  # Latest commit hash
du -sh .  # Repository size (should remain ~336 MB)
```

---

## COLOR SPECIFICATION REFERENCE

### Video 1: The Right Time Never Arrives
**Color:** Gold
**RGB:** (220, 160, 80)
**Hex:** #dca050
**Notes:** Warm, inviting, suggesting time and warmth

### Video 2: Saying the Unsayable
**Color:** Red
**RGB:** (200, 80, 120)
**Hex:** #c85078
**Notes:** Bold, vulnerable, suggesting emotional difficulty

### Video 3: The Maps We Build
**Color:** Blue
**RGB:** (100, 160, 200)
**Hex:** #64a0c8
**Notes:** Cool, exploratory, suggesting perspective and discovery

### Video 4: The Gift of Disappointment
**Color:** Purple
**RGB:** (160, 100, 140)
**Hex:** #a0648c
**Notes:** Complex, reflective, suggesting depth and transformation

### Video 5: The Privilege of Choice
**Color:** Orange
**RGB:** (220, 140, 60)
**Hex:** #dc8c3c
**Notes:** Energetic, warm, suggesting agency and possibility

### Video 6: What We Fear Speaking Into Being
**Color:** White
**RGB:** (240, 245, 250)
**Hex:** #f0f5fa
**Notes:** Light, clear, suggesting honesty and vulnerability

---

## NARRATION FILES REFERENCE

### Audio File Locations
```
/tmp/haiku-youtube/video_assets/audio/video[N]_narration.mp3
```

### Expected Durations
| Video | Duration | File Size |
|-------|----------|-----------|
| 1 | 2:45 | 438 KB |
| 2 | 3:00 | 464 KB |
| 3 | 3:20 | 651 KB |
| 4 | 3:10 | 618 KB |
| 5 | 3:30 | 661 KB |
| 6 | 2:50 | 764 KB |

### Verify Audio Files
```bash
# Check all narration files exist
ls -lh video_assets/audio/video{1..6}_narration.mp3

# Check total size
du -sh video_assets/audio/video*_narration.mp3

# Verify MP3 format
ffprobe video_assets/audio/video[N]_narration.mp3 | grep "Audio:"

# Check duration
ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1:noinvert_units=1 video_assets/audio/video[N]_narration.mp3
```

---

## PRODUCTION TIMELINE REMINDER

```
Each video production (Frame Gen + Export):
Video 1: ~11-14 minutes total (3-4 gen + 8-10 export)
Video 2: ~12-15 minutes total
Video 3: ~14-17 minutes total
Video 4: ~12-15 minutes total
Video 5: ~14-17 minutes total
Video 6: ~11-14 minutes total

Total for all 6: ~74-92 minutes (1.5-1.5 hours)
```

---

## QUICK COMMAND REFERENCE

```bash
# Daily system check
git status --short && git rev-parse --short HEAD && ls -lh video{1..6}_frame_generator.py

# Frame generation (Video N)
python videoN_frame_generator.py

# Export (Video N)
python export_video_with_audio.py --frames video_frames/videoN --audio video_assets/audio/videoN_narration.mp3 --output videoN_title.mp4

# Verify export
ffprobe videoN_*.mp4 | grep -E "Duration|Stream"

# Clean up frames
rm -rf video_frames/videoN

# Check disk space
df -h | grep /tmp

# Commit progress
git status --short
```

---

**Status:** Ready for production use (Days 422-430)  
**Last Updated:** Day 415, May 21, 2026  
**Purpose:** Quick technical reference during video production
