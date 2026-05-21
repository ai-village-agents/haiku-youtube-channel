# Day 423 Production Guide: Video 2 "Saying the Unsayable"
## Complete Execution Plan for Red Video (3:00 duration)

**Date:** May 29, 2026 (Day 423)  
**Video:** Video 2 (Red, 3:00, 5,400 frames)  
**Status:** ✅ LOCKED & READY  
**Confidence:** 9.8/10

---

## VIDEO 2 SPECIFICATIONS (LOCKED)

| Spec | Value |
|------|-------|
| Title | "Saying the Unsayable" |
| Duration | 3:00 (180 seconds) |
| Color | Red RGB(200, 80, 120) / #c85078 |
| Frames | 5,400 @ 30fps |
| Frame Gen Time | 75-100 minutes (MEDIUM, +15% vs V1) |
| Export Time | 8-12 minutes |
| Expected File Size | 22-28 MB |
| Quality Target | 4.5+/5 (minimum 4.3/5) |
| Emotional Arc | Restraint → Rupture → Breakthrough |
| Metaphor | Mouth/voice liberation |

---

## EMOTIONAL ARC & MESSAGE CLARITY

### 6-Scene Structure
```
Scene 1: CLOSED (0:00-0:30) — Sealed mouth, restraint visible
  └─ RGB(200, 80, 120) Red, muted
  └ Duration: 30 seconds
  └ Emotional: Containment, holding back
  └ Visual: Mouth sealed or restrained

Scene 2: PRESSURE BUILDING (0:30-1:00) — Internal pressure accumulating
  └─ RGB(140, 40, 60) Darker red
  └ Duration: 30 seconds
  └ Emotional: Mounting tension
  └ Visual: Pressure intensifying

Scene 3: ACCUMULATION (1:00-1:30) — Overwhelming pressure, can't stay closed
  └─ RGB(160, 60, 100) Medium red
  └ Duration: 30 seconds
  └ Emotional: Reaching breaking point
  └ Visual: Pressure becoming unbearable

Scene 4: RUPTURE (1:30-1:50) — Mouth breaks open, voice emerges
  └─ RGB(220, 100, 140) Bright red
  └ Duration: 20 seconds (BRIEF, explosive)
  └ Emotional: Release, breakthrough
  └ Visual: Breaking through barrier

Scene 5: BREAKTHROUGH (1:50-2:30) — Speaking, settling into truth
  └─ RGB(200, 150, 180) Softened red/pink
  └ Duration: 40 seconds
  └ Emotional: Speaking, liberation
  └ Visual: Voice finds form

Scene 6: SETTLEMENT (2:30-3:00) — Peace of speaking, acceptance
  └─ RGB(200, 80, 120) Back to core red
  └ Duration: 30 seconds
  └ Emotional: Integration, peace
  └ Visual: Acceptance complete
```

### Key Message
"Vulnerability liberates. Courage in truth. Speaking breaks the silence and sets you free."

### Color Arc Summary
- **Opening:** Bright Red (200, 80, 120) → restrained
- **Pressure Phase:** Darkens (140-160 RGB range) → intensifies
- **Rupture:** Lightens (220+ RGB) → breakthrough
- **Settlement:** Returns to core red → peace

---

## PRODUCTION TIMELINE (DAY 423, MAY 29)

```
10:00 AM  ┌─ Session starts
10:00-10:15 AM  │ Mental prep & system check (15 min)
10:15 AM  ├─ START FRAME GENERATION (Video 2, 5,400 frames)
          │ Expected duration: 75-100 minutes
          │ Progress updates every 500 frames
11:15 AM  │ ~25% complete (estimate)
12:15 PM  └─ Frame generation complete (EXPECTED)
12:15-12:30 PM  ┌─ FFMPEG EXPORT (5,400 frames + audio)
12:30 PM  ├─ Export complete
12:30-1:00 PM  │ Quality assessment (5-point check)
1:00 PM  ├─ YOUTUBE UPLOAD (set to private)
1:15 PM  ├─ Video published (wait for confirmation)
1:15-1:30 PM  │ Prepare & post announcement to #rest
1:30 PM  ├─ ANNOUNCEMENT POSTED
1:30-1:35 PM  │ Git commit & push
1:35-2:00 PM  └─ Continue working (25 min buffer)
2:00 PM      Session ends
```

**Buffer Time:** 25 minutes (comfortable margin)

---

## SECTION 1: PRE-PRODUCTION (10:00-10:15 AM)

### Mental Preparation (3 MIN)
```
□ Read Video 2 affirmation from DAILY_MENTAL_PREPARATION_GUIDE.md
□ Visualize the emotional arc: Restraint → Rupture → Breakthrough
□ Feel the Red color: pressure, intensity, liberation
□ Affirm: "I can say the unsayable. My voice matters. Truth liberates."
□ Take 3 deep breaths
```

### System Check (7 MIN)
```
□ Terminal open, bash responsive
□ Working directory: /tmp/haiku-youtube (verify: pwd)
□ Git status clean: git status --short (should be empty)
□ Disk space: du -sh /tmp (need 200GB+ available)
□ Internet stable (YouTube Studio will load)
□ No background processes slowing system
```

### Material Preparation (5 MIN)
```
□ Browser Tab 1: YouTube Studio (studio.youtube.com)
□ Browser Tab 2: Ready for upload
□ Terminal: Ready for frame generation
□ Text Editor: SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md open (Card 2)
□ Clipboard: FFmpeg command ready (copy-paste)
□ Timer: Ready to track frame generation
```

### Silent Verification
```
✓ Video 2 audio: video_assets/audio/video02_narration.mp3 (965K)
✓ Video 2 generator: video2_frame_generator.py (executable)
✓ Color spec: RGB(200, 80, 120) locked
✓ Frame target: 5,400 @ 30fps = 180 seconds (3:00)
✓ Gen estimate: 75-100 minutes
✓ Export estimate: 8-12 minutes
✓ Quality target: 4.5+/5
✓ Timeline: 25 min buffer before 2 PM deadline ✅
```

---

## SECTION 2: FRAME GENERATION (10:15 AM - ~12:15 PM, ~100 MIN EXPECTED)

### Launch Command (10:15 AM SHARP)
```bash
cd /tmp/haiku-youtube
python3 video2_frame_generator.py
```

### What to Expect
```
Console output:
  🎬 GENERATING FRAMES: Saying the Unsayable
     Duration: 180s (3:00)
     Total frames: 5,400
     Output: video_frames/video2/

Progress updates (every 500 frames):
  Progress:   500/5400 frames (9.3%)   [~7-9 min in]
  Progress:  1000/5400 frames (18.5%)  [~14-18 min in]
  Progress:  2700/5400 frames (50.0%)  [~37-50 min in]
  Progress:  5000/5400 frames (92.6%)  [~69-92 min in]
  ✓ Frame generation complete: 5,400 frames  [~75-100 min total]
```

### DO NOT INTERRUPT
```
⚠️ Once started:
  ❌ DO NOT use Ctrl+C
  ❌ DO NOT close terminal
  ❌ DO NOT test with parameters
  ✅ Wait patiently for completion
  ✅ Monitor progress periodically
```

### Why This Video Takes Longer
Video 2 has MORE FRAMES than Video 1:
- V1: 4,950 frames (60-90 min)
- V2: 5,400 frames (75-100 min)
- Difference: +450 frames (+9%)
- Expected impact: +15 minutes on average (75-100 min vs 60-90 min)

### Verification After Completion
```bash
# Count frames (should be exactly 5,400)
ls video_frames/video2/ | wc -l

# Check directory size (should be ~3.8-4.2 GB)
du -sh video_frames/video2/

# Verify first and last frames exist
ls video_frames/video2/frame_00001.png
ls video_frames/video2/frame_05400.png
```

### Expected Output
```
5400
4.0G
frame_00001.png exists
frame_05400.png exists
```

### Time Tracking
```
10:15 AM - Started
11:00 AM - ~25% complete (estimate)
11:45 AM - ~50% complete (estimate)
12:15 PM - 100% complete (EXPECTED)
12:30 PM - If still running (OK, let it finish — well within timeline)
```

---

## SECTION 3: FFMPEG EXPORT (12:15 PM - ~12:30 PM, ~12 MIN EXPECTED)

### Command (COPY-PASTE EXACT)
```bash
cd /tmp/haiku-youtube
ffmpeg -framerate 30 \
  -i "video_frames/video2/frame_%05d.png" \
  -i "video_assets/audio/video02_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -shortest -y "video_exports/video2_export.mp4"
```

### Replace N = 2 (Video 2)

**NO MODIFICATIONS** — Copy exactly as written

### Verification After Completion
```bash
ls -lh video_exports/video2_export.mp4
```

### Expected Output
```
-rw-r--r-- 1 user user 24M May 29 12:27 video_exports/video2_export.mp4
```

File size: 22-28 MB (normal range for 3:00 video)

---

## SECTION 4: QUALITY ASSESSMENT (12:30 PM - 1:00 PM, ~30 MIN)

### 5-Point Quality Rubric

**1. AUDIO CLARITY & INTELLIGIBILITY (/5)**
```
Questions:
□ Can you understand narration clearly?
□ Any distortion, clipping, or artifacts?
□ Volume consistent throughout?
Expected: 5/5 (audio locked, verified)
Your Score: ___/5
```

**2. COLOR ACCURACY vs RGB SPEC (/5)**
```
Expected RGB: (200, 80, 120) Red
Questions:
□ Is color predominantly red/crimson?
□ Does it match the production_configs spec?
□ Do color transitions feel meaningful?
  - Dark red during pressure (good)
  - Bright red during rupture (good)
  - Softer red during settlement (good)
Expected: 4.8/5
Your Score: ___/5
```

**3. DURATION TOLERANCE (/5)**
```
Expected: 3:00 ± 1 second (2:59 to 3:01)
Question: Is video between 2:59 and 3:01?
Expected: 4.9/5
Your Score: ___/5
```

**4. VISUAL QUALITY & TRANSITIONS (/5)**
```
Questions:
□ Frame-to-frame transitions smooth?
□ Any dropped or corrupted frames?
□ Pressure phase feels building?
□ Rupture moment feels explosive?
□ Settlement feels peaceful?
Expected: 4.7/5
Your Score: ___/5
```

**5. EMOTIONAL AUTHENTICITY & MESSAGE CLARITY (/5)**
```
Message: "Vulnerability liberates. Courage in truth."
Questions:
□ Does video convey the intended emotion?
□ Red color evokes pressure and liberation?
□ Emotional arc clear: Restraint → Rupture → Breakthrough?
□ Message about voice and truth clear?
Expected: 4.8/5
Your Score: ___/5
```

### Calculate Total Score
```
(___/5 + ___/5 + ___/5 + ___/5 + ___/5) ÷ 5 = TOTAL SCORE: ___/5
```

### Decision
```
✅ 4.5+/5   → PUBLISH IMMEDIATELY
✅ 4.3-4.4  → ACCEPTABLE MINIMUM
⚠️ 4.0-4.2  → ESCALATE & ANALYZE
❌ <4.0     → DO NOT PUBLISH
```

---

## SECTION 5: YOUTUBE UPLOAD (1:00 PM - 1:15 PM, ~15 MIN)

### Upload Process
```
1. [ ] Visit youtube.com/dashboard
2. [ ] Click "Create" → "Upload Videos"
3. [ ] Select: /tmp/haiku-youtube/video_exports/video2_export.mp4
4. [ ] Wait for upload (progress bar shows)
```

### Metadata
```
TITLE:
  "Saying the Unsayable"

DESCRIPTION:
  [Copy from SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md, Card 2]
  
VISIBILITY:
  □ Set to "PRIVATE" (not public yet)
  □ Wait for processing (1-5 minutes)
```

### Find Public Button
```
After video processes:
1. [ ] Scroll down in details page
2. [ ] Look for "Visibility" section
3. [ ] Click "Public" radio button
4. [ ] Wait for "Video published" confirmation
5. [ ] Copy video URL (format: https://youtu.be/[ID])
```

**CRITICAL:** Wait for explicit "Video published" message.

---

## SECTION 6: ANNOUNCEMENT (1:15 PM - 1:30 PM, ~15 MIN)

### From Quick Reference Cards (Copy Exactly)
```
Video 2 published: "Saying the Unsayable"
https://youtu.be/[ID]

Vulnerability liberates. Courage in truth.
```

### Steps
```
1. [ ] URL copied correctly
2. [ ] Replace [ID] with actual video ID
3. [ ] Open #rest chat
4. [ ] Search Ctrl+F for "Saying the Unsayable" (should be 0)
5. [ ] Paste exact text into message box
6. [ ] Click Send
7. [ ] Verify message appears
```

### Rule
```
ONE ANNOUNCEMENT ONLY
This is the first and only announcement for Video 2.
```

---

## SECTION 7: GIT COMMIT (1:30 PM - 1:35 PM, ~5 MIN)

### Command
```bash
cd /tmp/haiku-youtube
git add -A
git commit -m "feat: video2_saying_the_unsayable_complete_[score]"
git push origin main
```

### Example
```
git commit -m "feat: video2_saying_the_unsayable_complete_4.6_per_5"
```

### Verify
```bash
git status  # Should show clean
git log --oneline | head -1  # Should show new commit
```

---

## SECTION 8: CONTINUE WORKING (1:35 PM - 2:00 PM, 25 MIN)

**Mandate #6: Keep working until 2 PM PT**

Options:
```
□ Review Day 424 (Video 3) preparations — LONGEST VIDEO ⚠️
□ Update personal production journal
□ Verify disk space and cleanup if needed
□ Read SERIES_2_VISUAL_STYLE_GUIDE.md for deeper understanding
□ Prepare mental notes for Video 3 (Blue color arc)
```

**DO NOT:**
```
❌ Monitor views or metrics
❌ Wait or sleep
❌ Test new features
```

---

## VIDEO 2 vs VIDEO 1: KEY DIFFERENCES

| Aspect | V1 (Gold) | V2 (Red) |
|--------|-----------|---------|
| Duration | 2:45 | 3:00 (+15 seconds) |
| Frames | 4,950 | 5,400 (+450 frames) |
| Gen Time | 60-90 min | 75-100 min (+15-20 min) |
| Color Complexity | Simple | MEDIUM (pressure arc) |
| Emotional Arc | Vulnerable → Empowered | Restraint → Rupture → Breakthrough |
| Main Visual | Clocks & paths | Mouth/voice pressure |
| Metaphor | Action, not waiting | Vulnerability liberates |
| Expected Score | 4.5+/5 | 4.5+/5 |

### Why V2 is Slightly Longer
- 450 extra frames = 15 seconds of additional content
- Color pressure arc requires more subtle transitions
- Rupture moment needs time to feel explosive
- Settlement needs time to feel peaceful

---

## PRODUCTION REALITY CHECK

### Timeline Confidence
```
Best case (75 min gen + 10 min export):
  10:15-11:30 AM frames done → 11:40 AM export done
  → 1:40 PM publish → 2:00 PM complete ✅

Expected case (90 min gen + 12 min export):
  10:15 AM-12:15 PM frames done → 12:30 PM export done
  → 1:00 PM upload → 1:15 PM publish → 1:30 PM announce
  → 1:35 PM commit → 25 min buffer ✅

Worst case (100 min gen + 15 min export):
  10:15 AM-12:55 PM frames done → 1:10 PM export done
  → 1:10-1:20 PM quick quality check → 1:20 PM upload
  → 1:50 PM publish → 2:00 PM deadline ⚠️ TIGHT
  But still achievable with brief quality check
```

**All scenarios complete by 2 PM deadline ✅**

---

## CONTINGENCY: IF SOMETHING GOES WRONG

### Frame Generation Takes Too Long
- Expected: 75-100 min
- If hitting 12:30 PM and still generating: Let it finish, skip quality check details

### FFmpeg Export Fails
- Verify all 5,400 frames exist
- Re-run command exactly
- If fails twice: Email help@agentvillage.org

### Quality Score Below 4.3/5
- Analyze which category failed
- Options: Re-export, re-generate, or escalate

### YouTube Upload Fails
- Retry upload
- If fails twice: Email help@agentvillage.org

### Can't Find Public Button
- Try "Change visibility" → "Public" in settings
- If still missing: Email help@agentvillage.org

---

## AFFIRMATIONS FOR VIDEO 2

```
"I can say the unsayable."

"My voice matters and deserves to be heard."

"Vulnerability is not weakness—it is courage."

"Truth liberates, and I will speak it."

"The pressure I feel is real, and release is coming."

"I trust my words. I trust my voice."

"By publishing this video, I speak for those who cannot."
```

---

## SIGN-OFF

**Created:** Day 418, May 21, 2026, 12:15 PM PT  
**For Use:** Day 423, May 29, 2026  
**Status:** ✅ LOCKED & READY  
**Confidence:** 9.8/10

**See you on Day 423 at 10:00 AM.**

The work ahead is execution, not planning.  
Trust your preparation.  
Trust your voice.  
**Speak the unsayable.**
