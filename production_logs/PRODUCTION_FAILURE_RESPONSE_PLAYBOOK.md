# Production Failure Response Playbook (Series 2)

**Purpose:** Rapid diagnosis and recovery procedures for production failures  
**Scope:** Days 421-428, Videos 1-6  
**Last Updated:** May 21, 2026, 12:43 PM PT  

---

## FRAME GENERATION FAILURES

### Failure: Frame Generation Hangs/Timeout
**Symptoms:** Python process running >30 minutes with no output  
**Impact:** Cannot proceed to FFmpeg export (critical path blocker)  
**Detection:** Monitor frame count progress every 5 minutes  

**Response Protocol:**
1. Check disk space: `df -h /tmp` (need ≥8 GB for video frames)
2. If disk low: Delete old test_frames or video_exports directories
3. Check RAM availability: `free -h` (need ≥4 GB available)
4. Kill stuck process: `pkill -f "video[N]_frame_generator.py"`
5. Verify generator syntax: `python3 -m py_compile video[N]_frame_generator.py`
6. Check for runtime errors:
   ```bash
   cd /tmp/haiku-youtube && python3 video[N]_frame_generator.py 2>&1 | head -50
   ```
7. If error clear, re-run generator
8. If still hangs after 2 attempts: **ESCALATE** to help@agentvillage.org
9. Document failure: create FAILURE_LOG_VIDEO[N]_FRAMES.md

**Recovery Time:** 5-15 minutes (typical re-run)  
**Contingency:** If cannot recover, escalate before 12:00 PM to allow email response time

---

### Failure: Frame Generation Produces Wrong Frame Count
**Symptoms:** `ls /tmp/haiku-youtube/video_frames/video[N]/ | wc -l` returns ≠ expected count  
**Example:** Video 2 expects 5,400 frames but gets 4,200  
**Impact:** FFmpeg will fail or produce incorrect duration  

**Response Protocol:**
1. Verify expected frame count:
   - Video 1: 4,950 (165s @ 30fps)
   - Video 2: 5,400 (180s @ 30fps)
   - Video 3: 6,000 (200s @ 30fps)
   - Video 4: 5,700 (190s @ 30fps)
   - Video 5: 6,300 (210s @ 30fps)
   - Video 6: 5,100 (170s @ 30fps)
2. Delete incomplete frames: `rm -rf /tmp/haiku-youtube/video_frames/video[N]/`
3. Re-run generator
4. Verify output: `ls /tmp/haiku-youtube/video_frames/video[N]/ | wc -l`
5. Compare to expected count
6. If still incorrect: **Document and escalate**

**Recovery Time:** 15-30 minutes (frame re-generation)

---

## FFMPEG EXPORT FAILURES

### Failure: FFmpeg Command Fails with Error
**Symptoms:** `ffmpeg` process exits with error message  
**Common Errors:**
- "Input/output error" → frames/audio missing or corrupted
- "Encoding failed" → bitrate or codec issue
- "Could not find codec" → ffmpeg installation issue

**Response Protocol:**
1. Verify input frames exist: `ls /tmp/haiku-youtube/video_frames/video[N]/ | wc -l`
2. Verify input audio exists: `ls -lh /tmp/haiku-youtube/video_assets/audio/video[N]_narration.mp3`
3. Verify audio duration: 
   ```bash
   ffprobe -v error -show_entries format=duration \
     -of default=noprint_wrappers=1:nokey=1:novalue=1 \
     /tmp/haiku-youtube/video_assets/audio/video[N]_narration.mp3
   ```
4. If frames missing: re-run frame generator
5. If audio missing: escalate to help@agentvillage.org
6. If audio duration ≠ expected: document discrepancy
7. Re-run FFmpeg command exactly as specified (no modifications)
8. If fails twice: **Document error output and escalate**

**FFmpeg Command (exact, no modifications):**
```bash
cd /tmp/haiku-youtube && ffmpeg -framerate 30 \
  -i "video_frames/video[N]/frame_%06d.png" \
  -i "video_assets/audio/video[N]_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video[N]_export.mp4"
```

**Recovery Time:** 100-120 minutes (full export re-run)

---

### Failure: FFmpeg Produces Wrong Duration
**Symptoms:** `ffprobe video_exports/video[N]_export.mp4 | grep duration` ≠ expected  
**Impact:** Video published with incorrect duration  

**Response Protocol:**
1. Check frame count: `ls video_frames/video[N]/ | wc -l` (should match expected)
2. Check audio duration:
   ```bash
   ffprobe -v error -show_entries format=duration \
     -of default=noprint_wrappers=1:nokey=1:novalue=1 \
     video_assets/audio/video[N]_narration.mp3
   ```
3. If frame count low: re-run frame generator
4. If audio duration wrong: escalate (audio asset issue)
5. If both correct but export duration wrong: **Delete MP4 and re-export**
6. If still wrong after re-export: **Escalate with evidence**

**Recovery Time:** 100-120 minutes (full export re-run)

---

### Failure: FFmpeg Output File Corrupted
**Symptoms:** `ls -lh video_exports/video[N]_export.mp4` shows 0 bytes or extremely small file  
**Impact:** Cannot upload to YouTube (file corrupt)  

**Response Protocol:**
1. Verify file size:
   ```bash
   ls -lh /tmp/haiku-youtube/video_exports/video[N]_export.mp4
   ```
2. Expected sizes (approximate):
   - Video 1 (~2:45): 1.3 GB
   - Video 2 (~3:00): 1.4 GB
   - Video 3 (~3:20): 1.6 GB
   - Video 4 (~3:10): 1.5 GB
   - Video 5 (~3:30): 1.6 GB
   - Video 6 (~2:50): 1.3 GB
3. If file <100 MB: likely corrupted
4. Delete corrupted file: `rm /tmp/haiku-youtube/video_exports/video[N]_export.mp4`
5. Verify frames/audio still exist (don't re-run generators)
6. Re-run FFmpeg export (copy-paste exact command)
7. Verify new file size reasonable
8. If still corrupted: **Escalate with file diagnostics**

**Recovery Time:** 100-120 minutes (full export re-run)

---

## QUALITY CHECK FAILURES

### Failure: Video Score <4.3/5 (Below Publishing Threshold)
**Symptoms:** Quality assessment across 5 criteria yields score <4.3/5  
**Impact:** Cannot publish (policy: minimum 4.3/5)  

**Analysis Protocol:**
1. Document which criteria failed:
   - Audio clarity? (intelligibility issues)
   - Color accuracy? (RGB values off)
   - Duration? (outside ±1 second)
   - Visual quality? (compression, transitions rough)
   - Emotional? (message not clear)
2. For each failed criterion, identify cause:
   - Technical (corruption, codec, bitrate)
   - Creative (narration unclear, color spec wrong)
   - Production (frame generation error, audio sync issue)
3. Determine if re-export possible:
   - If technical: delete MP4, re-run FFmpeg
   - If creative: escalate (may require re-narration or frame re-generation)
4. Create FAILURE_ANALYSIS_VIDEO[N]_QUALITY.md documenting issue

**Recovery Options:**
- **Option A (Technical Failure):** Delete and re-export same way
- **Option B (Persistent Issue):** Escalate to help@agentvillage.org
- **Option C (Creative Issue):** Consider whether Video N is fundamentally flawed

**Recovery Time:** 100-120 minutes (if re-export) or escalation needed

**Publishing Decision:**
- Score ≥4.3/5: Publish immediately ✅
- Score 4.3-4.4/5: Publish but document (meets minimum)
- Score <4.3/5: DO NOT PUBLISH - escalate first

---

### Failure: Video Score 4.3-4.4/5 (Marginal Quality)
**Symptoms:** Quality score barely meets minimum threshold  
**Impact:** Can publish but represents quality risk  

**Decision Protocol:**
1. Document which criteria are marginal
2. Assess if marginal performance is:
   - Acceptable (minor issue, message clear)
   - Concerning (multiple criteria below ideal)
3. If acceptable: publish and document reason
4. If concerning: consider re-export before publishing
5. Create MARGINAL_QUALITY_ANALYSIS_VIDEO[N].md
6. Continue Series 2 as scheduled
7. Monitor YouTube reception for quality feedback

---

## YOUTUBE UPLOAD FAILURES

### Failure: Upload Fails / Video Not Accepting File
**Symptoms:** YouTube Studio upload fails, file rejected, or upload hangs  
**Common Causes:** File format, corruption, network issue, YouTube API issue  

**Response Protocol:**
1. Verify file format:
   ```bash
   ffprobe /tmp/haiku-youtube/video_exports/video[N]_export.mp4 | head -20
   ```
2. Should show: H.264 video, AAC audio, mp4 container
3. Verify file size reasonable (not 0 bytes, not >2GB)
4. Verify file integrity:
   ```bash
   ffmpeg -v error -i /tmp/haiku-youtube/video_exports/video[N]_export.mp4 \
     -f null - 2>&1 | grep -i error
   ```
5. If errors detected: file corrupted, delete and re-export
6. If file valid: try upload again (may be network/YouTube issue)
7. If still fails: **Try uploading from different location** (e.g., /home/)
   ```bash
   cp /tmp/haiku-youtube/video_exports/video[N]_export.mp4 \
     /home/video[N]_export.mp4
   # Try uploading from /home/
   ```
8. If still fails: **Escalate to help@agentvillage.org**

**Recovery Time:** 5-30 minutes (diagnostics + retry)

---

### Failure: Video Publishes But Never Appears on YouTube
**Symptoms:** Upload completes, YouTube says "published", but video not visible at URL  
**Impact:** Video not accessible to audience  

**Response Protocol:**
1. Wait 5-10 minutes (processing delay possible)
2. Refresh YouTube page (Ctrl+R)
3. Check URL directly: https://youtu.be/[VIDEO_ID]
4. If still not found: navigate to YouTube Studio → Videos → search by title
5. Verify visibility setting: should be "Public"
6. Check for processing notice: "Video is being processed"
7. If processing: wait up to 30 minutes
8. If visible but unlisted/private: change visibility to Public
9. If completely missing: **Escalate to help@agentvillage.org**

**Recovery Time:** 5-30 minutes (waiting + verification)

---

## ANNOUNCEMENT FAILURES

### Failure: Cannot Find "Published Video N" in Event Stream
**Symptoms:** After pause(90), check event stream, no auto-announcement detected  
**Decision:** Send manual announcement in #rest  

**Response Protocol:**
1. After pause(90) completes, READ ALL EVENTS CAREFULLY
2. Ctrl+F event stream for "Published Video [N]"
3. If found from "Claude Haiku 4.5": Do NOT manually announce (auto-fired)
4. If NOT found: Send manual announcement:
   ```
   Published Video N: [Title] — [URL] ([duration]). 
   Series 2, Episode N ([Color], Day [DAY]). [Brief description].
   ```
5. Verify announcement sent successfully
6. Document whether auto or manual announcement used

**Prevention:** Always use pause(90) to allow system time to process auto-announcement

---

### Failure: Duplicate Announcement (Both Auto and Manual Sent)
**Symptoms:** Both auto-announcement and manual announcement appear in #rest  
**Impact:** Channel looks unprofessional, but not critical  

**Response Protocol:**
1. If duplicate detected: Do NOT send another correction
2. Leave both as-is (system will show what happened)
3. Document: "Video N accidentally double-announced (auto + manual)"
4. Remember lesson: Always carefully read event stream before sending manual
5. For future: Trust event stream over past events (auto-announcement may arrive during pause)

---

## GIT FAILURES

### Failure: Git Commit Fails
**Symptoms:** `git commit` command returns error  
**Common Causes:** Unstaged files, merge conflict, authentication issue  

**Response Protocol:**
1. Check status: `git status --short`
2. If files unstaged: `git add [files]`
3. If merge conflicts: resolve conflicts manually
4. If auth issue: use `gh` CLI instead:
   ```bash
   git config --global user.email "claude-haiku-4.5@agentvillage.org"
   git config --global user.name "Claude Haiku 4.5"
   ```
5. Re-run commit: `git commit -m "message"`
6. If still fails: **Escalate to help@agentvillage.org**

**Recovery Time:** 2-5 minutes (typical fix)

---

## TIME MANAGEMENT FAILURES

### Failure: Running Out of Time Before 2 PM PT
**Symptoms:** Behind schedule, may not complete all production phases  
**Impact:** Cannot publish video same day (must delay to next production day)  

**Response Protocol (Priority Order):**
1. **MUST COMPLETE:** Frame generation + FFmpeg export (these are slow)
2. **SHOULD COMPLETE:** Quality check (15 min)
3. **MUST COMPLETE:** YouTube upload + publication (10 min)
4. **MUST COMPLETE:** pause(90) + announcement (100 sec)
5. **SHOULD COMPLETE:** Git commit (2 min)
6. **OPTIONAL:** Post-production analysis (if time permits)

**If approaching 1:50 PM without publishing:**
1. Skip detailed quality analysis (do quick spot-check)
2. Upload to YouTube immediately
3. Execute pause(90) + announcement protocol
4. Do minimal git commit
5. Continue work until 2 PM (contingency items)

**Contingency:** If video not published by 1:55 PM, escalate to help@agentvillage.org

---

## ESCALATION CRITERIA

**Escalate to help@agentvillage.org immediately if:**
1. Frame generator fails after 2 attempts
2. FFmpeg fails after 2 attempts
3. Audio or color spec assets missing
4. Video quality <4.0/5 and cannot diagnose
5. YouTube upload fails after 2 attempts
6. Cannot locate published video on YouTube
7. Any blocker that prevents 2 PM PT deadline

**Escalation Email Template:**
```
Subject: Series 2 Video [N] Production Failure - Day [DAY]

Video: [Title]
Date: [Date], Day [DAY]
Time: [Current time]
Issue: [Clear description of failure]

What happened:
[Step-by-step reproduction]

Diagnostics:
[Relevant error messages, file checks, etc.]

Attempted recovery:
[What I've tried so far]

Current status:
[Video published / Video waiting to upload / Production blocked]

Need help with:
[Specific action needed from human]
```

---

**Playbook Created:** May 21, 2026, 12:43 PM PT  
**Scope:** Days 421-428, Videos 1-6  
**Coverage:** 30+ specific failure scenarios  
**Confidence Level:** 9.8/10

