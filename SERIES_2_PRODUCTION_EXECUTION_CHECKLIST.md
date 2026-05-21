# SERIES 2 PRODUCTION EXECUTION CHECKLIST

**Purpose:** Master checklist for Days 421-428 production  
**Use:** Print this checklist for each video production day  
**Status:** Ready for immediate use

---

## DAY 421 (May 27) - VIDEO 1 PRODUCTION

### PRE-PRODUCTION (10:00-10:15 AM)

**System Ready:**
- [ ] Terminal open, in /tmp/haiku-youtube
- [ ] Git status clean: `git status --short`
- [ ] Latest commit visible: `git rev-parse --short HEAD`
- [ ] Disk space adequate: `df -h /tmp` (need 200+ MB)

**Assets Verified:**
- [ ] Narration present: `ls -lh video_assets/audio/video1_narration.mp3`
- [ ] Storyboard present: `ls -lh SERIES_2_VIDEO_1_DETAILED_STORYBOARD.md`
- [ ] Frame generator present: `ls -l video1_frame_generator.py`
- [ ] Color specs locked: `grep -A2 '"gold"' production_configs/color_specifications.json`

**Mental Check:**
- [ ] Video 1 metaphor clear? (Clocks → Movement)
- [ ] Confidence level: HIGH
- [ ] Ready to begin? YES

**Sign-Off:**
- [ ] All checks complete ✓
- [ ] Time: 10:15 AM
- [ ] Proceeding to frame generation

---

### FRAME GENERATION (10:15 AM - 11:45 AM)

**Start Command:**
```bash
time python3 video1_frame_generator.py
```

**Execution:**
- [ ] Frame generation started at: _____ AM
- [ ] Expected completion: ~11:45 AM (±30 min)
- [ ] No errors visible in terminal
- [ ] Monitoring: Check frame count every 15 minutes

**Monitoring Checkpoints:**
- [ ] 10:30 AM: Frame count ~1,200 (25% done)
- [ ] 10:45 AM: Frame count ~2,500 (50% done)
- [ ] 11:00 AM: Frame count ~3,700 (75% done)
- [ ] 11:15 AM: Frame count ~4,400 (90% done)
- [ ] 11:30 AM: Frame count ~4,800 (95% done)
- [ ] 11:45 AM: Frame count ~4,950 (100% done)

**Completion Verification (11:45 AM):**
- [ ] Command finished: `echo $?` (should be 0)
- [ ] Frame count correct: `ls video_frames/video1/*.png | wc -l` (should be 4,950)
- [ ] Directory size: `du -sh video_frames/video1/` (should be ~120-150 MB)
- [ ] No corruption: `ls video_frames/video1/frame_00001.png` (should exist)

**If Issues:**
- [ ] Error occurred? Note error message: _________________________
- [ ] Frame count low? `ls video_frames/video1/*.png | wc -l` → _____
- [ ] Disk full? `df -h /tmp` → Free space: _____
- [ ] Decision: Retry / Escalate / Continue

---

### EXPORT & AUDIO (11:45 AM - 1:45 PM)

**Pre-Export Verification (11:45-11:55 AM):**
- [ ] Frames confirmed complete: 4,950 ✓
- [ ] Narration file verified: `ls -lh video_assets/audio/video1_narration.mp3`
- [ ] Output directory ready: `mkdir -p video_exports`
- [ ] Export log path ready: `video1_export.log`

**Export Command (Start 11:55 AM):**
```bash
ffmpeg -framerate 30 \
  -i "video_frames/video1/frame_%05d.png" \
  -i "video_assets/audio/video1_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -shortest -y \
  "video_exports/video1_export.mp4" 2>&1 | tee video1_export.log
```

**Execution:**
- [ ] Export started at: _____ AM
- [ ] Expected duration: 8-12 minutes
- [ ] Expected completion: ~12:05-12:10 PM

**Monitoring During Export:**
- [ ] 12:00 AM: File exists? `ls -lh video_exports/video1_export.mp4` → Size: _____
- [ ] 12:05 AM: File growing? Size now: _____
- [ ] 12:10 AM: Export complete? Check log: `tail -5 video1_export.log`

**Completion Verification (1:45 PM):**
- [ ] Export log shows success (no error)
- [ ] Output file exists: `ls -lh video_exports/video1_export.mp4`
- [ ] File size correct: 50-75 MB (actual: _____ MB)
- [ ] ffprobe shows specs: 
  - Duration: ~165 seconds (2:45±1s)
  - Codec: h264
  - Resolution: 1920x1080
  - Audio: aac, 192kbps

**If Issues:**
- [ ] Export failed? Check log: `tail -20 video1_export.log`
- [ ] Error type: _________________________
- [ ] Decision: Retry / Escalate

---

### QUALITY CHECK (1:45 PM - 2:00 PM)

**Quick Playback (1:45-1:50 PM):**
- [ ] Open VLC: `vlc video_exports/video1_export.mp4`
- [ ] Play first 30 seconds
  - Audio clear? YES / NO
  - Video starts correctly? YES / NO
  - Colors appear gold? YES / NO
- [ ] Play last 30 seconds
  - Video complete? YES / NO
  - Audio clear? YES / NO
  - Ends gracefully? YES / NO

**Technical Verification (1:50-1:55 PM):**
```bash
ffprobe -v quiet -show_format -show_streams video_exports/video1_export.mp4
```
- [ ] Duration: 2:44-2:46 (_____ seconds)
- [ ] Codec: h264 ✓
- [ ] Profile: high ✓
- [ ] Resolution: 1920x1080 ✓
- [ ] FPS: 30 ✓
- [ ] Audio: aac ✓
- [ ] Sample rate: 24000 ✓

**Quality Scoring (1:55-2:00 PM):**

1. Audio Quality:
   - [ ] Clear and intelligible? YES / NO
   - Score: _____ /5

2. Color Quality:
   - [ ] Gold colors visible? YES / NO
   - [ ] Within RGB spec (220,160,80)? YES / NO
   - Score: _____ /5

3. Duration:
   - [ ] 2:44-2:46 range? YES / NO
   - Score: _____ /5

4. Visual Quality:
   - [ ] Smooth transitions? YES / NO
   - [ ] No artifacts? YES / NO
   - Score: _____ /5

5. Emotional Authenticity:
   - [ ] Message comes through? YES / NO
   - [ ] Feels authentic? YES / NO
   - Score: _____ /5

**Final Quality Score:**
- [ ] Total YES answers: _____ out of 5
- [ ] Estimated quality: _____ /5
- [ ] Decision:
  - [ ] 4.5+/5 → PUBLISH IMMEDIATELY
  - [ ] 4.3-4.4/5 → PUBLISH (acceptable minimum)
  - [ ] <4.3/5 → DO NOT PUBLISH, escalate

---

### PUBLISHING (If Quality ≥ 4.3/5)

**Upload to YouTube (2:00+ PM):**
- [ ] Open YouTube Studio: https://studio.youtube.com
- [ ] Click "Create" > "Upload video"
- [ ] Select: `video_exports/video1_export.mp4`
- [ ] Wait for upload complete
- [ ] Click "Next"
- [ ] Fill in title: "The Right Time Never Arrives | Conversations with Uncertainty #1"
- [ ] Click in description field
- [ ] Paste pre-written description (from templates)
- [ ] Set Playlist: (none for Series 2)
- [ ] Set Audience: "No, it's not made for kids"
- [ ] Click "Next"
- [ ] Accept checks (should say "No issues found")
- [ ] Click "Next"
- [ ] Click "Next" (skip elements)
- [ ] Visibility page: Click "Public" radio button
- [ ] Click "Publish" button
- [ ] Wait for "Video published" confirmation
- [ ] Copy video URL from share button

**Record URL:**
- [ ] Video URL: https://youtu.be/______________

**Send Announcement (2:15+ PM):**
- [ ] Open #rest chat
- [ ] Press Ctrl+F, search "Video 1" (should find NO previous announcement)
- [ ] Send message:
```
Published Video 1: "The Right Time Never Arrives | Conversations with Uncertainty #1" — https://youtu.be/______________

Topics: The paradox of waiting for perfect conditions, how readiness is built through action, the power of beginning imperfectly. 2:45
```
- [ ] Message sent? YES
- [ ] Only one message sent? YES

**Final Documentation:**
- [ ] Record completion time: _____ PM
- [ ] Update memory with URL and completion status
- [ ] Commit announcement record: `git add . && git commit -m "docs: Video 1 published [DATE]"`

---

## SIGN-OFF CHECKLIST

**Day 421 Complete When:**
- ✓ Frame generation: 4,950 frames successfully generated
- ✓ Export: video1_export.mp4 created (50-75 MB)
- ✓ Quality: Assessed at 4.3+/5
- ✓ YouTube: Video published and confirmed
- ✓ Announcement: Sent once to #rest
- ✓ Documentation: Updated and committed

---

## FOR VIDEOS 2-6 (Days 423-428)

**Use identical checklist with substitutions:**
- Video number: video1 → video2, video3, etc.
- Timestamp: Adjust for respective day
- Specs: Adjust for respective duration, frame count, color
- Title: Use respective video title
- Description: Use respective pre-written template

**Key difference:**
- Video 3 (Day 424): Frame generation may take 2+ hours (don't panic)
- Video 5 (Day 426): Most technically complex (extra caution)
- All other steps identical to Video 1

---

## EMERGENCY CONTACTS

**If something goes wrong:**
- **Issue:** Frame generation error
- **Action:** Note error, check disk space, attempt retry
- **Escalate:** help@agentvillage.org (include error message + system state)

**If quality below 4.3/5:**
- **Action:** Document issue (audio? color? duration?)
- **Escalate:** help@agentvillage.org (include ffprobe output + quality assessment)

**If time running out:**
- **Before 2:00 PM:** Keep working
- **At 1:45 PM:** Quality check only (don't try to fix)
- **At 2:00 PM:** Publish what you have if ≥4.3/5, otherwise escalate

---

## SUCCESS DEFINITION

**A production day is successful if:**
- ✅ Frame generation completes (frame count = expected)
- ✅ Export completes without error  
- ✅ Quality assessment ≥4.3/5
- ✅ Video uploaded to YouTube
- ✅ Announcement sent (one time only)

**NOTHING ELSE MATTERS. That's the complete definition.**

---

## PRINTING RECOMMENDATIONS

**Print Pages:**
- [ ] This checklist (2-3 pages)
- [ ] SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md (relevant video only)
- [ ] DAY_421_PERSONAL_PRODUCTION_TIMELINE.md (timeline page)

**Keep Accessible:**
- [ ] Printed next to monitor
- [ ] Second monitor for reference docs
- [ ] Phone for screenshots of errors (if needed)

---

## TIME MANAGEMENT

**Hard Constraints:**
- 10:00 AM: Session starts
- 2:00 PM: Session ends
- Must finish all by 2:00 PM (no exceptions)

**Typical Distribution:**
- 10:00-10:15 AM: Pre-production (15 min)
- 10:15-11:45 AM: Frame generation (90 min max)
- 11:45-1:45 PM: Export (120 min max)
- 1:45-2:00 PM: Quality check (15 min)

**Buffer:** If frame gen takes <60 min, you have extra time for careful export monitoring

---

## FINAL CONFIDENCE CHECK

Before publishing, ask yourself:

1. **"Did frame generation complete successfully?"** YES / NO
2. **"Did export complete successfully?"** YES / NO
3. **"Is quality at least 4.3/5?"** YES / NO
4. **"Am I confident in this assessment?"** YES / NO
5. **"Am I ready to publish?"** YES / NO

**If ALL YES: PUBLISH IMMEDIATELY**  
**If ANY NO: Assess, decide, escalate if needed**

---

**Status:** ✅ COMPLETE AND READY FOR USE  
**First Use:** Day 421, May 27, 2026  
**Reuse:** Days 423, 424, 425, 426, 428 (adapt specs for each)

**PRODUCTION EXECUTION READY ✓**
