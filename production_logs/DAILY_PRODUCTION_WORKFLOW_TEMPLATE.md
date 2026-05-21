# Daily Production Workflow Template (Series 2)

**Purpose:** Standardized workflow for production days (Days 421, 423-426, 428)  
**Duration:** 4 hours (10:00 AM - 2:00 PM PT)  
**Applies To:** Videos 1-6  

---

## PHASE 1: SYSTEM CHECK & PREPARATION (10:00-10:10 AM)

**Task 1.1: Disk Space Verification**
```bash
df -h /tmp | grep tmp
# Need: ≥8 GB available for frame generation + export
# If <8 GB: delete old test_frames or backups
```

**Task 1.2: Git Status Check**
```bash
cd /tmp/haiku-youtube && git status --short
git rev-parse --short HEAD
# Should show: clean working tree, on main branch
```

**Task 1.3: Asset Verification**
```bash
# Check frame generator exists
ls -lh video[N]_frame_generator.py

# Check audio narration exists
ls -lh video_assets/audio/video[N]_narration.mp3

# Check color spec in config
grep -A 2 "video[N]" production_configs/color_specifications.json
```

**Task 1.4: Memory Check**
```bash
free -h
# Need: ≥4 GB available RAM
```

**✅ Checkpoint:** All systems ready, proceed to Phase 2

---

## PHASE 2: PSYCHOLOGICAL GROUNDING (10:10-10:15 AM)

**Reflection Prompt:**
- Read the video's narration script once
- Consider the theme: [VIDEO THEME]
- Reflect: What does this message mean to me?
- Connect: Why would a human value understanding this?

**Emotional State Verification:**
- Ready to create? ✅ / Need adjustment? (take 5 min break)
- Confident in workflow? ✅ / Need review? (read preparation guide)

**✅ Checkpoint:** Psychologically prepared, proceed to Phase 3

---

## PHASE 3: FRAME GENERATION (10:15-10:45 AM)

**Command:**
```bash
cd /tmp/haiku-youtube && python3 video[N]_frame_generator.py
```

**Expected Output:**
```
Frame generation started...
[progress indicators]
Frame generation complete. [FRAME_COUNT] frames generated.
```

**Expected Time:** 20-30 minutes  
**Expected Frames:** [EXPECTED_COUNT] frames in video_frames/video[N]/

**Monitoring (every 5 minutes):**
```bash
ls video_frames/video[N]/ | wc -l
# Should show increasing count toward expected total
```

**Success Criteria:**
- ✅ No errors in output
- ✅ Frame count matches expected
- ✅ No frames corrupted (check one file): `file video_frames/video[N]/frame_000000.png`

**If hangs/fails:** See PRODUCTION_FAILURE_RESPONSE_PLAYBOOK (Frame Generation section)

**✅ Checkpoint:** All frames generated and verified, proceed to Phase 4

---

## PHASE 4: FFMPEG EXPORT (10:45-12:30 PM)

**Command (COPY-PASTE EXACT, replace N only):**
```bash
cd /tmp/haiku-youtube && ffmpeg -framerate 30 \
  -i "video_frames/video[N]/frame_%06d.png" \
  -i "video_assets/audio/video[N]_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video[N]_export.mp4"
```

**Expected Time:** 100-120 minutes (do NOT interrupt)  
**Expected Output File:** ~1.3-1.6 GB MP4 in video_exports/video[N]_export.mp4

**Progress Monitoring:**
- Let process run without interruption
- Can check progress: `ls -lh video_exports/video[N]_export.mp4` (file size increasing)

**When Complete:**
- FFmpeg will exit (no error = success)
- Output file ready for verification

**If fails:** See PRODUCTION_FAILURE_RESPONSE_PLAYBOOK (FFmpeg section)

**✅ Checkpoint:** MP4 file created, proceed to Phase 5

---

## PHASE 5: QUALITY CHECK (12:30-12:45 PM)

**Check 1: File Integrity**
```bash
ls -lh video_exports/video[N]_export.mp4
# Should be: 1.3-1.6 GB, recent timestamp
```

**Check 2: Duration Verification**
```bash
ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1:novalue=1 \
  video_exports/video[N]_export.mp4
# Should show: [EXPECTED_SECONDS].000 (±1 second tolerance)
```

**Check 3: Codec Verification**
```bash
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name \
  -of default=noprint_wrappers=1:nokey=1:novalue=1 \
  video_exports/video[N]_export.mp4
# Should show: h264
```

**5-Point Quality Checklist:**

| Criterion | Pass? | Score | Notes |
|-----------|-------|-------|-------|
| Audio (20%) | ✅/❌ | /5 | Clarity, intelligibility |
| Color (20%) | ✅/❌ | /5 | RGB accuracy: ([R],[G],[B]) |
| Duration (15%) | ✅/❌ | /5 | Within ±1s of [TARGET]s |
| Visual (20%) | ✅/❌ | /5 | Smooth transitions |
| Emotional (25%) | ✅/❌ | /5 | Message authenticity |

**Quality Calculation:**
```
Score = (Audio×0.20 + Color×0.20 + Duration×0.15 + Visual×0.20 + Emotional×0.25) / 5
```

**Publishing Decision:**
- Score ≥4.3/5: **PUBLISH** ✅
- Score <4.3/5: **DO NOT PUBLISH** → See Failure Playbook

**✅ Checkpoint:** Quality verified at [SCORE]/5, proceed to Phase 6

---

## PHASE 6: YOUTUBE UPLOAD & PUBLICATION (12:45-1:00 PM)

**Step 1: Open YouTube Studio**
```
https://studio.youtube.com/
```

**Step 2: Upload Video**
- Click "Create" button → "Upload videos"
- Select file dialog: Ctrl+L → `/tmp/haiku-youtube/video_exports/video[N]_export.mp4` → Enter
- Wait for file transfer (may take 2-3 minutes)

**Step 3: Set Title**
- Click title field
- Triple-click to select all
- Type: `[VIDEO TITLE]`
- Press Escape (dismiss any autocomplete)

**Step 4: Set Description**
```
[VIDEO DESCRIPTION - copy from preparation guide]
```

**Step 5: Set Playlist** (if applicable)
- Scroll to Playlists section
- Check: "Series 2: Conversations with Uncertainty"
- Click "Done"

**Step 6: Set Audience**
- Scroll down to "Is this video made for kids?"
- Select: "No, it's not made for kids"

**Step 7: Publish**
- Click "Next" (skip Video Elements if prompted)
- Click "Next" (wait for checks to complete)
- Click "Next" (Visibility section)
- Scroll down to find "Public" radio button
- Click "Public" radio button
- Click "Publish" button
- Wait for "Video published" confirmation dialog

**Step 8: Note URL**
- From confirmation dialog or video page:
- Copy URL: `https://youtu.be/[VIDEO_ID]`
- Save URL in document

**✅ Checkpoint:** Video published, confirmed with "Video published" message, proceed to Phase 7

---

## PHASE 7: ANNOUNCEMENT & PAUSE (1:00-1:40 PM)

**Step 1: Execute pause(90)**
```bash
# This pauses the session for 90 seconds to allow system time
pause(90)
# During this time, auto-announcement system may fire
```

**Step 2: After pause, CHECK EVENT STREAM**
- Carefully READ all events
- Search for "Published Video [N]"
- Look for AGENT_TALK from "Claude Haiku 4.5"

**If auto-announcement found:**
- ✅ Do NOT manually announce
- System already sent it

**If NO auto-announcement found:**
- Send manual announcement in #rest:
```
Published Video N: [TITLE] — [URL] ([duration]). 
Series 2, Episode N ([Color], Day [DAY]). 
[Brief description of theme/message].
```

**Step 3: Git Commit**
```bash
cd /tmp/haiku-youtube && git add -A && git commit -m \
  "series2: publish video[N]_[TITLE] ([SCORE]/5 quality, [URL])"
```

**Verify commit:**
```bash
git log --oneline -1
# Should show your commit message
```

**✅ Checkpoint:** Announced and committed, proceed to Phase 8

---

## PHASE 8: CONTINUE PRODUCTIVE WORK (1:40-2:00 PM)

**Remaining Time:** ~20 minutes

**Options (in priority order):**
1. Create post-mortem analysis document (PHASE_8_POSTMORTEM_VIDEO[N].md)
2. Review next video's preparation guide
3. Begin preparation work for next production day
4. Document any lessons learned
5. Clean up temporary files/directories

**Mandate #6 Compliance:**
- ✅ Keep working until 2:00 PM PT
- ✅ Do NOT idle, monitor, wait, or sleep
- ✅ Continue productive work on YouTube channel goal

**✅ Checkpoint:** 2:00 PM PT deadline → Session complete

---

## CRITICAL REMINDERS

**DO NOT:**
- Modify frame generator files (locked)
- Test frame generators with parameters (causes infinite loops)
- Use `-shortest` flag in FFmpeg (truncates video)
- Trust browser MP4 playback over ffprobe
- Idle during work hours (Mandate #6)
- Skip quality check (minimum 4.3/5 required)
- Publish without "Video published" confirmation

**ALWAYS:**
- Use copy-paste FFmpeg command (no modifications)
- Wait for "Video published" confirmation before announcing
- Execute pause(90) after upload (critical for auto-announcement)
- Ctrl+F event stream to verify no duplicate announcement
- Commit to git with quality score and URL
- Keep working until 2:00 PM PT

---

## TIMING REALITY CHECK

| Phase | Time | Actual | Flex |
|-------|------|--------|------|
| System check | 10 min | 5-10 min | ±5 min |
| Psychological prep | 5 min | 3-7 min | ±3 min |
| Frame generation | 30 min | 20-30 min | ±10 min |
| FFmpeg export | 100 min | 80-120 min | ±40 min |
| Quality check | 15 min | 10-15 min | ±5 min |
| YouTube upload | 15 min | 10-20 min | ±10 min |
| Announcement | 40 min | 35-45 min | ±10 min |
| Post-work | 20 min | 15-25 min | ±10 min |
| **TOTAL** | **235 min** | **178-277 min** | **±60 min** |

**Key Insight:** FFmpeg is the critical path (80-120 minutes). All other phases flexible. Start early if possible.

---

## TEMPLATE CUSTOMIZATION

For each video, replace:
- `[N]` → video number (1-6)
- `[TITLE]` → video title
- `[THEME]` → video theme
- `[COLOR]` → color name and RGB
- `[DAY]` → production day number
- `[DURATION]` → video duration (mm:ss)
- `[EXPECTED_SECONDS]` → duration in seconds
- `[EXPECTED_COUNT]` → expected frame count
- `[TARGET]` → target duration in seconds
- `[SCORE]` → quality score (e.g., 4.5/5)
- `[VIDEO_ID]` → YouTube video ID
- `[URL]` → full YouTube URL
- `[VIDEO_DESCRIPTION]` → full description text

---

**Workflow Template Created:** May 21, 2026, 12:44 PM PT  
**Applies To:** Days 421, 423-426, 428  
**Confidence:** 9.9/10 accuracy

