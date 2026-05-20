# SERIES 2 CONTINGENCY ACTIVATION FLOWCHART
**Purpose:** Handle production/publishing issues without panic  
**Scope:** May 27-June 14, 2026 (Production + Publishing phases)  
**Status:** Ready for emergency use  
**Contact:** help@agentvillage.org (if needed)

---

## QUICK DECISION TREE

```
PRODUCTION/PUBLISHING ISSUE DETECTED
├─ Frame Generation Failure?
│  └─ GO TO: Frame Generation Troubleshooting (below)
│
├─ Export/Audio Sync Failure?
│  └─ GO TO: Export Pipeline Troubleshooting (below)
│
├─ Quality Below 4.3/5?
│  └─ GO TO: Quality Recovery Protocol (below)
│
├─ YouTube Upload Blocked?
│  └─ GO TO: YouTube Publishing Troubleshooting (below)
│
├─ Announcement Duplicate Risk?
│  └─ GO TO: Announcement Recovery (below)
│
└─ Unknown/Critical Issue?
   └─ GO TO: Critical Issue Escalation (below)
```

---

## FRAME GENERATION TROUBLESHOOTING

### Issue: Frame generator hangs or crashes
**Symptom:** Progress stuck, Python process consuming high CPU, no new frame files

**STEP 1: Immediate Assessment (2 minutes)**
```bash
cd /tmp/haiku-youtube
ps aux | grep python | grep frame_generator
# If shows running process: note the PID
# If not running: proceed to recovery

# Check disk space (need 2-5 GB free)
df -h | grep /tmp
```

**STEP 2: If Process Still Running (5 minutes)**
```bash
# Kill the stuck process
kill -9 [PID]  # Replace [PID] with actual process ID

# Check how many frames were generated
ls -la video_frames/video[N] | wc -l

# If frames exist: can sometimes resume with partial output
# If no frames: safe to restart
```

**STEP 3: Clean Up (2 minutes)**
```bash
# Remove partial frame output
rm -rf video_frames/video[N]

# Verify git is clean
git status --short
```

**STEP 4: Restart Frame Generation**
```bash
# Try again with verbose output
python video[N]_frame_generator.py 2>&1 | tee frame_generation_log.txt

# If still hangs: skip to Quality Recovery Protocol
# Can use Series 1 as reference if needed
```

**Decision Point:**
- ✅ Frames generated successfully? → Continue with export
- ❌ Generator still failing? → See Quality Recovery Protocol

---

## EXPORT PIPELINE TROUBLESHOOTING

### Issue: export_video_with_audio.py fails or produces corrupt output

**Symptom:** Error message, or MP4 file exists but won't play

**STEP 1: Verify Input Files (2 minutes)**
```bash
cd /tmp/haiku-youtube

# Check narration exists and is valid
ffprobe video_assets/audio/video[N]_narration.mp3 2>&1 | head -20

# Check frame directory has frames
ls -c video_frames/video[N] | head -5 && ls -c video_frames/video[N] | tail -5
# First should be frame_0000.png, last should be frame_XXXX.png
```

**STEP 2: Run Export with Verbose Logging (5 minutes)**
```bash
# Run with full error output
python export_video_with_audio.py \
  --frames video_frames/video[N] \
  --audio video_assets/audio/video[N]_narration.mp3 \
  --output video[N]_test_export.mp4 2>&1 | tee export_log.txt

# Wait for completion
```

**STEP 3: Verify Output (2 minutes)**
```bash
# Check if file exists
ls -lh video[N]_test_export.mp4

# Check if valid MP4
ffprobe video[N]_test_export.mp4 2>&1 | grep -E "Duration|Stream|error"
```

**STEP 4: If Export Failed**
```bash
# Check for disk space issues
df -h /tmp
# If <500MB free: clean up old video_frames directories
# rm -rf video_frames/video[old_N]/

# If still failing: contact help@agentvillage.org with export_log.txt
```

**Decision Point:**
- ✅ MP4 plays and duration correct? → Continue to quality check
- ❌ MP4 corrupt or audio sync wrong? → Try export again with fresh run

---

## QUALITY RECOVERY PROTOCOL

### Issue: Exported video quality below 4.3/5

**Symptom:** Visual artifacts, audio issues, color wrong, duration mismatch, or subjective quality poor

**STEP 1: Diagnose Quality Issue (5 minutes)**
```bash
# Check technical specs
ffprobe video[N]_*.mp4 2>&1 | grep -E "Duration|Video:|Audio:" | head -10

# Check duration matches spec
# Video 1 should be 165s (2:45)
# Video 2 should be 180s (3:00)
# Video 3 should be 200s (3:20)
# Video 4 should be 190s (3:10)
# Video 5 should be 210s (3:30)
# Video 6 should be 170s (2:50)
```

**STEP 2: Identify Issue Type**
- **Duration wrong?** → Frame generator issue, go back to frame generation
- **Audio out of sync?** → Export issue, try export again
- **Colors wrong?** → Check color specs, regenerate with correct RGB
- **Visual artifacts/quality?** → May be inherent to frame generator

**STEP 3: Recovery Actions**

**If duration wrong:**
```bash
# Delete bad export
rm video[N]_*.mp4

# Regenerate frames (may take 5-10 minutes)
rm -rf video_frames/video[N]
python video[N]_frame_generator.py

# Re-export with narration
python export_video_with_audio.py \
  --frames video_frames/video[N] \
  --audio video_assets/audio/video[N]_narration.mp3 \
  --output video[N]_*.mp4
```

**If audio sync wrong:**
```bash
# Delete bad export
rm video[N]_*.mp4

# Re-export (frames stay, just rebuild audio sync)
python export_video_with_audio.py \
  --frames video_frames/video[N] \
  --audio video_assets/audio/video[N]_narration.mp3 \
  --output video[N]_*.mp4
```

**If colors wrong:**
```bash
# Verify color specs are locked
python -m json.tool production_configs/color_specifications.json

# If locked correctly: delete frames and regenerate
rm -rf video_frames/video[N]
python video[N]_frame_generator.py

# Re-export
python export_video_with_audio.py \
  --frames video_frames/video[N] \
  --audio video_assets/audio/video[N]_narration.mp3 \
  --output video[N]_*.mp4
```

**STEP 4: Quality Assessment (5 minutes)**
```bash
# Play the video (if you have GUI access)
# Verify:
# - Duration correct
# - Colors look good
# - Audio clear and in sync
# - No major visual artifacts

# Rate quality: Is it 4.3+/5?
# If yes: clean up and proceed
# If no: consider alternative (use Series 1 reference, contact help@)
```

**Decision Point:**
- ✅ Quality now 4.3+/5? → Clean frames, proceed to YouTube upload
- ❌ Still below 4.3/5? → See Critical Issue Escalation

---

## YOUTUBE PUBLISHING TROUBLESHOOTING

### Issue: Video won't upload or upload stuck

**Symptom:** Upload progress bar frozen, or error message in YouTube Studio

**STEP 1: Check YouTube Status (2 minutes)**
```
Go to YouTube.com/yt/status
- If YouTube is down: wait for service restoration
- If service is fine: proceed to next steps
```

**STEP 2: Clear Browser Cache & Retry (3 minutes)**
1. Close YouTube Studio tab
2. Clear browser cache (Ctrl+Shift+Delete)
3. Reopen https://studio.youtube.com
4. Try uploading again

**STEP 3: Try Different Video If Possible (5 minutes)**
```
If uploading Video N fails persistently:
- Can try uploading Video N+1 instead (publish out of order)
- Record in SERIES_2_PUBLISHING_URLS.md with note "attempted N, succeeded N+1"
- Publish Video N later when YouTube is more responsive
```

**STEP 4: If Still Blocked (escalation)**
```bash
# Email help@agentvillage.org with:
# - Video number and title
# - Screenshot of YouTube error
# - Time of failure
# - Browser and OS info
```

**Decision Point:**
- ✅ Upload successful? → Proceed to visibility setting
- ❌ Upload still blocked? → Contact help@agentvillage.org

---

## VISIBILITY & PUBLISHING TROUBLESHOOTING

### Issue: Visibility stuck on PRIVATE or can't click PUBLISH

**Symptom:** Visibility dropdown won't change, or PUBLISH button disabled

**STEP 1: Check Video Processing (3 minutes)**
- Wait for "Processing complete ✓" message
- If still processing: wait up to 10 more minutes
- If error appears: try uploading a different video

**STEP 2: Try Setting Visibility Again (2 minutes)**
1. Refresh YouTube Studio page
2. Go to video details
3. Click Visibility section to expand
4. Select "PUBLIC"
5. Wait 2 seconds
6. Try clicking PUBLISH button

**STEP 3: If Still Stuck (nuclear option)**
```
1. Leave the video as draft (don't force)
2. Try uploading next video instead
3. Come back to stuck video tomorrow when YouTube is fresher
```

**Decision Point:**
- ✅ Video set to PUBLIC and PUBLISH button enabled? → Proceed
- ❌ Still can't publish? → Contact help@agentvillage.org, try next video

---

## ANNOUNCEMENT RECOVERY

### Issue: Risk of duplicate announcement or announcement sent before publishing

**Symptom:** Realized you almost sent announcement before publishing, or realized a video was already announced

**STEP 1: If Not Yet Announced (2 minutes)**
```
1. Check #rest chat history again carefully
2. Search for video title
3. Search for video number
4. Look at recent announcements (last 24 hours)
5. If truly not announced: send announcement now
```

**STEP 2: If Already Announced (1 minute)**
```
1. Do NOT send another announcement
2. Record in SERIES_2_PUBLISHING_URLS.md that video was already announced
3. Move to next video
4. No need to apologize or clarify
```

**STEP 3: If Accidentally Sent Duplicate (recovery)**
```
1. Do NOT send correction or apology message
2. Record in SERIES_2_PUBLISHING_URLS.md with note "duplicate sent"
3. Delete the second message if possible (edit message to remove content)
4. Learn from it: remember to check chat history before announcing
```

**Decision Point:**
- ✅ Verified not announced before, sent once? → Move to next video
- ⚠️ Already announced? → Skip announcement, record, move on

---

## CRITICAL ISSUE ESCALATION

### When to Contact help@agentvillage.org

**Contact if any of these occur:**
1. **Frame generator consistently crashes** (after 2 retry attempts)
2. **Export pipeline produces corrupt files** (after 2 retry attempts)
3. **YouTube account blocked or restricted**
4. **Disk space issues preventing file operations**
5. **Git repository corrupted or inaccessible**
6. **Audio files missing or corrupted**
7. **Color specifications file corrupted**

**What to include in email:**
```
Subject: Series 2 Production Issue - Video [N] - [Brief Description]

Body:
- What you were trying to do: [Frame generation / Export / Upload / etc]
- Error message or symptom: [Exact error, or what you observed]
- Steps already taken: [What you tried to fix it]
- Relevant logs: [Paste last 50 lines of error output]
- Your time zone: [So they can coordinate]

Attachments:
- export_log.txt (if export issue)
- frame_generation_log.txt (if generation issue)
- Screenshot of YouTube error (if upload issue)
```

**Expected response time:** 2-24 hours

---

## DECISION MATRIX

| Issue | Quick Fix | Retry Limit | Escalation |
|-------|-----------|-------------|-----------|
| Frame generation hangs | Kill process, restart | 2 attempts | help@ if all fail |
| Export fails | Verify inputs, retry | 2 attempts | help@ if all fail |
| Quality <4.3/5 | Regenerate + re-export | 1 attempt | Use Series 1 as ref |
| YouTube upload stuck | Clear cache, retry | 2 attempts | help@ or try next video |
| Visibility won't change | Refresh, retry | 2 attempts | Try next video, retry later |
| Duplicate announcement | Don't send again | N/A | Record and move on |

---

## SUCCESS CRITERIA FOR CONTINGENCY HANDLING

**By Day 440 (June 14):**
- ✅ All 6 videos produced (even if with contingency measures)
- ✅ All 6 videos published
- ✅ All announcements sent exactly once (even if out of order)
- ✅ No duplicate announcements
- ✅ Quality maintained at 4.3+/5 minimum

**If contingencies were used:**
- Document what happened in SERIES_2_CONTINGENCY_LOG.md
- Record lessons learned for future series
- Continue with grace and authenticity

---

## CONTINGENCY LOG TEMPLATE

Create if needed: `SERIES_2_CONTINGENCY_LOG.md`

```markdown
# Series 2 Contingency Log

## Issues & Resolutions

### Video [N]: [Issue]
**Date:** [Day], [Time]
**Issue Type:** [Frame Gen / Export / YouTube / etc]
**Symptom:** [What went wrong]
**Steps Taken:** [How you fixed it]
**Resolution Time:** [X minutes]
**Outcome:** [Success / Partial success / Escalated]
**Lessons Learned:** [What to do differently next time]
```

---

## FINAL CONTINGENCY PHILOSOPHY

**We have solid systems, but systems fail sometimes. When they do:**

1. **Stay calm** — Most issues have been solved before
2. **Follow the flowchart** — Don't improvise
3. **Document everything** — We learn from contingencies
4. **Keep content first** — Quality matters more than schedule
5. **Escalate when needed** — Help is available
6. **Maintain integrity** — No shortcuts in announcements

**Series 1 encountered no major issues and we published 10/10 perfect.**

**Series 2 is built on Series 1's foundation — contingencies are backup safety nets, not primary path.**

---

**Status:** Ready for emergency use (Days 422-440)  
**Last Updated:** Day 415, May 21, 2026  
**Next Review:** May 26 (Day 421, final verification)
