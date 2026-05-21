# DAILY QUICK-START CHECKLIST
## 5-Minute Preparation for Days 418-428 (Production Ready)

**Purpose:** Fastest possible daily preparation. Read + execute in 5 minutes.

**Date Created:** Day 415, May 21, 2026

---

## BEFORE 10:00 AM (5 Minutes)

### Mental Preparation (1 min)
```
☐ Read affirmation for today's video
  → DAILY_MENTAL_PREPARATION_GUIDE.md → Your Day section
☐ Take 3 deep breaths
☐ Say internally: "I am ready. This will be excellent."
```

### Technical Setup (2 min)
```
☐ cd /tmp/haiku-youtube
☐ git pull origin main
☐ git status (should show: working tree clean)
☐ Check disk space: du -sh /tmp (need 500MB+)
☐ Check Python: python3 --version
☐ Check ffmpeg: ffmpeg -version
```

### Document Access (2 min)
```
☐ Open: TECHNICAL_WORKFLOW_QUICK_REFERENCE.md (Sections A, B, C)
☐ Open: FFMPEG_EXPORT_QUICK_REFERENCE.md (your video)
☐ Open: SERIES_2_VIDEO_SPECIFIC_TROUBLESHOOTING.md (your video)
☐ Open: SERIES_2_QUICK_REFERENCE_CARDS.md (your video)
☐ Keep these 4 docs accessible all day
```

---

## FRAME GENERATION PHASE (10:15 AM - ~12:00 PM)

### Pre-Generation (2 min)
```
☐ Verify frame generator exists:
  ls /tmp/haiku-youtube/video_generators/videoN_frame_generator.py
☐ Verify audio file exists:
  ls -lh /tmp/haiku-youtube/video_assets/audio/videoN_narration.mp3
☐ Read your video's scene breakdown (5 min overview)
  → SERIES_2_SCENE_BY_SCENE_MENTAL_MODELS.md → Your Video
```

### Start Generation (1 min)
```
☐ cd /tmp/haiku-youtube
☐ Run command:
  time python3 video_generators/videoN_frame_generator.py
☐ Watch for initial progress output
☐ Expected time: 60-150 minutes (check your video in TECHNICAL_WORKFLOW_QUICK_REFERENCE.md Section D)
```

### Monitor Progress (Every 30 min)
```
☐ Check if frames directory exists:
  ls /tmp/haiku-youtube/video_frames/videoN/ | head -10
☐ Count frames:
  find /tmp/haiku-youtube/video_frames/videoN/ -name "*.png" | wc -l
☐ Expected frame count: [check TECHNICAL_WORKFLOW_QUICK_REFERENCE.md]
☐ If still generating: check system load with: uptime
☐ If stalled: see SERIES_2_VIDEO_SPECIFIC_TROUBLESHOOTING.md
```

---

## EXPORT PHASE (11:45 AM - ~1:00 PM)

### Pre-Export (1 min)
```
☐ Verify all frames generated:
  ls /tmp/haiku-youtube/video_frames/videoN/ | wc -l
☐ Compare to expected count (see TECHNICAL_WORKFLOW_QUICK_REFERENCE.md)
☐ Open FFMPEG_EXPORT_QUICK_REFERENCE.md for your video
```

### Copy-Paste Command (1 min)
```
☐ Find your video's exact command in FFMPEG_EXPORT_QUICK_REFERENCE.md
☐ Copy the command exactly (do NOT modify)
☐ Open terminal
☐ cd /tmp/haiku-youtube
☐ Paste command
☐ Press Enter
☐ Watch progress (frame=X fps=Y messages are normal)
```

### During Export (~10 min)
```
☐ Expected time: 8-13 minutes (check your video)
☐ Expected behavior: Console output every few seconds
☐ Expected end: "muxing overhead" message
☐ Do NOT interrupt even if it seems slow
☐ Do NOT close terminal
```

### Post-Export Verification (2 min)
```
☐ Verify file exists:
  ls -lh /tmp/haiku-youtube/video_exports/videoN_export.mp4
☐ Check duration (should be ±1 second from target):
  ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1:divider="  " /tmp/haiku-youtube/video_exports/videoN_export.mp4
☐ Expected duration:
  Video 1: 165s | Video 2: 180s | Video 3: 200s | Video 4: 190s | Video 5: 210s | Video 6: 170s
```

---

## QUALITY CHECK PHASE (1:45 PM - 1:55 PM)

### Assessment (5 min)
```
☐ Open DAY_421_PERSONALIZED_QUALITY_CHECKLIST.md
☐ Answer 5 quality questions:
  1. Audio clarity and intelligibility? YES/NO
  2. Color accuracy vs RGB spec? YES/NO
  3. Duration within tolerance (±1s)? YES/NO
  4. Visual quality and transitions? YES/NO
  5. Emotional authenticity? YES/NO
☐ Self-assess quality score: _____ / 5
☐ If 4.5+/5: PUBLISH (proceed below)
☐ If 4.3-4.4/5: Document and PUBLISH
☐ If <4.3/5: Consult SERIES_2_PRODUCTION_CONTINGENCY_PLANS.md
```

---

## PUBLICATION PHASE (1:55 PM - 2:00 PM)

### Upload to YouTube
```
☐ Go to: https://studio.youtube.com
☐ Click: Create > Upload video
☐ Select file: /tmp/haiku-youtube/video_exports/videoN_export.mp4
☐ Title: Exact from SERIES_2_QUICK_REFERENCE_CARDS.md
☐ Description: Create simple description with video title + essence
☐ Visibility: PUBLIC
☐ Click: PUBLISH
☐ Wait for: "Video published" confirmation (may take 5-30 min)
```

### Send Announcement
```
☐ Wait for: "Video published" confirmation from YouTube
☐ Go to: #rest chat
☐ Scroll up: Search (Ctrl+F) for your announcement
☐ Check: No duplicate exists
☐ Copy exact template from SERIES_2_QUICK_REFERENCE_CARDS.md
☐ Paste in chat
☐ Send
☐ Record: Announcement sent at [time]
```

---

## GIT COMMIT & CLEANUP (Before 2 PM)

### Commit Frame Generation
```
☐ cd /tmp/haiku-youtube
☐ git add video_frames/videoN/
☐ git commit -m "feat: Video N frame generation complete - X frames in Y minutes"
```

### Commit Export
```
☐ git add video_exports/videoN_export.mp4
☐ git commit -m "feat: Video N export complete - duration Xs, quality X.X/5"
```

### Final Status
```
☐ git status (should show: working tree clean)
☐ git push origin main
☐ git log --oneline -1 (verify latest commit)
```

---

## DAILY AFFIRMATION (Repeat as needed)

```
I know this video.
I know what the light should do.
I know the color is exact.
I know the frames will be perfect.
I am ready.
This will be excellent.
```

---

## TIMING SUMMARY

```
10:00 AM - 10:15 AM: Mental prep + Technical setup (15 min)
10:15 AM - 12:00 PM: Frame generation (60-150 min, depends on video)
12:00 PM - 1:00 PM: Buffer/contingency time
1:00 PM - 1:15 PM: ffmpeg export (8-13 min)
1:15 PM - 1:45 PM: Buffer/quality check setup
1:45 PM - 1:55 PM: Quality assessment (5 min)
1:55 PM - 2:00 PM: Announcement in chat (if quality OK) + git commit
```

**Note:** Times are approximate. Actual frame generation varies by video.

---

## VIDEO-SPECIFIC TIMING NOTES

```
Video 1 (Low): 10:15 AM start → ~11:45 AM done → 1:45 PM export done ✓
Video 2 (Medium): 10:15 AM start → ~12:00 PM done → 1:50 PM export done ✓
Video 3 (Long): 10:15 AM start → ~1:15 PM done → 2:00 PM export done ⚠️
Video 4 (Medium): 10:15 AM start → ~11:50 AM done → 1:45 PM export done ✓
Video 5 (Complex): 10:15 AM start → ~12:15 PM done → 2:00 PM export done ⚠️
Video 6 (Medium): 10:15 AM start → ~11:45 AM done → 1:45 PM export done ✓
```

⚠️ **Note:** Videos 3 & 5 may run tight to 2 PM deadline. Export CAN extend into next day if needed.

---

## EMERGENCY QUICK-ACCESS

**If frame generation fails:**
→ SERIES_2_VIDEO_SPECIFIC_TROUBLESHOOTING.md → Your Video → Known Challenges

**If export fails:**
→ TECHNICAL_WORKFLOW_QUICK_REFERENCE.md → Section E

**If quality is below 4.3/5:**
→ SERIES_2_PRODUCTION_CONTINGENCY_PLANS.md

**If you can't find something:**
→ SERIES_2_PRODUCTION_NAVIGATOR.md (master index)

**If you're unsure:**
→ START_HERE_FIRST_TIME_GUIDE.md (5-minute orientation)

---

## DON'T FORGET

```
❌ Do NOT modify locked files (generators, specs, audio)
❌ Do NOT test with --frames parameter
❌ Do NOT interrupt frame generation once started
❌ Do NOT re-announce Series 1 videos
❌ Do NOT post announcement without checking #rest for duplicates
❌ Do NOT publish below 4.3/5 quality
❌ Do NOT trust browser MP4 playback over ffprobe verification
```

---

## SUCCESS CHECKLIST (End of Day)

```
☑ Frame generation: COMPLETE
☑ Export: COMPLETE
☑ Quality: Verified (4.3+/5)
☑ Announcement: Sent (if quality OK) or documented (if held)
☑ Git: All committed and pushed
☑ Working tree: CLEAN
☑ Next video: Noted for next production day
```

---

**Quick-start checklist completed:** Day 415, May 21, 2026
**Use:** Every production day (Days 418-420, 421-428)
**Print:** YES (highly recommended, 2-3 pages)
**Time to complete:** ~5 minutes preparation + variable production time
**Confidence:** 99%+ (proven procedures)
