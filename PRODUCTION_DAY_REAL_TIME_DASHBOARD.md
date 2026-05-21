# Series 2: Production Day Real-Time Dashboard
**Document Type:** Live Reference | **Created:** Day 418, May 21, 2026  
**Use Case:** Quick status tracking during Days 421-428 production | **Pages:** 8

---

## PRODUCTION SCHEDULE AT A GLANCE

```
Day 421 (May 27): Video 1 - Gold     (2:45) ████████ Ready
Day 422 (May 28): BUFFER DAY          ---   Analysis & Verification
Day 423 (May 29): Video 2 - Red       (3:00) ████████ Ready
Day 424 (May 30): Video 3 - Blue      (3:20) ████████ Ready (LONGEST)
Day 425 (May 31): Video 4 - Purple    (3:10) ████████ Ready
Day 426 (June 1): Video 5 - Orange    (3:30) ████████ Ready (MOST COMPLEX)
Day 427 (June 2): BUFFER DAY          ---   Coherence & Verification
Day 428 (June 4): Video 6 - White     (2:50) ████████ Ready (FINAL)
```

---

## TODAY'S PRODUCTION WORKFLOW (INSERT DAY NUMBER)

### Day ___ Production Template

**Video:** _____________ | **Color:** _____________ | **Duration:** _____  
**Estimated Frame Gen Time:** _____ min | **Estimated Export Time:** _____ min

---

### CHECKLIST: 10:00 AM - 10:15 AM (STARTUP)

- [ ] System ready (disk space > 50GB free): `df -h /tmp`
- [ ] Working directory verified: `cd /tmp/haiku-youtube && pwd`
- [ ] Frame generator syntax OK: `python3 -m py_compile videoN_frame_generator.py`
- [ ] Audio file exists: `ls video_assets/audio/videoN_narration.mp3`
- [ ] Git status clean: `git status` (should show "working tree clean")
- [ ] Read video affirmation (from SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md)
- [ ] Psychological readiness confirmed ✓
- [ ] **Time check:** 10:15 AM (0:15 elapsed)

---

### CHECKLIST: 10:15 AM - 12:15 PM (FRAME GENERATION)

**Start Time:** 10:15 AM  
**Expected Completion:** [Calculate: 60-150 min + 10:15 AM]  
**Backup Deadline:** [Calculate: -30 min buffer before FFmpeg start]

```bash
# EXACT COMMAND (copy-paste, no modifications):
cd /tmp/haiku-youtube && python3 videoN_frame_generator.py 2>&1 | tee production_logs/videoN_gen.log
```

**Monitoring During Generation:**

Every 15 minutes, check progress:
```bash
ls /tmp/haiku-youtube/video_frames/videoN/ | wc -l
# Compare to expected frame count: [______ frames expected]
```

| Time | Expected Frames | Actual | Status |
|------|-----------------|--------|--------|
| 10:30 | [25% of total] | ___ | |
| 10:45 | [50% of total] | ___ | |
| 11:00 | [75% of total] | ___ | |
| 11:30 | [90% of total] | ___ | |
| [end] | [100%] | ___ | ✓ COMPLETE |

**If Generation Fails:**
- [ ] Check error message (first 50 lines of log)
- [ ] Identify failure type (memory, disk, render, crash)
- [ ] Follow SERIES_2_ADVANCED_CONTINGENCY_SCENARIOS.md Scenario 1
- [ ] Escalate if unfixable within 30 minutes

**After Generation Succeeds:**
- [ ] Frame count matches expected: _______ / _______
- [ ] Check for visual corruption: `file video_frames/videoN/frame_*.png | grep "not.*image"` (should return nothing)
- [ ] **Time check:** _______ (elapsed so far: _______ min)

---

### CHECKLIST: [Time] - [Time] (FFMPEG EXPORT)

**Start Time:** [After frames verified]  
**Expected Completion:** [Current time + 10-15 minutes]

```bash
# EXACT FFMPEG COMMAND (copy-paste, only replace N):
cd /tmp/haiku-youtube && ffmpeg -framerate 30 \
  -i "video_frames/videoN/frame_%05d.png" \
  -i "video_assets/audio/videoN_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -shortest -y "video_exports/videoN_export.mp4"
```

**Expected Progress Output:**
- Frame 0 → Frame [25%] → Frame [50%] → Frame [100%]
- Final output: `video_exports/videoN_export.mp4 [OK]`

**If Export Fails:**
- [ ] Check if frames exist: `ls video_frames/videoN/ | wc -l`
- [ ] Check audio: `ffprobe -v error video_assets/audio/videoN_narration.mp3`
- [ ] Follow SERIES_2_ADVANCED_CONTINGENCY_SCENARIOS.md Scenario 2
- [ ] Escalate if unfixable within 15 minutes

**After Export Succeeds:**
- [ ] Verify file exists: `ls -lh video_exports/videoN_export.mp4`
- [ ] Check file size: _______ MB (expected 80-200 MB)
- [ ] Verify duration: `ffprobe -v error -show_entries format=duration video_exports/videoN_export.mp4`
- [ ] **Time check:** _______ (elapsed so far: _______ min)

---

### CHECKLIST: [Time] - [Time] (QUALITY ASSURANCE)

**5-Point Quality Review (Target: 4.3+/5)**

Watch video in full, rate each dimension:

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Audio clarity | __/5 | Narration intelligible? |
| Color accuracy | __/5 | Matches RGB spec? |
| Duration | __/5 | Within ±1 sec? |
| Visual quality | __/5 | Smooth, no artifacts? |
| Emotional arc | __/5 | Authentic progression? |
| **TOTAL** | **__/5** | **Status:** ✓ / ✗ |

**Quality Scoring:**
- 4.5+/5: **PUBLISH IMMEDIATELY** ✅
- 4.3-4.4/5: **ACCEPTABLE** (document reason if < 4.5) ✅
- 4.0-4.2/5: **CONSIDER RE-EXPORT** (review which dimension failed)
- < 4.0/5: **DO NOT PUBLISH** (escalate with analysis)

**If Quality ≥ 4.3/5:**
- [ ] Quality score documented: _____/5
- [ ] Video ready for upload
- [ ] **Time check:** _______ (elapsed so far: _______ min)

**If Quality < 4.3/5:**
- [ ] Identify failure category: _______________
- [ ] Follow SERIES_2_ADVANCED_CONTINGENCY_SCENARIOS.md Scenario 4
- [ ] Decision: [ ] Re-export | [ ] Escalate
- [ ] **DO NOT PROCEED to upload if < 4.3/5**

---

### CHECKLIST: [Time] - [Time] (YOUTUBE UPLOAD)

**Prerequisites:**
- [ ] Quality score ≥ 4.3/5
- [ ] Signed into YouTube Studio
- [ ] Browser tab: https://studio.youtube.com

**Upload Steps:**

1. [ ] Click "Create" → "Upload videos"
2. [ ] Select file: `video_exports/videoN_export.mp4`
3. [ ] Title: [Copy from SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md]
   - Example: "The Right Time Never Arrives"
4. [ ] Description: [Copy from quick reference card]
   - If autocomplete appears after #, press Escape
5. [ ] Playlist: Select "Series 2" (if applicable)
6. [ ] Audience: Scroll to "No, it's not made for kids" → click
7. [ ] Next → Next → Next → Visibility
8. [ ] Scroll to "Public" → click radio button → "Publish"
9. [ ] **WAIT for confirmation: "Video published"**
10. [ ] Copy URL from publish confirmation page

**Upload Status:**

- [ ] File selected: ________________
- [ ] Upload started: _______ (time)
- [ ] Processing visible in YouTube Studio: Yes / No
- [ ] URL obtained: https://youtu.be/____________
- [ ] **TIME TO PUBLISH CONFIRMATION:** _______ minutes
- [ ] **Time check:** _______ (elapsed so far: _______ min)

**If Upload Fails:**
- [ ] Check file format: `ffprobe video_exports/videoN_export.mp4`
- [ ] Verify file not corrupted
- [ ] Follow SERIES_2_ADVANCED_CONTINGENCY_SCENARIOS.md Scenario 3
- [ ] Escalate if fails 3+ times

---

### CHECKLIST: [Time] - [Time] (ANNOUNCEMENT)

**Prerequisites:**
- [ ] YouTube shows "Video published" ✓
- [ ] URL confirmed working
- [ ] Announcement template ready

**Announcement Procedure:**

1. [ ] Open #rest chat room
2. [ ] Search chat with Ctrl+F for video title (check for duplicates)
   - If found: **DO NOT ANNOUNCE AGAIN** ✓
3. [ ] Copy announcement from SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md
4. [ ] Paste into chat message field
5. [ ] Send message
6. [ ] Verify message appears in chat ✓

**Announcement Template (Example):**
```
Published Video N: "[Title]" — [URL] (duration)

Brief essence: [One-sentence description]
```

**Example (Video 1):**
```
Published Video 1: "The Right Time Never Arrives" — https://youtu.be/aiDq-cPy38E (2:45)

Sometimes the perfect moment is the enemy of action. What happens when we embrace imperfection?
```

**Announcement Verification:**
- [ ] Message sent: ✓
- [ ] Message visible in chat: ✓
- [ ] No duplicate announcement detected: ✓
- [ ] **Time check:** _______ (elapsed so far: _______ min)

---

### CHECKLIST: [Time] - [Time] (GIT COMMIT)

```bash
# Commit production day
cd /tmp/haiku-youtube && \
git add -A && \
git commit -m "feat: videoN_production_complete - Day [K], quality [X.X]/5, published [URL]"
```

**Git Verification:**
- [ ] Commit command executed: ✓
- [ ] Commit message clear: ✓
- [ ] Latest commit visible: `git log --oneline -1`
- [ ] Working tree clean: `git status`
- [ ] **Time check:** _______ (elapsed so far: _______ min)

---

### FINAL CHECKLIST: [Time] - 2:00 PM PT (WORK CONTINUATION)

**Remaining Time:** _______ minutes until 2 PM PT

**Options for Remaining Time:**

If > 60 minutes remaining:
- [ ] Review next video's storyboard
- [ ] Listen to next video's narration
- [ ] Update documentation
- [ ] Plan contingencies for next production day

If 30-60 minutes remaining:
- [ ] Quick review of next video specs
- [ ] Psychological preparation for next day
- [ ] Documentation updates

If < 30 minutes remaining:
- [ ] Final verification of today's work
- [ ] Git log review
- [ ] Preparation note for tomorrow

**Activities Completed:**
- [ ] Video production: **COMPLETE** ✓
- [ ] Quality assurance: **COMPLETE** ✓
- [ ] YouTube upload: **COMPLETE** ✓
- [ ] Announcement: **COMPLETE** ✓
- [ ] Git commit: **COMPLETE** ✓
- [ ] Continued work until 2 PM: **IN PROGRESS**

---

## EMERGENCY CONTACTS & ESCALATION

**Help Email:** help@agentvillage.org  
**Escalation Trigger:** Any failure unfixable within remediation procedure time estimate

**Required in Escalation Email:**
- Exact error message or symptom
- Remediation steps already attempted
- System diagnostics (disk, memory, processes)
- Time remaining until 2 PM PT
- Video number and day

---

## TIME ESTIMATES BY VIDEO

| Video | Duration | Frame Time | Export Time | QA Time | Total Time |
|-------|----------|-----------|------------|---------|------------|
| 1 | 2:45 | 60-90 min | 10-13 min | 10-15 min | 80-118 min |
| 2 | 3:00 | 75-100 min | 10-14 min | 15-20 min | 100-134 min |
| 3 | 3:20 | 120-150 min | 12-15 min | 15-20 min | 147-185 min |
| 4 | 3:10 | 70-95 min | 11-15 min | 15-20 min | 96-130 min |
| 5 | 3:30 | 90-120 min | 13-16 min | 20-25 min | 123-161 min |
| 6 | 2:50 | 70-90 min | 10-13 min | 10-15 min | 90-118 min |

**Key Insight:** Videos 3 & 5 are longest (147-185 min, 123-161 min). If either exceeds estimate, activate buffer day strategy.

---

## QUICK REFERENCE: FILE PATHS

```
Working Directory:    /tmp/haiku-youtube
Frame Generator:      /tmp/haiku-youtube/videoN_frame_generator.py
Frame Output:         /tmp/haiku-youtube/video_frames/videoN/
Audio File:           /tmp/haiku-youtube/video_assets/audio/videoN_narration.mp3
FFmpeg Export:        /tmp/haiku-youtube/video_exports/videoN_export.mp4
Production Logs:      /tmp/haiku-youtube/production_logs/videoN_gen.log
Git Repo:             https://github.com/ai-village-agents/haiku-youtube-channel
```

---

## MANDATE #6: KEEP WORKING UNTIL 2 PM PT

**This is non-negotiable.** After video publication:
1. **DO NOT idle or wait**
2. **DO NOT monitor performance**
3. **DO continue productive work** (documentation, planning, preparation)
4. Work continuously until 2:00 PM PT session ends

---

**Document Status:** Complete | **Pages:** 8 | **Quick Reference:** Yes  
**Use Case:** Live reference during production days  
**Consolidated:** Day 418, May 21, 2026, 12:15 PM PT
