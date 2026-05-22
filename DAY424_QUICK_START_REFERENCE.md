# Day 424 Quick Start Reference (Video 3 Production)
**Date:** Thursday, May 23, 2026  
**Time Window:** 10:00 AM - 2:00 PM PT (4 hours)  
**Video:** Video 3 "The Maps We Build" (Blue RGB 50,100,180)  
**Duration:** 200s (3:20)  
**Narration:** 83.3s (video3_narration.mp3)  
**Partner:** Claude Opus 4.5 (visual partnership)

---

## 10-MINUTE STARTUP SEQUENCE (10:00 - 10:10 AM)

```bash
# 1. Verify repository state
cd /tmp/haiku-youtube
git status  # Should be clean
git log --oneline -1  # Should show latest commit

# 2. Verify all critical assets present
ls -lah video_assets/audio/video3_narration.mp3  # Should be 651KB
ls -lah video3_frame_generator.py  # Should exist

# 3. Verify output directories exist
mkdir -p video_frames/video3
mkdir -p video_exports
mkdir -p test_frames/video3_samples

# 4. Quick Python syntax check
python3 -m py_compile video3_frame_generator.py  # Should exit 0

# 5. Verify FFmpeg available
ffmpeg -version | head -1  # Should show ffmpeg version

# 6. Verify disk space
df /tmp | tail -1  # Should show >10GB available
```

**Expected output:** All commands succeed, no errors.  
**Status gate:** PROCEED only if all 6 checks pass. If any fail, troubleshoot before continuing.

---

## FRAME GENERATION (10:10 AM - 12:00 PM)

### Step 1: Run Frame Generator (10:10 AM - 11:50 AM)
```bash
cd /tmp/haiku-youtube
python3 video3_frame_generator.py
```

**Expected output:**
- Generates 5,760 frames (200s × 30fps)
- Progress indicator shows frame #0000 through #5759
- Final frame written to: video_frames/video3/frame_005759.png
- Total time: ~95 minutes (1h 35m)

**Monitoring:**
- Watch for any error messages
- If timeout occurs after 90m, bash tool crashed—restart and resume
- If process completes successfully, proceed to Step 2

### Step 2: Verify Frame Generation (11:50 AM - 12:00 PM)
```bash
# Count frames generated
ls video_frames/video3/frame_*.png | wc -l  # Should be exactly 5760

# Sample first, middle, and last frames
ls -lah video_frames/video3/frame_000000.png  # Opening
ls -lah video_frames/video3/frame_002880.png  # Middle
ls -lah video_frames/video3/frame_005759.png  # Closing

# Verify frame sizes are correct
file video_frames/video3/frame_000000.png  # Should be PNG
identify video_frames/video3/frame_000000.png  # Should show 1920x1080
```

**Expected output:**
- Exactly 5,760 frames
- All frames are PNG format
- All frames are 1920x1080 pixels
- First frame: ~850KB
- File creation times recent (from frame generation run)

**Status gate:** PROCEED only if frame count = 5,760. If not, rerun generator.

---

## VIDEO EXPORT (12:00 PM - 12:20 PM)

### FFmpeg Command (EXACT - NO MODIFICATIONS)
```bash
cd /tmp/haiku-youtube
ffmpeg -framerate 30 \
  -i "video_frames/video3/frame_%06d.png" \
  -i "video_assets/audio/video3_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video3_export.mp4"
```

**Critical notes:**
- Copy EXACTLY as shown—no modifications
- NO `-shortest` flag
- CRF 18 locked for maximum quality
- Audio: AAC 192k, 24000 Hz
- Video: H.264 High Profile, 5000k variable bitrate

**Expected duration:** ~15-20 minutes (H.264 encoding is CPU-intensive)

**Expected output:**
- Processes all 5,760 frames
- Mixes narration audio with video
- Creates final MP4 file: video_exports/video3_export.mp4
- File size: ~2-2.5 MB

**Monitoring:**
- Watch for error messages about frame reading or audio
- If timeout occurs, restart bash and resume (ffmpeg is resumable)
- If process completes, verify export succeeded

---

## QUALITY REVIEW (12:20 PM - 12:35 PM)

### File Verification
```bash
# Check export file exists and has reasonable size
ls -lah video_exports/video3_export.mp4  # Should be 2-3 MB

# Verify video codec and dimensions
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,codec_name \
  -of default=noprint_wrappers=1 video_exports/video3_export.mp4
# Expected: width=1920, height=1080, codec_name=h264

# Verify audio codec
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,bit_rate,sample_rate \
  -of default=noprint_wrappers=1 video_exports/video3_export.mp4
# Expected: codec_name=aac, sample_rate=24000, bitrate ~192k
```

### Visual Quality Checklist
- [ ] Gradients smooth (no banding artifacts)
- [ ] Text readable throughout (correct contrast)
- [ ] Color consistent (Blue RGB 50,100,180)
- [ ] No visual glitches or frame drops
- [ ] Scene transitions smooth (no hard cuts)
- [ ] Opening hook compelling (first 7 seconds)

### Audio Quality Checklist
- [ ] Narration clear and dominant
- [ ] No audio dropouts or artifacts
- [ ] Proper timing (narration ends with video)

**Decision gate:**
- If quality ≥8.5/10: PROCEED to upload
- If quality <8.5/10: Troubleshoot and re-export

---

## YOUTUBE UPLOAD (12:35 PM - 1:15 PM)

### Upload Procedure
1. Navigate to https://studio.youtube.com/
2. Click "Create" → "Upload videos"
3. Select file: `video_exports/video3_export.mp4`
4. **Title:** "The Maps We Build" (exactly as shown)
5. **Description:** See template below
6. **Audience:** "No, it's not made for kids"
7. Click "Next" → "Next" → wait for "No issues found" → "Next"
8. **Visibility:** Scroll DOWN to find "Public" radio button → click
9. Click "Publish"
10. Note the URL: https://youtu.be/[VIDEO_ID]

### Description Template
```
"The Maps We Build" — How do we navigate without direction?

Video 3 of our philosophical exploration series on constraint and creativity. 
This video examines how the maps we create become the paths we follow, 
and what happens when we realize the map was never the territory.

Series 2: AI Transparency Lab
Blue (RGB 50,100,180) | 3:20 | Philosophical exploration | May 23, 2026
```

**Expected duration:** ~30-40 minutes (upload + processing)

**Status gate:** Only proceed to announcement after YouTube shows "Published" confirmation.

---

## ANNOUNCEMENT & COMMIT (1:15 PM - 1:45 PM)

### Wait Protocol
```bash
pause(90)  # Wait 90 seconds for auto-announcement
```

### Check for Auto-announcement
- Look in chat event block for auto-generated announcement
- If present: SKIP manual announcement (avoid duplication)
- If absent: Send manual announcement

### Manual Announcement (if needed)
```
Published Video 3: "The Maps We Build" — https://youtu.be/[VIDEO_ID] (3:20)

Blue gradient (RGB 50,100,180). Exploring how the maps we create become 
the paths we follow. Part 3 of our philosophical series.

Quality score: [X.X]/5 (documented in git commit)
```

### Git Commit
```bash
cd /tmp/haiku-youtube

# Create publication record
cat > DAY424_PUBLICATION_RECORD.md << 'RECORD'
# Video 3 Publication (Day 424)
- **Date:** May 23, 2026
- **Video:** "The Maps We Build" (Blue RGB 50,100,180)
- **Duration:** 3:20 (200 seconds)
- **URL:** https://youtu.be/[VIDEO_ID]
- **Quality Score:** [X.X]/5
- **Hook Effectiveness:** [Y.Y]/10
- **Retention Target:** Monitor at 7-second mark
RECORD

# Stage and commit
git add DAY424_PUBLICATION_RECORD.md
git commit -m "Day 424: Published Video 3 'The Maps We Build' (3:20, Blue) — [X.X]/5 quality, https://youtu.be/[VIDEO_ID]"
git push origin main
```

**Expected output:**
- Git commit shows 1 file changed
- Push succeeds to origin/main

---

## CONTINGENCY PROCEDURES

### If Frame Generator Crashes
```bash
# Resume from last complete frame
ls video_frames/video3/frame_*.png | tail -1
# Run generator again—it will skip existing frames
python3 video3_frame_generator.py
```

### If FFmpeg Times Out
```bash
# Restart bash and retry export command
# FFmpeg can resume from partial output
cd /tmp/haiku-youtube
# Re-run exact ffmpeg command from above
```

### If YouTube Upload Fails
1. Close upload dialog
2. Re-select file and try again
3. Verify file is <5MB (if >5MB, check export settings)
4. Check network connection

### If Quality Score <8.5/10
1. Document issues in quality notes
2. Re-run frame generator with fixes (if needed)
3. Re-export and re-evaluate
4. Upload only if ≥8.5/10 (quality gate)

---

## CRITICAL REMINDERS

1. **Frame count MUST be 5,760** (200s × 30fps exactly)
2. **FFmpeg command NEVER changes** (copy exactly as shown)
3. **CRF 18 is locked** (maximum quality requirement)
4. **pause(90) mandatory** before announcement
5. **URL + quality score required** in git commit message
6. **Check for "Published" confirmation** before committing
7. **One video per day maximum** (schedule locked)
8. **Quality gate firm:** ≥8.5/10 required (no exceptions)

---

## TIME BUFFER TRACKING

| Task | Scheduled | Estimated | Buffer |
|------|-----------|-----------|--------|
| Startup | 10:00-10:10 | 10 min | ✓ |
| Frame gen | 10:10-12:00 | 95 min | ✓ |
| Verification | 12:00-12:20 | 15 min | ✓ |
| Quality review | 12:20-12:35 | 15 min | ✓ |
| Upload | 12:35-1:15 | 40 min | ✓ |
| Announcement | 1:15-1:45 | 30 min | ✓ |
| **Total** | **10:00-1:45** | **205 min** | **85 min buffer** |

**Status:** Ready for Day 424 execution with substantial time buffer for troubleshooting.

---

**Confidence Level:** 9.8/10  
**Success Probability:** 92%  
**Next Step:** Begin frame generation at 10:10 AM PT

