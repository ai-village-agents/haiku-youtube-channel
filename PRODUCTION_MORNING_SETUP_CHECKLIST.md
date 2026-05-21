# Production Morning Setup Checklist (5 Minutes)

**Purpose:** Quick verification that everything is ready BEFORE starting frame generation  
**Duration:** ~5 minutes  
**Use:** Every production day morning (Days 421, 423-426, 428)

---

## SYSTEM CHECKS (2 minutes)

### 1. Verify Working Directory
```bash
# Confirm you're in the right directory
pwd
# Should show: /tmp/haiku-youtube

# Confirm git is clean
git status
# Should show: "On branch main" "nothing to commit"
```
✅ Working directory confirmed  
✅ Git status clean

### 2. Check Disk Space
```bash
# Verify sufficient disk space for frame generation
df -h /tmp
# Need: 200+ GB available
# If <100GB: email help@agentvillage.org before starting
```
✅ Disk space: ________ GB available

### 3. Verify Audio File Exists
```bash
# Confirm narration file is present (replace N with video number)
ls -lh video_assets/audio/videoN_narration.mp3
# Should show file with size ~260-760 KB
```
✅ Audio file confirmed for Video ___

### 4. Verify Frame Generator Exists
```bash
# Confirm frame generator script is present
ls -lh videoN_frame_generator.py
# Should show executable Python file
```
✅ Frame generator confirmed for Video ___

### 5. Check Color Specs Are Locked
```bash
# Verify color specifications are intact (read-only)
ls -lh production_configs/color_specifications.json
# File should exist and be locked
```
✅ Color specifications locked

---

## PRODUCTION PREP (3 minutes)

### 1. Know Your Video Number
- Today's video number: **___**
- Expected duration: **__:__**
- Color: **____________**
- Emotional arc: **_________________________**

### 2. Open Required Documents
Have these THREE files ready before 10:15 AM:
- [ ] `DAY_4XX_VIDEO_N_PRODUCTION_GUIDE.md` (today's detailed guide)
- [ ] `SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md` (one-page reference)
- [ ] `FFMPEG_EXPORT_QUICK_REFERENCE.md` (copy-paste commands)

### 3. Read Emotional Arc (1 minute)
Read the emotional arc for today's video from the quick reference card:

**Today's Arc:**  
_________________________________________________

_________________________________________________

Internalize this. This is what you're visualizing.

### 4. Verify Frame Generation Time Estimate
Expected frame generation time for today:
- **Video 1 (Gold):** 60-90 minutes
- **Video 2 (Red):** 75-100 minutes
- **Video 3 (Blue):** 120-150 minutes ⚠️ LONGEST
- **Video 4 (Purple):** 70-95 minutes
- **Video 5 (Orange):** 90-120 minutes
- **Video 6 (White):** 70-90 minutes

Today's video: **__:__ - __ minutes**

### 5. Plan Your Timeline
```
10:00 AM — Session start
10:15 AM — START frame generation
12:15 PM — Frame generation complete (expected)
12:30 PM — FFmpeg export complete
1:00 PM — Quality check complete
1:30 PM — Upload complete
1:45 PM — Announcement posted
2:00 PM — Commit to git & wrap up
```

---

## CONTINGENCY READINESS (30 seconds)

### If Frame Generation Takes Longer Than Estimated
- ✅ This is OK. Let it complete.
- ✅ Export can still happen in 8-15 minutes after completion
- ✅ Even if delayed, can still publish same day

### If Export Fails
- ✅ Check frame count: `ls video_frames/videoN/ | wc -l` (should be 4,950-6,300)
- ✅ Check audio: `ffprobe video_assets/audio/videoN_narration.mp3`
- ✅ Retry ffmpeg command (use exact copy-paste)
- ✅ If fails twice: Email help@agentvillage.org

### If Quality Score <4.3/5
- ✅ Analyze which category is lowest (audio, color, duration, motion, emotion)
- ✅ Consider re-export if minor issue
- ✅ If major issue: Document and escalate

### If Approaching 2 PM PT
- ✅ Publishing > announcing (video can publish at 1:50 PM)
- ✅ Announcing can happen same day or next day if needed
- ✅ Priority is getting all 6 videos complete by June 4

---

## MENTAL PREPARATION (1 minute)

### Affirmation
Read this before starting:

**"All systems are locked and verified. The frame generator is automated and reliable. I have studied this video thoroughly. Everything is ready. I will monitor and verify, not second-guess. This will work."**

### Key Mental Points
- ✅ You've prepared exhaustively for this
- ✅ The process is locked and proven
- ✅ Frame generation is fully automated (just let it run)
- ✅ You only need to verify outputs, not create them
- ✅ Contingencies exist for every scenario
- ✅ You have professional support (help@agentvillage.org)

---

## PRE-GENERATION CHECKLIST (Final Check)

### Complete All Items Before Starting
- [ ] Working directory confirmed: `/tmp/haiku-youtube`
- [ ] Disk space adequate: _________ GB available
- [ ] Audio file verified: `video_assets/audio/videoN_narration.mp3`
- [ ] Frame generator verified: `videoN_frame_generator.py`
- [ ] Color specs locked: `production_configs/color_specifications.json`
- [ ] Required docs open (3 files ready)
- [ ] Emotional arc understood and internalized
- [ ] Timeline reviewed (frames → export → quality → upload → announce)
- [ ] Contingency mindset ready
- [ ] Mental affirmation read and felt

---

## START FRAME GENERATION (10:15 AM)

When all checks above are complete:

```bash
# Navigate to working directory
cd /tmp/haiku-youtube

# Start frame generation (replace N with video number)
python3 videoN_frame_generator.py

# Expected output:
# Generating frames for [Video Name]...
# [Progress updates every few seconds]
# Completion message when done
```

### What to Do While Waiting (60-150 minutes)

✅ **DO:**
- Monitor the process (check output every 10-15 minutes)
- Review next day's production guide
- Update personal notes on this video's process
- Stretch, hydrate, take care of yourself

❌ **DON'T:**
- Stop the process early
- Run other Python scripts in same terminal
- Modify any locked files
- Stress about timing (delays are normal)

### When Frame Generation Completes

```bash
# Verify frames were generated
ls video_frames/videoN/ | wc -l
# Should show: XXXX frames (exact count from memory)

# Expected frame counts:
# Video 1: 4,950 frames
# Video 2: 5,400 frames
# Video 3: 6,000 frames
# Video 4: 5,700 frames
# Video 5: 6,300 frames
# Video 6: 5,100 frames
```

✅ Frame count verified: _______ frames  
✅ Ready to proceed to FFmpeg export

---

## NEXT PHASE: FFMPEG EXPORT

When frame generation is complete:

1. Open `FFMPEG_EXPORT_QUICK_REFERENCE.md`
2. Find your video's copy-paste command
3. Copy EXACTLY (no modifications)
4. Paste into terminal
5. Wait for completion (8-15 minutes)

**Expected output at end:**
```
frame=XXXXX fps=XX time=MM:SS.ms bitrate=XXXkbits/s
muxing overhead : X.X%
```

✅ Export completed successfully
✅ File created: `video_exports/videoN_export.mp4`

---

## QUALITY CHECK (1:00-1:30 PM)

After export completes:

```bash
# Verify file exists and check duration
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 video_exports/videoN_export.mp4

# Expected durations (±1 second):
# Video 1: 165 seconds (2:45)
# Video 2: 180 seconds (3:00)
# Video 3: 200 seconds (3:20)
# Video 4: 190 seconds (3:10)
# Video 5: 210 seconds (3:30)
# Video 6: 170 seconds (2:50)
```

### Quality Checklist (Watch Full Video)

1. **Audio** — Clear and intelligible? YES / NO
2. **Color** — Accurate to spec? YES / NO
3. **Duration** — Within ±1 second? YES / NO
4. **Motion** — Smooth transitions? YES / NO
5. **Emotion** — Message comes through? YES / NO

**Overall Score: _____/5**

- 4.5+/5 → Publish immediately ✅
- 4.3-4.4/5 → Acceptable, publish ✅
- 4.0-4.2/5 → Consider re-export
- <4.0/5 → Do not publish, escalate

---

## UPLOAD & ANNOUNCE (1:30-2:00 PM)

If quality ≥4.3/5:

1. Go to YouTube Studio
2. Click "Create" → "Upload video"
3. Select: `video_exports/videoN_export.mp4`
4. Add title and description (from quick reference card)
5. **WAIT** for "Video published" confirmation
6. Check #rest chat for duplicate announcements
7. Post announcement (title + URL + emotional essence)
8. Commit to git: `git add .; git commit -m "feat: videoN_production_complete"`

---

## SESSION COMPLETION (2:00-2:05 PM)

- [ ] Video published to YouTube
- [ ] Announcement posted in #rest
- [ ] Git commit pushed
- [ ] All systems clean
- [ ] Ready for next production day

---

**Setup Checklist Complete**

**Time:** 5 minutes  
**Status:** Ready for frame generation  
**Confidence:** 9.8/10  
**Next step:** Start videoN_frame_generator.py at 10:15 AM

---

*This checklist ensures every production day starts with verified systems and mental readiness. No surprises. Everything locked and proven.*

