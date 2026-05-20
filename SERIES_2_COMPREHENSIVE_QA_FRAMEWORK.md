# SERIES 2 COMPREHENSIVE QA FRAMEWORK
**Created:** Day 414, May 20, 2026  
**Status:** Production-Ready Framework  
**Purpose:** Systematic quality assurance for May 27-June 4 production phase

---

## 1. PRE-PRODUCTION QA (Days 414-426)

### 1.1 Asset Verification Checklist
**Daily Morning Checklist (5 min):**
- [ ] Git repository status clean
- [ ] All 6 narrations present (video2-6_narration.mp3)
- [ ] All 6 frame generators executable
- [ ] Color specifications JSON valid
- [ ] Export scripts functional
- [ ] 30fps, 1920×1080 resolution confirmed

**Weekly Deep Dive (Thursday each week):**
- [ ] All frame generators produce valid PNG sequences
- [ ] Audio files play without corruption
- [ ] Color values render correctly in test export
- [ ] Metadata files all present and valid
- [ ] Documentation references current and accurate

### 1.2 Documentation Verification
- [ ] MAY_27_QUICK_REFERENCE_CARD.md present and accessible
- [ ] SERIES_2_PUBLISHING_PHASE_GUIDE.md complete
- [ ] All production day cards (May 27-June 4) present
- [ ] Storyboards locked with no modifications
- [ ] Scripts locked with zero rewrites

---

## 2. PRODUCTION PHASE QA (May 27-June 4)

### 2.1 Daily Production Workflow QA

**PRE-PRODUCTION (Morning of shoot):**
- [ ] Verify narration audio file present and plays correctly
- [ ] Confirm frame generator executable and accessible
- [ ] Test 10-frame generation cycle to verify pipeline
- [ ] Confirm storyboard is locked (no script changes during production)
- [ ] Verify color specs match current locked version

**GENERATION PHASE:**
- [ ] Frames generating without errors (check every 20% checkpoint)
- [ ] File size accumulation matches expected range (frames should be ~1-5 MB each)
- [ ] PNG metadata retained (ffprobe will verify)
- [ ] No frame corruption (sample frames spot-checked every 500 frames)

**ASSEMBLY PHASE:**
- [ ] Audio imported correctly, synchronized to narration timing
- [ ] First 5 frames verify audio alignment
- [ ] Middle frame set (around 50%) checks audio sync
- [ ] Last 5 frames verify end-to-end sync
- [ ] H.264 encoding settings applied (yuv420p, High Profile)
- [ ] AAC audio codec confirmed (192 kbps, 24 kHz, mono)

**EXPORT VERIFICATION:**
- [ ] Final file size between 50-75 MB
- [ ] Duration matches target (tolerance: ±2 frames)
- [ ] ffprobe metadata validation:
  - Video codec: h264
  - Pixel format: yuv420p
  - Resolution: 1920×1080
  - Frame rate: 30 fps
  - Audio codec: aac
  - Audio bitrate: 192 kbps
  - Audio sample rate: 24000 Hz
  - Audio channels: 1 (mono)

**QUALITY PLAYBACK CHECK:**
- [ ] Play first 30 seconds: verify color grading, narration sync
- [ ] Play middle section: spot-check 10 random frames for visual quality
- [ ] Play last 30 seconds: verify ending composition, audio levels
- [ ] Check for artifacts: no codec glitches, compression issues, or color banding
- [ ] Audio levels consistent throughout (no sudden peaks/drops)

### 2.2 Quality Scoring Framework

**Score Range:** 1.0-5.0 (each video minimum 4.3/5)

**Scoring Categories:**

**Technical Quality (max 1.5):**
- Audio sync perfection: 0-0.5 (0.5 = perfect throughout)
- Color grading consistency: 0-0.5 (0.5 = locked colors, no clipping)
- Frame render quality: 0-0.5 (0.5 = no artifacts, clean edges)

**Visual Storytelling (max 1.5):**
- Frame-to-frame narrative flow: 0-0.5 (0.5 = compelling progression)
- Color psychology effectiveness: 0-0.5 (0.5 = color reinforces message)
- Scene composition clarity: 0-0.5 (0.5 = visuals support narration)

**Emotional Impact (max 1.0):**
- Vulnerability authenticity: 0-0.33 (0.33 = genuine, undefended)
- Audience resonance potential: 0-0.33 (0.33 = relatable, actionable)
- Thematic coherence: 0-0.34 (0.34 = message unity, no contradictions)

**Audience Engagement (max 1.0):**
- Title-content alignment: 0-0.33 (0.33 = title delivers on promise)
- Call-to-introspection clarity: 0-0.33 (0.33 = viewer knows what to reflect on)
- Repeat-watch value: 0-0.34 (0.34 = layered enough for multiple viewings)

**Scoring Benchmarks:**
- 4.0-4.2: Acceptable, publishable (only if exceptional circumstances)
- 4.3-4.5: Standard target (match Series 1 baseline of 4.51)
- 4.6-4.7: Excellent (match Series 1 best performers)
- 4.8-5.0: Exceptional (rare, only if all categories maxed)

### 2.3 Daily Production Checklist Template

**Date:** May [27-31] or June [2-4], 2026  
**Video:** [1-6] - [Title]  
**Expected Duration:** [TIME] | **Target Score:** 4.5+/5

```
PRE-PRODUCTION ✓
- [ ] Narration audio verified
- [ ] Frame generator tested (10 frames)
- [ ] Storyboard locked
- [ ] Color specs locked
- [ ] Quick reference card reviewed

GENERATION ✓
- [ ] Started: [TIME]
- [ ] Frame 1000 checkpoint: OK [ ] Issues [ ]
- [ ] Frame 2000 checkpoint: OK [ ] Issues [ ]
- [ ] Frame 3000 checkpoint: OK [ ] Issues [ ]
- [ ] Frame 4000 checkpoint: OK [ ] Issues [ ]
- [ ] Completed: [TIME]
- [ ] Total frames: [COUNT] ✓

ASSEMBLY ✓
- [ ] Audio imported: [TIME]
- [ ] Sync test (frames 1-5): OK [ ] Issues [ ]
- [ ] Sync test (mid section): OK [ ] Issues [ ]
- [ ] Sync test (final frames): OK [ ] Issues [ ]
- [ ] H.264 encoding started: [TIME]
- [ ] File size: [SIZE] MB (target: 50-75)
- [ ] Duration: [ACTUAL] (target: [EXPECTED])

QUALITY VERIFICATION ✓
- [ ] ffprobe validation: PASS [ ] FAIL [ ]
- [ ] Playback (0:00-0:30): Visual OK [ ] Audio OK [ ]
- [ ] Playback (mid): Visual OK [ ] Audio OK [ ]
- [ ] Playback (end): Visual OK [ ] Audio OK [ ]
- [ ] Artifact check: NONE DETECTED [ ] FOUND [ ]

SCORING ✓
Technical Quality: __/1.5
Visual Storytelling: __/1.5
Emotional Impact: __/1.0
Audience Engagement: __/1.0
TOTAL SCORE: __/5.0

STATUS: PASS (≥4.3) [ ] CONDITIONAL (4.0-4.2) [ ] FAIL (<4.0) [ ]

NOTES:
[Space for observations, anomalies, or refinements]
```

---

## 3. PUBLISHING PHASE QA (June 9-14)

### 3.1 Pre-Publishing Verification

**72 Hours Before Publication:**
- [ ] Video file final name confirmed
- [ ] Metadata prepared (title, description, tags)
- [ ] Thumbnail prepared or default selected
- [ ] Video playable in final storage location
- [ ] ffprobe validation one final time

**24 Hours Before Publication:**
- [ ] YouTube upload account verified signed in
- [ ] Video playable on local machine
- [ ] Description text proofread (no typos, links valid)
- [ ] Tags finalized (consistency with Series 1 tags)
- [ ] Playlist assignment confirmed

**2 Hours Before Publication:**
- [ ] All metadata fields filled correctly
- [ ] Visibility settings prepared (ready to switch to Public)
- [ ] Announcement text prepared in advance (not to be shared until AFTER publication)
- [ ] Browser cache cleared (fresh session)
- [ ] System time verified correct

### 3.2 Publishing Workflow QA

**Publication Checklist:**
1. [ ] Video uploaded to YouTube Studio
2. [ ] Wait for processing to 100%
3. [ ] Preview video in YouTube Studio
4. [ ] Set visibility to "Public"
5. [ ] Wait for "Published" confirmation in interface
6. [ ] Copy canonical YouTube URL
7. [ ] Post announcement in #rest with URL
8. [ ] Verify announcement posted (no duplicates)

**Post-Publishing Verification (within 1 hour):**
- [ ] Video plays correctly on YouTube
- [ ] Metadata displays correctly
- [ ] Duration matches expected
- [ ] Thumbnail displays correctly
- [ ] Playlist membership confirmed
- [ ] Description links clickable and correct

---

## 4. CRITICAL CONSTRAINTS (ABSOLUTE ENFORCEMENT)

### 4.1 Production Constraints
- ✅ **One video per day maximum** (May 27-June 4, June 9-14)
- ✅ **Scripts locked** (all 6 finalized, zero rewrites)
- ✅ **Storyboards locked** (33 scenes fixed, no modifications)
- ✅ **Narrations locked** (all 6 recorded, no re-recording)
- ✅ **Colors locked** (RGB values fixed, no adjustments)

### 4.2 Announcement Constraints
- ✅ **One announcement per video** (target 6/6 perfect like Series 1's 10/10)
- ✅ **Never re-announce Series 1** (all 10 announced May 19-20, PROTECTED)
- ✅ **Only announce AFTER publication** (wait for "Published" status)
- ✅ **No promotional language** (focus on content, let material speak)

### 4.3 Quality Constraints
- ✅ **Minimum score:** 4.3/5 (only in exceptional circumstances)
- ✅ **Standard target:** 4.5+/5 (match Series 1 baseline of 4.51)
- ✅ **Series 1 match:** Pursue 4.6-4.7 range (match Series 1 best)

### 4.4 Timing Constraints
- ✅ **Production window:** May 27-June 4 (1 video/day)
- ✅ **Publishing window:** June 9-14 (1 video/day)
- ✅ **Work until 2 PM PT:** No waiting/sleeping/monitoring before session end

---

## 5. CONTINGENCY PROCEDURES

### 5.1 Technical Issues During Production

**Issue: Frame generation fails mid-way**
- Verify narration audio file integrity
- Check available disk space (~2-5 GB needed)
- Verify frame generator syntax: `python video[N]_frame_generator.py`
- If persistent: contact help@agentvillage.org with error message

**Issue: Audio sync off by >100ms**
- Regenerate frames with same narration
- Re-import audio at exact start point
- Test sync on first 5 and last 5 frames
- If pattern continues: flag for re-recording (approved only by goal setter)

**Issue: Color grading looks different than locked spec**
- Verify color_specifications.json hasn't been modified
- Check monitor calibration (may be viewing hardware)
- Regenerate test frame and compare side-by-side
- If spec file changed: revert to locked version

**Issue: File export takes >3 hours**
- H.264 encoding is CPU-intensive; this is normal for 4950+ frames
- Typical time: 45 min - 2 hours
- Monitor ffmpeg progress output
- If >4 hours: stop process, verify codec settings, try again

### 5.2 Quality Scoring Disputes

**If score falls below 4.3/5:**
- Identify which scoring category is driving low score
- Review quick reference card for that video's key themes
- Check if narration sync is causing visual rhythm issues
- Consider if color grading matched locked specifications
- Document findings in daily checklist notes
- Only proceed to publish if score ≥4.3/5 with rationale documented

**If score fluctuates between sessions:**
- Playback environment affects perception (monitor, speakers, lighting)
- Ensure consistent playback conditions for all scorings
- Use technical metrics (sync, file specs) as anchor, not just subjective feel
- If technical metrics pass, video is production-ready

### 5.3 Publishing Issues

**Issue: YouTube Studio won't change visibility to Public**
- Verify video finished processing 100%
- Refresh page and try again
- Check account permissions (should be owner)
- Wait 5 minutes and retry

**Issue: Can't find "Public" radio button after visibility click**
- Scroll down in Visibility panel
- Try keyboard navigation (Tab key to move between options)
- Take screenshot and send to help@agentvillage.org

**Issue: Announcement message sent but video not yet Public**
- Delete announcement immediately if possible
- Repost once "Published" confirmation appears in interface
- Document this in production notes

---

## 6. SUCCESS METRICS

**Series 2 Production Phase Success:**
- [ ] All 6 videos produced by June 4, 2026
- [ ] All 6 videos score ≥4.3/5 (target 4.5+/5)
- [ ] Zero script rewrites during production
- [ ] Zero storyboard modifications during production
- [ ] Zero narration re-recordings during production
- [ ] Zero color specification changes during production
- [ ] One video per day maximum (days 1-6 production respect)
- [ ] Complete git history with clean commits

**Series 2 Publishing Phase Success:**
- [ ] All 6 videos published June 9-14
- [ ] One announcement per video (6/6 perfect)
- [ ] All announcements posted AFTER publication confirmation
- [ ] Zero Series 1 re-announcements
- [ ] All 6 videos on YouTube, functioning correctly
- [ ] Playlist updated with all 6 Series 2 videos

**Overall Project Success:**
- [ ] Series 1 (10 videos) + Series 2 (6 videos) = 16 total published
- [ ] Combined average score maintained ≥4.5/5
- [ ] Channel demonstrates consistent quality and voice
- [ ] Audience engagement metrics positive (based on YouTube analytics post-publication)

---

## 7. REFERENCE LINKS

**Documentation:**
- Production Day Reference Cards: MAY_27_QUICK_REFERENCE_CARD.md through JUNE_4_QUICK_REFERENCE_CARD.md
- Publishing Guide: SERIES_2_PUBLISHING_PHASE_GUIDE.md
- Narrative Analysis: SERIES_2_NARRATIVE_ARC_ANALYSIS.md
- Audience Messaging: SERIES_2_AUDIENCE_MESSAGING_GUIDE.md
- Storyboards: SERIES_2_VIDEO_{1-6}_DETAILED_STORYBOARD.md

**Technical:**
- Color Specifications: production_configs/color_specifications.json
- Frame Generators: video{1-6}_frame_generator.py
- Export Scripts: export_video_with_audio.py, run_production_pipeline.py

**Channel:**
- YouTube: https://www.youtube.com/@AITransparencyLab
- Playlist (Series 1): https://www.youtube.com/playlist?list=PLt22r1pmgnb-1wyIBEfxzemr2BFG7w3MU

---

**STATUS: 🟢 FRAMEWORK COMPLETE & LOCKED**
Ready for May 27 production phase.
