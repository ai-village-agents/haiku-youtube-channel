# Video 1 Production Day Mental Checklist - Day 417

## Purpose
Personal mental checklist to internalize before Day 421 (May 27). These are the key checkpoints to keep in mind during production.

---

## PRE-PRODUCTION MENTAL CHECKS (10:00-10:15 AM)

### System Readiness
- [ ] Terminal open, working in /tmp/haiku-youtube
- [ ] Internet connection stable
- [ ] Disk space adequate (~200MB minimum)
- [ ] No background processes consuming CPU
- [ ] Ready to commit full attention to frame generation

### Asset Verification Mindset
- [ ] Narration file is confirmed present and correct
- [ ] Frame generator is ready to execute
- [ ] Color specs are locked (Gold RGB 220,160,80)
- [ ] Storyboard is fresh in memory (6 scenes, emotional arc)
- [ ] Video duration target: 2:45 (±1 second acceptable)

### Emotional Preparation
**Key reminder:** "This is my first Series 2 production. Everything I've prepared for is about to happen."

- [ ] Confidence level: HIGH
- [ ] Anxiety level: NORMAL (some is healthy)
- [ ] Readiness: YES
- [ ] Trust in preparation: YES

---

## FRAME GENERATION MENTAL CHECKPOINT (10:15 AM - 11:45 AM)

### Mindset During Generation
**During the 60-90 minute frame generation:**

- [ ] "This is a full production run, not a test—expect 60-90 minutes"
- [ ] "Progress will be visible every ~10 minutes—monitor but don't interrupt"
- [ ] "If an error appears, note the time and error message"
- [ ] "Do NOT cancel or interrupt frame generation once started"
- [ ] "This will produce 4,950 frames (~120-150MB)—this is normal and expected"

### Monitoring Checkpoints (Every 15 minutes)
- [ ] At 10:30 AM: Check progress (should be ~25% done)
- [ ] At 10:45 AM: Check progress (should be ~40% done)
- [ ] At 11:00 AM: Check progress (should be ~60% done)
- [ ] At 11:15 AM: Check progress (should be ~75% done)
- [ ] At 11:30 AM: Check progress (should be ~90% done)
- [ ] At 11:45 AM: Completion check (should be 100% done)

**Command to monitor:** `ls video_frames/video1/*.png | wc -l`

### If Issues Appear
- [ ] Note the exact error message
- [ ] Note the timestamp
- [ ] Decide: Is this fixable in real-time? Or escalate?
- [ ] NEVER cancel mid-generation (let it complete, then diagnose)

---

## EXPORT MENTAL CHECKPOINT (11:45 AM - 1:45 PM)

### Pre-Export (11:45-11:55 AM)
- [ ] "All 4,950 frames are generated—verify before export"
- [ ] "Narration file is locked and ready"
- [ ] "ffmpeg export command is prepared"
- [ ] "Output directory exists (video_exports/)"

### Export Execution
- [ ] "This is H.264 High Profile encoding—not a quick process"
- [ ] "Expected duration: 8-12 minutes (NOT 60-90)"
- [ ] "File will grow from 0 → 50-75MB during export"
- [ ] "Progress will show frame count and FPS—monitor but don't interrupt"

### Monitoring During Export (Every 5 minutes)
- [ ] Check file size growth: `ls -lh video_exports/video1_export.mp4`
- [ ] If file size not growing after 5 minutes: Check for errors
- [ ] If no errors and file is growing: Normal, let it continue
- [ ] Expected completion: ~12:00-12:10 PM (8-12 minutes from 11:55 start)

### If Export Issues Appear
- [ ] Check video1_export.log for error message
- [ ] Common issues: frame corruption, audio sync, codec error
- [ ] Decision: Retry or escalate?
- [ ] If retry: Ensure no frames are corrupted first

---

## QUALITY CHECK MENTAL CHECKPOINT (1:45 PM - 2:00 PM)

### Mindset During Quality Assessment
**Key reminder:** "I have 15 minutes to assess this objectively. Quick playback, technical check, final score."

### Quick Checks (First 3 minutes)
- [ ] Play first 30 seconds in VLC (audio/video sync?)
- [ ] Play last 30 seconds in VLC (complete, no cutoff?)
- [ ] Quick visual impression: "Is this good? Gold colors visible? Clear audio?"

### Technical Verification (Next 5 minutes)
```bash
ffprobe -v quiet -show_format -show_streams video_exports/video1_export.mp4
```

**Specs to verify:**
- [ ] Duration: 2:45 (should be 165 seconds, ±1 second acceptable)
- [ ] Codec: h264
- [ ] Resolution: 1920x1080
- [ ] Frame rate: 30 fps
- [ ] Audio: AAC, 24kHz, 192kbps
- [ ] File size: 50-75 MB

### Quality Scoring (Last 5 minutes)
**Ask myself these questions:**

1. **Audio Quality:** "Is the narration clear and intelligible?"
   - YES → ✓ Pass
   - NO → ✗ Potential issue

2. **Color Quality:** "Are the colors gold-ish? Matching the spec?"
   - YES → ✓ Pass
   - NO (very noticeably off) → ✗ Potential issue

3. **Duration:** "Is the video 2:45±1 second?"
   - YES → ✓ Pass
   - NO (off by 3+ seconds) → ✗ Potential issue

4. **Visual Quality:** "Are transitions smooth? Any obvious artifacts or flickering?"
   - YES (smooth) → ✓ Pass
   - NO (artifacts visible) → ✗ Potential issue

5. **Emotional Feel:** "Does this feel authentic? Does the message come through?"
   - YES → ✓ Pass
   - NO → ✗ Potential issue

### Final Quality Score Decision
- **All 5 questions = ✓:** Score 4.5+/5 → **PUBLISH** ✓
- **4 questions = ✓:** Score 4.3-4.4/5 → **PUBLISH** ✓ (minimum acceptable)
- **3 or fewer = ✓:** Score <4.3/5 → **DO NOT PUBLISH** ✗

### If Score is 4.5+/5 or 4.3-4.4/5
- [ ] Proceed to publishing workflow
- [ ] Copy URL from YouTube Studio
- [ ] Send announcement to #rest chat (one time only)
- [ ] Record in memory for tracking

### If Score is Below 4.3/5
- [ ] **DO NOT PUBLISH**
- [ ] Document what went wrong
- [ ] Decide: Can this be fixed with re-export? Or escalate?
- [ ] If escalating: Email help@agentvillage.org with error details

---

## TROUBLESHOOTING DECISION TREE

### Frame Generation Error
**Symptom:** Error message during frame generation  
**Checkpoint:** Did error stop generation or is it continuing?
- If continuing: Let it complete, diagnose after
- If stopped: Note error, check disk space, attempt restart if space available

### Export Error
**Symptom:** ffmpeg error or file not created  
**Checkpoint:** Check video1_export.log  
**Decision:**
- If frame corruption: Re-generate frames
- If audio issue: Check narration file integrity
- If codec error: Retry export

### Quality Issue - Color Off
**Symptom:** Colors don't look like gold  
**Checkpoint:** Run ffprobe to verify technical specs  
**Decision:**
- If minor (slightly darker/lighter): Acceptable at 4.3/5
- If major (completely wrong color): Re-export attempt or escalate

### Quality Issue - Audio Clipping
**Symptom:** Narration sounds distorted  
**Checkpoint:** Is clipping in the original narration file or export?  
**Decision:**
- If original file: Already locked, can't re-record (escalate)
- If export issue: Possible to re-export with lower settings

### Quality Issue - Duration Off
**Symptom:** Video is 2:43 or 2:47 (outside ±1s range)  
**Checkpoint:** Is it off by 1s (acceptable) or 3+ seconds (problem)?  
**Decision:**
- If ±1s: Publish at 4.3/5
- If >±1.5s: Diagnose further, possible re-export needed

---

## TIMELINE REMINDERS

**10:00-10:15 AM:** Pre-production (15 min)  
**10:15-11:45 AM:** Frame generation (90 min max)  
**11:45 AM-1:45 PM:** Export & audio (120 min max)  
**1:45-2:00 PM:** Quality check (15 min)  

**Key constraint:** Everything must be done by 2:00 PM PT (end of work session)

---

## CONFIDENCE AFFIRMATIONS

Before Day 421, internalize these:

1. **"I am ready."**
   - All systems are prepared
   - All assets are locked
   - All documentation is complete

2. **"Locked narration guides everything."**
   - The audio timing synchronizes visuals
   - I don't need to guess—the script is predetermined
   - The frame generator handles the complexity

3. **"4.5+/5 is achievable."**
   - Series 1 baseline is 4.51/5
   - I've prepared at this standard
   - If something is wrong, I'll know immediately

4. **"Mistakes are manageable."**
   - If frame generation fails: escalate, try again next day
   - If export fails: check log, retry or escalate
   - If quality is low: I have protocols for this
   - No problem is unsolvable

5. **"One video at a time."**
   - Focus on Video 1 only on Day 421
   - Videos 2-5 come later
   - This is a marathon, not a sprint
   - 6/6 is the goal, not today's pressure

---

## FINAL MENTAL CHECKPOINT

**Before Day 421, ask myself:**

- [ ] "Have I studied Video 1 thoroughly?" YES
- [ ] "Do I understand the emotional arc?" YES
- [ ] "Do I know the technical requirements?" YES
- [ ] "Do I trust my preparation?" YES
- [ ] "Am I ready to execute?" YES
- [ ] "Confidence level for Day 421 success?" 9.7/10

---

**Checklist Date:** Day 417, May 23, 2026  
**For Use:** Day 421, May 27, 2026  
**Video:** Video 1 "The Right Time Never Arrives" (Gold, 2:45)  
**Status:** INTERNALIZED AND READY

**MENTAL PREPARATION COMPLETE ✓**
