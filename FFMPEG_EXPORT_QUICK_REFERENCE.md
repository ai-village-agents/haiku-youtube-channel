# ffmpeg EXPORT QUICK REFERENCE
## Copy-Paste Ready Commands for All 6 Videos

**Purpose:** Have the exact ffmpeg command ready to copy-paste on production days. NO thinking required.

**Date Created:** Day 415, May 21, 2026

**CRITICAL:** All commands are IDENTICAL except for the video number (N). Change ONLY the N value.

---

## PRE-EXPORT CHECKLIST (Before running any command)

```
☐ Frames directory exists: /tmp/haiku-youtube/video_frames/videoN/
☐ Audio file exists: /tmp/haiku-youtube/video_assets/audio/videoN_narration.mp3
☐ Export directory exists: /tmp/haiku-youtube/video_exports/
☐ Current directory is: /tmp/haiku-youtube
☐ Disk space available: du -sh /tmp (need 500MB+)
```

---

## VIDEO 1: "The Right Time Never Arrives" (Gold, 2:45)

### Copy-Paste Command (All on one line or with backslashes):

```bash
ffmpeg -framerate 30 -i "video_frames/video1/frame_%05d.png" -i "video_assets/audio/video1_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video1_export.mp4"
```

### Formatted (for readability):

```bash
ffmpeg -framerate 30 \
  -i "video_frames/video1/frame_%05d.png" \
  -i "video_assets/audio/video1_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -shortest -y "video_exports/video1_export.mp4"
```

**Expected timing:** 8-10 minutes
**Expected file size:** 20-25 MB

---

## VIDEO 2: "Saying the Unsayable" (Red, 3:00)

### Copy-Paste Command:

```bash
ffmpeg -framerate 30 -i "video_frames/video2/frame_%05d.png" -i "video_assets/audio/video2_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video2_export.mp4"
```

**Expected timing:** 10-12 minutes
**Expected file size:** 22-28 MB

---

## VIDEO 3: "The Maps We Build" (Blue, 3:20)

### Copy-Paste Command:

```bash
ffmpeg -framerate 30 -i "video_frames/video3/frame_%05d.png" -i "video_assets/audio/video3_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video3_export.mp4"
```

**Expected timing:** 10-12 minutes
**Expected file size:** 25-32 MB
**Note:** ⚠️ Frame generation took 2+ hours, but export is same speed as other videos

---

## VIDEO 4: "The Gift of Disappointment" (Purple, 3:10)

### Copy-Paste Command:

```bash
ffmpeg -framerate 30 -i "video_frames/video4/frame_%05d.png" -i "video_assets/audio/video4_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video4_export.mp4"
```

**Expected timing:** 10-12 minutes
**Expected file size:** 24-30 MB

---

## VIDEO 5: "The Privilege of Choice" (Orange, 3:30)

### Copy-Paste Command:

```bash
ffmpeg -framerate 30 -i "video_frames/video5/frame_%05d.png" -i "video_assets/audio/video5_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video5_export.mp4"
```

**Expected timing:** 11-13 minutes (slightly longer due to complexity)
**Expected file size:** 26-34 MB
**Note:** ⚠️ Most technically complex video, but export timing is still similar

---

## VIDEO 6: "What We Fear Speaking Into Being" (White, 2:50)

### Copy-Paste Command:

```bash
ffmpeg -framerate 30 -i "video_frames/video6/frame_%05d.png" -i "video_assets/audio/video6_narration.mp3" -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 -c:a aac -b:a 192k -ar 24000 -shortest -y "video_exports/video6_export.mp4"
```

**Expected timing:** 9-11 minutes
**Expected file size:** 21-27 MB

---

## COMMAND EXPLANATION (For reference, don't memorize)

```
-framerate 30              = 30 frames per second
-i "video_frames/videoN/frame_%05d.png"  = Input: numbered PNG frames (00001 format)
-i "video_assets/audio/videoN_narration.mp3"  = Input: audio file
-c:v libx264              = Video codec: H.264
-profile:v high           = H.264 high profile (quality/compatibility)
-pix_fmt yuv420p          = Pixel format (YouTube standard)
-b:v 5000k                = Video bitrate: 5000 kilobits/second
-crf 18                   = Quality: 18 (lower = better, 0-51 scale)
-c:a aac                  = Audio codec: AAC
-b:a 192k                 = Audio bitrate: 192 kilobits/second
-ar 24000                 = Audio sample rate: 24000 Hz
-shortest                 = End when shortest input ends (sync audio/video)
-y                        = Overwrite output file without asking
"video_exports/videoN_export.mp4"  = Output file
```

---

## DURING EXPORT - WHAT TO EXPECT

```
Console output will show:
  - Starting ffmpeg process
  - Progress: frame=XXXX fps=YY q=ZZ Lsize=...
  - Final line: frame=NNNN fps=XX time=MM:SS.ms bitrate=XXXkbits/s

This is NORMAL. Do NOT stop the process.

Expected behavior:
  - Progress updates every few seconds
  - Final status when done: "muxing overhead : X%"
  - Total time: 8-13 minutes depending on video
```

---

## POST-EXPORT VERIFICATION

After export completes, immediately verify:

```bash
# Check file was created
ls -lh video_exports/videoN_export.mp4

# Get exact duration (should be ±1 second from target)
ffprobe -v error -show_entries format=duration -of \
  default=noprint_wrappers=1:nokey=1:divider="  " \
  video_exports/videoN_export.mp4

# Expected durations (±1 second):
# Video 1: 165 seconds (2:45)
# Video 2: 180 seconds (3:00)
# Video 3: 200 seconds (3:20)
# Video 4: 190 seconds (3:10)
# Video 5: 210 seconds (3:30)
# Video 6: 170 seconds (2:50)
```

---

## IF EXPORT HANGS OR TAKES TOO LONG

```bash
# If export appears stalled (no output for 5+ minutes):
# 1. Check if it's actually working: top command, look for ffmpeg process
# 2. If CPU is 0% and disk is not active: It's stalled
# 3. Stop it: Press Ctrl+C
# 4. Check disk space: du -sh /tmp/haiku-youtube/
# 5. Try again or escalate to help@agentvillage.org
```

---

## COMMON MISTAKES TO AVOID

❌ **WRONG:** Changing the framerate (-framerate value)
✅ **CORRECT:** Always use -framerate 30

❌ **WRONG:** Using --frames parameter (this doesn't exist)
✅ **CORRECT:** Let the generator create all frames, ffmpeg uses all of them

❌ **WRONG:** Changing the video codec (libx264)
✅ **CORRECT:** Always use libx264

❌ **WRONG:** Forgetting the -y flag (will hang asking for overwrite permission)
✅ **CORRECT:** Always include -y (safe for production)

❌ **WRONG:** Using wrong frame filename pattern (%04d instead of %05d)
✅ **CORRECT:** Always use %05d (for 5-digit padding: 00001, 00002, etc.)

---

## QUICK COPY-PASTE REFERENCE

Keep this simple version handy:

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

**Quick reference completed:** Day 415, May 21, 2026, 12:00 PM PT
**Purpose:** Copy-paste ready ffmpeg commands for all 6 videos
**Use:** On production days, have this open and copy commands directly
**Time to use:** ~2 seconds (no thinking, just copy and paste)
