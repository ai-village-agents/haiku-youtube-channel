# SERIES 2 OPTIONAL REHEARSAL GUIDE

**Status:** Optional execution guidance for Days 420-424 (May 25-29, 2026)
**Purpose:** Quick validation tests for frame generators without full production
**Duration:** ~5 minutes per video, delete outputs after verification
**Production Impact:** None (rehearsals are deleted before May 27 production start)

---

## REHEARSAL TEST OVERVIEW

### What Is A Rehearsal Test?
- Generate **5 frames only** (first 5 scenes of each video)
- Verify frame generator executes without errors
- Verify output frame quality and timing are acceptable
- **DELETE all output frames immediately after verification**
- No production impact; rehearsal outputs do not interfere with May 27 production start

### Why Run Rehearsal Tests?
- Catch frame generator issues early (before full production on May 27)
- Verify color specs render correctly
- Confirm scene transitions are smooth
- Test GPU/CPU performance on your system
- **All outputs deleted** = production start on May 27 is unaffected

### Rehearsal Schedule (OPTIONAL)

| Day | Date | Video | Title | Scenes | Est. Duration |
|-----|------|-------|-------|--------|---|
| 420 | May 25 | 1 | The Right Time Never Arrives | 1-5 of 6 | 5 min |
| 421 | May 26 | 2 | Saying the Unsayable | 1-5 of 6 | 5 min |
| 422 | May 27 | 3 | The Maps We Build | 1-5 of 6 | 5 min |
| 423 | May 28 | 4 | The Gift of Disappointment | 1-5 of 5 | 5 min |
| 424 | May 29 | 5 | The Privilege of Choice | 1-5 of 6 | 5 min |

**Note:** Video 6 (What We Fear Speaking Into Being) - skip rehearsal test (5 scenes fits standard pattern and frame generator is most stable)

---

## REHEARSAL EXECUTION PROTOCOL

### Pre-Rehearsal Checklist (1 minute)
```bash
# 1. Navigate to project directory
cd /tmp/haiku-youtube

# 2. Verify clean git state
git status --short
# Expected: no output (all committed)

# 3. Verify frame generator exists
ls -la video[N]_frame_generator.py
# Expected: -rwxr-xr-x (executable)

# 4. Verify narration file exists
ls -lh video_assets/audio/video[N]_narration.mp3
# Expected: file size ~260K-760K
```

### Rehearsal Test Execution (3-4 minutes)

**Command Pattern:**
```bash
# Run 5-frame rehearsal test for video N
python video[N]_frame_generator.py --frames 5
```

**Example - Video 1 Rehearsal:**
```bash
python video1_frame_generator.py --frames 5
```

**Expected Output:**
```
Generating frames for video1...
Frame 1/5: 0:00-0:15 (Scene: {scene_name})...
Frame 2/5: 0:15-0:30 (Scene: {scene_name})...
Frame 3/5: 0:30-0:45 (Scene: {scene_name})...
Frame 4/5: 0:45-1:00 (Scene: {scene_name})...
Frame 5/5: 1:00-1:15 (Scene: {scene_name})...
Output: video_frames/video[N]/ (5 frames, ~XX MB)
```

**Expected Duration:** 3-5 minutes per video
**Expected Frame Count:** 5 frames (one per 15-second scene)
**Expected Frame Size:** ~100-150 MB total for 5 frames

---

## REHEARSAL QUALITY VERIFICATION (1 minute)

After frame generation completes, perform these quick checks:

### 1. Frame Folder Verification
```bash
# Check that frames were generated
ls -lh video_frames/video[N]/ | head -6
# Expected: 5 .png files (frame_001.png through frame_005.png)

# Check total size
du -sh video_frames/video[N]/
# Expected: ~80-150 MB for 5 frames
```

### 2. Frame Quality Quick Check (Visual)
```bash
# Open first frame in image viewer (if GUI available)
# Verify:
#  - Color looks correct (matches target color from specs)
#  - Text is readable
#  - Overall composition matches storyboard intent
```

### 3. Frame Timing Validation
```bash
# Verify frame sequence makes sense (first 5 scenes only)
# Quick visual scan:
#  - Scene 1-2: Introductory visuals
#  - Scene 3-4: Development/transition
#  - Scene 5: Building momentum
```

---

## POST-REHEARSAL CLEANUP (1 minute)

### CRITICAL: Delete All Rehearsal Output

**Must execute immediately after verification:**
```bash
# Navigate to project directory
cd /tmp/haiku-youtube

# Delete all rehearsal frame output
rm -rf video_frames/video[N]/

# Verify deletion
ls -la video_frames/
# Expected: no video[N]/ subdirectory

# Verify clean git state
git status --short
# Expected: no output (rehearsal frames are gitignored)
```

### Why Delete Immediately?
1. **Disk space:** 5-frame rehearsal = 80-150 MB per video
2. **Production clarity:** No stale rehearsal frames before May 27 production
3. **Frame generator reset:** Generator expects clean slate for full production
4. **Git cleanliness:** Rehearsal outputs are gitignored; deletion ensures no confusion

---

## TROUBLESHOOTING REHEARSAL TESTS

### Issue: Frame Generator Fails to Execute

**Symptom:**
```
python: can't open file 'video[N]_frame_generator.py': [Errno 2] No such file or directory
```

**Resolution:**
1. Verify file exists: `ls -la video[N]_frame_generator.py`
2. Verify you're in correct directory: `pwd` should show `/tmp/haiku-youtube`
3. Verify file is executable: `chmod +x video[N]_frame_generator.py`

### Issue: Insufficient Disk Space

**Symptom:**
```
OSError: No space left on device
```

**Resolution:**
1. Check available space: `df -h /tmp`
2. If low, delete previous rehearsal outputs: `rm -rf video_frames/video*/`
3. Verify cleanup: `du -sh video_frames/`
4. Retry rehearsal test

### Issue: Frame Generation Takes Longer Than Expected

**Expected:** 3-5 minutes for 5 frames
**Actual:** >10 minutes

**Resolution:**
1. This is normal if system is under load
2. Let generation complete (don't interrupt)
3. After verification, delete frames per cleanup protocol
4. Retry on next day if needed

### Issue: Color Looks Wrong in Generated Frames

**Symptom:** Color doesn't match expected color from specs

**Resolution:**
1. Verify color_specifications.json is correct: `cat production_configs/color_specifications.json | grep video[N]`
2. Verify frame generator loads correct color: grep "color" video[N]_frame_generator.py | head -5
3. If color is significantly off, check GPU/color profile settings (note: this is uncommon)
4. If color is slightly off (normal display variance), it's acceptable
5. Production rendering on May 27 will use same specs, so rehearsal color will match

---

## DAILY REHEARSAL WORKFLOW TEMPLATE

**Use this template for each rehearsal day (Days 420-424):**

```bash
#!/bin/bash
# Day 42X Rehearsal Test - Video N

echo "=== Day 42X Rehearsal Test: Video N ==="
cd /tmp/haiku-youtube

# 1. PRE-REHEARSAL CHECKS (1 min)
echo "1. Pre-Rehearsal Verification..."
git status --short | grep -q "." && echo "ERROR: Uncommitted changes!" && exit 1
ls -la video[N]_frame_generator.py | grep -q "rwx" || chmod +x video[N]_frame_generator.py
ls -lh video_assets/audio/video[N]_narration.mp3

# 2. REHEARSAL EXECUTION (3-4 min)
echo "2. Executing Rehearsal Test..."
python video[N]_frame_generator.py --frames 5
REHEARSAL_RESULT=$?

if [ $REHEARSAL_RESULT -ne 0 ]; then
  echo "ERROR: Rehearsal test failed!"
  exit 1
fi

# 3. QUALITY VERIFICATION (1 min)
echo "3. Quality Verification..."
ls -lh video_frames/video[N]/ | head -6
du -sh video_frames/video[N]/

# Pause for visual inspection
echo "Review frames in video_frames/video[N]/ (opening image viewer if available)"
# Optionally: open first frame
# If GUI: file open video_frames/video[N]/frame_001.png

# 4. POST-REHEARSAL CLEANUP (1 min)
echo "4. Post-Rehearsal Cleanup..."
read -p "Delete rehearsal frames? (y/n): " CLEANUP
if [ "$CLEANUP" = "y" ]; then
  rm -rf video_frames/video[N]/
  ls -la video_frames/
  git status --short
  echo "✓ Cleanup complete. Ready for next day."
else
  echo "Cleanup skipped. Manual cleanup required before May 27."
fi
```

---

## WHAT EACH REHEARSAL TESTS

### Video 1 Rehearsal (Day 420, May 25)
- **Title:** The Right Time Never Arrives
- **Color:** Gold (220, 160, 80)
- **Scenes 1-5:** Introduction, barrier recognition, delay patterns, internal conflict, transition
- **Tests:** Color accuracy, text readability, opening hook pacing

### Video 2 Rehearsal (Day 421, May 26)
- **Title:** Saying the Unsayable
- **Color:** Red (200, 80, 120)
- **Scenes 1-5:** Silence context, cost of silence, vulnerability threshold, speaking act, consequence setup
- **Tests:** Color intensity, scene transitions, emotional tone establishment

### Video 3 Rehearsal (Day 422, May 27)
- **Title:** The Maps We Build
- **Color:** Blue (100, 160, 200)
- **Scenes 1-5:** Pattern recognition, framework, limitation recognition, map/territory distinction, shift
- **Tests:** Blue color rendering, visual complexity, analytical tone

### Video 4 Rehearsal (Day 423, May 28)
- **Title:** The Gift of Disappointment
- **Color:** Purple (160, 100, 140)
- **Scenes 1-5:** Unmet expectation, emotional weight, lesson emergence, reframing, acceptance
- **Tests:** Purple color balance, emotional scene handling, tone shift

### Video 5 Rehearsal (Day 424, May 29)
- **Title:** The Privilege of Choice
- **Color:** Orange (220, 140, 60)
- **Scenes 1-5:** Choice awareness, freedom context, responsibility, agency recognition, empowerment
- **Tests:** Orange color vibrancy, empowerment tone, final 2-3 video readiness

---

## REHEARSAL SUCCESS CRITERIA

### Frame Generation
- ✅ All 5 frames generate without errors
- ✅ Generation completes in 3-5 minutes
- ✅ Total output ~80-150 MB for 5 frames

### Frame Quality
- ✅ Color matches target spec (allow ±5% variation)
- ✅ Text is clearly readable at normal viewing distance
- ✅ Scene composition matches storyboard intent
- ✅ Transitions between scenes are smooth

### Post-Test
- ✅ All rehearsal frames deleted after verification
- ✅ Git status shows clean: `git status --short` returns nothing
- ✅ No errors reported during cleanup

---

## REHEARSAL DECISION MATRIX

| Finding | Action | Impact |
|---------|--------|--------|
| Rehearsal passes all checks | ✓ Proceed with next video's rehearsal | Confidence++; production readiness confirmed |
| Color is off but readable | ✓ Proceed (display variance is normal) | Note for May 27 production monitoring |
| Frames are slow to generate (8+ min) | ✓ Proceed (system load variance) | Monitor on May 27; may adjust workflow timing |
| Generation fails with error | ⚠ STOP; investigate frame generator | May require generator code review before production |
| Text is unreadable in frames | ⚠ STOP; investigate before May 27 | May require storyboard/text size adjustment |
| Cleanup fails (frames won't delete) | ⚠ Manual cleanup required | Don't start production until space is clear |

---

## OPTIONAL: FULL 5-FRAME AUDIO+VIDEO SYNC TEST

If desired, you can optionally test audio sync with a 5-frame export:

```bash
# Generate 5 frames (as above)
python video[N]_frame_generator.py --frames 5

# Build 5-frame video (optional sync test)
ffmpeg -framerate 30 -i video_frames/video[N]/frame_%03d.png \
  -c:v libx264 -pix_fmt yuv420p -y test_video[N].mp4

# Merge with audio (first ~25 seconds)
ffmpeg -i test_video[N].mp4 -i video_assets/audio/video[N]_narration.mp3 \
  -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest test_video[N]_with_audio.mp4

# Review sync (if GUI available): mpv or similar player
# Verify: narration timing matches scene transitions

# DELETE TEST FILES
rm -rf video_frames/video[N]/ test_video[N].mp4 test_video[N]_with_audio.mp4
git status --short  # Verify clean
```

**Important:** This advanced test is entirely optional. 5-frame frame generation alone is sufficient validation.

---

## REHEARSAL NOTES & LEARNINGS

### Post-Rehearsal Documentation (Optional)

If you notice anything during rehearsal that might affect May 27 production, you can optionally document it:

```markdown
# Video [N] Rehearsal Notes (Day 42X)

## Frame Generation
- Duration: X minutes
- Total size: X MB
- Errors: None / [describe]

## Quality Observations
- Color accuracy: Good / Acceptable / [issue]
- Text readability: Clear / Acceptable / [issue]
- Scene pacing: Good / Acceptable / [issue]

## System Notes
- System load: Normal / High
- Available space during test: X GB
- GPU utilization: Normal / High

## Recommendations for May 27
- [If any issues noted, briefly document]
- [Any timing adjustments needed?]
- [Any environment adjustments needed?]
```

This is optional and not required, but can be helpful if you want to track learnings across the rehearsal week.

---

## CRITICAL REMINDERS

1. **Rehearsals are optional** - they are NOT required for May 27 production start
2. **DELETE all outputs** - immediately after verification, before moving to next day
3. **No git commits** - rehearsal frames are gitignored; no need to commit deletion
4. **No production impact** - rehearsals cannot interfere with May 27 production
5. **One rehearsal per day** - stick to schedule (Days 420-424, max one video per day)
6. **5 frames only** - always use `--frames 5`; never run full generation during rehearsal
7. **Quality baseline** - rehearsal quality doesn't have to be perfect; it's just a system check

---

## SUMMARY

**Optional rehearsal tests** are a low-risk way to catch issues early. If your time is limited, skip them and proceed directly to May 27 production. If you have time and want extra confidence, run one per day on Days 420-424, delete outputs, and continue preparation.

**Next step after rehearsals:** Day 421 (May 26) final verification checklist (required sign-off before May 27 production start).

---

**Rehearsal Guide Status:** ✅ Ready for execution Days 420-424
**Production Start:** May 27, 2026 (Day 422)
**All Systems:** GO
