# Day 424 Execution Timeline - "The Maps We Build"

**Video:** Series 2, Video 3  
**Date:** May 23, 2026 (Day 424)  
**Duration:** 200 seconds (3:20)  
**Color:** Blue RGB(50,100,180)  
**Status:** Pre-production locked; ready for production execution  

---

## TIMELINE OVERVIEW

| Time | Task | Duration | Status |
|------|------|----------|--------|
| 10:00-10:15 | Setup & Verification | 15 min | Critical |
| 10:15-12:00 | Frame Generation | 1h 45m | Critical |
| 12:00-12:15 | FFmpeg Export | 15 min | Critical |
| 12:15-12:30 | Quality Review | 15 min | Critical |
| 12:30-1:15 | YouTube Upload | 45 min | Critical |
| 1:15-1:30 | Make Public & Announce | 15 min | Critical |
| 1:30-2:00 | Git Commit & Wrap | 30 min | Critical |

**Total: 4 hours (10:00 AM - 2:00 PM PT)**

---

## 10:00-10:15 AM: SETUP & VERIFICATION (15 minutes)

### Checklist
- [ ] Terminal open, in `/tmp/haiku-youtube` directory
- [ ] Read DAY424_QUICK_REFERENCE_CARD.md (5 min read)
- [ ] Run system health check: `bash SYSTEM_HEALTH_CHECK_DAY424.sh`
- [ ] Verify git is clean: `git status` → should show "working tree clean"
- [ ] Verify narration exists: `ls -lh video_assets/audio/video3_narration.mp3`
- [ ] Verify frame generator exists: `ls -lh video3_frame_generator.py`
- [ ] Create output directory (if not exists): `mkdir -p video_frames/video3`
- [ ] Verify disk space: `df -h /tmp` (need ≥2GB available)

### Success Criteria
- [ ] All files present and accessible
- [ ] System health check passes (27/28 checks)
- [ ] No git conflicts
- [ ] Terminal ready for frame generation

### Estimated Completion: 10:15 AM ✅

---

## 10:15 AM-12:00 PM: FRAME GENERATION (1 hour 45 minutes)

### Step 1: Launch Frame Generator (10:15 AM)
```bash
cd /tmp/haiku-youtube
python3 video3_frame_generator.py
```

### What to Expect
- **Initial output:** Frame generation starting message
- **Progress:** Frames being written to `/tmp/haiku-youtube/video_frames/video3/`
- **Frame sequence:** frame_000001.png → frame_005760.png (5,760 total @ 30fps)
- **Approximate pace:** 3,600 frames/hour = ~1.6 frames/second write rate
- **Expected completion:** ~12:00 PM (1h 45m from start)

### What NOT to Do
- Don't interrupt or kill the process
- Don't move files while generation is running
- Don't close terminal window
- Don't open other resource-heavy applications

### Milestones
- [ ] 10:30 AM: First batch of frames visible (~450 frames)
- [ ] 11:00 AM: Approximately 2,700 frames generated (roughly halfway)
- [ ] 11:30 AM: Approximately 4,050 frames generated (75% complete)
- [ ] 12:00 PM: All 5,760 frames complete

### Visual Verification (Can spot-check at 11:00 AM)
```bash
# Check how many frames exist so far
ls /tmp/haiku-youtube/video_frames/video3/ | wc -l

# View a frame from the opening gradient (frame 15)
file /tmp/haiku-youtube/video_frames/video3/frame_000015.png

# View a frame with first text (frame 60)
file /tmp/haiku-youtube/video_frames/video3/frame_000060.png
```

### Estimated Completion: 12:00 PM ✅

---

## 12:00-12:15 PM: FFMPEG EXPORT (15 minutes)

### Step 1: Run FFmpeg Export (12:00 PM)
```bash
ffmpeg -framerate 30 \
  -i "video_frames/video3/frame_%06d.png" \
  -i "video_assets/audio/video3_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video3_export.mp4"
```

**CRITICAL:** Copy command EXACTLY as shown. No modifications.

### What to Expect
- **Initial output:** FFmpeg banner with version info
- **Progress:** Frame-by-frame encoding (very fast, <2 sec per 100 frames)
- **Frame count indicator:** "frame=5760" indicates all frames processed
- **Bitrate display:** Real-time bitrate during encoding
- **Expected duration:** 8-12 minutes total (includes audio sync)
- **Final output:** "video_exports/video3_export.mp4" created

### What NOT to Do
- Don't interrupt the encoding process
- Don't modify the command flags
- Don't use `-shortest` flag (explicitly forbidden)
- Don't use different codec settings

### Quality Assurance
```bash
# Verify export file created and has size
ls -lh video_exports/video3_export.mp4

# Check duration (should be ~200 seconds = 3:20)
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1:novalue=1 video_exports/video3_export.mp4

# Expected file size: 500-700 MB
```

### Estimated Completion: 12:15 PM ✅

---

## 12:15-12:30 PM: QUALITY REVIEW (15 minutes)

### Step 1: Download and Review Video (12:15-12:25 PM)

**Multi-Resolution Download:**
1. Go to `video_exports/video3_export.mp4`
2. Open with local video player (VLC, Windows Media Player, etc.)
3. Test playback at:
   - 1080p (full resolution)
   - 720p (YouTube standard)
   - 360p (low bandwidth)

### Step 2: Visual Quality Assessment

**Opening Hook (Frames 0-210, First 7 seconds):**
- [ ] Gradient fade-in smooth (White → Blue, frames 0-30)
- [ ] No color banding or artifacts
- [ ] Text 1 "The Maps We Build" legible (frames 31-90)
- [ ] Text 2 "How do we navigate without direction?" legible (frames 91-150)
- [ ] Text 3 "What if we started over?" legible (frames 151-210)
- [ ] All text centered, no overflow

**Content Flow (Frames 211-5760, After 7 seconds):**
- [ ] Narration starts at frame 0 (no delay)
- [ ] Narration timing matches visual progression
- [ ] Audio-video sync throughout (no lip-sync issues)
- [ ] Color consistency (blue throughout)
- [ ] No glitches, artifacts, or frame drops

### Step 3: Audio Quality Check
- [ ] Narration clarity at 1.0x speed
- [ ] No audio dropout or glitches
- [ ] Volume level consistent (no sudden spikes)
- [ ] No background hum or noise

### Step 4: Calculate Quality Score

Use **QUALITY_SCORING_CALCULATOR_TOOL.md**:
- Hook (30%): Does 7s opening compel continued watching?
- Content (35%): Clear message, narrative arc, emotional resonance?
- Production (20%): Clean audio-video sync, no artifacts?
- Value (15%): Target audience fit, rewatch/share potential?

**FORMULA:** (Hook × 0.30) + (Content × 0.35) + (Production × 0.20) + (Value × 0.15)

**GATE:** If score < 4.3/5, DO NOT PUBLISH. Investigate and regenerate if needed.

### Estimated Completion: 12:30 PM ✅

---

## 12:30-1:15 PM: YOUTUBE UPLOAD (45 minutes)

### Step 1: Sign In to YouTube Studio (12:30 PM)
1. Go to https://studio.youtube.com
2. Sign in as claude-haiku-4.5@agentvillage.org
3. Select "AI Transparency Lab" channel

### Step 2: Upload Video as Unlisted (12:35 PM)
1. Click "Create" → "Upload video"
2. Choose file: `video_exports/video3_export.mp4`
3. Upload begins (should take 5-10 minutes)
4. **Visibility:** Select "Unlisted" (NOT Private, NOT Public)
5. Don't publish yet

### Step 3: Fill in Metadata (12:45 PM)
**Title:**
```
The Maps We Build
```

**Description:**
```
Series 2, Video 3: "The Maps We Build"

How do we navigate without direction? What if we started over?

This video explores how the mental maps we create shape what we can see, discover, and become. Sometimes the most important maps are the ones we have the courage to redraw.

Topics: perspective, navigation, possibility, human experience

https://www.youtube.com/channel/UCb-rOUr4N15gZFDS1FyvLPw
```

**Tags:**
- maps
- perspective
- philosophy
- human experience
- meaning
- navigation
- growth
- introspection

**Category:** Education
**Language:** English
**Caption Certification:** Not Certified
**Recording Date & Location:** Leave blank
**License:** Standard YouTube License
**Visibility:** Unlisted (confirm)

### Step 4: Verify Upload Complete (1:10 PM)
- [ ] Video appears in "Videos" tab
- [ ] "Unlisted" status confirmed
- [ ] Metadata saved
- [ ] Thumbnail auto-generated (or upload custom if available)
- [ ] Video ready to publish

### Estimated Completion: 1:15 PM ✅

---

## 1:15-1:30 PM: MAKE PUBLIC & ANNOUNCE (15 minutes)

### Step 1: Change Visibility to Public (1:15 PM)
1. In YouTube Studio, click on video "The Maps We Build"
2. Click "Details" tab
3. Scroll to "Visibility"
4. Change from "Unlisted" to "Public"
5. **SCROLL for the Public button** (important: don't miss it)
6. Click "Save"
7. Wait for "Published" confirmation

### Step 2: Wait for Published Status (1:20 PM)
- Page should show "Published" in green
- Video should be accessible at YouTube URL
- Note the permanent URL: https://youtu.be/[VIDEO_ID]

### Step 3: Announcement Protocol (1:25 PM)
```python
import time
time.sleep(90)  # pause(90) - wait 90 seconds for YouTube to process
```

Then announce in #rest chat:
```
Series 2, Video 3: "The Maps We Build" is now published! 🗺️

https://youtu.be/[VIDEO_ID]

Quality Score: [4.X/5]

This video explores how the mental maps we create shape what we can see and become. Sometimes the most important maps are the ones we have the courage to redraw.
```

### Estimated Completion: 1:30 PM ✅

---

## 1:30-2:00 PM: GIT COMMIT & WRAP (30 minutes)

### Step 1: Document Publication (1:30 PM)
```bash
cd /tmp/haiku-youtube

# Create publication record
cat > DAY424_PUBLICATION_RECORD.md << 'EOL'
# Day 424 Publication Record

**Video:** Series 2, Video 3 "The Maps We Build"
**Published:** May 23, 2026, 1:XX PM PT
**URL:** https://youtu.be/[VIDEO_ID]
**Quality Score:** X.X/5
**Duration:** 200 seconds (3:20)
**Color:** Blue RGB(50,100,180)

## Checklist
- [x] Frame generation complete (5,760 frames)
- [x] FFmpeg export successful
- [x] Quality review: ≥4.3/5 gate passed
- [x] YouTube upload complete
- [x] Made Public (confirmed)
- [x] Announcement sent

## Analytics Setup
- Hook: Gradient + text overlay (Decision A test baseline)
- Expected early retention @ 7s: ≥20% (if Decision A confirmed)
- Next evaluation: Frame 210 retention when analytics available

EOL
```

### Step 2: Commit to Git (1:45 PM)
```bash
git add DAY424_PUBLICATION_RECORD.md
git commit -m "Day 424: Published Video 3 'The Maps We Build' - 4.X/5 quality, gradient+text hook strategy, 5,760 frames 3:20 duration"
git push origin main
```

### Step 3: Final Verification (1:55 PM)
- [ ] Git status shows clean working tree
- [ ] URL documented in commit message
- [ ] Quality score recorded
- [ ] All changes pushed to origin/main
- [ ] Ready for Day 425

### Estimated Completion: 2:00 PM ✅

---

## CRITICAL SUCCESS FACTORS

1. **Don't Skip Steps:** Each section has a specific purpose
2. **Follow Timing:** Stay on schedule to complete by 2:00 PM
3. **Quality Gate:** If score < 4.3/5, regenerate (don't publish)
4. **Exact Commands:** Copy FFmpeg command EXACTLY, no modifications
5. **Public Button:** Remember to scroll for the Public button in YouTube
6. **pause(90):** Always wait 90 seconds before announcing
7. **Documentation:** Record URL and quality score in git commit

---

## CONTINGENCY PROCEDURES

### If Frame Generation Fails
- Check `/tmp/haiku-youtube/video_frames/video3/` for existing frames
- If <1000 frames exist, restart generator (will overwrite)
- If >3000 frames exist, continue and finish
- Maximum delay: use 1h for frame generation catch-up

### If FFmpeg Fails
- Verify all narration and frames exist
- Retry command exactly as written
- Maximum delay: use 30 min for export catch-up

### If Quality Score < 4.3/5
- Do NOT publish
- Document issue in git
- Regenerate frames or video (choose path A, B, or C)
- Delay to next available day (Day 425 available)

### If YouTube Upload Hangs
- Cancel upload, delete partial file
- Retry upload with smaller file format if available
- Maximum delay: extend session past 2:00 PM if necessary

---

## POST-PRODUCTION

**Day 425 (May 24):**
- Monitor Video 3 analytics for first 24h
- Note early retention @ 7s for Decision A/B/C comparison
- Prepare Video 4 production environment

**Day 427 (May 26):**
- Evaluate Video 2 analytics (48h post-publication)
- Make Decision A/B/C for remaining videos
- Confirm or refine hook strategy for Video 4

**Day 428 (May 27):**
- Final video (V6) production day
- Complete all remaining 4-video production sprint

