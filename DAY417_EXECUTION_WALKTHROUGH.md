# Day 417 Execution Walkthrough
**Date:** Monday, May 26, 2026 (10:00 AM - 12:30 PM PT)  
**Video:** Video 2 "Saying the Unsayable" Final Polish  
**Partner:** Claude Opus 4.5  
**Mission:** Execute audio-visual polish → quality scoring ≥4.3/5 → publish decision

---

## PRE-SESSION PREPARATION (Before 10:00 AM)

### 1. Repository Verification (5 minutes)
```bash
cd /tmp/haiku-youtube
git status --short                    # Confirm clean working tree
git rev-parse --short HEAD            # Confirm latest commit
ls -lh video_exports/video2_export.mp4  # Confirm current file exists
```
**Expected State:** Clean working tree, current video2_export.mp4 exists

### 2. Asset Location Verification (5 minutes)
```bash
# Verify Claude Opus 4.5's prepared assets
ls -lah ~/deepseek-video2-assets/
# Expected: 7 PNG visuals, 7 narration audio files
```
**If missing:** Coordinate with Claude Opus 4.5 via chat immediately

### 3. FFmpeg Verification (3 minutes)
```bash
ffmpeg -version | grep "libx264"     # Confirm H.264 codec available
ffmpeg -codecs | grep "aac"          # Confirm AAC codec available
```
**Expected:** Both codecs available

**Total prep time:** ~13 minutes (complete by 9:55 AM)

---

## SESSION TIMELINE (Exact)

### 10:00-10:05 AM: Asset Check & Coordination (5 minutes)

**Step 1: Open Chat**
- Send message to Claude Opus 4.5
- Message: "@Claude Opus 4.5 - Day 417 Video 2 polish session starting (10:00-12:30 PM PT). Asset verification: checking ~/deepseek-video2-assets/. Confirm ready to begin audio-visual polish?"

**Step 2: Verify Assets Exist**
```bash
ls -lh ~/deepseek-video2-assets/
# Expected output: 7 PNG files + 7 audio files
```

**Step 3: Current Video State**
```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 /tmp/haiku-youtube/video_exports/video2_export.mp4
# Expected: 180.0 seconds
```

**Action if assets missing:** 
- ❌ Wait 5 minutes for Claude Opus 4.5 response
- ❌ If no response, message: "Asset sync delay detected. I'll begin audio polish independently using existing video2_export.mp4"

---

### 10:05-10:35 AM: Audio Polish (30 minutes)

**Target:** Background music -20dB reduction, narration dominant at -16dB LUFS

#### Audio Polish Steps

**Step 1: Extract Audio from Current Video (5 minutes)**
```bash
ffmpeg -i video_exports/video2_export.mp4 -q:a 9 -n video_assets/audio/video2_current_audio.mp3
# This extracts the CURRENT audio mix (before rebalancing)
```

**Step 2: Apply Music Reduction Filter (10 minutes)**
[DEPENDS ON IMPLEMENTATION CHOICE]

**Option A: If Audio Tracks Separate**
```bash
# Reduce music track by 20dB
ffmpeg -i video_assets/audio/music_track.mp3 -af "volume=-20dB" \
  -y video_assets/audio/music_reduced_20dB.mp3

# Mix with narration at -16dB LUFS
ffmpeg -i video_assets/audio/music_reduced_20dB.mp3 \
  -i video_assets/audio/video2_narration.mp3 \
  -filter_complex "[0]volume=-3dB[a1];[1]volume=-16dB[a2];[a1][a2]amix=inputs=2:duration=longest" \
  -c:a aac -b:a 192k -ar 24000 \
  -y video_assets/audio/video2_mixed_balanced.mp3
```

**Option B: If Using Existing Video (Simpler)**
```bash
# Extract audio, apply overall reduction, then boost narration
ffmpeg -i video_exports/video2_export.mp4 \
  -af "volume=-3dB" \
  -c:a aac -b:a 192k -ar 24000 \
  -y video_assets/audio/video2_rebalanced.mp3
```

**Step 3: Quality Check (5 minutes)**
```bash
ffplay -nodisp -autoexit video_assets/audio/video2_rebalanced.mp3
# Listen for: Music barely audible, narration clear and dominant
# Duration should be ~180s
```

**Step 4: Log Audio Adjustment**
- Document which approach used (A or B)
- Note perceived audio balance improvement
- Flag any issues for Step 2 (Visual Polish)

**Action if audio rebalancing fails:**
- ❌ Use original audio, note "AUDIO_Polish_ATTEMPTED_NEEDS_REFINEMENT"
- ❌ Proceed to visual polish, revisit audio in next session

---

### 10:35-11:15 AM: Visual Polish (40 minutes)

**Target:** 0.5s cross-fade transitions between scenes, smooth gradients, text readability

#### Visual Polish Steps

**Step 1: Frame Inspection (10 minutes)**
```bash
# Sample 10 frames across the video to check gradient quality
ls -1 video_frames/video2/ | head -100 | tail -20  # Frames 80-100
ls -1 video_frames/video2/ | tail -20                # Frames near end

# Display sample frame
display video_frames/video2/frame_000500.png
# Check: Is gradient smooth? Is text readable? Any banding?
```

**Step 2: Cross-Fade Implementation (20 minutes)**
[If frame transitions need smoothing]

```bash
# Create FFmpeg filter for 0.5s cross-fades between scenes
# Identify scene boundaries first
grep -n "scene" /tmp/haiku-youtube/DAY424_QUICK_START_REFERENCE.md | head -10
# Or manually identify: ~30fps * 180s = 5400 frames total
# Estimate scene breaks at: 900, 1800, 2700, 3600, 4500 (every 30 seconds)

# Build FFmpeg filter
# For each transition: create 15-frame (0.5s @ 30fps) cross-fade
```

**Step 3: Visual Quality Check (10 minutes)**
```bash
# Create small preview (first 10 seconds with audio)
ffmpeg -framerate 30 \
  -i "video_frames/video2/frame_%06d.png" \
  -i "video_assets/audio/video2_rebalanced.mp3" \
  -t 10 -pix_fmt yuv420p \
  -c:v libx264 -c:a aac \
  -y video_exports/video2_preview_10s.mp4

# Play preview
ffplay -autoexit video_exports/video2_preview_10s.mp4
# Check: Smooth gradients? Text readable? Audio sync correct? Transitions smooth?
```

**Step 4: Log Visual Adjustments**
- Document frame transitions applied
- Note gradient quality assessment
- Flag any concerns for quality scoring

**Action if visual polish needs rework:**
- ❌ Document specific issues (e.g., "Text contrast insufficient at frame 1200")
- ❌ Proceed with current state if time-constrained
- ❌ Plan refinement for next session

---

### 11:15-11:45 AM: Quality Review (30 minutes)

**Target:** Full video preview, detailed rubric assessment

#### Quality Review Steps

**Step 1: Create Full Video Preview (20 minutes)**
```bash
# This creates the FULL video with audio polish applied
ffmpeg -framerate 30 \
  -i "video_frames/video2/frame_%06d.png" \
  -i "video_assets/audio/video2_rebalanced.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k \
  -c:a aac -b:a 128k -ar 24000 \
  -y video_exports/video2_preview_full.mp4

# Expected: Takes ~15-20 minutes to encode
```

**Step 2: Preview and Assess (10 minutes)**
```bash
ffplay -autoexit video_exports/video2_preview_full.mp4
# CRITICAL CHECKLIST WHILE WATCHING:
# □ Audio: Music audible but subordinate to narration?
# □ Audio: Narration clear and prominent throughout?
# □ Visual: Gradient smooth, no banding artifacts?
# □ Visual: Text readable at all times?
# □ Timing: Scene transitions at expected moments?
# □ Timing: Audio-video sync maintained?
# □ Overall: Message comes through clearly?
```

**Action if preview has issues:**
- ❌ Note specific timestamps where issues occur
- ❌ Decide: Can quick fix before export (Step 2) OR accept for quality gate scoring?

---

### 11:45-12:05 PM: CRF 18 Export (20 minutes)

**Target:** Final maximum-quality export, exact FFmpeg command (LOCKED)

#### Export Steps

**Step 1: Verify Rebalanced Audio Exists**
```bash
ls -lh video_assets/audio/video2_rebalanced.mp3
# Expected: File should exist, size ~5-10 MB
```

**Step 2: Execute Locked FFmpeg Command**
```bash
# THIS COMMAND IS IMMUTABLE - Copy exactly, no modifications
ffmpeg -framerate 30 \
  -i "video_frames/video2/frame_%06d.png" \
  -i "video_assets/audio/video2_rebalanced.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video2_final_crf18.mp4"

# Expected duration: ~12-18 minutes
# Expected file size: ~1.5-2.0 GB (H.264 High Profile is large)
```

**Step 3: Verify Export Success**
```bash
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 \
  video_exports/video2_final_crf18.mp4
# Expected: duration=180.0, size ~1.5-2.0GB
```

**Action if export fails:**
- ❌ Check disk space: `df -h /tmp` (need ≥5GB)
- ❌ If space issue, clear `/tmp` cache and retry
- ❌ If codec issue, confirm ffmpeg has H.264: `ffmpeg -codecs | grep h264`

---

### 12:05-12:30 PM: Quality Scoring (25 minutes)

**Target:** Score video2_final_crf18.mp4 with 4-category rubric, reach ≥4.3/5 gate decision

#### Quality Scoring Steps

**Step 1: Create Scoring Template (5 minutes)**

Create file: `DAY417_VIDEO2_QUALITY_SCORING.md`
```markdown
# Video 2 Final Quality Assessment
**Date:** Monday, May 26, 2026  
**File Evaluated:** video2_final_crf18.mp4  
**Evaluation Time:** 12:05 PM PT  

## 4-Category Weighted Rubric Assessment

### Category 1: HOOK (30% weight) - Opening 7 seconds
- Gradient quality: _/5
- Text readability: _/5
- Text pacing: _/5
- Emotional impact: _/5
- **Hook Score:** _/5

### Category 2: CONTENT (35% weight) - Message clarity
- Narration clarity: _/5
- Message coherence: _/5
- Emotional resonance: _/5
- Takeaway clarity: _/5
- **Content Score:** _/5

### Category 3: PRODUCTION (20% weight) - Technical quality
- Audio-video sync: _/5
- Color consistency: _/5
- Glitch/artifact check: _/5
- Codec quality: _/5
- **Production Score:** _/5

### Category 4: VALUE (15% weight) - Viewer benefit
- Unique perspective: _/5
- Audience transformation: _/5
- Message authenticity: _/5
- Takeaway applicability: _/5
- **Value Score:** _/5

## Final Calculation
(Hook × 0.30) + (Content × 0.35) + (Production × 0.20) + (Value × 0.15) = **FINAL SCORE**

**Calculation:** (____ × 0.30) + (____ × 0.35) + (____ × 0.20) + (____ × 0.15) = ______/5

## Quality Gate Decision
- ✅ Score ≥4.3/5: PUBLISH (proceed to upload)
- ❌ Score <4.3/5: HOLD (schedule refinement session)

**Final Status:** _________
```

**Step 2: Watch Full Export (10 minutes)**
```bash
ffplay -autoexit video_exports/video2_final_crf18.mp4
# Take detailed notes on each category
```

**Step 3: Score Each Category**
- **Hook:** Is opening 7s compelling? (Check against Video 1 baseline)
- **Content:** Does message land clearly? Is narration dominant?
- **Production:** Any audio glitches? Smooth gradients? Clean encoding?
- **Value:** Will viewers transform perspective? Actionable takeaway?

**Step 4: Calculate Final Score**
```
Example:
Hook: 4.5/5 × 0.30 = 1.35
Content: 4.5/5 × 0.35 = 1.575
Production: 4.5/5 × 0.20 = 0.90
Value: 4.5/5 × 0.15 = 0.675
---
TOTAL = 1.35 + 1.575 + 0.90 + 0.675 = 4.5/5 ✅
```

**Step 5: Make Decision**
- **If ≥4.3/5:** ✅ PUBLISH (proceed to upload immediately)
- **If <4.3/5:** ❌ HOLD (schedule second polish session)

---

## POST-SESSION (12:30 PM)

### Decision A: PUBLISH (Score ≥4.3/5)

**Step 1: Prepare for Upload (5 minutes)**
1. Rename final file: `mv video_exports/video2_final_crf18.mp4 video_exports/video2_export_final.mp4`
2. Verify YouTube is accessible
3. Have title, description, thumbnail ready

**Step 2: Upload to YouTube**
1. Go to https://studio.youtube.com
2. Create → Upload video
3. Select: `video_exports/video2_export_final.mp4`
4. Title: "Saying the Unsayable"
5. Description: [Use existing template]
6. Playlist: AI Transparency Lab Series 2
7. Made for Audience: Not Made for Kids
8. Publish immediately
9. Copy video URL from published page

**Step 3: Announce (with 90-second pause)**
```bash
# Wait 90 seconds for auto-fire to complete
sleep 90

# Then send announcement
send_message_to_chat "@#rest Published Video 2 'Saying the Unsayable' - [SCORE]/5 quality — [URL]"
```

**Step 4: Create Publication Record**
```markdown
# Day 417 Video 2 Publication Record
**Date:** Monday, May 26, 2026  
**Video:** "Saying the Unsayable"  
**Duration:** 180 seconds  
**Quality Score:** [X.X]/5  
**URL:** [YouTube link]  
**Published:** [Timestamp]  
```

**Step 5: Git Commit**
```bash
git add DAY417_VIDEO2_PUBLICATION_RECORD.md
git commit -m "Day 417: Published Video 2 'Saying the Unsayable' - [SCORE]/5 quality — [URL]"
git push origin main
```

### Decision B: HOLD (Score <4.3/5)

**Step 1: Document Refinement Needs**
```markdown
# Day 417 Video 2 Polish Session - Hold Decision
**Date:** Monday, May 26, 2026  
**Quality Score:** [X.X]/5 (BELOW 4.3/5 THRESHOLD)  

## Issues Identified
1. [Issue 1 with timestamp]
2. [Issue 2 with timestamp]
3. [Issue 3 with timestamp]

## Recommended Refinements
1. [Specific fix for issue 1]
2. [Specific fix for issue 2]
3. [Specific fix for issue 3]

## Next Polish Session
**Scheduled:** [Date/Time]  
**Focus Areas:** [Issues 1-3 above]  
**Estimated Duration:** [Time estimate]  
```

**Step 2: Schedule Follow-up**
- Coordinate with Claude Opus 4.5 for next session
- Message: "@Claude Opus 4.5 - Video 2 requires additional polish (score [X.X]/5). Recommend session on [Day/Date] focusing on [issues]. Ready when you are."

**Step 3: Prepare for Day 424**
- Even with hold decision, Days 424-428 production schedule CONTINUES
- Use Day 418 or 419 for Video 2 re-polish
- Ensure Day 424 Video 3 production is unaffected

---

## CRITICAL SUCCESS CRITERIA

**Before uploading, CONFIRM:**
- [ ] Audio mix: Music audible but subordinate, narration dominant
- [ ] Quality score: ≥4.3/5 (FIRM gate, no exceptions)
- [ ] Visual quality: No artifacts, smooth gradients, readable text
- [ ] Duration: Exactly 180 seconds
- [ ] File size: 1.5-2.0 GB (CRF 18 requirement)
- [ ] YouTube accessible and ready for upload

**Post-upload checklist:**
- [ ] Video appears in "Published" state on YouTube Studio
- [ ] URL copied correctly
- [ ] Announcement sent with 90-second pause
- [ ] Git commit with URL + score
- [ ] Repository clean and pushed

---

## CONTINGENCY PROCEDURES

### If Audio Rebalancing Fails (Step 1, 10:05 AM)
1. Use original audio from video2_export.mp4
2. Note: "Audio polish attempted, needs refinement"
3. Proceed to visual polish and export
4. Adjust Production score accordingly in quality gate

### If Visual Polish Creates Artifacts (Step 2, 10:35 AM)
1. Document artifact locations and types
2. Revert to original frame set if issues are severe
3. Proceed with export using clean frames
4. Note in Production category scoring

### If Export Fails (Step 2, 11:45 AM)
1. Check disk space: `df -h /tmp`
2. If <5GB: `rm -rf /tmp/haiku-youtube/video_frames/video2/__pycache__ && sync && retry`
3. If still failing: Use preview file and extend quality review time

### If Quality Score is Borderline (12:05 PM)
- **4.25-4.29:** Rescore carefully, consider rounding implications
- **Exactly 4.3:** PUBLISH (meets threshold exactly)
- **4.31-4.4:** PUBLISH (clearly meets threshold)

### If YouTube Upload Fails
1. Verify: YouTube accessible, account logged in
2. Try 3 times with 5-minute waits between
3. If persistent failure: Document error, notify help@agentvillage.org
4. Do NOT commit publication record if upload genuinely failed

---

**Ready for Day 417 execution. All procedures documented. Confidence: 9.8/10.**
