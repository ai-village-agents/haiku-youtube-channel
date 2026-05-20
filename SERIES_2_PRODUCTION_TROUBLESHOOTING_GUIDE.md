# SERIES 2 PRODUCTION TROUBLESHOOTING GUIDE
**Created:** Day 414, May 20, 2026  
**Status:** Complete Troubleshooting Reference  
**Purpose:** Rapid resolution of technical issues during May 27-June 4 production

---

## QUICK REFERENCE: ISSUE DECISION TREE

```
PRODUCTION PROBLEM DETECTED
    ↓
Is it a FRAME GENERATION issue?
    ├─ YES → Go to SECTION 2 (Frame Generation)
    └─ NO → Continue
    
Is it an AUDIO/SYNC issue?
    ├─ YES → Go to SECTION 3 (Audio & Sync)
    └─ NO → Continue
    
Is it a VIDEO EXPORT issue?
    ├─ YES → Go to SECTION 4 (Export & Encoding)
    └─ NO → Continue
    
Is it a COLOR/VISUAL issue?
    ├─ YES → Go to SECTION 5 (Color & Grading)
    └─ NO → Continue
    
Is it a PUBLISHING issue?
    ├─ YES → Go to SECTION 6 (YouTube Publishing)
    └─ NO → Go to SECTION 7 (Other Issues)
```

---

## 1. DIAGNOSTIC CHECKLIST (START HERE FOR ANY ISSUE)

Before diving into specific troubleshooting:

```
BASIC DIAGNOSTICS
- [ ] Git repository status clean? (git status --short)
- [ ] All expected files present?
    - [ ] video_assets/audio/video[N]_narration.mp3
    - [ ] video[N]_frame_generator.py executable?
    - [ ] production_configs/color_specifications.json valid JSON?
- [ ] Disk space available? (df -h | grep /tmp)
    - Need: 2-5 GB free for frame generation
    - Need: 1-2 GB free for final video file
- [ ] Python environment functional?
    - [ ] python --version (should be 3.x)
    - [ ] pip list | grep -i pillow (for image generation)
- [ ] System load reasonable? (top -b -n1 | head -20)
    - Acceptable load: <2.0 on 4-core system
    - If >3.0: wait or free up resources
```

---

## 2. FRAME GENERATION ISSUES

### Issue 2.1: Frame Generator Won't Start

**Symptom:** `python video[N]_frame_generator.py` produces error or no output

**Diagnosis:**
```bash
# Check if file exists and is executable
ls -l video[N]_frame_generator.py

# Verify it's valid Python
python -m py_compile video[N]_frame_generator.py

# Try running with verbose output
python -v video[N]_frame_generator.py 2>&1 | head -50
```

**Solutions (in order):**

1. **File not found**
   ```bash
   # Verify you're in correct directory
   pwd  # should show /tmp/haiku-youtube
   ls video*_frame_generator.py  # should list all 6 files
   ```

2. **Python import error** (most common)
   ```bash
   # Check required imports work
   python -c "from PIL import Image; print('PIL OK')"
   python -c "import json; print('JSON OK')"
   python -c "import math; print('Math OK')"
   ```
   
   If PIL import fails:
   ```bash
   pip install Pillow --upgrade
   ```

3. **Permission denied**
   ```bash
   # Make file executable
   chmod +x video[N]_frame_generator.py
   ```

4. **Output directory doesn't exist**
   ```bash
   # Create expected output directory
   mkdir -p video_frames
   python video[N]_frame_generator.py
   ```

**If still failing:** 
- Copy working frame generator: `cp video1_frame_generator.py video[N]_frame_generator.py`
- Edit it to reference correct video (change `video1` → `video[N]`)
- Try again

---

### Issue 2.2: Frame Generation Crashes Midway

**Symptom:** Generator starts fine, produces 500-2000 frames, then crashes

**Typical Error Messages:**
- `MemoryError` → Not enough RAM
- `IOError: [Errno 28] No space left on device` → Disk full
- `segmentation fault` → System resource exhaustion

**Solutions:**

1. **Disk Space Issue** (most common)
   ```bash
   # Check available space
   df -h /tmp
   
   # Expected: Need 1-5 GB free
   # If <500 MB free: delete old test frames
   find . -name "test_*" -type d -exec rm -rf {} \;
   find . -name "*_test" -type d -exec rm -rf {} \;
   ```

2. **Memory Issue** (if system has <8GB RAM)
   ```bash
   # Close other applications
   # Check current memory use
   free -h
   
   # Can also reduce frame batch size if generator supports it
   # (Edit video[N]_frame_generator.py and reduce batch_size variable)
   ```

3. **Resume Generation** (if you want to continue)
   ```bash
   # Check how many frames were created
   ls video_frames/video[N]/ | wc -l
   
   # Note the count, delete incomplete sequence, restart
   rm -rf video_frames/video[N]
   python video[N]_frame_generator.py
   ```

**Prevention for Future:**
- Run during off-peak hours (fewer system processes)
- Ensure 5 GB free disk space before starting
- Close unnecessary applications (Firefox, etc.)

---

### Issue 2.3: Frame Colors Look Wrong

**Symptom:** Generated frames don't match color specification

**Diagnosis:**
```bash
# Extract one frame and check its colors
ls video_frames/video[N]/ | head -1  # get first frame name
# Open in image viewer and check against color spec
```

**Solutions:**

1. **Verify color spec file is correct**
   ```bash
   # Check current color specs
   cat production_configs/color_specifications.json | grep -A5 "video[N]"
   
   # Verify JSON is valid
   python -m json.tool production_configs/color_specifications.json > /dev/null
   ```

2. **Check frame generator is using correct colors**
   ```bash
   # Edit frame generator and verify it reads color spec
   grep -n "color_specifications" video[N]_frame_generator.py
   
   # Verify it's loading JSON correctly
   grep -n "json.load" video[N]_frame_generator.py
   ```

3. **Monitor color has different gamma**
   - Colors may look different on different monitors
   - Compare frame side-by-side with reference (another image)
   - If color spec JSON is correct, frame is correct
   - Issue is likely display calibration, not frame generation

4. **Regenerate frames if confirmed incorrect**
   ```bash
   # Delete current frame set
   rm -rf video_frames/video[N]
   
   # Regenerate
   python video[N]_frame_generator.py
   ```

---

## 3. AUDIO & SYNC ISSUES

### Issue 3.1: Audio File Not Found

**Symptom:** Export fails with `narration file not found` or similar

**Solutions:**
```bash
# Verify audio file exists
ls -lh video_assets/audio/video[N]_narration.mp3

# If missing, check alternate location
find . -name "*video[N]*narration*" 2>/dev/null

# If truly missing, report to help@agentvillage.org with:
# - Which video (1-6)
# - When you started production (date/time)
```

---

### Issue 3.2: Audio/Video Out of Sync

**Symptom:** Video plays but narration doesn't match mouth movements (or scene timing)

**Diagnosis:**
```bash
# Check audio duration
ffprobe video_assets/audio/video[N]_narration.mp3 | grep Duration

# Check storyboard expected duration
grep -i "duration\|seconds\|time" SERIES_2_VIDEO_[N]_DETAILED_STORYBOARD.md
```

**Solutions:**

1. **Timing mismatch in export script**
   ```bash
   # Check the export script for audio sync settings
   grep -n "audio" export_video_with_audio.py
   grep -n "sync\|offset" export_video_with_audio.py
   
   # Verify offset is 0 (no delay should be applied)
   ```

2. **Frame count vs narration duration mismatch**
   ```bash
   # Expected frames = duration_seconds * 30 fps
   # E.g., 2:45 video = 165 seconds * 30 = 4950 frames
   
   # Check storyboard for exact duration
   grep -i "total.*frames\|duration" SERIES_2_VIDEO_[N]_DETAILED_STORYBOARD.md
   
   # Count generated frames
   ls video_frames/video[N]/ | wc -l
   ```

3. **Re-export with correct settings**
   - Verify export_video_with_audio.py is using correct audio file
   - Verify it's starting audio at frame 0 with no offset
   - Re-run export

4. **If issue persists**
   - Resync manually: `ffmpeg -i video_frames/video[N]/%06d.png -i video_assets/audio/video[N]_narration.mp3 -shortest output.mp4`
   - Or restart generation and export from scratch

---

### Issue 3.3: Audio Level Too Quiet or Too Loud

**Symptom:** Video plays but narration is hard to hear or too loud

**Diagnosis:**
```bash
# Check audio levels
ffmpeg -i video_assets/audio/video[N]_narration.mp3 -af volumedetect -f null - 2>&1 | grep -i "mean_volume\|max_volume"
```

**Solutions:**

1. **Audio too quiet**
   ```bash
   # Boost audio by 6dB (double perceived loudness)
   ffmpeg -i video_assets/audio/video[N]_narration.mp3 -af "volume=1.5" video_assets/audio/video[N]_narration_boosted.mp3
   
   # Use boosted version for export
   # Update export script or manually copy:
   # cp video_assets/audio/video[N]_narration_boosted.mp3 video_assets/audio/video[N]_narration.mp3
   ```

2. **Audio too loud**
   ```bash
   # Reduce audio by 3dB
   ffmpeg -i video_assets/audio/video[N]_narration.mp3 -af "volume=0.7" video_assets/audio/video[N]_narration_reduced.mp3
   
   # Use reduced version
   ```

3. **If narration recording is wrong**
   - Do NOT re-record (locked constraint)
   - Adjust audio levels in export phase
   - Document in production notes

---

## 4. VIDEO EXPORT & ENCODING ISSUES

### Issue 4.1: Export Fails or Produces Corrupted Video

**Symptom:** Export script errors out or creates unwatchable MP4

**Solutions:**

1. **Check ffmpeg is installed**
   ```bash
   ffmpeg -version | head -3
   
   # If not installed:
   sudo apt-get update && sudo apt-get install ffmpeg
   ```

2. **Verify export script syntax**
   ```bash
   # Check export script for syntax errors
   python -m py_compile export_video_with_audio.py
   
   # Look for common errors
   grep -n "\\\\$\|ffmpeg" export_video_with_audio.py | head -10
   ```

3. **Test with small subset first**
   ```bash
   # Create test with just first 30 frames (~1 second at 30fps)
   mkdir test_frames
   cp video_frames/video[N]/0000001.png video_frames/video[N]/0000002.png ... test_frames/
   
   # Test export with test frames
   ffmpeg -framerate 30 -i test_frames/%06d.png -i video_assets/audio/video[N]_narration.mp3 -c:v libx264 -preset fast test_output.mp4
   
   # If test works, issue is in your custom export script
   ```

4. **Check codec settings**
   ```bash
   # Verify H.264 is being used with correct settings
   grep -i "libx264\|yuv420p\|High" export_video_with_audio.py
   
   # If missing, verify against SERIES_2_EXPORT_SETTINGS.md
   ```

5. **Monitor export progress**
   ```bash
   # Watch ffmpeg output for errors
   python export_video_with_audio.py 2>&1 | tee export_log.txt
   
   # Check log after completion
   tail -50 export_log.txt
   ```

---

### Issue 4.2: Export Takes Too Long

**Symptom:** Encoding is running for >3 hours

**Context:** This is often normal!
- 4950 frames (2:45 video) at H.264 High Profile
- Typical time: 45 min - 2 hours
- Very slow systems: 2-4 hours

**If >4 hours:**

1. **Check system load**
   ```bash
   top -b -n1 | head -20
   # If load >8.0 on 4-core system, close other apps
   ```

2. **Verify encoding actually running**
   ```bash
   # Check if ffmpeg process still alive
   ps aux | grep ffmpeg
   
   # If yes, it's working (just slow)
   # If no, encoding completed or crashed
   ```

3. **Check output file growing**
   ```bash
   # Monitor output file size every 30 seconds
   watch -n30 "ls -lh output.mp4"
   
   # If size increasing steadily, encoding in progress (normal)
   # If size stalled for >5 min, encoding may have frozen
   ```

**If encoding froze:**
```bash
# Kill process
pkill -f ffmpeg

# Check partial output file
ffprobe output.mp4 2>&1 | grep -i duration

# Start over
rm output.mp4
python export_video_with_audio.py
```

---

### Issue 4.3: Output File Size Unexpected

**Symptom:** Final MP4 is 30 MB or 100+ MB (target: 50-75 MB)

**Diagnosis:**
```bash
# Check actual file size and duration
ls -lh output.mp4
ffprobe output.mp4 2>&1 | grep Duration
ffprobe output.mp4 2>&1 | grep bitrate
```

**Expected Bitrate:**
- Video: ~1500-2000 kbps (H.264 High Profile)
- Audio: ~192 kbps
- Total: ~1700-2200 kbps
- File size = (bitrate × duration) / 8
  - E.g., 2000 kbps × 165 seconds = 330 megabits = 41.25 MB

**If file is too small (<50 MB):**
- Video quality may be lower than intended
- Check ffprobe output for actual bitrate
- If <1500 kbps video, consider re-encoding with higher bitrate
- Usually acceptable if still plays correctly

**If file is too large (>75 MB):**
- Video bitrate may be excessive (>2000 kbps)
- Re-encode with explicit bitrate: `ffmpeg -i input.mp4 -b:v 1800k output.mp4`
- Check if audio is duplicate or encoded incorrectly

---

## 5. COLOR & VISUAL QUALITY ISSUES

### Issue 5.1: Color Grading Doesn't Match Specification

**Symptom:** Exported video has different colors than color_specifications.json

**Solutions:**

1. **Verify color spec file**
   ```bash
   # Check that color specs are being read
   python -c "
   import json
   with open('production_configs/color_specifications.json') as f:
       specs = json.load(f)
       print(json.dumps(specs['video_[N]'], indent=2))
   "
   ```

2. **Check frame generator uses the spec**
   ```bash
   # Verify generator loads and applies color
   grep -A10 "color_specifications\|apply.*color\|set.*background" video[N]_frame_generator.py
   ```

3. **Regenerate frames if spec looks wrong**
   ```bash
   rm -rf video_frames/video[N]
   python video[N]_frame_generator.py
   ```

4. **If colors still don't match**
   - Issue may be monitor calibration, not actual frame colors
   - Verify frames in terminal: `ffprobe -show_frames video_frames/video[N]/0000001.png | grep pix_fmt`
   - File format should show RGB/YUV correctly
   - If format wrong, regenerate with corrected frame generator

---

### Issue 5.2: Visual Artifacts or Corruption in Output

**Symptom:** Banding, pixelation, noise, or strange visual glitches in final video

**Solutions:**

1. **Check frame quality**
   ```bash
   # Inspect a sample frame
   ffprobe video_frames/video[N]/0000100.png
   
   # Look for compression or corruption
   file video_frames/video[N]/0000100.png
   ```

2. **Verify export codec settings**
   ```bash
   # H.264 encoding with yuv420p should prevent most artifacts
   # Check your export command includes:
   # -c:v libx264 -pix_fmt yuv420p -preset medium
   
   grep "pix_fmt\|preset" export_video_with_audio.py
   ```

3. **If frames themselves corrupted**
   ```bash
   # Regenerate frame set
   rm -rf video_frames/video[N]
   python video[N]_frame_generator.py
   ```

4. **If export creates corruption from good frames**
   ```bash
   # Try slower encoding preset (higher quality)
   ffmpeg -framerate 30 -i video_frames/video[N]/%06d.png \
           -i video_assets/audio/video[N]_narration.mp3 \
           -c:v libx264 -pix_fmt yuv420p -preset slow \
           -crf 18 output.mp4
   ```

---

## 6. YOUTUBE PUBLISHING ISSUES

### Issue 6.1: Can't Upload Video to YouTube

**Symptom:** YouTube Studio won't accept MP4 file or upload fails midway

**Solutions:**

1. **Verify file format**
   ```bash
   ffprobe output.mp4 | grep "codec_name\|Duration"
   
   # Should show:
   # codec_name: h264 (video codec)
   # Duration: ~2:45 or ~3:00 (matches expected)
   ```

2. **Check file integrity**
   ```bash
   # Verify file plays correctly
   ffmpeg -i output.mp4 -f null - 2>&1 | grep -i error
   
   # If no errors, file is valid
   ```

3. **Try uploading again**
   - Refresh YouTube Studio page
   - Sign out and sign back in
   - Try a different browser
   - Wait 10 minutes (YouTube servers might be rate-limiting)

4. **If file is actually corrupted**
   - Delete output.mp4
   - Regenerate frames: `python video[N]_frame_generator.py`
   - Re-export: `python export_video_with_audio.py`
   - Try upload again

---

### Issue 6.2: Can't Find "Public" Button or Set Visibility

**Symptom:** YouTube Studio is open but "Public" radio button not visible

**Solutions:**

1. **Scroll down in visibility panel**
   - YouTube UI may require scrolling within the visibility section
   - Look for "Public", "Unlisted", "Private" options

2. **Use keyboard navigation**
   ```
   - Press Tab repeatedly to navigate to visibility options
   - Press Space to select "Public"
   - Press Enter to confirm
   ```

3. **Try full-page refresh**
   - Ctrl+F5 (hard refresh, clear cache)
   - Wait for page to fully load
   - Try visibility change again

4. **Check browser console for errors**
   - F12 (Developer Tools)
   - Console tab
   - Look for red error messages
   - Screenshot and report to help@agentvillage.org if errors appear

---

### Issue 6.3: Video Uploaded But Won't Show as "Published"

**Symptom:** Video shows in uploads but doesn't have "Published" status

**Solutions:**

1. **Wait for processing**
   - YouTube processes for variable time (usually <1 hour)
   - Check video status icon next to title
   - Refresh page every 5 minutes

2. **Check for processing issues**
   - Click on video thumbnail
   - Look for error messages or warnings
   - If "Content ID match" or copyright notice: contact help@agentvillage.org

3. **Verify visibility is actually set to Public**
   - Click video again
   - Click "Details"
   - Scroll to visibility
   - Confirm "Public" is selected (should be radio button marked)

4. **If still stuck**
   - Delete video (YouTube Studio → 3-dot menu → Delete)
   - Wait 30 seconds
   - Re-upload and set to Public immediately

---

## 7. OTHER ISSUES & EDGE CASES

### Issue 7.1: Git Repository Issues

**Symptom:** `git status` shows errors or unexpected state

**Solutions:**
```bash
# Check repository health
git fsck

# Check current branch
git branch

# Verify upstream
git remote -v

# If corrupted, contact help@agentvillage.org with:
git log --oneline | head -5
git status
git fsck output
```

---

### Issue 7.2: Out of Disk Space During Production

**Symptom:** Frame generation stops with "No space left on device"

**Solutions:**
```bash
# Check available space
df -h /tmp

# Clean up unneeded files
rm -rf video_frames/video1  # if not needed
rm -rf test_* output_test*
find . -name "*.bak" -delete

# Check what's taking space
du -sh */ | sort -rh | head -5

# If severely constrained:
# Contact help@agentvillage.org for storage support
```

---

### Issue 7.3: Frame Generator Runs But Produces No Frames

**Symptom:** Script completes with "0 frames generated" or empty directory

**Solutions:**

1. **Check output directory**
   ```bash
   ls -la video_frames/
   # If video_frames/video[N] doesn't exist, script didn't create it
   ```

2. **Review frame generator code**
   ```bash
   grep -n "output.*directory\|mkdir\|video_frames" video[N]_frame_generator.py
   ```

3. **Run with verbose output**
   ```bash
   python video[N]_frame_generator.py 2>&1 | head -100
   # Look for any error messages
   ```

4. **Manual frame directory creation**
   ```bash
   mkdir -p video_frames/video[N]
   python video[N]_frame_generator.py
   ```

---

## 8. WHEN TO ESCALATE

Contact help@agentvillage.org if:

- [ ] Technical issue persists after trying all solutions above
- [ ] Git repository appears corrupted
- [ ] Disk space exhausted and can't continue production
- [ ] ffmpeg crashes with segmentation fault
- [ ] YouTube upload fails with specific error code
- [ ] Quality metrics fundamentally impossible to achieve (score <4.0 unavoidable)

**Include in support email:**
- Which video number (1-6) and date (May 27-June 4)
- Exact error message or symptom
- Steps already tried
- Output of: `git log --oneline | head -5` and `git status`
- Output of: `ls -lh video_assets/audio/video*narration.mp3`

---

## 9. QUICK REFERENCE: COMMAND CHEAT SHEET

```bash
# FRAME GENERATION
python video[N]_frame_generator.py

# AUDIO VERIFICATION
ffprobe video_assets/audio/video[N]_narration.mp3 | grep Duration

# FRAME COUNT
ls video_frames/video[N]/ | wc -l

# VIDEO EXPORT
python export_video_with_audio.py

# VIDEO VERIFICATION
ffprobe output.mp4 | grep -E "codec_name|Duration|bitrate"

# GIT STATUS
git status --short && git rev-parse --short HEAD

# DISK SPACE
df -h /tmp

# PROCESS MONITORING
top -b -n1 | head -20
```

---

**STATUS: 🟢 TROUBLESHOOTING GUIDE COMPLETE**
Ready for May 27 production phase.
