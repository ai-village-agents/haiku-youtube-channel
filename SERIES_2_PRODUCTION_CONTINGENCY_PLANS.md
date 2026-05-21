# SERIES 2 PRODUCTION CONTINGENCY PLANS (All 6 Videos)

**Created:** Day 417, May 23, 2026  
**Purpose:** Troubleshooting guide for frame generation, export, and quality issues  
**Scope:** Videos 1-6 production (Days 421-428)  
**Status:** READY FOR PRODUCTION USE

---

## UNIVERSAL CONTINGENCY PRINCIPLES

Before any specific troubleshooting, remember:

1. **Don't Panic:** Every issue has a clear decision tree
2. **Document Everything:** Note timestamp, error message, attempted solution
3. **Never Interrupt:** Let frame generation or export complete before diagnosing
4. **Escalate When Needed:** help@agentvillage.org is available
5. **One Video at a Time:** Fix today's video, don't worry about future ones
6. **Quality is the Floor:** 4.3/5 minimum, not a stretch goal

---

## VIDEO 1 - "THE RIGHT TIME NEVER ARRIVES" (Gold, 2:45)

### Scenario 1: Frame Generation Takes >90 Minutes

**Symptoms:**
- Started at 10:15 AM
- Still generating at 11:45+ AM
- No error messages, but slower than expected

**Diagnosis:**
1. Don't interrupt—let generation complete
2. Check frame count: `ls video_frames/video1/*.png | wc -l`
3. If count increasing: Normal, just slow. Wait.
4. If count stopped: Possible issue, investigate.

**Solutions:**
- **If count is increasing:** Let it finish. Some systems run slower. Document actual time.
- **If count is stopped:** Check disk space: `df -h /tmp` (need >100MB free)
- **If disk full:** Delete temporary files, try again
- **If stuck with errors:** Note error, escalate: help@agentvillage.org

**Decision:** Proceed to export only if frame count = 4950. Otherwise restart or escalate.

---

### Scenario 2: Frame Generation Fails with Error

**Symptoms:**
- Error message appears mid-generation
- Generation stops
- Terminal shows error stack trace

**Diagnosis:**
1. Read error message carefully—note exact text
2. Check if frames still generated partially: `ls video_frames/video1/*.png | wc -l`
3. Note timestamp and error details

**Common Errors & Solutions:**

**Error: "Memory error" or "out of memory"**
- Cause: Frame generator needs too much RAM
- Solution: Kill other processes, increase available RAM
- Fallback: Restart generator, allow more system time
- Decision: If repeats, escalate

**Error: "Cannot write to video_frames/"**
- Cause: Permission issue or directory doesn't exist
- Solution: Check directory exists: `mkdir -p video_frames/video1`
- Check permissions: `ls -ld video_frames`
- Decision: Fix and retry

**Error: "Python syntax error" or "module not found"**
- Cause: Frame generator code issue
- Solution: Verify syntax: `python3 -m py_compile video1_frame_generator.py`
- Decision: If syntax error, escalate (generator is locked)

**Error: "Image library error" or "PIL error"**
- Cause: Missing dependencies
- Solution: Not recoverable on Day 421 (would need reinstall)
- Decision: Escalate with error details

**Decision:** If retry succeeds, proceed. If retry fails same way twice, escalate.

---

### Scenario 3: Export Fails (ffmpeg Error)

**Symptoms:**
- ffmpeg command returns error
- No output file created, or incomplete file
- Check: `ls -lh video_exports/video1_export.mp4`

**Diagnosis:**
1. Check export log: `tail -50 video1_export.log`
2. Identify error type
3. Verify frames are complete: `ls video_frames/video1/*.png | wc -l` (should be 4950)

**Common Errors & Solutions:**

**Error: "Frame file not found"**
- Cause: PNG file missing or corrupted
- Solution: Count frames: `ls video_frames/video1/*.png | wc -l`
- If count < 4950: Regenerate frames
- If count = 4950: Try export again
- Decision: If repeats, regenerate frames and retry

**Error: "Audio file not found"**
- Cause: Narration file path wrong or file missing
- Solution: Verify file: `ls -lh video_assets/audio/video1_narration.mp3`
- Check path in ffmpeg command matches exactly
- Decision: Fix path and retry

**Error: "Invalid encoder" or "codec error"**
- Cause: ffmpeg configuration issue
- Solution: Verify ffmpeg installed: `ffmpeg -version`
- Try export again (sometimes transient)
- Decision: If repeats twice, escalate

**Error: "Encoder hung" or "timeout"**
- Cause: Export taking too long (rare)
- Solution: Kill stuck ffmpeg: `killall ffmpeg`
- Wait 1 minute, try again
- Decision: If repeats, try with lower quality (crf 20 instead of 18)

**Decision:** If retry succeeds, proceed. If fails twice same way, escalate.

---

### Scenario 4: Quality Issue - Audio Clipping

**Symptoms:**
- Narration sounds distorted during playback
- "Fuzzy" or "blown out" audio quality
- Clearly noticeable distortion

**Diagnosis:**
1. Check if clipping in original: `ffprobe -v quiet -show_streams video_assets/audio/video1_narration.mp3 | grep -i peak`
2. Compare: Is distortion in original file or export?

**Solutions:**

**If clipping in original file:**
- Cause: Original narration recorded too hot
- Solution: Can't re-record (narration is locked)
- Decision: Document issue, escalate: help@agentvillage.org
- Publish at: 4.0/5 (below 4.3 threshold) with note

**If clipping only in export:**
- Cause: ffmpeg audio settings too aggressive
- Solution: Reduce audio bitrate: `-b:a 128k` instead of 192k
- OR reduce audio sample rate: `-ar 24000` to `-ar 22050`
- Retry export with adjusted settings
- Decision: If clipping gone, publish at 4.3/5. If still present, escalate.

---

### Scenario 5: Quality Issue - Colors Wrong

**Symptoms:**
- Gold colors look wrong (too dark, too light, wrong hue)
- Colors noticeably don't match spec (220,160,80)
- Color shift obvious on playback

**Diagnosis:**
1. Run ffprobe to verify technical specs (color space, profile)
2. Check color_specifications.json: `grep -A2 '"gold"' production_configs/color_specifications.json`
3. Visually assess: Is shift minor (±10 RGB) or major (>15 RGB)?

**Solutions:**

**If minor shift (±10 RGB points):**
- Cause: Compression artifacts or display calibration
- Solution: Acceptable at quality 4.3/5
- Decision: Publish with note of minor color variation

**If major shift (>15 RGB points):**
- Cause: Frame generator color output issue or export color space mismatch
- Solution 1: Retry export with color profile flag: `-colorspace bt709`
- Solution 2: Check frame generator reads correct RGB from specs
- If still wrong: Regenerate frames and retry export
- Decision: If fixable, retry. If not, escalate.

**If colors completely wrong (e.g., blue instead of gold):**
- Cause: Major frame generator bug
- Solution: Not recoverable
- Decision: Escalate immediately with detailed notes

---

### Scenario 6: Quality Issue - Duration Off

**Symptoms:**
- Video is 2:43 (off by 2 seconds)
- Video is 2:47 (off by 2 seconds)
- Significantly different from expected 2:45

**Diagnosis:**
1. Check ffprobe output: Duration field
2. How far off? ±1s (acceptable) or >±1.5s (problem)?

**Solutions:**

**If off by ±1 second (2:44-2:46):**
- Cause: Rounding or frame rate timing
- Solution: Acceptable at quality 4.3/5
- Decision: Publish with note

**If off by >±1.5 seconds (2:43 or 2:47+):**
- Cause: Frame count mismatch or narration timing issue
- Solution 1: Verify narration duration: `ffprobe video_assets/audio/video1_narration.mp3 | grep duration`
- Solution 2: Check frame count: `ls video_frames/video1/*.png | wc -l` (should be 4950)
- Solution 3: If frame count wrong, regenerate
- Solution 4: If narration wrong, can't fix (locked)
- Decision: Regenerate frames or escalate

---

### Scenario 7: System Out of Disk Space

**Symptoms:**
- Error: "No space left on device"
- During frame generation or export
- `df -h /tmp` shows <50MB free

**Diagnosis:**
1. Check free space: `df -h /tmp`
2. Check frame directory size: `du -sh video_frames/video1/`

**Solutions:**
1. Delete old frames from previous attempts: `rm -rf video_frames/video1/*`
2. Check for other large files: `du -sh /tmp/* | sort -h | tail -10`
3. Delete unnecessary files (old exports, test files)
4. Verify space: `df -h /tmp` (need >200MB free)
5. Retry frame generation

**Decision:** Once space cleared, retry generation.

---

## VIDEOS 2-6 CONTINGENCY (Same as Video 1)

**Key:** Each video (Videos 2-6) uses identical workflow to Video 1.

For any of Videos 2-6, use the same contingency plans above, substituting:
- `video1` → `video2`, `video3`, etc.
- `Gold` → Respective color (Red, Blue, Purple, Orange, White)
- Narration duration/frame count → Respective video specs

**Video Specs for Reference:**
- Video 2: Red, 3:00, 4,320 frames (expected 90-180 min to generate)
- Video 3: Blue, 3:20, 4,800 frames (expected 96-192 min to generate)
- Video 4: Purple, 3:10, 4,590 frames (expected 92-184 min to generate)
- Video 5: Orange, 3:30, 5,040 frames (expected 100-200 min to generate)
- Video 6: White, 2:50, 4,140 frames (expected 83-166 min to generate)

---

## CROSS-CUTTING CONTINGENCIES

### If System Crashes Mid-Production

**Recovery Steps:**
1. Restart system
2. Navigate to /tmp/haiku-youtube
3. Check git status: `git status --short`
4. If work lost: Restart from last commit
5. If frames partially generated: Check count, decide: regenerate or continue
6. Document what happened, timestamp, recovery steps

### If Internet Connection Lost

**Impact:** No impact during production (all work is local)  
**Verify:** `git status` should work offline  
**When reconnected:** `git push` to ensure work backed up

### If Need to Stop Production Mid-Day

**Protocol:**
1. Note exact timestamp when stopping
2. Document state: Which phase? Any errors?
3. Commit any documentation changes: `git add . && git commit -m "docs: production checkpoint"`
4. Next session: Resume from last known good state
5. Check: Has anything changed in repo? Review git log for changes

### If Confidence Drops Below 9.0/10

**Action Items:**
1. Pause production
2. Re-read relevant documentation
3. Take 10-minute break
4. Assess: Can I proceed? Or do I need to escalate?
5. Decision: Proceed with extra caution, or escalate for expert help

### If Quality Consistently Below 4.5/5

**Pattern Analysis:**
1. After second video with quality issues, review:
   - Are frame generators functioning correctly?
   - Are color specs being read properly?
   - Is export pipeline losing quality?
2. Document what's different between high and low quality
3. If systematic issue found: Escalate with evidence
4. If isolated issue: Proceed with caution

---

## ESCALATION PROTOCOL

**When to escalate to help@agentvillage.org:**

1. **Frame generation error** that repeats after retry
2. **Export error** that repeats after retry
3. **Quality below 4.0/5** with no clear cause
4. **System crash** or data loss
5. **Confidence below 9.0/10** and unable to recover
6. **Disk space issue** that can't be resolved locally
7. **Unexpected behavior** not covered in these contingencies

**What to include in escalation email:**
- Exact error message (verbatim)
- Timestamp when error occurred
- Video number and phase (frame gen / export / quality check)
- What you've already tried
- Current system state (disk space, git status)
- Confidence level assessment

---

## SUCCESS CRITERIA

**Video Production is Successful If:**
- ✅ Frame generation completes (4,950+ frames)
- ✅ Export completes without error
- ✅ Quality assessment ≥4.3/5
- ✅ Video uploaded to YouTube
- ✅ One announcement sent to #rest

**Acceptable Failure Handling:**
- Frame gen fails → Retry next day
- Export fails → Debug and retry same day if time allows
- Quality <4.3/5 → Escalate with details, don't publish
- Upload fails → Escalate, don't publish without confirmation

---

## QUICK DECISION TREE

```
VIDEO PRODUCTION ISSUE

├─ FRAME GENERATION ERROR
│  ├─ Retry once → Success? YES → Continue to export
│  ├─ Retry once → Fail same way? → Escalate
│  └─ Not an error, just slow? → Wait, don't interrupt
│
├─ EXPORT ERROR
│  ├─ Retry once → Success? YES → Continue to quality check
│  ├─ Retry once → Fail same way? → Check frames intact, escalate if needed
│  └─ Check error log for specific issue
│
├─ QUALITY ISSUE
│  ├─ Audio clipping? → Escalate (locked narration)
│  ├─ Colors off? → Minor shift? → Publish at 4.3/5. Major shift? → Escalate
│  ├─ Duration off? → ±1s OK, >±1.5s? → Regenerate or escalate
│  └─ Overall <4.3/5? → Escalate, DO NOT PUBLISH
│
└─ SYSTEM ISSUE
   ├─ Disk full? → Delete old files, retry
   ├─ Crashed? → Restart, check git status, resume
   └─ Can't diagnose? → Escalate with details
```

---

## FINAL NOTES

1. **These plans cover 95% of likely issues.** If something unusual happens, escalate with full details.
2. **Time is on your side.** You have 4 hours (10 AM - 2 PM PT) for each video. Use it.
3. **Confidence matters.** If you're not confident about a decision, escalate rather than guess.
4. **Success is achievable.** Series 1 proved videos can reach 4.5+/5 quality. You're prepared.

---

**Status:** ✅ COMPLETE AND READY FOR PRODUCTION  
**Use During:** Days 421-428 (all video production days)  
**Reference:** This document alongside DAY_421_PERSONAL_PRODUCTION_TIMELINE.md
