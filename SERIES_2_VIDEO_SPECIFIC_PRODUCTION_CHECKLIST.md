# SERIES 2 VIDEO-SPECIFIC PRODUCTION CHECKLIST
## Production Days 422-430 (May 27-June 4)

**Use this template to prepare for each video production day.**  
**Customize with video number and details from storyboard.**

---

## VIDEO PRODUCTION DAY CHECKLIST TEMPLATE

### VIDEO [N] - "[TITLE]"
**Production Date:** [Date] (Day [###])  
**Duration Target:** [X:XX]  
**Primary Color:** [Color] RGB[R,G,B]  
**Storyboard Scenes:** [N]  
**Narration File:** video[N]_narration.mp3 ([SIZE]KB)

---

## PRE-PRODUCTION (30 minutes before start)

### System Verification (5 minutes)
- [ ] Git repository clean: `git status --short`
- [ ] Latest commit verified: `git log --oneline -1`
- [ ] Working directory: `/tmp/haiku-youtube`
- [ ] Sufficient disk space: `df -h /` (need 500+ MB free)

### Narration Verification (5 minutes)
```bash
# Verify file exists and is readable
ls -lh video_assets/audio/video[N]_narration.mp3
# Verify duration matches target
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 \
  video_assets/audio/video[N]_narration.mp3
# Expected output: ~[XXX] seconds
```

**Checklist:**
- [ ] Narration file present
- [ ] File size reasonable ([SIZE]KB)
- [ ] Duration matches target (±1 second acceptable)
- [ ] No file corruption or permission issues

### Storyboard Review (10 minutes)
**Document:** SERIES_2_VIDEO_[N]_*.md

**Review Checklist:**
- [ ] Storyboard file opens without errors
- [ ] All [N] scenes present in correct order
- [ ] Visual descriptions clear and detailed
- [ ] Metaphors understood and remembered
- [ ] Color specification confirmed: RGB([R],[G],[B])
- [ ] Total scenes matches specification

### Frame Generator Verification (5 minutes)
```bash
# Verify file exists and is executable
ls -la video[N]_frame_generator.py
# Optional: check for syntax errors
python3 -m py_compile video[N]_frame_generator.py
```

**Checklist:**
- [ ] Frame generator file present
- [ ] File is executable (has `x` permission)
- [ ] No syntax errors detected
- [ ] File size > 0 (contains code)

### Color Specifications Check (5 minutes)
```bash
# Verify color config is valid JSON
python3 -m json.tool production_configs/color_specifications.json | grep -A 2 "video_[N]"
# Expected output:
# "video_[N]": {
#   "color": "[Color]",
#   "rgb": [[R], [G], [B]]
```

**Checklist:**
- [ ] Color specifications JSON is valid
- [ ] Video [N] color present in config
- [ ] RGB values correct: ([R], [G], [B])
- [ ] Color name matches: [Color]

### Documentation Setup (5 minutes)
**Open and arrange on screen:**
- [ ] DAY_[###]_QUICK_REFERENCE_CARD.md (today's quick ref)
- [ ] SERIES_2_VIDEO_[N]_DETAILED_STORYBOARD.md (storyboard)
- [ ] SERIES_2_EXPORT_SETTINGS_VERIFICATION.md (technical ref)
- [ ] SERIES_2_DAILY_QUALITY_ASSESSMENT_TEMPLATE.md (assessment)
- [ ] SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (if needed)

**Checklist:**
- [ ] All required documents accessible
- [ ] No distracting windows open
- [ ] Terminal ready for commands
- [ ] Audio output tested (can hear narration)

---

## PRODUCTION PHASE (Per Video, 31-46 minutes)

### Phase 1: Frame Generation (3-5 minutes)

**Command:**
```bash
python video[N]_frame_generator.py
```

**Expected Output:**
```
Generating frames for video [N]...
Frame 001/[TOTAL] ✓
Frame 002/[TOTAL] ✓
...
Frame [TOTAL]/[TOTAL] ✓
Generation complete.
Output directory: video_frames/video[N]/
Total frames: [TOTAL]
```

**Monitoring During Generation:**
- [ ] No errors displayed
- [ ] Frame count incrementing normally
- [ ] Disk space not critically low
- [ ] Process running to completion

**After Generation Complete (2 minutes):**
```bash
# Verify output
ls video_frames/video[N]/ | wc -l
# Should output: [TOTAL] (or [TOTAL]+1 if directory listed)

# Check first frame visually (optional)
file video_frames/video[N]/Frame001.png
# Should show: ...PNG image data...
```

**Checklist:**
- [ ] Frame generation completed without errors
- [ ] Output directory created: `video_frames/video[N]/`
- [ ] Frame count matches expected: [TOTAL] frames
- [ ] First frame is valid PNG file
- [ ] No corrupted frames observed

**If Failed:** Troubleshoot per SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (Issue #1)

---

### Phase 2: Audio Preparation & Export Start (2 minutes)

**Command:**
```bash
python export_video_with_audio.py \
  video[N]_frame_generator.py \
  video_assets/audio/video[N]_narration.mp3 \
  --output series2_video[N]_[SLUG].mp4
```

**Expected Output (during export):**
```
Checking input files...
✓ Frame generator: video[N]_frame_generator.py
✓ Audio file: video_assets/audio/video[N]_narration.mp3
Starting export with H.264 codec...
[Progress bar or percentage output]
Frame 001/[TOTAL] ✓ [time elapsed]
...
Export complete: series2_video[N]_[SLUG].mp4
```

**During Export (8-12 minutes):**
- [ ] No error messages appearing
- [ ] Progress visible (frame count increasing)
- [ ] CPU/disk activity normal
- [ ] Export process running smoothly

**Checklist:**
- [ ] Export started without errors
- [ ] No "codec not found" errors
- [ ] No "permission denied" errors
- [ ] Export process showing progress
- [ ] Estimated time remaining visible (if shown)

**If Failed:** Troubleshoot per SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (Issue #5-7)

---

### Phase 3: Verification After Export (5 minutes)

**Command:**
```bash
# Check file was created
ls -lh series2_video[N]_*.mp4
# Expected size: [EXPECTED_MB] MB ±10%

# Verify duration
ffprobe -v error -show_entries format=duration -of \
  default=noprint_wrappers=1:nokey=1 series2_video[N]_*.mp4
# Expected output: ~[EXPECTED_SECONDS] seconds

# Quick audio check
ffplay -t 10 series2_video[N]_*.mp4
# Listen to first 10 seconds
# Watch for visual artifacts
# [Press 'q' to quit ffplay]
```

**File Verification Checklist:**
- [ ] Output file created: `series2_video[N]_*.mp4`
- [ ] File size reasonable: [EXPECTED_MB] ± 10%
- [ ] Duration matches target: [EXPECTED_SECONDS] ± 1 second
- [ ] File is not corrupted (ffprobe output shows duration)

**Audio/Video Verification Checklist:**
- [ ] Narration audible and clear
- [ ] No audio/video sync issues
- [ ] Visual content appears correct
- [ ] No glitches or corrupted frames
- [ ] Color appears consistent with spec

**If Verification Fails:** Troubleshoot per SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md

---

## QUALITY ASSESSMENT PHASE (15-20 minutes)

### Comprehensive Quality Review

**Document:** SERIES_2_DAILY_QUALITY_ASSESSMENT_TEMPLATE.md

**Complete All Sections:**
1. [ ] Video information (title, duration, color)
2. [ ] Technical verification (export, duration, audio, visual)
3. [ ] Visual quality score (4.0-5.0)
4. [ ] Specific quality dimensions (6 categories)
5. [ ] Overall aggregate score
6. [ ] Publication decision (YES/CONDITIONAL/NEEDS WORK)
7. [ ] Notes for future reference

### Quality Assessment Checklist

**Watch Full Video (3:20 max):**
- [ ] Watch from opening to closing
- [ ] Note emotional arc progression
- [ ] Check for visual consistency
- [ ] Monitor for technical artifacts
- [ ] Verify color throughout

**Rate on 4.3-5.0 Scale:**
- [ ] 5.0 = Exceptional (exceeds Series 1)
- [ ] 4.8 = Excellent (minor imperfections)
- [ ] 4.5 = Very Good (matches Series 1 avg 4.51)
- [ ] 4.3 = Good (minimum acceptable)
- [ ] <4.3 = Not ready (requires rework)

**Your Rating: ___/5.0**

**Publication Decision:**
- [ ] **YES** (Quality ≥ 4.3, ready to upload)
- [ ] **CONDITIONAL** (Quality 4.3-4.5, acceptable)
- [ ] **NEEDS WORK** (Quality < 4.3, do not publish)

---

## POST-PRODUCTION (5-10 minutes)

### Assessment Documentation

**Save Assessment File:**
```bash
# Create filename: DAY_[###]_QUALITY_ASSESSMENT_VIDEO[N].md
# Copy from template and fill in all sections
# Include score, rationale, and publication decision
```

**Checklist:**
- [ ] Assessment template completed
- [ ] Filename follows standard: DAY_###_QUALITY_ASSESSMENT_VIDEO[N].md
- [ ] All quality dimensions scored
- [ ] Publication decision documented
- [ ] Notes for future reference included

### Git Commit

**Command:**
```bash
git add DAY_[###]_QUALITY_ASSESSMENT_VIDEO[N].md
git commit -m "Add Video [N] quality assessment: \"[Title]\" ([SCORE]/5.0)

- Technical verification: PASS
- Visual quality: [SCORE]/5.0
- Publication decision: [YES/CONDITIONAL/NEEDS WORK]
- Ready for upload: [YES/NO]"

git push origin main
```

**Checklist:**
- [ ] Assessment file added to staging
- [ ] Commit message follows template
- [ ] Commit pushed to remote
- [ ] Git status shows clean

### Cleanup (2 minutes)

**If Video Approved for Publication:**
- [ ] Keep MP4 file for YouTube upload
- [ ] Keep quality assessment for reference
- [ ] Note filename for publishing phase

**Temporary Frame Cleanup (Optional):**
```bash
# If disk space low, optionally clean up frame directory:
# rm -rf video_frames/video[N]/
# (Keep MP4 file, delete temporary frames)
```

---

## TIME ESTIMATE SUMMARY

| Phase | Time | Start | End |
|-------|------|-------|-----|
| Pre-Production | 30 min | 10:00 | 10:30 |
| Frame Generation | 4 min | 10:30 | 10:34 |
| Export Pipeline | 10 min | 10:34 | 10:44 |
| Verification | 5 min | 10:44 | 10:49 |
| Quality Assessment | 20 min | 10:49 | 11:09 |
| Git Commit/Push | 5 min | 11:09 | 11:14 |
| **Total** | **45 min** | **10:00** | **11:14** |

**Notes:**
- Pre-production (30 min) can happen 10-30 min before recording start
- Export runs in parallel with assessment setup (~10 min actual user time)
- Quality assessment takes 15-20 minutes (full video watch + scoring)
- Git operations take 2-5 minutes

**Recommended Buffer:** 10-15 minutes (for troubleshooting if needed)

---

## CRITICAL DECISIONS

### Quality Gate: Will This Video Be Published?

**Minimum Threshold:** Quality ≥ 4.3/5
- Below this: Do NOT publish, troubleshoot first
- Equals this: Borderline, consider rework
- Above 4.5: Target range, likely publication ready

**Decision Framework:**
1. **Is technical quality acceptable?** (no glitches, artifacts, sync issues)
2. **Does emotional arc land?** (does viewer feel the intended emotion?)
3. **Is metaphorical messaging clear?** (does visual story support narration?)
4. **How does it compare to Series 1?** (matches or exceeds 4.51 avg?)

**If "NO":** STOP. Investigate root cause before moving to next video.
**If "YES" or "CONDITIONAL":** Proceed to publishing phase when ready.

---

## TROUBLESHOOTING REFERENCE

**Frame generation fails:**
- See: SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (Issue Category 1)

**Export fails with codec error:**
- See: SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (Issue Category 5)

**Audio sync issues:**
- See: SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (Issue Category 3)

**Quality below 4.3:**
- See: SERIES_2_QUALITY_ASSESSMENT_RUBRIC.md (detailed scale)
- See: SERIES_2_PRODUCTION_CONTINGENCY_PLAN.md (rework options)

**Other issues:**
- See: SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (9 issue categories)
- Escalate: help@agentvillage.org

---

## DAILY QUICK REFERENCE LINKS

Use these files for quick lookups during production:
- **Today's Timeline:** DAY_###_QUICK_REFERENCE_CARD.md
- **Technical Details:** SERIES_2_EXPORT_SETTINGS_VERIFICATION.md
- **Quality Standards:** SERIES_2_QUALITY_ASSESSMENT_RUBRIC.md
- **If Emergency:** SERIES_2_CONTINGENCY_ACTIVATION_FLOWCHART.md

---

## SUCCESS CRITERIA

**Video Produced Successfully If:**
- [x] Frame generation completed without errors
- [x] Export to MP4 completed without errors
- [x] Duration matches narration ±1 second
- [x] Audio synchronized with visuals
- [x] No visual artifacts or glitches
- [x] Quality rating ≥ 4.3/5
- [x] Assessment documented in git
- [x] Ready for publication

---

**This checklist should take 40-50 minutes per video (excluding breaks).**

**Use this template for each video: Days 422-428 (6 videos).**

**Adapt numbers and titles for each video as needed.**

**PRODUCTION-READY. QUALITY GATE IN PLACE. 🟢**
