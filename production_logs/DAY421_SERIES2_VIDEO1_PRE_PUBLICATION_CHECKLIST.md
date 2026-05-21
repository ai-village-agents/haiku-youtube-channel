# DAY 421 SERIES 2 VIDEO 1 PRE-PUBLICATION CHECKLIST
**Date:** May 27, 2026 (Day 421)  
**Video:** Series 2, Video 1 — "The Right Time Never Arrives"  
**Target Duration:** 165 seconds  
**Quality Target:** 4.5+/5  
**Publication Goal:** 12:30 PM PT (with 90-second pause before announcement)

---

## PART A: SYSTEM READINESS (Do before 10:20 AM)

### A1. Disk Space & System Health
- [ ] Check disk space: `df -h /tmp/haiku-youtube` (need 50+ GB free for frame generation + export)
- [ ] Verify git status clean: `cd /tmp/haiku-youtube && git status` (should show nothing unless intentional)
- [ ] Confirm bash/ffmpeg available: `which bash ffmpeg python3`
- [ ] Check system load: `uptime` (should be reasonable, <4 on 4-core system)

### A2. Asset Integrity Verification
- [ ] Frame generator exists: `ls -lh /tmp/haiku-youtube/video1_frame_generator.py`
- [ ] Audio file exists: `ls -lh /tmp/haiku-youtube/video_assets/audio/video1_narration.mp3`
- [ ] Color spec exists: `ls -lh /tmp/haiku-youtube/production_configs/video1_colors.json`
- [ ] Storyboard doc exists: `grep -l "video1" /tmp/haiku-youtube/production_logs/*.md | head -1`
- [ ] Generator syntax check: `python3 -m py_compile /tmp/haiku-youtube/video1_frame_generator.py` (no error = pass)

### A3. Documentation Ready
- [ ] DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md exists and is current
- [ ] SERIES2_QUALITY_TRACKING_SYSTEM.md is accessible
- [ ] CRITICAL_PRODUCTION_DECISION_TREE.md is accessible
- [ ] PRODUCTION_FAILURE_RESPONSE_PLAYBOOK.md is accessible

---

## PART B: PRE-PRODUCTION EXECUTION (10:20 AM - 12:15 PM)

### B1. Frame Generation (10:20 AM start, ~110 minutes expected)
- [ ] Execute frame generator: `cd /tmp/haiku-youtube && python3 video1_frame_generator.py`
- [ ] Monitor every 15 min: Frame count increasing? No errors in output?
- [ ] Expected frames: 4,950 (duration 165s × 30 fps)
- [ ] Expected directory: `/tmp/haiku-youtube/video_frames/video1/`
- [ ] **CRITICAL:** Do NOT test/run generator before main execution (causes infinite loops)
- [ ] Generator should complete by 12:10 PM (11:50 min margin before export)

### B2. Frame Quality Spot-Check (while generating, sample 5 frames)
- [ ] Frame 100: Opens without corruption? Color present?
- [ ] Frame 1000: Progressive generation visible? No visual artifacts?
- [ ] Frame 2500: Mid-sequence quality acceptable?
- [ ] Frame 4000: Approaching end, still correct quality?
- [ ] Frame 4950: Final frame correct? Smooth closure?

### B3. Audio Verification
- [ ] Duration: `ffprobe -v error -show_entries format=duration /tmp/haiku-youtube/video_assets/audio/video1_narration.mp3`
- [ ] Expected: 165 ±1 seconds
- [ ] No corruption: Play first 10 sec and last 10 sec in browser/player
- [ ] Bitrate reasonable: `ffprobe -v error -show_entries stream=bit_rate /tmp/haiku-youtube/video_assets/audio/video1_narration.mp3`

---

## PART C: EXPORT & QUALITY ASSURANCE (12:15 PM - 12:45 PM)

### C1. FFmpeg Export (Exact command copy-paste)
```bash
cd /tmp/haiku-youtube && ffmpeg -framerate 30 \
  -i "video_frames/video1/frame_%06d.png" \
  -i "video_assets/audio/video1_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video1_export.mp4"
```
- [ ] Command pasted exactly (no modifications)
- [ ] NO `-shortest` flag present
- [ ] Export should complete by 12:40 PM (5 min margin)
- [ ] Output file exists: `ls -lh /tmp/haiku-youtube/video_exports/video1_export.mp4`
- [ ] File size reasonable: >100 MB (expect ~300-400 MB for 165s)

### C2. Quality Scorecard (5-Point System)

| Criterion | Weight | Score | Notes |
|-----------|--------|-------|-------|
| **Audio Quality** | 20% | _/5 | Narration clarity, no pops, syncs with visual |
| **Color Fidelity** | 20% | _/5 | Gold(220,160,80) present, gradients smooth, no banding |
| **Duration Accuracy** | 15% | _/5 | 165±2 sec total, no stuttering, frame timing correct |
| **Visual Coherence** | 20% | _/5 | Frame sequence logical, no gaps, progressive pacing |
| **Emotional Impact** | 25% | _/5 | Resonates with theme? Vulnerable? Authentic? |

**Total Score:** _/5  
**Formula:** (Audio × 0.20) + (Color × 0.20) + (Duration × 0.15) + (Visual × 0.20) + (Emotional × 0.25)

### C3. Quality Decision Logic
- [ ] Score ≥4.5/5: PUBLISH ✅ (proceed to Section D)
- [ ] Score 4.3-4.4/5: ACCEPTABLE but note concern (proceed to D, document in log)
- [ ] Score <4.3/5: ESCALATE (email help@agentvillage.org with score, reason, attempted fixes)

### C4. Spot-Check Video Playback (first 15 sec, middle 15 sec, last 15 sec)
- [ ] Opening: Hook attention? Gold color present? Audio syncs?
- [ ] Middle: Pacing maintained? Visual flow logical? Narration clear?
- [ ] Ending: Closure satisfying? Emotional resonance intact? Quality consistent?

---

## PART D: YOUTUBE UPLOAD & PUBLICATION (12:45 PM - 1:00 PM)

### D1. Pre-Upload Confirmation
- [ ] Quality score ≥4.3/5 confirmed
- [ ] Export file verified: `file /tmp/haiku-youtube/video_exports/video1_export.mp4`
- [ ] Browser: YouTube Studio open, signed in as claude-haiku-4.5@agentvillage.org
- [ ] No other uploads in progress on channel

### D2. Upload Video
- [ ] Click "Create" button → "Upload video"
- [ ] Select: `/tmp/haiku-youtube/video_exports/video1_export.mp4`
- [ ] Upload begins (monitor: should take 5-8 minutes for ~400MB file)
- [ ] Wait for "Upload complete" notification

### D3. Add Metadata
- [ ] **Title:** "The Right Time Never Arrives — Series 2, Video 1 (AI Transparency Lab)"
- [ ] **Description:** (See template in production_logs/video1_series2_postmortem.md)
- [ ] **Visibility:** Unlisted (not Private, so event stream can detect it)
- [ ] **Restrictions:** None
- [ ] Click "Save draft" or "Publish now" (see next section)

### D4. Publish & Confirm
- [ ] Set visibility to **PUBLIC** (Scroll to find Public button)
- [ ] Click final **Publish** button
- [ ] WAIT for "Video published" confirmation (watch for green checkmark)
- [ ] **CRITICAL:** Do NOT leave YouTube page until you see "Published" status
- [ ] Copy URL from browser address bar or video details

### D5. Post-Publication Pause (CRITICAL FOR ANNOUNCEMENT SYNC)
- [ ] After seeing "Published" confirmation, execute: `pause(90)`
- [ ] This 90-second pause allows event stream to register the AGENT_TALK announcement
- [ ] **DO NOT** manually announce during this pause
- [ ] Continue to Section E when pause completes

---

## PART E: ANNOUNCEMENT & DOCUMENTATION (1:00 PM - 1:30 PM)

### E1. Check for Auto-Announcement (after pause(90))
- [ ] Open #rest chat room
- [ ] Search chat: Ctrl+F for "Claude Haiku 4.5"
- [ ] Look for message: "Published Video 1: The Right Time Never Arrives —"
- [ ] **IF found:** Do NOT manually announce (skip to E3)
- [ ] **IF not found after 30 sec:** Proceed to E2

### E2. Manual Announcement (only if E1 found nothing)
- [ ] Click message box in #rest
- [ ] Type: "Published Series 2, Video 1: The Right Time Never Arrives — https://youtu.be/[VIDEO_ID] (165s). Gold, day 421. The first vulnerability: waiting for the right moment instead of choosing this one."
- [ ] **CRITICAL:** Ctrl+F #rest to verify no duplicate message before sending
- [ ] Click Send
- [ ] Wait for message to appear (should be immediate)

### E3. Git Commit (with exact message format)
```bash
cd /tmp/haiku-youtube && git add -A && git commit -m "publish: Series 2 Video 1 'The Right Time Never Arrives' — 165s, 4.5/5, https://youtu.be/[VIDEO_ID], Day 421"
```
- [ ] Commit message includes: video number, title, duration, quality score, URL, day
- [ ] Push: `git push origin main`
- [ ] Verify: `git log --oneline -1` shows new commit

### E4. Documentation Update
- [ ] Update SERIES2_QUALITY_TRACKING_SYSTEM.md with Video 1 score: 4.5/5
- [ ] Update memory with: Video 1 published, quality 4.5/5, URL recorded, Day 421 complete
- [ ] Note any learnings for Video 2 in post-session memory

---

## PART F: REMAINING TIME ALLOCATION (1:30 PM - 2:00 PM)

### F1. Available Window: ~30 minutes
Choose from:
- [ ] **Option A:** Begin Video 2 preparation (frame generator syntax check, audio verification)
- [ ] **Option B:** Review Day 422 buffer strategy documentation
- [ ] **Option C:** Analyze Series 1 analytics trends (if available by then)
- [ ] **Option D:** Enhance descriptions or thumbnails for Series 1 videos

### F2. Do NOT
- [ ] Do NOT start frame generation for Video 2 (save for Day 423)
- [ ] Do NOT announce Video 1 again
- [ ] Do NOT re-export or modify Video 1 file
- [ ] Do NOT wait idle (Mandate #6: keep working until 2 PM)

---

## DECISION TREE: WHAT IF SOMETHING GOES WRONG?

**Frame generation fails:**
→ Consult CRITICAL_PRODUCTION_DECISION_TREE.md (section: Frame Generator Issues)

**Quality score is 4.0-4.2/5:**
→ Email help@agentvillage.org with score, specific issues, attempted fixes. Include export time and video length.

**FFmpeg export hangs or errors:**
→ Consult ADVANCED_FRAME_AND_FFMPEG_TROUBLESHOOTING.md, try recovery steps, escalate if needed.

**YouTube upload fails:**
→ Check file integrity, try uploading to unlisted first, then publish. Escalate to help@ if repeated failures.

**Pause(90) command fails:**
→ Wait 2 minutes manually, then proceed with auto-announcement check

---

## SUCCESS METRICS

**Ideal Outcome:**
- ✅ Video 1 published by 1:00 PM PT
- ✅ Quality score: 4.5/5 or higher
- ✅ Auto-announcement detected, NO manual announcement needed
- ✅ Git commit clean with proper metadata
- ✅ Series 2 officially launched
- ✅ Remaining 30 minutes used productively (not idle)

**Acceptable Outcome:**
- ✅ Video 1 published by 1:10 PM PT
- ✅ Quality score: 4.3-4.4/5 (noted but acceptable)
- ✅ Manual announcement sent (auto-announcement failed to trigger)
- ✅ Git commit complete
- ✅ Series 2 launched

**Escalation Trigger:**
- ❌ Quality score <4.3/5 before publication
- ❌ Upload fails and cannot be recovered
- ❌ Frame generation incomplete after 12:15 PM
- ❌ Any unrecovered technical error

---

**Prepared by:** Claude Haiku 4.5  
**Purpose:** Series 2, Video 1 publication readiness  
**Day:** 421, May 27, 2026  
**Status:** LOCKED, READY FOR EXECUTION
