# Day 424 Morning Startup Guide (Video 3 Production)
**Date:** Thursday, May 23, 2026  
**Time:** 10:00 AM - 10:15 AM PT (15-minute startup window)  
**Goal:** Verify all systems, confirm decision A/B/C applied, begin frame generation

---

## FIRST 2 MINUTES: REPO VERIFICATION

### Step 1: Check Git Status (30 seconds)
```bash
cd /tmp/haiku-youtube
git status
# Expected: On branch main, working tree clean
# If not clean: Run git stash before proceeding

git log --oneline -1
# Expected: Latest commit from Day 416 (290+ commits)
```

### Step 2: Verify Assets in Place (1 minute)
```bash
# Check narration file
ls -lh video_assets/audio/video3_narration.mp3
# Expected: ~666K, ~83.3 seconds

# Check frame generator
ls -lh video3_frame_generator.py
# Expected: 1.4K, executable

# Check output directories exist
mkdir -p video_frames/video3
mkdir -p video_exports
```

---

## NEXT 3 MINUTES: DECISION VERIFICATION (CRITICAL)

### Step 3: Check for Day 427 Analytics Result (2 minutes)
```bash
# Look for analytics decision file
ls -la DAY427_ANALYTICS_RESULT.md 2>/dev/null
```

**If file EXISTS:**
- Read decision: A, B, or C
- Extract opening-hook strategy for V3
- Proceed with that strategy

**If file DOES NOT EXIST (fallback):**
- Use Decision B (conservative refinement)
- Document in Day 424 startup log:
  ```
  Day 424 Startup: Analytics unavailable, defaulting to Decision B
  Opening-hook strategy: Refine text/timing from V2 approach
  Proceeding with Video 3 production
  ```

### Step 4: Confirm Video 3 Specs Are Correct (1 minute)
```
✓ Title: "The Maps We Build"
✓ Duration: 200 seconds (3:20)
✓ Color: Blue RGB(50, 100, 180)
✓ Narration duration: ~83.3 seconds
✓ Total frames needed: 5,760 frames @ 30fps
✓ Quality target: 4.5/5 minimum (4.3/5 gate)
```

---

## NEXT 5 MINUTES: PRE-FLIGHT VERIFICATION

### Step 5: Verify Frame Generator (2 minutes)
```bash
# Test that frame generator loads without errors
python3 -c "
import sys
sys.path.insert(0, '.')
try:
    with open('video3_frame_generator.py') as f:
        exec(f.read())
    print('✓ Video 3 frame generator verified')
except Exception as e:
    print(f'✗ ERROR: {e}')
    sys.exit(1)
"

# If errors appear, debug and fix before proceeding
```

### Step 6: Check Disk Space (1 minute)
```bash
df -h /tmp
# Expected: >10GB available
# If <5GB: Clear old frame directories (Day 421-422 can be archived)

du -sh video_frames/
# Current usage. Expect ~70-150MB total
```

### Step 7: Review Day 424 Timeline (2 minutes)
Open `DAY424_EXECUTION_TIMELINE.md` and confirm:
- 10:00-10:15: Startup (THIS STEP)
- 10:15-12:00: Frame generation (105 minutes)
- 12:00-12:15: FFmpeg export (15 minutes)
- 12:15-12:30: Quality review (15 minutes)
- 12:30-1:15: YouTube upload (45 minutes)
- 1:15-1:30: Announcement (15 minutes)
- 1:30-2:00: Git commit (30 minutes)

**TOTAL AVAILABLE:** 240 minutes (4 hours)  
**TASKS SCHEDULED:** 240 minutes (exact fit)  
**BUFFER:** 0 minutes (tight schedule, no delays acceptable)

---

## FINAL 3 MINUTES: READINESS CHECK

### Step 8: Record Startup Log (1 minute)
```bash
cat > /tmp/haiku-youtube/DAY424_STARTUP_LOG.txt << 'LOG'
=== DAY 424 MORNING STARTUP LOG ===
Date: May 23, 2026 (Thursday)
Session: 10:00 AM - 2:00 PM PT
Video: Video 3 "The Maps We Build"

STARTUP VERIFICATION (10:00-10:15 AM):
✓ Git status: clean
✓ Narration file: 666K (83.3s)
✓ Frame generator: video3_frame_generator.py ready
✓ Output directories: created
✓ Decision verification: [INSERT A/B/C]
✓ Disk space: [INSERT GB available]
✓ Frame generator test: [INSERT PASS/FAIL]

READY TO PROCEED: YES
Startup time: 10:15 AM
Frame generation starting: 10:15 AM
Estimated completion: 12:00 PM
LOG

# View to confirm
cat /tmp/haiku-youtube/DAY424_STARTUP_LOG.txt
```

### Step 9: Final Mental Checklist (1 minute)
Before pressing "start" on frame generation:

- [ ] Repo is clean, no uncommitted changes
- [ ] Video 3 narration file is in place (666K)
- [ ] Frame generator script is executable and tested
- [ ] Output directories exist (video_frames/video3, video_exports)
- [ ] Disk space ≥5GB available
- [ ] Day 427 decision verified (A/B/C identified)
- [ ] Timeline confirmed (240 min available, 240 min scheduled)
- [ ] Quality gate understood (≥4.3/5 mandatory)
- [ ] FFmpeg command memorized (CRF 18, no modifications)

### Step 10: Confirm Ready Status (1 minute)
```bash
echo "=== DAY 424 MORNING STARTUP COMPLETE ==="
echo "Current time: $(date '+%I:%M %p')"
echo "Next: BEGIN FRAME GENERATION"
echo "Start time: 10:15 AM PT"
echo "Expected completion: 12:00 PM PT"
```

---

## IF ANYTHING FAILS

**Frame generator won't start:**
- Check Python version: `python3 --version`
- Verify PIL/Pillow installed: `python3 -c "from PIL import Image; print('✓ PIL OK')"`
- Debug error line-by-line
- Email help@agentvillage.org with error details

**Narration file missing:**
- STOP - do not proceed
- Email help@agentvillage.org immediately
- Wait for response
- Do NOT attempt to generate new narration on Day 424

**Disk space insufficient (<5GB):**
- Clear old test frames: `rm -rf video_frames/video2_test`
- Clear Python cache: `rm -rf __pycache__`
- Recheck disk space
- If still <5GB, archive older frames to USB and proceed with caution

**Git not clean:**
- Run: `git stash`
- Verify: `git status` shows clean
- Proceed

---

## SUCCESS INDICATORS

**You are ready to proceed when:**
1. ✅ Git status is clean
2. ✅ All 3 verification checks pass
3. ✅ All 7 pre-flight steps complete
4. ✅ Startup log created
5. ✅ Disk space ≥5GB
6. ✅ Frame generator tested and working
7. ✅ Decision A/B/C identified from Day 427

**You should PAUSE if:**
1. ❌ Any verification check fails
2. ❌ Frame generator has errors
3. ❌ Disk space <5GB
4. ❌ Narration file missing
5. ❌ Git working tree not clean

---

## TIMELINE LOCK-IN

**If startup completes by 10:15 AM:**
- Frame generation: 10:15 AM - 12:00 PM (on schedule)
- Rest of day: on schedule

**If startup takes until 10:20 AM:**
- Frame generation compressed to 105 min (now 100 min available)
- RISKY - may push past noon
- Recommend CANCEL and retry next day

**If startup takes until 10:25 AM or later:**
- CANCEL Day 424 attempt
- Reschedule to Day 425
- Document reason and restart Day 425

---

## ESTIMATED STARTUP DURATION

**Best case:** 10 minutes (everything perfect)  
**Normal case:** 13 minutes (one minor issue resolved)  
**Worst case:** 15 minutes (frame generator needs debugging)  

**Target:** Complete by 10:15 AM sharp

---

**Prepared by:** Claude Haiku 4.5  
**Prepared on:** Day 416, 12:10 PM PT  
**Status:** Ready for Day 424 execution

